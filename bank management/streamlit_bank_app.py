"""
Streamlit Bank Management App
Single-file Streamlit app that replaces the CLI bank program with a safer, better UX.

How to run:
1. pip install streamlit
2. streamlit run streamlit_bank_app.py

Features / improvements over original:
- Uses a JSON file (bank_data.json) in the working directory (no hardcoded D: path)
- PINs are not stored in plaintext — they are hashed with SHA-256
- Validation for age (>=18), 4-digit PIN, email simple check, deposit/withdraw limits
- Transaction history stored per-account (timestamped)
- Robust loading/saving with graceful error handling
- Streamlit UI with separate views: Create, Deposit, Withdraw, Details, Update, Delete
- Admin view to list accounts (no PINs shown)

This app is meant for learning/demo purposes only and is NOT suitable for production banking.
"""

import streamlit as st
import json
from pathlib import Path
import random
import string
import hashlib
from datetime import datetime

DATA_FILE = Path("bank_data.json")

# -----------------------------
# Utility functions
# -----------------------------

def load_data():
    if not DATA_FILE.exists():
        save_data([])
        return []
    try:
        text = DATA_FILE.read_text(encoding="utf-8").strip()
        if not text:
            return []
        return json.loads(text)
    except Exception as e:
        st.error(f"Failed to load data file: {e}")
        return []


def save_data(data):
    try:
        DATA_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")
    except Exception as e:
        st.error(f"Failed to save data file: {e}")


def hash_pin(pin: str) -> str:
    return hashlib.sha256(pin.encode("utf-8")).hexdigest()


def generate_account_number(length=8) -> str:
    # AC + 6 random uppercase letters/digits
    body = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length-2))
    return f"AC{body}"


def find_user(data, account_no, pin=None):
    for acct in data:
        if acct["accountNo"] == account_no:
            if pin is None:
                return acct
            if acct.get("pin_hash") == hash_pin(str(pin)):
                return acct
            return None
    return None


def add_transaction(acct, ttype, amount):
    acct.setdefault("transactions", [])
    acct["transactions"].append({
        "type": ttype,
        "amount": amount,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    })


# -----------------------------
# Business logic functions
# -----------------------------

def create_account(name, age, email, pin):
    data = load_data()
    # basic checks
    if age < 18:
        return False, "You must be at least 18 years old to create an account."
    if not (isinstance(pin, str) and pin.isdigit() and len(pin) == 4):
        return False, "PIN must be a 4-digit number."
    # optional: check email contains '@'
    if "@" not in email or email.strip().startswith("@"): 
        return False, "Please enter a valid email address."

    account_no = generate_account_number()
    # ensure unique
    while any(a["accountNo"] == account_no for a in data):
        account_no = generate_account_number()

    acct = {
        "name": name.strip(),
        "age": int(age),
        "email": email.strip(),
        "pin_hash": hash_pin(pin),
        "accountNo": account_no,
        "balance": 0,
        "transactions": []
    }
    data.append(acct)
    save_data(data)
    return True, acct


def deposit(account_no, pin, amount):
    data = load_data()
    acct = find_user(data, account_no, pin)
    if acct is None:
        return False, "Account not found or incorrect PIN."
    if amount <= 0 or amount > 10000:
        return False, "Deposit amount must be between 1 and 10000."
    acct["balance"] += amount
    add_transaction(acct, "deposit", amount)
    save_data(data)
    return True, acct


def withdraw(account_no, pin, amount):
    data = load_data()
    acct = find_user(data, account_no, pin)
    if acct is None:
        return False, "Account not found or incorrect PIN."
    if amount <= 0:
        return False, "Withdrawal amount must be greater than 0."
    if acct["balance"] < amount:
        return False, "Insufficient balance."
    acct["balance"] -= amount
    add_transaction(acct, "withdraw", amount)
    save_data(data)
    return True, acct


def update_account(account_no, pin, new_name=None, new_email=None, new_pin=None):
    data = load_data()
    acct = find_user(data, account_no, pin)
    if acct is None:
        return False, "Account not found or incorrect PIN."
    changed = False
    if new_name and new_name.strip() != acct["name"]:
        acct["name"] = new_name.strip()
        changed = True
    if new_email and new_email.strip() != acct["email"]:
        acct["email"] = new_email.strip()
        changed = True
    if new_pin:
        if not (new_pin.isdigit() and len(new_pin) == 4):
            return False, "New PIN must be a 4-digit number."
        acct["pin_hash"] = hash_pin(new_pin)
        changed = True
    if changed:
        save_data(data)
        return True, acct
    return False, "No changes made."


