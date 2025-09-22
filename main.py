# print("Hello World! Kaise h aap log !");

# print("Hello world!");

# sher  = "harsh bhaiya";
# print(sher);

# SheriyansSchool = "Students"; #pascal case
# sheriyanSchool = "students"; #camel case
# sheriyans_school = "students" #snake case 


# a = -12;
# print(type(a));
# b = 22/7;
# print(type(b));

# # complex data types
# v = 34j;

# print(type(v));


# # st = '12fnnfwiefwnfwfsfnnfls';


# b = True 
# t = False;

# print(type(b));


# a = ""
# # char to unicode 
# print(ord(b));

# # unicode to char
# a = 65;
# print(chr(a));


# ''''strings'''



# a = "hello brother"

# -------------------------------String slicing--------------------#
# a = "SHER CODER"

# a[start : stop : steps]

# print(a[5::]);



# -----------type conversion-------------#

# a = "asd";
# # convert the int to string
# a = str(a);
# print(type(a));


# a = 0;
# print(bool(a));


# implicit conversion
# a = 12;
# print(a/3);

# name = "vishu";
# age = 23;
# print("hello my name is ",name,"and my age is ",age);
# print(f"hello my name is {name} and my age is {age}");



# -----------input from user--- 


# a = int(input("hello what is your age : "));
# print(a);


# -----------------what are operators -------------#


# a = 5;
# b = 32;
# print(a - b);
# print(a *b);
# print(a %b);
# print(b/a);
# print(b//a); #floor divison
# print(a +b);
# print(a**b);
# print(32%5);
# print(12+4/2);


# ----------------Assignment Operator ----------------#


# a = 23;


#  Compound assignment operations

# a = 20
# a = a + 20;
# print(a);



# a = 20
# a = a + 20
# a = a + 40
# print(a)

# a += 60 
# print(a)

# ---------------Comparison operator---------------#

# a = 12.1
# b = 12
# print(a == b)
# print(a != b) 

# print(ord("A"));
# print(ord("B"));

# print("ABCE" < "BCB");


#-----------------logical Operator---------#
# AND
# b = (14 > 13) and (19 == 0)
# print(b);

# OR 
# b = (14 > 13) or (19 == 0)
# print(b);

# print(12 > 20 and 123 > 111 and 34 == 34 and 45 < 90)

# print(12 != 12 or 23 == 45 or 67 == 65 or 10 > 5)

# print(not 12 == 12)



#--------------------Question-----------------#

 
 
 
#  IF ELSE

# a = 13

# if a > 10:
#     print("Yes I will do task A")
# else : 
#     print("No I will do task B")



# money = int(input("Please provide me the money:- "))

# if money == 10:
#     print("I will have a choco bar icecream")
# elif money == 20 :
#      print("I will have mango dolly")
# elif money == 30 :
#      print("I will have forsty")
# else:
#     print("I will have cone")

# Question ----->

# a  = int(input())
# b = int(input())

# if a > b:
#     print(f"a is greater {a}")
# else : 
#     print(f"b is greater {b}")


# a = input()

# if  a[0] == 'M' : 
#     print("Hello sir")
# else : print("Hello Mam")


# ----check the leap year 
# a = int(input())

# if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
#     print("Year leap year")
# else:
#     print("Not a leap year")



# t = int(input("Please tell the temperatur :- "))

# if t < 0:
#     print("Freezing cold")
# elif t>= 0 and t < 10:
#     print("Very cold")
# elif t>= 10 and t < 20:
#     print("cold")
# elif t>= 20 and t < 30:
#     print("Pleasant")
# elif t>= 30 and t < 40:
#     print("hot")
# else :
#     print("Temperature is very hot")



# loops in python


# for loop 

# range(start,stop,steps)

# for i in range(1,21,1):
#     print("Hello world!")
#     print(i)


# for i in range(21):
#     print(i)


# reverse printing
# for i in range(16,0,-1):print(i)


# for i in range(-5,-16,-1):
#     print(i)



# lets print a table of 5

# n = int(input())
# for i in range(n,n*10+1,n):
#     print(i);




# a = "SHERYIANS TEACHES INDUSTRY"

# print(len(a))
# for i in range(len(a)):
#     print(a[i]);


# a = "SHERIYANS"

# for i in a:
#     print(i)


# for i in range(1,21):
#     print(i)

