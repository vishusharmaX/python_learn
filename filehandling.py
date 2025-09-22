# print("Hello World!")
from pathlib import Path
import os

def readfileandFolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1} : {items}")


def createfile():
    try:
        readfileandFolder()
        name = input("Please tell your file name :- ")
        p = Path(name)
        if not p.exists():
            with open(p,"w") as fs:
                data = input("what you want to write int this file:- ")
                fs.write(data)
            
            print(f"File created Successfully")
        else:
            print("this file already exist")
    except Exception as err :
        print(f"An error occured as {err}")



def readFile():
    readfileandFolder()
    name = input("which file you want to read :- ")
    p = Path(name)
    if p.exists() and p.is_file():
        with open(p,'r') as fs:
            data = fs.read()
            print(data)
        print("Readed successfully")            
    
    else :
        print("the file doesnot exits")


def updateFile():
    try :
        readfileandFolder()
        name = input("tell which file you want to update:- ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("press 1 for changing the name of your file :- ")
            print("press 2 for overwriting  the data of your file :- ")
            print("press 3 for appending some content in your file :- ")
            res = int(input("tell your response:- "))
            
            if res == 1:
                name2 = input("tell your new file name :- ")
                p2 = Path(name2)
                p.rename(p2)
            if res == 2:
                with open(p,'w') as fs:
                    data = input("tell what you want to write but it overwrite the data")
                    fs.write(data)
            if res == 3:
                with open(p,'a') as fs:
                    data = input("tell what you want to write the data")
                    fs.write(" " + data)
    except Exception as err :
        print(f"An error occured as {err}")
        

def deleteFile():
    try:
        readfileandFolder()
        name = input("tell which file you want to update:- ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print("file remove successfully")
        else :
            print("No such file exists")
    except Exception as err :
        print(f"An error occured as {err}")
        

print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file")

check = int(input("please tell your response :- "))


if check  == 1:
    createfile()
    
if check == 2:
    readFile()
    
if check == 3:
    updateFile()
if check == 4:
    deleteFile()