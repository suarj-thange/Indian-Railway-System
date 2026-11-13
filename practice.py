# for i in range(1,11,2):
#     print(i)

# for i in range(1,21):            # even no
#     if i %2 ==0:
#      print(i)    
         
# for i in range(1,21):           # odd no
#     if i %2 !=0:
#      print(i) 


# num = 5                          # Table Example
# for i in range(1,11):
#     print(num, "x", i, "=", num*i)
     
# total = 0                            # sum of numbers in range 
# for i in range (1,11):
#     total = total + i
# print("Total: ",total)     
     
# num = 5                 # Factorial Example
# fact = 1

# for i in range(1,num + 1):
#     fact = fact * i
# print("Factorial: ",fact)      


# chars = "Python"              # Character in single string
# for char in chars:
#     print(char)

# names =["Suraj","Tejas","Om","Yash"]         # Character in list Sequencley
# for name in names:
#     print(name)    
    
# num  = [10,30,20,45,40,200,60,202,756]         # Find Largest Number in list
# largest = num[0]
# for i in num:
#     if i > largest:
#         largest = i 
# print("The Largest Number: ",largest)        

# text = "python programming"           # Count Number Of Vowels (IN)
# count = 0
# for char in text:
#     if char in "aeiou":
#         count +=1
# print("Number Of Vowels: ",count)        
              
# While loop----------

# i = 1                     # Print while condnition Fails
# while i <= 10:
#     print(i)
#     i+=1
    
# i=1                      #
# total=0
# while i <= 10:
#     total += i
#     i += 1 
# print("Total: ",total) 

# num = 12345                     # Reverse
# reverse =0 

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num //= 10
    
# print("Reverse Number: ", reverse)    

# num = 7532484237                   -- Count Numbers
# count = 0
# while num > 0:
#     num //= 10
#     count += 1

# print("The Number of digits: ", count)

# correct_number = 4                           ------- Guess Number

# guess = int(input("Enter a number: "))
       
# while guess != correct_number:
#      print("Wrong Number!!")
     
#      guess  = int(input("Enter a number: ")) 
     
# print("Correct Guess!!")           

# loop control statment

# for i in range(20):            ---------------- Break
#     if i == 12:
#         break 
#     print(i)
    
# for i in range(20):       ---------- Continue
#     if i == 12:
#         continue 
#     print(i)   


# ----------- Assingn Variables

train_name = "Mahalakshmi Express"           
train_number = 12001
ticket_price = 1800.00
is_ac_available = True
seat_number = [1,2,3,4,5,6,7,8,9,10]

# print("Train Name: ",train_name)              
# print("Train Number: ",train_number)
# print("Ticket Price:" ,ticket_price)
# print("AC Availability: ",is_ac_available)
# print("Seat Numbers: ",seat_number)      

# print("The data Type of train_name: ",type(train_name))              ------ print variables data type
# print("The data type of train_number:",type(train_number))
# print("The data type of ticket_price: ",type(ticket_price))
# print("The data type of is_ac_available: ",type(is_ac_available))
# print("The data type of seat_number: ",type(seat_number))

# print("=== Indian Railway Booking System ====")                   ---------- input 

# passenger_name = input("Enter Passenger Name: ")
# Age = input("Enter Passenger Age: ")
# Destination = input("Enter Destination: ")

# print("\n === Passenger Booking Details ===")              ----------- print input 
# print(f"Passenger Name: {passenger_name}")
# print(f"Passenger Age: {Age}")
# print(f"Destination: {Destination}")
# print("\n Booking Confirmed !!!")

# base_price = 1800                               --------- Arithmetic Operation
# service_charge = 150
# total_price = base_price + service_charge

# print(f"Base Ticket Price: ₹{base_price}")
# print(f"Service Charge: ₹{service_charge}")
# print(f"Total Ticket Price: ₹{total_price}")


# has_ticket = True                         ----- Logical operator
# has_id_proof = True
# can_board = has_ticket and has_id_proof
# print(f"Can Board Train? {can_board}")

# passenger_age = int(input("Enter Passenger Age: "))                   -------- if condition