# # continue
# for i in range(1,21):
#     if i == 15:
#         continue;
#     else:print(i)
    
# break
# for i in range(1,21):
#     if i == 15:
#         break;
#     else:print(i)
 
 
# for i in range(1,21):
#     if i == 90:
#         print("break statement is executed")
#         break;
#     else:print(i)
# else:
#     print("Break statement is not executed")



# Question ----------------------------->>>

# n = int(input("which table you want :- "))

# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")


# sum = 0
# n = int(input())
# for i in range(1,n+1):
#     sum+=i
    
# print(sum)


# factorial of a number

# n = int(input())
# fact = 1;
# for i in range(1,n+1):
#     fact*=i
# print(fact)

# n = int(input())

# even = 0 
# odd = 0

# for i in range(1,n+1):
#     if i % 2 == 0:
#         even+=i
#     else : 
#         odd +=i
        
# print(f"even : {even} and odd : {odd}")


# n = int(input())

# for i in range(1,n+1):
#     if(n%i ==0):
#         print(i)


# -------------------Perfect Number-------------------> 

# n = int(input())
# sum = 0
# for i in range(1,n):
#     if(n%i == 0):
#         print(i)
#         sum+=i
    
# if sum == n:
#     print("Yes")
# else:
#     print("No")


# n = int(input())
# a = True
# for i in range(2,n//2+1):
#     if(n%i == 0):
#         a = False
     
# if a == True:
#     print("Yes it is prime no")
# else :
#     print("No it not a prime number")



# ---------Reverse the string using for loops----------->
# a = "SHERIYANS"

# print(a[::-1])

# b = ""
# for i in range(len(a)-1,-1,-1):
#     b+=a[i]
    
# print(b)

# a = input()
# b = False
# n = len(a)-1
# for i in range(len(a)//2):
#     if a[i] != a[n-i]:
#         b = True

# if b == False:
#     print("Yes Pallindrome")
# else : 
#     print("Not a Pallindrome")


# a = "aejfaefanefoia193q9!4@@##"
# char = 0
# dig = 0
# spchr = 0

# for i in a:
#     if i.isdigit():
#         dig+=1
#     elif i.isalpha():
#         char +=1
#     else:
#         spchr +=1
        
        
# print(f"your digits are {dig} and your alphabets are {char}  and  special char is {spchr}")


# print(dir(str))



# ---------------while--------------

# a = 1
# while(a <= 30):
#     print(a);
#     a+=1



# a = 256

# while a > 0:
#     last = a % 10
#     print(last)
#     a = a//10
    


# a = int(input())
# b = 0
# while a > 0:
#     last = a % 10
#     b = b * 10 + last
#     a = a//10

# print(b)    



# a = int(input())
# c = a
# b = 0
# while a > 0:
#     last = a % 10
#     b = b * 10 + last
#     a = a//10

# if c == b:
#     print("Pallindrome ")
# else :
#     print("Not a Pallindrome")




# -----------------Random Guessing game------------

# import random

# num = random.randint(1,11)

# trys = 0
# while True:

#     guess = int(input())
#     if num == guess :
#         trys +=1
#         print("Right")
#         break
#     else:
#         trys += 1
#         print("Wrong")



# -----------------------------Functions----------------->


# def hello(a):
#     print(f"Hello World! {a}")

# name = input()
# hello(name)


# def sum(a,b):
#     print(f"The sum of yout number is {a+b}")
    
    
# sum(12,13)
# sum(24,98)


# def hello(name,age):
#     print(f"your name is {name} and your age is {age}")
    

# hello(age = 22, name = "Vishu") #key word arguments


# -- Default Parameter ----
# def sum(a= 1,b = 1):
#     print(f"The sum of yout number is {a+b}")
    
    
# sum(12,13)
# sum()



# def Pallindrome(str):
#     b = ""
#     for i in range(len(str)-1,-1,-1):
#         b = b + str[i]
        
#     if b == str:
#         return True

#     return False


# if Pallindrome("Vishu") == True:
#     print("Pallindrome")
# else :
#     print("Not a Pallindrome")



# if Pallindrome("mam") == True:
#     print("Pallindrome")
# else :
#     print("Not a Pallindrome")



# ----------------list----------------------#

# a = [12,13,14,15,16,12,12,34.5]

# lst way using index

# for i in range(len(a)):
#     print(a[i])

#  2nd way directly on values

