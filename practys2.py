#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 20:19:35 2023

@author: morningstar
"""

#  (00:05:57​) variable
# variable = a container for a value. Behaves as the value that 


# -it contains

# string= is a series of chareckers 

# integer = int = is a whole number

# float= floating point of numbers
# =which is mean a decimal number

# boolean = True or False = that mean a varieble that can only
# store True or False 
 

#first_name= "Jarvis"
#last_name= " Sins"
#full_name= first_name + last_name  
#print(type(first_name))
#print("Hello"+": "+full_name)

#age =33
#age = age+ 1
#print ("your age is: "+str(age))
#print ((age))
#print(type(age))

#height= 250.5
#print(height)
#print(type(height))
#print("your height is"+": "+str(height)+"cm")

#human = True
#print("are you a human: "+ str(human))
#print(type(human))








#  (00:20:27​) string methods
# multible assigment = allowes us to assign multible variables at
# -the same time in one line of code

#name = "Jarvis"
#age= 33
#attractive= True 

#name, age, attractive= "jarvis",33,True

#print(name)
#print(age)
#print(attractive)

#spongebob=30
#Patrick =30
#sandy=30
#Squidward=30 

#print(spongebob)
#print(Patrick)
#print(sandy)
#print(Squidward)


#name = "jarvis sins "
#print(len(name))
#print(name.find("")) 
#print(name.capitalize())
#print(name.upper())
#print(name.lower())
#print(name.isdigit())
#print(name.isalpha())
#print(name.count("j"))
#print(name.replace("s", "l"))
#print(name*4)









# (00:25:13​) type cast 💱
# type casting = convert the data type of a value to another 
# -data type 

#x= 1      #int
#y= 2.0   #float
#z= "3"   #str

#x = float(x)
#y= float(y)
#z= float(z)

#print("X is "+str(x))
#print("Y is "+str(y))
#print(z *3)




# (00:30:14​) user input ⌨️
#name=  input("What is your name?: ")
#age  = int(   input("How old are?: ")) +1
#height= float(input("How tall are you?: "))

#print(" hello "+name)
#print("you are: "+ str(age)+" years old")
#print("You are: "+ str(height)+ "cm tall")




#(00:36:50​) math functions 🧮
# abs = return the absulate value of the argument 
# =that will tall us how far a number is away from zero

import math
 
#pi= 3.14

#x=1
#y=2
#z=3

#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#print(abs(pi)) 
#print(pow(pi, 3 )) 
#print(math.sqrt(pi)) 
#print(max(x,y,z))
#print(min(x, y,z))



 




#(00:40:58​) string slicing ✂️
# slicing = create a substring by extracting elements
# from another string
        # indexing[] or slice
        # [start:stop:step]
        
#name = "Jarvis Sins"
 
#first_name=name[:6 ]
#last_name=name[7:]
#funny_name=name[0:11:2]
#reversed_name= name[::-1]

#print(reversed_name)
#print(first_name)
#print (last_name)
#print(funny_name)


# slicing= create asub
#website="http://google.com"
#website2="http://wikipedia.com"
#slice= slice(7,-4)

#name= website[7:13]
#print(name)
#print(website[slice])
#print(website2[slice])
#print (pow(3,4))
#print(math.sqrt(3.3))







# (00:51:52​) if statements 🤔
# if statement= a block of code that will execute if it's 
# condition is true

#age = int(input("How old are you?: "))

#if age >= 18 ==99:
    #print("You are an adult!")
#elif age <0:
    #print("You haven't been born yet")
#elif age == 100:
    #print("You are a century old guy!")
#else:
    #print("You are a kid!")
    
    
    
    




#  (00:58:19)​ logical operators 🔣
# logical operation (and,or,not)= used to check if two or
# -more conditional statements are true

#temp= float(input("What is the temperatur outside?: " ))

#if not temp >=0 and temp<=30:
    #print("The temperatur is good today!")
    #print("go outide!")
#elif not temp <0 or temp >30 :
        #print("The temperatur is bad today!")
        #print("Don't go outside! ")
    
    
    
    
    
    
    
    
    
    
# (01:04:03​) while loops 🔄 
# while loop= a statement that will execute it's block of
# -code, as long as it's condition remains true

#while 1==1:
    #print("Help, Im stock in a loop")
    
#name = None

#while not name:
    #name = input("Enter your name: ")

#while len(name)==0:
    #name=(input("Enter yout name: "))
 
# print("Hello"+" "+name)








# (01:07:31​) for loops ➰
import time

#for loop=a statement that will execute its block of code
         #a limited amount of times
    #while loop= unlimited 
    #for a loop= limited
 
#for i in range(10):
    #print (1 +i)
#for i in range(50, 100+1,2):
    #print (i+1,i-1)
#for i in "Jarvis":
    #print(i)

#for seconds in range(10,0,-1):
    #print(seconds) 
    #time.sleep(1)
    
#print("happy birthday")
#name="good morning"

#for seconds in range (10,0,-1):
    #((print(seconds)))
    #(time.sleep(1))
#print(name)















# (01:13:04​) nested loops ➿
# nested loop= the "inner loop" will finish all of it's iterations
# -before. Finishing one iteration of the  "outer loop"


#rows= int(input("How many rows?:"))
#columns= int(input("How many columns?:"))
#symbol= input("Enter a symbol to use:")
 
#for i in range(rows):
#    for j in range(columns):
#        print(symbol,end="")
#   print()
 








# (01:17:08) break continue pass ⛔
#loop control statements= change a loops execution from its normal
#- sequence
# Break= used to terminate the loop entirely
# continue= skips to the next iteration of the loop
# pass = does nothing, actes as a placeholder
#while True:
    #name= input("enter your name: ")
    #if name!= "":
        #break
#phone_number= "123-456-7890"
#for i in phone_number:
    #if i=="-":
        #continue
    #print(i, end="")
    
    
#list=[4,3,2]
#list.sort()
#print(list)
    
#for i in range(1,21):         
    #if i==13:
     #    pass
     #else:
      #   print(i)
 
    
 
    
 
    
 
    
 

# (01:21:06​) lists 🧾
    
# list = used to store multiple items in a single variable 

#Food =["pizza","hamburger","hotdog" ,"spaghetti","pudding"]
#food.append("ice cream")
#food.remove("hotdog")
#food[0] ="sushi" 
#food.pop()
#food.insert(0,"cake")
#food.sort()
#food.clear()


#print (food[3])
#for x in  (food):
 #     print(x) 





       
# (01:26:58​) 2D lists 📜 
# 2D lists = a list of lists
 
#drinks= ["coffee","soda","tea"]
#dinner= ["pizza","hamburger","hotdog"]
#dessert= ["cake","ice cream"]
#dessert.append("pudding")
#dessert.insert(0, "chocolate milk")
#ood=[drinks,dinner,dessert]
#print(food[2][0])








# (01:30:47​) tuples 📄
# tuple= collection which is ordered and unchangeable
# used to group together realated data

#student=("sins",21,"male")
#print(student.count("jarvis"))
#print(student.index("male"))

#for x in student:
    #print(x)
     
    
#if "jarvis" in student:
    #print("jarvis is here!")

#else:
    #print("jarvis is not here!")
 
    
 
    
    
 
    
# (01:33:47​) sets 🍴
# Set = collection which is unordered, unindexed. No duplicate 
# -valuse
 
#utensils= {"fork","spoon","knife"}
#dishes= {"bowl","plate","cup","knife"}
#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()
#utensils.update(dishes)
#dinner_table= utensils.union(dishes)

#print(dishes.difference(utensils))

#print(utensils.intersection(dishes))

#for x in dinner_table:
 #     print(x)
    





# (01:40:03​) dictionaries 📖
# dictionary = a challangeable,unordered collection of unique 
# -key:value pairs 
# fast because they use hashing, allow us to access a value
# -quickly

#capitals= {'USA': 'Washington DC', 'India': 'New Dehli'
#           ,'China':'Beijing', "Russia":"Moscow"}
#print(capitals["Russia"])
#print(capitals.get("USA"))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

#capitals.update({"Germany":"Berlin"})
#capitals.update({"USA":"Las Vegas"})
#capitals.pop("China")
 

#for key, value in capitals.items():
#    print(value,":",key)






# (01:47:20​) indexing 📑
# Index opration []= gives access to a sequence's element 
# -(str,list,tuples)

#if (name[0].islower()):
    #name=True
#else:                        My own creation
    #name=False
#print(name)

#name= "jarvis sins!"
#if (name[0].islower()):
 #   name= name.capitalize()
  
#first_name= name[0:7].upper()
#last_name=name[7:].lower()
#last_charecter= name[-1]
 
#print(first_name)
#print(last_name)   
#print(last_charecter)  


 





# (01:53:23​) functions 📞
# function = a block of code which is executed only when it is
# -called

#def hello(first_name ,last_name, age):
    #print("hello! "+ first_name+" "+ last_name)
    #print("You are "+str(age) +" years old")
    #print("Have a nice day!")
    
#my_name= "jarvis"
#hello("Jarvis")
#hello("Jarvis","Sins",21)




# (02:02:03​) return statement 🔙
# return statement =Function send python values/objects back
# -to the caller.
#     this values/objects are known as the function's return 
# -value

#def multibly(number1,number2):
    #return number1*number2
#    result= number1 *number2
    #return result
#x=multibly(5,6)
#print(x)





# (02:04:51) keyword arguments 🔑
# Keybord agument = arguments preceded by an identifier when
# -we pass them to a function. The order of the arguments 
# -dosen't matter, unlike positional arguments Python knows
# -the names of the arguments that our function receives

#def hello(first, middle, last):
    #print("hello! "+first+" "+middle+" "+last)
#hello(last="Jr", middle="sins", first="jarvis")







# (02:07:09​) nested function calls 🖇️
# nested function calls= function calls inside other function
# -calls
# innermost function calls are resolved first
# returned value is used as argument for the next function

#num= input("Enter a whole positive number: ")
#num= float(num)
#num= abs(num)
#num= round(num)
#print(num)

#print (round(abs(float(input("Enter a whole positive number: ")))))









# (02:09:40​) variable scope 🔬
# scope= the region that a variable is recognized 
# A variable is only availible from inside the region it is
# -created
# A global and locally scoped versions of a variable can be
# -created

# the Python follow suit rules:
    # L = local
    # E = enclosing
    # G = global
    # B = built-in

#name= "Jarvis" #global scope (available inside & outside functions)

#def display_name():
    #name = "Sins" #local scope (available only inside this function)
    #print(name)
    
#display_name()
#print(name)










# (02:13:23​) *args 📦
# *args= parameter that will pack all arguments into a tuple useful
# -so that a function can accept a varying amount of arguments

# *; that is an asterisk- symbol

#def add(num1,num2):
    #sum= num1+num2
    #return sum
#def add(*stuff):
    #sum=0
    #stuff=list(stuff)
    #stuff[0]=0
    
    #for i in stuff:
        #sum += i
    #return sum

#print(add(2,10000,3))







# (02:16:58​) **kwargs 🎁
# **kwargs= paramater that will pack all argumentents into a 
# -dictionary 
#           useful so that a function can accept a varying amount 
# -of keyword arguments

#def hello(first_name,last_name):
    #print("Hello"+" "+first_name+" "+last_name)
    
#hello(first_name="Jarvis",last_name="Sins")

#def hello(**kwargs):
    #print("Hello"+" "+kwargs["first_name"]+" "+kwargs["last_name"])
    #print("hello",end=" ")
    #for key,value in kwargs.items():
        #print(value,end=" ")
        
#hello(first_name="Jarvis", middle_name = "Loftås" ,last_name="Sins")








# (02:21:17​) string format 💬
# str.format()= optional method that gives usere #              more control when diplaying output

#animal = "cow"
#item= "moon"

#print("the "+animal+" jumped over the "+item)
#print("the {} jumped over the {}".format(animal, item))
#print("the {1} jumped over the {1}".format(animal, item))    #positional argument
#print("the {animal} jumped over the {animal}".format(animal="cow", item="moon"))      # keyword argument
#name= input("what is your name:"+" ")
#print("helo {:^10} my name is jarvis".format(name))

#pi=3.14159


#print("pi number≈{0:.2f}".format(pi))


#text= "the {} jumped over the {}"
#print(text.format(animal, item))

#name= "Jarvis "

#print("Hello, my name is {}".format(name))
#print("Hello, my name is {:10}. Nice to meet you".format(name))
#print("Hello, my name is {:<10}. Nice to meet you".format(name))
#print("Hello, my name is {:>10}. Nice to meet you".format(name))
#print("Hello, my name is {name:^10}. Nice to meet you".format(name="Jarvis"))

#number =3.14159
#number=1000000
#cock_length= 21.23234


 
#print("Number is{0:.2f} and my pennis≈{1:.3f}cm".format(number, cock_length))
#print("the number is {:,}".format(number))
#print("the number is {:b}".format(number))    # this will display binary number
#print("the number is {:o}".format(number))   # this will display octal number 
#print("the number is {:X}".format(number))   This will display hexadecimal; x= lower case and X= upper case
#print("the number is {:e}".format(number)) # this will display number as scientific notation; = lover
#print("the number is {:E}".format(number)) # this will display number as scientific notation; = uper










# (02:33:22​) random numbers 🎲
import random

#x=random.randint(1, 6)

#y=random.random()

#myList=["rock","paper","scissors"]
#z=random.choice(myList)

#cards=[1,2,3,4,5,6,7,8,9,"K","Q","A","J"]

#random.shuffle(cards)

#print(z)
#print(y)
#print(x)
#print(cards)

#y= random.random()

#print(("the random number  is{0:.2f}").format(y))










# collection = single "variable" used to store multiple values
    # list = [] ordered and changeable. Duplicates OK
    # set = {} unordered and immutable, but Add/Remove OK. No duplicates
    # Tuple = () ordered and unchangeable, Duplicates OK. FASTER

# [] = square brackets
# {} = curly braces
# () = parantheses 

#fruit = "apple"

#print(fruit)

#fruits= ["apple","orange","banana","coconut", "pineapple"]

#print(fruits[::2])
#print(fruits.count())

#fruits.append("peach")
#fruits[0]= "mango"
#fruits.append("mango")
#fruits.remove("mango")
#fruits.insert(0, "mango")

#fruits.sort()
#fruits.reverse()
#fruits.clear()
#print(fruits.count("apple"))

#print(fruits.index("orange"))
     
#fruits= {"apple","orange","banana","coconut", "pineapple",
         #"apple"}

#fruits.add("peach")
#fruits.remove("apple")
#fruits.pop()
#fruits.clear()

#fruits= ("apple","orange","banana","coconut", "pineapple",
         #"coconut")

#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))
#print("pineapple"in fruits)

#print(fruits.index("pineapple"))

#print(fruits.count("coconut"))

#for fruit in fruits:
    #print(fruit)
    
    
    
    
  
    
  
    

    
# 02:36:43​) exception handling ⚠️
# exeption= events detected during execution that interrupt the
# -flow of a program

#try:
    #numerator = float(input("Enter a number to divide: "))
    #denominator= float(input("Enter a number to divideby: "))
    #result= numerator/denominator
    
#except Exception as e:
    #print(e)
    #print("somthing went wrong")

#except ZeroDivisionError as e:
    #print(e)
    #print("You can't divide by zero")
#except ValueError as e:
    #print(e)
    #print("you can only enter numbers, not words!")
#except Exception as e:
    #print(e)
    #print("Something went wrong")
#else:
    #print(result)
#finally:
    #print("this will always execute")
    
    
    
    
    
    
    
    
    
# while loop= execute some code WHILE some condition remains 
# -true

#name = input("Enter your name: ")
#while name =="":
   # print("you did not enter your name")
#    name = input("Enter your name: ")    
#else:
    #print("hallo {}".format(name))
    
#try:
    #age= int(input("how old are you?: "))
    #while age<0:
        #print("age can't be negative!")
        #age= int(input("how old are you?: "))   
        #print("you are {0}".format(age)) 
     
#except ValueError as e:
    #print(e)
    #print("you should enter your age, not words")
    #age_2= input("the last time enter your age!: ")
#print(f"you are {age_2} years old")

#food= input("Enter a food you like (q as quit): ")

#while not food == "q":
    #print(f"you like {food}")
    #food = input("Enter a food you like (q as quit): ")
    
#print("goodbye")

#num= int(input("enter a number 1 - 10: "))

#while num<1 or num>10:
    #print(f"{num} is not vallid")
    #num= int(input("enter a number 1 - 10: "))
    
#print("your number is {0}".format(num))









#(02:43:40) file detection 📁
# basics of file detection

import os

#path= "/Users/morningstar/Library/Group Containers/UBF8T346G9.ms/Microsoft Word.MERP.params.txt"
#if os.path.exists(path):
    #print("that location excest") 
    #if os.path.isfile(path):
        #print("That is a file")
    #elif os.path.isdir(path):
        #print("that is a directory")
    
#else:
    #print("that location dosen't excest")
     
    
    
 
    
 
# (02:47:28​) read a file 🔍
# open and read a file
#try:    
    #with open("test.txt") as file:
         #print(file.read())
         
#except FileNotFoundError as e:
    #print(e)
    #print("that file was not found")
    
#print(file.closed)
    






# (02:51:00​) write a file 📝
#text=" good morning Tepes\n that a new text\n have a good time\n "
#text= "have a nice day"

#with open("test.txt","a") as file:
    #file.write(text)
    
    
    
    
    
    
    
    
# (02:53:45​) copy a file 🖨️  
# copyfile()= copies contects of a file 
# copy()= copyfile() + permission mode+ destination can be a 
# -directory 
# copy2()= copy() copies metadata (file's creation and 
        #  -modification times)    
       
#import shutil

#shutil.copyfile("text.txt", "copy.txt") #src= sorce dst= destination
 








        
        



    
    
# String methods in Python are easy    
    
# 3. username must not conrain digits

#name = input("Enter your full name: ")
#result = len(name)
#result= name.find(" ")
#result= name.rfind(" ")  # r: stands for reverse 
#name=name.capitalize()
#name = name.upper()
#name = name.lower()
#name= name.isdigit()

#print(name)
#print(result)

#phone_number= input("Enter you phone#: ")
#result=phone_number.count("-")
#result=phone_number.replace("-"," ")
#print(result)

#print(help(str))

# validate user input exercise
# 1. username is no more than 12 characters 
# 2. uername must not contain spaces 
# 3. username must not contain digits

#username= input("Enter your username: ")

#if len(username) > 12:
    #print("your username can't be more than 12 character")
#elif not username.find(" ")==-1:
    #print("Your username can't contain spaces!")
#elif not username.isalpha():
    #print("Your username can't contain numbers")
    
#else:
    #print("Welcome {}".format(username))




           

                



# 02:57:05​) move a file 🗃️
#source="test.txt"
#destination="/Users/morningstar/Downloads/test.txt"

#try:
    #if os.path.exists(destination):
        #print("there is already a file their")
    #else:
        #os.replace(source, destination) 
        #print("{} was replaced".format(source))
        
#except FileNotFoundError:
    #print(f"{source} was not found")






# (03:01:20​) delete a file 🗑️
#path="text.txt"

#try:
    #os.remove(path)  # delete file
    #os.rmdir(path)   # delete an empty directory. rmdir is abbraviation for: remove directory
    #shutil.rmtree(path) # delete a directory containing files. rmtree is abbraviation for: remove tree 
    
#except FileNotFoundError:
    #print("thats file was not found")
#except FileExistsError:
    #print("that file don't excest")
    
#except PermissionError:
    #print("you do not have a permission to delete that")
#except OSError:
    #print("you cannot delete that using that function")
#else:
    #print(f"{path} was deleted")
    
    
    
    
    
 
    

# (03:06:15​) modules 💌
# module= a file containing python code. May contain function
# -, classes, etc.
# used with modular programming, which is to separate a
# -program into parts


#import messages as msg

# another way to call a module

#from messages import hello,bye

#another way to call a module

#from messages import *

# the astresk will call all the functions in module

#msg.hello()
#msg.bye()
#hello()
#bye()

#print(help("module"))  # that will show in console window, all the modules in python



    







# 03:10:26) rock, paper, scissors game 🗿
#while True:
    #choises=["rock","paper","scissor"]

    #computer= random.choice(choises)
 
    #player=input("rock, paper or scissor: ").lower()
    
    #while player not in choises:

        #print(f"you can't chose {player}")
        #print("try again")
        #player=None
        #player=input("rock, paper or scissor: ").lower()
    
    #print("computer: {}".format(computer))
    #print("player: {}".format(player))

    #if player==computer:
        #print("computer: ",computer)
        #print("player: ",player)
        #print("Tie")   
    #elif player== "rock":
        #if computer== "scissor":
            #print("You win")      
        #if computer== "paper":
            #print("you lose")
        
    #elif player== "scissor":
        #if computer== "paper":
            #print("player win")      
        #if computer== "rock":
            #print("you lose") 
        
    #elif player== "paper":
        #if computer== "rock":
            #print("player win")      
        #if computer== "scissor":
            #print("you lose")
    #play_again= input("Play again (yes/no): ").lower()
    #if play_again != "yes": #  !=  ;they mean dose not
        #break
#print("Bye")

    















# (03:18:32​) Quiz-game:

#________________   
#def new_game():
    #guesses=[]
    #correct_guesses=0
    #questions_num=1
    #pass
    #for key in questions:
        #print("-----------------")
        #print(key)
        #for i in options[questions_num-1 ]:
            #print(i)
        #guess= input("Enter A,B,C or D: ").upper()
        #guess=guess.upper()
        #guesses.append(guess)
        
        #correct_guesses+=check(questions.get(key),guess)
    
        #questions_num+=1
    #display_score(correct_guesses,guesses)

#________________  
#def check(answer,guess):
    #if answer ==guess:
        #print("correct")
        #return 1
    #else:
        #print("wrong")
        #return 0

#________________
#def display_score(correct_guesses,guesses):
    #print("-------------")
    #print("results:")
    #print("-------------------")
    #print("answers: ",end="")
    #for i in questions:
        #print(questions.get(i),end=" ")
    #print()
    
    #print("Gusses: ",end=" ")
    #for i in guesses:
        #print((i),end=" ")
    #print()
    #score= int((correct_guesses/len(questions))*100)
    #print(f" your score is {score}%")
    
#________________  
#def play_again():
    #response= input("do you want to play again? (yes/no): ")
    #response= response.capitalize()
    #if response=="Yes":
        #return True 
    #else:
        #return False

#questions={"who created python?: ": "A",
            #"what year was python created?: ":"B",
            #"Python is trilbuted to which comedy group?: ":"C",
            #"Is the Earth round?: ":"A"}





#options  =[["A. Guide van Rossum","B. Elon Musk","C. Bill Gates",
            #"D. Mark Zuckenburg"],
          #["A. 1989","B. 1991","C. 2000","D. 2016"],
          #["A. Lonely Island","B. Smosh","C. Monty Python","D. SNL"],
          #["A. True","B. False","C. sometimes","D. what's Earth"]]
         
#new_game()
        
#while play_again():
    #new_game()
#print("goodbye")
     









# (03:35:45​) Object Oriented Programming (OOP) 🐍

#class car:
    #make =None
    #model= None
    #year= None
    #color = None
    
# def __init__(self,...) = that we call for a constructor were
# -asssigning arguments that we will receive
    #def __init__(self,make, model,year,color):
        #self.make = make
        #self.model= model
        #self.year= year
        #self.color= color
        
    
# def drive/stop(self,...)= that we call for a methods, than mean what can do
    #def drive(self):  # self = refers to the object 
                      # -that is using this method
        
        #print(f"This {self.make} {self.model} is driving")
    #def stop(self):
        #print(f"This {self.make} {self.model} has stopped")
        
        
#car_1=car("Bugatti", "Chiron", 2016, "Orange")
#car_2= car("Ford", "Mustang", 2022,"red")

#print(car_1.make)
#print(car_1.year)
#print(car_1.model)
#print(car_1.color)

#car_1.stop()





# (03:45:06​) class variables 🚗


#class Car:
    
    #wheels = 4              #class variable 
    
    #def __init__(self,make,model,year, color):
        
        #self.make = make    #instance varible
        #self.model = model  #instance varible
        #self.year = year    #instance varible
        #self.color = color  #instance varible
# instance variables is declared inside of constructor and they can be given unique values
# class varibles they are declared with in a class, but also outside of the constructor and you can set a defult value for all instances of this class
        
        
        
#car_1= Car("Bugatti", "Chiron",2016, "orange")
#car_2= Car("Mercedes", "AMG-G63", 2015, "Black")

#print(car_1.wheels)

#Car.wheels= 2

#print(car_1.wheels)
#print(Car.wheels)



    
    
    
    


# (03:48:54​) inheritance 👪  

#class Animal: 
    
    #alive = True
    
    #def eat(self):
        #print("this animal is eating")
        
    #def sleep(self):
        #print("This animal is sleeping")
        
#class Rabbit(Animal):
    #def run(self):
        #print("This rabbit is runing")
        

#class Fish(Animal):
    #pass

#class Hawk(Animal):
    #pass


#rabbit = Rabbit()
#fish = Fish()
#hawk = Hawk()

#print(hawk.alive)
#rabbit.eat()
#fish.sleep()


        

    

# (03:55:30​) multilevel inheritance 👴

# multi-level inheritance = when a derived (child) class 
# - inherits another derived (child) class inherits another 
# - derived (child) class


#class Organisme:
    
    #alive = True
    
#class Animal(Organisme):
    #def eat(self):
        #print("This animal is eating")
        
#class Dog(Animal):
    
    #def bark(self):
        #print("This dog is barking")

#dog = Dog()
#print(dog.alive)

#dog.bark()
#dog.eat()
  





# (03:58:32) multiple inheritance 👨‍👩‍👧‍👦
  
# multiple inheritance = when a child class is derived from 
# -more than one parent class


#class Prey:
    #def flee(self):
        #print("This animal flees")
        
#class Predator: 
    #def hunt(self):
        #print("This animal is hunting")

#class Rabbit(Prey):
    #pass

#class Hawk(Predator):
    #pass

#class Fish(Prey, Predator):
    #pass


#rabbit= Rabbit()
#hawk= Hawk()
#fish=Fish()

#rabbit.flee()
#fish.hunt()
#fish.flee()





# (04:01:49) method overriding 🙅  

# method overriding = is the ability of an object oriented programming language to allow a subclass/child class to provide a specific implementation



#class Animal:
    #def eat(self):
        #print("This animal is eating")
    
#class Rabbit(Animal):
    #def eat(self):
        #print("This rabbit is eating a carrot")

#rabbit= Rabbit()
#rabbit.eat()   
    
    





# (04:04:14​) method chaining ⛓️

# Method chaining = calling multiple methods sequentailly each
# -call performs an action on the same object and returns self


#class Car: 
    
    #def turn_on(self):
        #print("You are start the engine")
        #return self
        
    #def drive(self):
        #print("you drive the car")
        #return self
        
    #def brake(self):
        #print("you stop on the brakes")
        #return self
    
        
    #def turn_off(self):
        #print("you turn off the engine")
        #return self
 
# \(backslash) = this is line continuation character
#car_1= Car()

#car_1.turn_on()\
    #.drive()\
    #.brake()\
    #.turn_off()
    
    
    
    
    
    
    
# (04:08:08) super function 🦸

# super() = Function used to give access to the methods of a 
# -parent class. Returns a temporary object of a parent class
# -when used



#class Rectangle:
        
    #def __init__(self,length, width):
        #self.length= length
        #self.width = width
        
    
#class Square(Rectangle):
    #def __init__(self, length, width):
        #super().__init__(length,width)
        
    #def area(self):
        #return self.length * self.width
    

#class Cuba(Rectangle):
    #def __init__(self, length, width,height):
        #super().__init__(length, width)
        #self.height = height
    #def volume(self):
        #return self.height * self.length * self.width
        

#square = Square(2, 3)
#cuba = Cuba(2,3,3)

#print(square.area())
#print(cuba.volume())






# (04:12:09​) abstract classes 👻

# prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class


# abstract class = a class which contains one or more abstract
# -methods

# abstract methods = a method that has a declaration but does
# -not have an implementation



#from abc import ABC, abstractmethod
#abc= abstract base class  


#class Vehicle(ABC):
    #@abstractmethod    
    #def go(self):
        #pass
    #@abstractmethod
    #def stop(self):
        #pass

#class car(Vehicle):
    #def go(self):
        #print("you driving the car")
    #def stop(self):
        #print("this car is stopped")
        

#class motorcycle(Vehicle):
    #def go(self):
        #print("you ride the motorcycle")
        
    #def stop(self):
        #print("this motorcycle is stopped")


#car_1 = car()
#motorcycle_1 = motorcycle()


#motorcycle_1.go()
#car_1.stop()








# (04:19:12) objects as arguments 🏍️


#class car:
    #color = None
    
#class motorcycle:
    #color = None

#def change_color(vehicle,color):
    #vehicle.color = color
    
    
#car_1= car()
#change_color(car_1,"green")

#car_2= car()
#change_color(car_2,"red")

#motorcycle_1= motorcycle()
#change_color(motorcycle_1, "yellow")

#print(car_1.color)
#print(car_2.color)
#print(motorcycle_1.color)








# (04:23:20​) duck typing 🦆

#Duck typing: concept where the class of an object is less
           #  important than the methods/ attributes 
           #  class type is not checked if minimum
           #  methods/attributes are present 
           #  "If it walks like a duck, and it quacks like a 
           #  duck, then it must be a duck."
           

#class Duck:
    #def walk(self):
        #print("This duck is walking")
        
    #def talk(self):
        #print("This duck i qwuacking")
        
#class Chicken:
   #def walk(self):
        #print("this chicken i walking")
        
    #def talk(self):
        #print("this chicken is clucking")
        
#class Person:
    #def catch(self,duck):
        #duck.walk()
        #duck.talk()
        #print("You caught the critter!")
        
#duck = Duck()
#chicken = Chicken()
#person= Person()

#person.catch(duck)








# (04:27:38) walrus operator 🦦

# walrus operator :=

# new type python 3.8
# assigment expression aka walrus operator 
# assigns values to varibles as part of a larger expression


# happy = True
# print(happy)

# or we can right that in one line of code with using  
# -walrus operator

#print(happy:=True)


#foods = list()

#while True:
    #food = input("What food do you like?: ")
    #if food == "quit":
        #break
    #foods.append(food)
    
    


# assign values to variables as part of a larger expression

#foods= list()    

#while food := input("What food do you like?: ") != "quit":
    #foods.append(food)
    








# (04:31:45​) functions to variables 📛

#def Hello():
    #print("Hello")

#print(Hello)
#hi = Hello

#print(hi)
#Hello()
#hi()

#say = print

#say("i can't belive this works! :O")






# (04:31:45​) functions to variables 📛

# Higher Order Function = a function that either:
                        # 1. accept a function as an argument 
                        #   or
                        # 2. return a function 
                        # (In python, functions are also treated as objects)


#def loud(text):
    #return text.upper()

#def quite(text):
    #return text.lower()

#def Hello(func):
    #text = func("Hello")
    #print(text)
    
    
#Hello(loud)
#Hello(quite)



#def divisor(x):
    #def dividend(y):
        #return y / x
    #return dividend

#divide= divisor(2)

#print(divide(8))





# (04:41:06​) lambda λ

# lambda function = function written in 1 line using lambda 
                  # keyword accepts any number of arbuments,
                  # only has one expression. 
                  # (think of it as a shortcut)
                  # (useful if needed for a short perioded of
                  # time, throw-away)
                  
# lambda parameters:expression


#def double(x):
    #return x*2

#print(double(2))

#double=lambda x: x*2

#multiply = lambda x,y: x*y

#add = lambda x,y,z : x+y+z


#age_check= lambda age: True if age >= 18 else False

#full_name = lambda first_name, last_name: first_name + " "+ last_name
 


#print(multiply(2,4))
#print(full_name("Keylo","Tepes"))
#print(add(2,3,4))
#print(age_check(19))



 




# (04:45:44​) sort 🗄️

# sort() method = used with lists
# sort() function = used with iterables 


#students=["Squidward","Sandy","Patrick","Spongebob","Mr.Krabs"]

#students=("Squidward","Sandy","Patrick","Spongebob","Mr.Krabs")

#students.sort(reverse=True)

#sorted_students = sorted(students,reverse=True)
#for i in students:
    #print(i)
 
#for i in sorted_students:
    #print(i)



#students=(("Squidward","F",60),
          #("Sandy","A",33),
          #("Patrick","D",36),
          #("Spongebob","B",20),
          #("Mr.Krabs","C",78))

#grade = lambda grades: grades[1]
#age = lambda age: age[2]
#students.sort(key= grade,reverse=True)
#students.sort(key=age,reverse=True)
#sorted_students= sorted(students,key=age)

#for i in sorted_students:
    #print(i)







# (04:53:22​) map 🗺️

# map()= applies a function to each item in an iterable (list,tuple and set)


# map(function,iterable)


#store= [("shirt", 20.00),
        #("pants", 25.00),
        #("Jacket",50.00),
        #("socks",10.00)]

#to_euros = lambda data: (data[0],data[1]*0.82)
#to_nok=  lambda data: (data[0],data[1]*11)


#store_euros = list(map(to_euros, store))


#store_nok = list(map(to_nok,store))
#print(store_euros)

#print(store_nok)

#for i in store_nok:
    #print(i)









# (04:57:17​) filter 🍺


# filer() = creates a collection of elements from an iterable 
#           for which a function returns 

# filter(function, iterable)




#friends = [("Rachel", 19),
           #("Monica",18),
           #("Phoebe",17),
           #("Joey",16),
           #("Chandler",21),
           #("Ross",20)]

#age = lambda data: data[1]>= 18

#drinking_buddies= list(filter(age, friends))

#for i in drinking_buddies:
    #print(i)







# (05:00:10​) reduce ♻️

# reduce() = apply function to an iterable and reduce it to 
#            a single cumulative value. Performs function
#            on first two elements and repeats process until
#            1 value remains



#reduce(function, iterable)

import functools

#letters = ["H","E","L","L","O"]
#word = functools.reduce(lambda x,y: x+y, letters)
#print(word)


#facturial = [5,4,3,2,1]

#result= functools.reduce(lambda x,y: x*y, facturial)
#print(result)










# (05:04:54​) list comprehensions 📰

# list comprehension = a way to create a new list with less 
#                      syntax can mimic certain lambda function,
#                      easier to read 
#                      list = [expression (if/else) for item in iterable if conditional]

#squares = []

#for i in range(1,11):
    #squares.append(i**2)
#print(squares)
    
#squares_1 = [i*i for i in range(1,11)]

#print(squares_1)


#students = [100,90,80,70,60,50,40,30,0]

#passed_student = list(filter(lambda x: x>= 60, students))

#passed_student = [i for i in students if i >= 60]
#passed_students = [i if i >= 60 else "idiot" for i in students]

#print(passed_students)









# (05:10:54) dictionary comprehensions 🕮

# dictionary comprehensions = create dictionaries using an  
#                           = expression can replace for loops
#                           = and certain lambda functions


# dictionary = {key: expression for (key,value) in iterable.item()}
# dictionary = {key: expression for (key,value) in iterable.item()
#               if conditional}
# dictionary = {key: (if,else) for (key,value) in iterble.item()}
# dictionary = {key: function(value) for (key,value) in iterable.item()}

# ---------------------------------------------------------

#cities_in_F = {"New York":32, "Bosten": 75,"Los Angeles":100, 
               #"Chicago":50}
#cities_in_c= {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
#print(cities_in_c)

# ---------------------------------------------------------
#weather= {"New York":"Snowing", "Bosten": "sunny",
          #"Los Angeles":"sunny", 
          #"Chicago":"Cloudy"}
#sunny_weather= {key: value for (key,value) in weather.items() if value =="sunny"}
#print(sunny_weather)

# ---------------------------------------------------------

#cities= {"New York":32, "Bosten": 75,"Los Angeles":100, 
               #"Chicago":50}


#cities_measure = {key: value if value >= 50 else "cold" for (key,value) in cities.items() }
#print(cities_measure)

#cities_desc = {key: ("Warm" if value >= 40 else "Cold") for (key,value) in cities.items()}


# ---------------------------------------------------------

#cities= {"New York":32, "Bosten": 75,"Los Angeles":100, 
               #"Chicago":50}
#def check_temp(value):
    #if value >= 70:
        #return ("Hot")
    #elif value >= 40 and value <=79:
        #return "Warm"
    #else:
        #return "COLD"
        


#cities_desc = {key: check_temp(value) for (key,value) in cities.items() }
#print(cities_desc)






# (05:18:59​) zip function 🤐

# zip(*iterables) = aggregate elemnts from two or more
#                   iterbales (list,tuples,set, etc.)
#                   creates a zip object with paired elements
#                   stored in tuples for each elements

#usernames = ["Dude", "Bro","Mister"]
#passwords = ("p@ssword","abc123","guest")
#login_date= ["1/1-2021","2/1-2021","3/1-2021"]


#users= zip(usernames,passwords)

#users= list(zip(usernames,passwords))

#print(type(users))

#for i in users:
    #print(i)

#users= dict(zip(usernames,passwords))

#for key,value in users.items():
   #print(key+" : "+ value)
   
#users = zip(usernames,passwords,login_date)

#for i in users:
   #print(i)
    
#print(type(users))

   
    







#  (05:23:41​) if name == '__main__' ❓

# ********************************************************
# if __name__ == "__main__"
# ********************************************************


# y tho?
# 1) module can be run as a standalone program
# 2) module can be imported and used by other modules 


# Python interpreter sets "special varibles", one of which is
# __name__ then Python will execute the code found within __main__ 



#def Hello():
    #print("hello")
    
#if __name__ =="__main__":
    #pass
    #print("running this module directly")
#else:
    #print("running other module indirectly")
    

# Python interpreter sets "special varibles", one of which is __name__
# Python will assign the __name__ variables a value of "__main__"
# if its the initial module being run  



#import module_two
#print(__name__)
#print(module_two.__name__)










# (05:29:21​) time module ⌚

# epoch = a date and time from which a computer measures system time

#print(time.ctime(0))# convert a time expression in seconds sine 
                     # epock to a readeble string 
                     # epock = when your computer thinks time begin (reference point)

#print(time.time())  #return current seconds since epock

#print(time.ctime(time.time()))


#time_object = time.localtime()
#print(time_object)
#local_time=time.strftime("%B %d %Y %H: %M %S",time_object)
#print(local_time)


#UTC = coordinated Universal Time is the primary time standard by which
#      the world regulates clock and time. It is within about 1 second
#      of men solar time at 0˚ longitude, and is not adjusted for 
#      daylight saving time.
#print(time.gmtime())

#time_string = "20 April, 2021"

#time_object = time.strptime(time_string,"%d %B, %Y")
#print(time_object)


#(year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)

#time_tuple = (2020,4,15,5,30,2,0,0,0)

#time_string = time.asctime(time_tuple)
#print(time_string)


#(year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)

#time_tuple = (2020,4,15,5,30,2,0,0,0)

#time_string = time.mktime(time_tuple)
#print(time_string)








# (05:39:58​) threading 🧵

# thread = a flow of expecuttion. Like a separate order of instructions.
         # However each thread takes a turn running to achieve
         # concurrency 
         # GIL = (global interpreter lock).
         # allows only one thread to hold the control of the Python
         # interpreter at any one time
         
# cpu bound = program/task spends most of it's time waiting for 
#             internal events (CPU intensive) use multiprocessing

# io bound = program/task spends most of it's time waiting for 
#            external events (user input, web scraping) 
#            use multiprocessing 
         

#print(threading.active_count())
#print(threading.enumerate())

import threading



#def eat_breakfast():
    #time.sleep(3)
    #print("You eat breakfast")
     

#def drink_coffee():
    #time.sleep(4)
    #print("you drank coffee")

#def study():
    #time.sleep(5)
    #print("you finish studying")
    
#x = threading.Thread(target=eat_breakfast,args=())

#y = threading.Thread(target=drink_coffee)

#z = threading.Thread(target= study)

#x.start()
#y.start()
#z.start()

#x.join()
#y.join()
#x.join()

#eat_breakfast()
#drink_coffee()
#study()


#print(time.perf_counter())
    







# (05:53:31​) daemon threads 😈

#deamon thread = a thread that runs in the background, not important 
#                for program to run. Your program will not wait for 
#                daemon threads to complete before exiting. Non-daemon
#                threads cannot normally be killed, stay alive until
#                task is complete 

#                ex.background tasks, garbage collection, waiting for
#                input, long running precess 







import threading
import time



#def timer():
    #print()
    #print()
    #count = 0 
    #while True:
        #time.sleep(1)
        #count +=1 
        #print(f"Logged in for {count} seconds")
        
    
#x = threading.Thread(target=timer, daemon=True)
#x.start()

#x.setDaemon(True)
#print(x.isDaemon())

#answer = input("Do you wish to exist?")



from multiprocessing import Process, cpu_count



#def counter(num):
    #count = 0
    #while count < num:
        #count += 1



#def main():
    #a = Process(target = counter ,args= (1000000000,))
    #a.start()
    #a.join()
    #result = time.perf_counter()
    #print(f"finished in: {result} seconds")
    

#if __name__ == "__main__":
    #main()



#from tkinter import *


#label = an area widget that holds text and/or an image wihin a window 


#window = Tk() #instation an instance of a window
#window.geometry("420x420")
#window.title("Jarvis first GUI program")

#icon = PhotoImage(file= "/Users/morningstar/Pictures/johny.jpg")
#window.iconphoto(True,icon)
#window.config(background="black")

#window.mainloop()  #place window on computer screen. listen for events





#68 (06:14:38​) labels 🏷️



#label = an area widget that holds text and/or an image wihin a window

#photo = PhotoImage(file ="/Users/morningstar/Pictures/python_animal.jpg")


#window = Tk()
#label = Label(window,text = "Hellow world",
              #font=("Arial",40, "bold"),
              #fg="green",
              #bg="black", relief= RAISED,
              #bd=10,padx=20,pady=20,
              #image = photo,compound="bottom")



#label.pack()
#label.place(x=100, y=100)


#window.mainloop()




#69 (06:24:24​) buttons 🛎️





#from tkinter import *



#count = 0

#def click(): 
    #print("you click the button")
    #global count
    #count +=1
    #print(count)



# button = you click it, then it does stoff

#window = Tk()
#photo = PhotoImage(file="//Users//morningstar//Pictures//ronnie colmen2.png")


#button = Button(window, text ="click me",command=click, 
                #font=("Comic Sans", 30), fg="#B940D4",
                #bg = "1A18BF",
                #activeforeground="#B940D4",
                #activebackground="1A18BF",
                #state= ACTIVE,
                #image=photo,
                #compound="bottom")


#button.pack()

#window.mainloop()




#70 (06:30:44​) entrybox ⌨️




#from tkinter import *



# netry widget = textbox that accepts a single line 
#                of user input


#def sumbit():
    #username = entry.get()
    #print(f"Hallo {username}")
    #entry.config(state=DISABLED)

#def delete():
    #entry.delete(0,END)

#def backspace():
    #entry.delete(len(entry.get())-1,END)

#window = Tk()


#entry = Entry(window, font=("Arial",50), background="#FCC203",
              #foreground="#03FCF8",
              #show="*")
#etnry.insert(0,"spongbob")
#entry.pack(side=LEFT)


#sumbit_button = Button(window,text="sumbit", command=sumbit)
#sumbit_button.pack(side=RIGHT)

#delet_button = Button(window,text="delete", command=delete)
#delet_button.pack(side=RIGHT)


#backspace_button = Button(window,text="backspace", 
                          #command=backspace)
#backspace_button.pack(side=RIGHT)


#window.mainloop()






#71 (06:40:15​) checkbox ✔️

#from tkinter import *



#def display():
    #if(x.get()==1):
        #print("you agree")
    #else:
        #print("you dont agree")


#window = Tk()
#x = IntVar()

#Python_photo = PhotoImage(file= "/Users/morningstar/Downloads/python_photo_image.png")

#check_button = Checkbutton(window, text="I agree to something",
                           #variable=x,
                           #onvalue=1,
                           #offvalue=0,
                           #command=display,
                           #font=("Arial",20),
                           #foreground="#00FF00",
                           #background="black",
                           #activebackground="black",
                           #activeforeground="#00FF00",
                           #padx=25, pady=10,
                           #image=Python_photo,
                           #compound="left")


#check_button.pack()
#window.mainloop()




#72 (06:49:08​) radio buttons 🔘



# radio button = similar to checkbox, but you can only select one
#                a group 


#from tkinter import *


#food = ["pizza", "hamburger","hotdog"]
#window = Tk()
#x = IntVar()

#def order():
    #if(x.get()==0):
        #print("You ordered pizza")
    #elif(x.get()==1):
        #print("you ordered a hamburger")
    #elif(x.get()==2):
        #print("you ordered a hotdog")
    #else:
        #print("huh?")
        
    
#for index in range(len(food)):
    #radiobutton = Radiobutton(window,
                              #text=food[index], #adds text to radio buttons
                              #variable = x, #groups radiobuttons together if they share the same variable
                              #value=index,
                              #padx= 25, #adds padding on x-axis
                              #font=("Impact",50),
                              #indicatoron=0, #eliminate circle indicators
                              #width=375,#sets width of radio buttons
                              #command=order #sets command of radiobutton to function
                              #)
    #radiobutton.pack(anchor=W)


#window.mainloop()




#73 (07:00:47​) scale 🌡️


#from tkinter import *


#def sumbitt():
    #print(f"tempuratur in {scale.get()} C˚")




#window = Tk()

#hot_image = PhotoImage(file= "/Users/morningstar/Downloads/flame_image3.png")
#hot_label = Label(image=hot_image)
#hot_label.pack()

#scale = Scale(window,from_= 100,
              #to = 0,
              #length=600,
              #orient=VERTICAL, # orientation of the scale
              #font=("Consolas",20),
              #tickinterval=10, # adds numeric indicators for value
              #showvalue=0, #hide current value
              #resolution=5, #increment of slider
              #troughcolor="#69EAFF",
              #foreground="#FF1C00",
              #background="#111111",)

#scale.set((scale["from"]-scale["to"])/2) # set current value of slider
#scale.pack()

#cold_image = PhotoImage(file= "/Users/morningstar/Downloads/ice_image.png")
#cold_label = Label(image=cold_image)
#cold_label.pack()

#button = Button(window, text="Sumbit",command=sumbitt)
#button.pack()

#window.mainloop()






#74 (07:10:24​) listbox 📋

# listbox = a listbox of selectable text items within it's own container

#from tkinter import *


#def sumbit():
    #food = []
    #for i in listbox.curselection():
        #food.insert(i, listbox.get(i))
    #print(f"You have ordered {listbox.get(listbox.curselection())}")
    #print("You have ordered")
    #for i in food:
        #print(i)
        

#def add():
    #listbox.insert(listbox.size(),entry_box.get())
    #listbox.config(height=listbox.size())
    
#def delete():
    #for i in reversed(listbox.curselection()):
        #listbox.delete(i)

    
    #listbox.delete(listbox.curselection())
    #listbox.config(height=listbox.size())
    
    
    
#window = Tk()


#listbox = Listbox(window,
                  #background="#A8A632",
                  #font=("Constantia",35),
                  #width=15,
                  #selectmode=MULTIPLE)


#listbox.insert(1,"pizza")
#listbox.insert(2,"pasta")
#listbox.insert(3,"garlic bread")
#listbox.insert(4,"soup")
#listbox.insert(5,"salad cezar")
#listbox.pack()

#listbox.config(height=listbox.size())

#entry_box = Entry(window)
#entry_box.pack()

#sumbit_button = Button(window,text="sumbit",command=sumbit)
#sumbit_button.pack()

#add_button = Button(window,text="add",command=add)
#add_button.pack()

#delete_button = Button(window,text="delete",command=delete)
#delete_button.pack()

#window.mainloop()








#75 (07:24:41​) messagebox 💭

#from tkinter import *
#from tkinter import messagebox # import massegebox library


#def click():
    #messagebox.showinfo(title="this is an info message box", 
                        #message="you are a person")
    #while(True):
        #messagebox.showwarning(title="WARNING", message="you have a VIRUS!")
    #messagebox.showerror(title= "ERROR",message="something went wrong!")
    #if messagebox.askokcancel(title = "ask ok cancel",message="do you want to do the thing?: "):
        #print("you did the thing")
    #else:
        #print("you canceled a thing")
    #if messagebox.askretrycancel(title="ask ok cancel",message="you want to retry the thing"):
        #print("retried the thing")
    #else:
        #print("you canceled a thing")
    
    #if messagebox.askyesno(title="ask yes or no", message="do you like cake"):
        #print("i like cake too")
    #else:
        #print("you dont like a cake")
        
        
    #answer = (messagebox.askquestion(title="do ask quastion",message="do you like pie"))
    #if(answer) == "yes":
        #print("you like pie")
    #else:
        #print("you dont like pie")
    #answer = messagebox.askyesnocancel(title="yes no cancel",message="do you like to code?: ",icon = "info")
    #if(answer== True):
        #print("you like to code")
    #elif(answer) == False:
        #print("you dont like to code")
    #else:
        #print("you have dodged the question")
    
    
    
#window = Tk()

#button = Button(window, text = "click", command=click)
#button.pack()


#window.mainloop()







#76 (07:37:17​) colorchooser 🎨



#from tkinter import *
#from tkinter import colorchooser #submodule


#def click():
    #color = colorchooser.askcolor()
    #print(color)
    #coloHex = color[1]
    #print(coloHex)
    #window.config(bg=coloHex) #change backround color
    #window.config(background=colorchooser.askcolor()[1]) #altarnativ way to write the code
    
   
    
#window = Tk()
#window.geometry("420x420")
#button = Button(window, text="click me", command=click)
#button.pack()



#window.mainloop() 






#77 (07:43:10​) text area 📒


#text widget = functions like a text area, you can enter multiple lines of text

#from tkinter import *

#def sumbitt():
    #input = text.get("1.0",END)
    #print(input)

#window = Tk()


#text = Text(window,
            #bg="yellow",
            #font=("Inc Free",25),
            #height=8, 
            #width=20,
            #padx=20,
            #pady=20,
            #foreground="purple")
#text.pack()

#button = Button(window,text = "sumbitt",command=sumbitt)
#button.pack()


#window.mainloop()




#78 (07:48:38​) open a file (file dialog) 📁


#from tkinter import *
#from tkinter import filedialog


#def openfile():
    #filepath = filedialog.askopenfilename(title = "open file",
                                          #filetypes =( ("text files","*.txt"),
                                                      #("all files","*.*")))
    #file = open(filepath,"r")
    #print(file.read())
    #file.close()

#window = Tk()

#button= Button(window,text = "upen file",command=openfile)
#button.pack()

#window.mainloop()




#79 (07:55:33​) save a file (file dialog) 💾



#from tkinter import *
#from tkinter import filedialog

#def savefile():
    
    #file = filedialog.asksaveasfile(initialdir="" ,defaultextension = ".txt",filetypes=[
        #("text file",".txt"),("html file",".html"),("all file",".*")])
    
    
    #if file is None:
        #return
    #filetext = text.get(1.0,END)
    #filetext = input("Etner some text: ") //use this if you want to use console terminal
    #file.write(filetext)
    
    #file.close()


#window= Tk()
#button = Button(window, text="save",command=savefile)
#button.pack()

#text = Text(window)
#text.pack()


#window.mainloop()