# if passenger_age < 5:
#     print("Category: Infant")
# elif passenger_age <= 18:
#     print("Category: Young")
# elif passenger_age <= 45:
#     print("Category: Adult")
# elif passenger_age <= 60:
#     print("Category: Senior")
# else: 
#   print("Category: Old")    
                
# Ticket_price = 1800                                          ------ Discount Calculation
# passenger_age = int(input("Enter Passenger Age: ")) 

# if passenger_age <= 5:
#     print("Category: Infant")
#     print(f"Ticket Price: 0")
# elif passenger_age <=18:
#      print("Category: Young") 
#      discounted_price = Ticket_price - (Ticket_price * 0.20)  
#      print(f"Base Ticket Price: {Ticket_price} \n Discounted Ticket Price: {discounted_price}")
# elif passenger_age <= 45:
#     print("Category: Adult")  
#     discounted_price = Ticket_price - (Ticket_price * 0.35)  
#     print(f"Base Ticket Price: {Ticket_price} \n Discounted Ticket Price: {discounted_price}")                   
# elif passenger_age <= 60:
#     print("Category: Senior") 
#     discounted_price = Ticket_price - (Ticket_price * 0.50)  
#     print(f"Base Ticket Price: {Ticket_price} \n Discounted Ticket Price: {discounted_price}")  
# else: 
#     print("Category: Old")     
#     discounted_price = Ticket_price - (Ticket_price * 0.70)  
#     print(f"Base Ticket Price: {Ticket_price} \n Discounted Ticket Price: {discounted_price}")  

# trains = [
#     {"name": "Rajdhani Express",
#      "number": 12301,
#      "destination": "New Delhi"},
#     {"name": "Shatabi Express",
#      "number": 12001,
#      "destination": "Chennai"},
#     {"name": "Duronto Express",
#      "number": 12291,
#      "destination": "Mumbai"}
# ]   
# print("Available Trains: ")
# for train in trains:
#     print(f"{train['number']} - {train['name']} to {train['destination']}")

# num = 7
# fact = 1
# for i in range(1,num + 1):
#     fact = fact * i

# print("Factorial: ",fact)

# def greet():
#     print("Hello Mister/Miss!!!")

# greet() 

# def greet():
#     name = input("Enter Your Name! : ")
#     print(f"Hello {name}!, How are you?")
    
# greet()  

# def greet(name):
#     print(f"Hello {name}!, How are you?") 
    
# greet("Suraj")

# def greet(name="Guest"):
#     print(f"Hello! {name}! How are you?")
    
# greet("Suraj") 

# def welcome():
#     print("Welcome to the proffesional Course!!!")
#     print("Let's Learn Data Science!!!") 

# welcome() 

# def age_verification():
#     age = int(input("Enter your age: "))
    
#     if age>=18:
#         print("Applicable for the License !!!")
#     else:
#         print("Try Again Next Time")
        
# age_verification()            
                                      
# Login System 
                                      
# def login(user_name):     
#     password = input("Enter your password: ")
#     while password != "suraj123":
#         print("Wrong Password")
#         password = input("Enter your password: ")    
#     else:
#         print(f"Hello! {user_name}")
  
# login("Suraj")       

# def add(a,b):
#     return a+b 

# def multiply(x,y):
#     print(x*y)
    
# add(2,3)
# multiply(2,3)

# print("Add: ",add(2,3))
# print("Multiply: ",multiply(2,3)) 

# def student(name,age):
#     print(f"{name} is {age} years old !!!")
    
# student("suraj",22)

# def total_score(*marks):
#     print("Marks: ",marks)
#     print("Total Score: ",sum(marks))
#     print("percentage: ",sum(marks)/len(marks))
    
# total_score(85, 97, 99)
 
# def total_score(*marks):
#     print("Marks: ",marks)
#     print("Total Score: ",sum(marks)) 
#     import numpy as np
#     print("percentage: ",np.mean(marks))            
    
# total_score(85, 97, 99)

# def employee_details(**details):
#     for key,value in details.items():
#         print(key,":",value)
        
# employee_details(
#     Emp_name = "Suraj",
#     Age = 22,
#     Department = "IT",
#     Salary = "10k"
# )