# for i in a:
#     print(i)


# print(dir(list))

# l = [1,3,4,5]
# l[0] = 10
# print(l)
# l.append(6)
# l.append(67)

# l.insert(1,2)
# l.remove(2)


# print(l)



# l  = [-39,39,-90,-290,20,90]
# p =[]
# n = []
# for i in l :
#     if i < 0:
#         n.append(i)
#     else :
#         p.append(i)
        
# print("Negative : " ,n)
# print("Positive : " ,p)



# l = [1,2,3,4,5]
# s = 0

# for i in l:
#     s += i
    
# print("Mean is  : ", s/len(l))


# l = [12,36,10,10,91,128,6,13]
# maxi = 0
# indx =0;
# for i in range(len(l)):
#     if maxi <=  l[i]:
#         maxi = l[i]
#         indx = i
        
# print(maxi," ",indx)


# l = [12,36,10,10,91,128,6,13]
# l = [12,16,13,19,17]

# l.sort()
# print(l)
# print(l[len(l) -2])
# maxi = 0
# smaxi =0;
# for i in l:
#     if maxi <=  i:
#         smaxi = maxi
#         maxi = i
#     elif i > smaxi:
#         smaxi = i
        
# print(maxi," ",smaxi)



# l = [12,13,14,15,9]
# b = True
# for i in range(1,len(l)):
#     if l[i] < l[i-1]:
#         b = False

# if b == True:
#     print("Sorted")
# else :
#     print("Not sorted")        


# ---------------Tuple-------------------->


# a = (1,2,3,4,5,5,5,5)
# Tuple is immutable  u can't change the value in tuple
# print(type(a))

# for i in a:
#     print(i)

# print(a[0])


# a = (1,2,3,4,5,5,5,5)

# index = a.index(5)
# print(index)

# cnt = a.count(5)
# print(cnt)


# a,b,c,d = (1,2,3,4)
# a = (1,)
# print(type(a))
# print(a)
# print(b)



# --------------Set--------------#
# s = {1,2,3,4,5,5,4}
# sets are -> it is mutable in nature 
# print(s)

# b = hash("Hello")
# print(b)


# c = hash((1,2,234))
# print(c)

# ----------------Traversing in Set ----
# a = {1,2,8,9,"hello",3,4,5}

# for i in a:
#     print(i)

# a = {1,2,3,4}

# a.remove(2)
# a.pop()
# print(a)


# ------------------SET METHOD-=----------
# a=  {1,2,3,4,5}
# b = {4,5,6,7,8}

# s = a.union(b) # A | B
# print(s)

# t = a.intersection(b) # A & B
# print(t)

# u = a.difference(b)  # A - B
# print(u)

# z = a.symmetric_difference(b) # A^ B
# print(z)



# -----------------------Dictionary -------------#

# d = {1 : "Hello",2 : 122 ,10 :100 , 20 : 200, 30:300}
# # it is mutable in nature 
# # key value pair 
# print(d[10])

# d[10] = 1000 
# print(d[10])

# d.update({50:100}) #upating
# d[50] = 500 # creating

# del d[30] #deleting

# print(d)



# d = {1 : "Hello",2 : 122 ,10 :100 , 20 : 200, 30:300}

# for i in d :
#     print(d[i])

# d[100] = 100
# del d[1]

# print()

# for i in d :
#     print(d[i])


# help(dict)


#  ---------------Deep and Shallow Copy--------------
# a = [1,2,3,4,5]
# b = a.copy() # .copy shallow copy create karta h without these is create the deep copy
# b[0] = 100

# print(a)
# print(b)


# d = {1 : "Hello",2 : 122 ,10 :100 , 20 : 200, 30:300}

# d2 = d.get(20)
# print(d2)
# print(d.items())

# d1 = {10 : 100,20 :200,40 :300}
# d2 = {40 : 400,50 :500,60 :600}

# for i in d2:
#     d1[i] = d2[i]

# print(d1)


# d1 = {10 : 100,20 :200,40 :300}

# s = 0

# for i in d1:
#     s+=d1[i]
    
# print(s)

# a = [1,1,1,2,2,3,3,3,3,4,4,4,4,5,5,5]
# d ={}
# for i in a:
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1
    
# print(d)



# d1 = {10 : 100,20 :200,40 :300}
# d2 = {40 : 400,50 :500,60 :600}