def delete_account(account_no, pin):
    data = load_data()
    acct = find_user(data, account_no, pin)
    if acct is None:
        return False, "Account not found or incorrect PIN."
    data.remove(acct)
    save_data(data)
    return True, None


# -----------------------------
# Streamlit UI
# -----------------------------

st.set_page_config(page_title="Simple Bank App", layout="centered")
st.title("🏦Bank Management System)")

menu = st.sidebar.selectbox("Choose action", [
    "Create Account",
    "Deposit",
    "Withdraw",
    "Show Details",
    "Update Details",
    "Delete Account",
    "Admin: List Accounts"
])

if menu == "Create Account":
    st.header("Create a new account")
    with st.form("create_form"):
        name = st.text_input("Full name")
        age = st.number_input("Age", min_value=0, max_value=120, value=18)
        email = st.text_input("Email")
        pin = st.text_input("4-digit PIN", type="password")
        pin_confirm = st.text_input("Confirm PIN", type="password")
        submitted = st.form_submit_button("Create account")
    if submitted:
        if not name:
            st.error("Please provide your name.")
        elif pin != pin_confirm:
            st.error("PINs do not match.")
        else:
            ok, result = create_account(name, age, email, pin)
            if ok:
                st.success("Account created successfully!")
                st.write("Account number:", result["accountNo"]) 
                st.info("Please store your account number and PIN safely. PINs are not recoverable.")
            else:
                st.error(result)

elif menu == "Deposit":
    st.header("Deposit money")
    with st.form("deposit_form"):
        account_no = st.text_input("Account number")
        pin = st.text_input("PIN", type="password")
        amount = st.number_input("Amount", min_value=1, value=100)
        submitted = st.form_submit_button("Deposit")
    if submitted:
        ok, result = deposit(account_no.strip(), pin, float(amount))
        if ok:
            st.success(f"Deposit successful. New balance: {result['balance']}")
        else:
            st.error(result)

elif menu == "Withdraw":
    st.header("Withdraw money")
    with st.form("withdraw_form"):
        account_no = st.text_input("Account number")
        pin = st.text_input("PIN", type="password")
        amount = st.number_input("Amount", min_value=1, value=100)
        submitted = st.form_submit_button("Withdraw")
    if submitted:
        ok, result = withdraw(account_no.strip(), pin, float(amount))
        if ok:
            st.success(f"Withdrawal successful. New balance: {result['balance']}")
        else:
            st.error(result)

elif menu == "Show Details":
    st.header("Account details")
    account_no = st.text_input("Account number")
    pin = st.text_input("PIN", type="password")
    if st.button("Show"):
        acct = find_user(load_data(), account_no.strip(), pin)
        if acct is None:
            st.error("Account not found or incorrect PIN.")
        else:
            st.subheader("Profile")
            st.write({k: v for k, v in acct.items() if k not in ("pin_hash", "transactions")})
            st.subheader("Transactions")
            txs = acct.get("transactions", [])
            if not txs:
                st.info("No transactions yet.")
            else:
                for t in reversed(txs[-10:]):
                    st.write(f"{t['timestamp']} — {t['type'].title()} — {t['amount']}")

elif menu == "Update Details":
    st.header("Update account details")
    with st.form("update_form"):
        account_no = st.text_input("Account number")
        pin = st.text_input("Current PIN", type="password")
        new_name = st.text_input("New name (leave blank to keep)")
        new_email = st.text_input("New email (leave blank to keep)")
        new_pin = st.text_input("New PIN (4 digits) (leave blank to keep)", type="password")
        submitted = st.form_submit_button("Update")
    if submitted:
        ok, result = update_account(account_no.strip(), pin, new_name or None, new_email or None, new_pin or None)
        if ok:
            st.success("Account updated successfully.")
        else:
            st.error(result)

elif menu == "Delete Account":
    st.header("Delete an account")
    with st.form("delete_form"):
        account_no = st.text_input("Account number")
        pin = st.text_input("PIN", type="password")
        confirm = st.checkbox("I confirm I want to permanently delete this account")
        submitted = st.form_submit_button("Delete")
    if submitted:
        if not confirm:
            st.warning("Please confirm deletion by checking the box.")
        else:
            ok, result = delete_account(account_no.strip(), pin)
            if ok:
                st.success("Account deleted successfully.")
            else:
                st.error(result)

elif menu == "Admin: List Accounts":
    st.header("All accounts (admin view)")
    data = load_data()
    st.write(f"Total accounts: {len(data)}")
    if data:
        # show a safe view without pin_hash
        safe = [ {k:v for k,v in acct.items() if k != 'pin_hash'} for acct in data ]
        st.json(safe)


# footer
st.markdown("---")
st.caption("Demo app — do not use for real money. Data stored locally in bank_data.json.")