# for i in d2:
#     if i in d1.keys():
#         d1[i] += d2[i]
#     else :
#         d1[i] = d2[i]
        
# print(d1)



# print("Hello world!")

# --------------------Exception handling -----------------

# a = int(input())
# try:
#     print(10/a)
# # except ZeroDivisionError:
# #     print("sorry you cant divide by zero")
# except Exception as e:
#     print(f"sorry you cant divide by {e}")

# else :
#     print("Good there is no exception")

# finally :
#     print("i will run no matter what")

# # when there is exception so exception will run not the else one 
# # but there is no exception then the else part will run 
# # finally will run no matter what when ever it need to run


# print("ok i have done ")



# age = int(input())

# try :
#     if age < 10 or age > 18 :
#         raise ValueError("Your age must be between 10 and 18")
#     else:
#         print("Welcome to the club")

# except Exception as e:
#     print(f"an error occured as {e}")

# print("the club will start soon")




# -----------File handling-----------------------#

 

# p = open(r'C:\Users\Vishu\OneDrive\Desktop\Closure.txt')
# print(p.read())


# r = open("superman.txt",'a')
# r.write("and appending these content in these");
# r.close()





#  -------------OOPS------------------------------#


# a= 12
# b = 12
# print(a+b)



# def addition(a,b):
#     return a+b

# print(addition(12,4))



# class Factory:
#     a = 12 #attribute
    
#     def hello(self):   #method
#         print("how are you")
    
    
    
# # print(Factory().a)

# # Factory().hello()


# obj1 = Factory()
# print(obj1.a)
# obj1.hello()


# obj2 = Factory()

# obj3 = Factory()




# class Factory:
#     def __init__(self,material,zips,pockets):
#         # print(self)
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets

#     def show(self):
#         print(f"Your object details are {self.material} ,{self.pockets},{self.zips}")
        

# reebok = Factory("cotton",3,2)

# campus = Factory("nylon",3,3)


# print(reebok.pockets)
# print(campus.pockets)
# reebok.show()
# campus.show()





# class Animal:
#     name = "lion" #class attribute
    
#     def __init__(self,age):
#         self.age = age  #instance attribute
        
#     def show(self): #instance method
#         print(f"how are you age is {self.age}")
    
#     @classmethod
#     def hello(cls):
#         print(f"how are you brother {cls.age}")
    
#     @staticmethod #na hi class or instance ko target karta h ye 
#     def static():
#         print("how are you")
        

# obj = Animal(12)
# obj.show()



# ------------------Four PILLAR OF OOPs--------

# ================INHERITANCE===================


# class Factory: #Parent class
#     a = "1"
#     def hello(self):
#         print("hello I am a method mentioned inside Factory")
        

# class FactoryPune(Factory): #child clsss
#     pass

# obj = Factory()
# obj1 = FactoryPune()
# print(obj.a)
# print(obj1.a)
# obj.hello()
# obj1.hello()



# ==========Constructor Inheritance===========#

# class Animal:
#     def __init__(self,name):
#         self.name = name
    
#     def show(self):
#         print(f"Hello your name is : {self.name}")
        

# class Human(Animal):
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age = age
#     def show(self):
#         print(f"Hello your name is : {self.name},{self.age}")



# a1 = Animal("Lion")
# a1.show()

# p1 = Human("joker",19)
# p1.show()



# ============Mutiple Inheritance==========#

# class Animal:
#     def __init__(self,name):
#         pass
#     name1 = "lion"

# class Human:
#     def __init__(self,name,age):
#         pass
#     name2 = "harsh"

# class Robots(Animal,Human):
#     name3 = "vishu"
    
    
# obj = Robots("lion")
# print(obj.name3)




# class Factory:
#     def __init__(self,material,zips):
#         self.material = material
#         self.zips = zips
#     def show1(self):
#         print(self.material , self.zips)
        
# class BhopalFactory(Factory):
#     def __init__(self, material, zips,color):
#         super().__init__(material, zips)
#         self.color = color
#     def show2(self):
#         print(self.material , self.zips, self.color)

# class Punefactory(BhopalFactory):
#     def __init__(self, material, zips, color,pockets):
#         super().__init__(material, zips, color)
#         self.pockets = pockets
        
#     def show(self):
#         print(self.material , self.zips, self.pockets, self.color)
        

# obj = Punefactory("nylon",1,"red",1)
# obj.show1()
# obj.show2()
# obj.show()



# =======Polymorphism ===================


# Over ridding
# over loading doesn't exists in the python

# class Animal:
#     def show(self):
#         print("hello I am Vishu")
               
# class Human(Animal):
#     def show(self):
#         print("how are you")
        

# obj = Human()
# obj.show()


# class Animal:
#     def show(self):
#         print("I am showing")

# class human:
#     def show(self):
#         print("hello")
    
# obj = Animal()
# obj1  = human()

# obj.show()
# obj1.show()


# -----------------------Encapsulation--------------#


# class Factory:
#     __a = "pune" #protected modifier use _
    
#     def show(slef): #private modifier use __
#         print("hello i am pune factory")
        

# obj = Factory()
# print(obj.__a)
# obj.show()



# -----------------Abstraction--------------------#

# from abc import ABC, abstractmethod

# class abstract(ABC):
#     @abstractmethod
#     def perimeter(self):
#         pass
#     @abstractmethod
#     def area(self):
#         pass
    

# class Square(abstract):
#     def __init__(self,side):
#         self.side = side
        

# class Circle(abstract):
#     def __init__(self,radius):
#         self.radius  = radius
    
#     def perimeter(self):
#         print("i have created")
    
#     def area(self):
#         print("i have created this")

# obj = Circle(7)
# obj.perimeter()


#--------------Dunder Method-------------------#


# class Animal:
    
#     def __init__(self,name,age):
#         self.age = age
#         self.name = name
#     def __str__(self):    #dunder method when obj print the it return these
#         return f"hello how are you ,{self.name} and {self.age}"
#     # dunder method to sum the obj and obj their age
#     def __add__(self,other):
#         sum = 0
#         for i in other:
#             sum = sum + i.age
#         return f"your sum of age are : {self.age + sum}"
    

# obj = Animal("lion",12)
# print(obj)
# obj1= Animal("dolphin",26)
# print(obj1)
# obj2= Animal("tiger",36)
# print(obj2)

# print(obj+(obj1,obj2))
        



# ---------------Advanced Stuff--------------#

# class Animal:
#     @property
#     def show(self):
#         print("hello how are you")

# obj = Animal()

# obj.show



# ==================Decorate the function================#

# def decorate(func):
#     def wrapper(a,b):
#         print("the addition to your number are")
#         func(a,b)
#         print("I will print after the function")
    
#     return wrapper

# @decorate
# def hello(a,b):
#     print(f"your total is : {a+b}")

# hello(12,17)


#=================Args and kwargs==============#


# def addition(*args):
#     sum = 0
#     for i in args:
#         sum += i 
#     print(sum)

# addition(12,12,23,56,100)


# # kargs

# def addition(**kargs):
#     sum = 0
#     print(kargs)

# addition(a = 12,b = 56, c = 13)




# def info(**kwargs):
#     print("your information is \n")
#     for i in kwargs:
#         print(f"{i} : {kwargs[i]}")
    

# info(name = "Vishwajeet" , age = 18, course = "B.Tech")



# def decorate(func):
#     def wrapper(*args,**kwargs):
#         print("the addition to your number are")
#         func(*args,**kwargs)
#         print("I will print after the function")
    
#     return wrapper

# @decorate
# def hello(a,b):
#     print(f"your total is : {a+b}")

# hello(12,17)


# l = []

# for i in range(1,21):
#     if i % 2 == 0:
#         l.append(i)
        
# print(l)


# l = { i : i**2 for i in range(1,21) if i% 2 == 0}

# print(l)

#------------------lamda functions--------------------#

# addition = lambda a: "even" if a % 2 == 0 else "odd"

# print(addition(13))




# --------------Maps-------------------------#


# a = [1,2,3,4,5]

# def double(x):
#     return x*2

# result  = map(double,a)
# # result  = map(lambda x : x*2,a)
# print(list(result))



# --------------Filter-------------------------#

# def even(x):
#     if x% 2 == 0:
#         return True
#     else:
#         return False
        
# a = [1,2,3,4,5,6,7,8,9]

# result = filter(lambda x : True if x % 2 == 0 else False,a)
# temp  =filter(lambda x : True if x % 2 == 1 else False,a)
# print(list(temp))
# print(list(result))



# import maths


# print(maths.add(12,41))
# print(maths.multiply(3,5))


# from modelss.model import hello,maths

# hello.how()




