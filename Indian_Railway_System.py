# Defining Variables For Indian Railway System

train_name= "Rajdhani Express"
train_number = 12301
ticket_price = 2450.50
is_ac_available = True
seat_number = [1,2,3,4,5]

# Showing the details using print function

# print("Train Name: ",train_name)
# print("Train Number: ",train_number)
# print("Ticket Price:" ,ticket_price)
# print("AC Availability: ",is_ac_available)
# print("Seat Numbers: ",seat_number)

# Show The data types of the variables using type function 

# print("The data type of train_name: ",type(train_name))
# print("The data type of train_number:",type(train_number))
# print("The data type of ticket_price: ",type(ticket_price))
# print("The data type of is_ac_available: ",type(is_ac_available))
# print("The data type of seat_number: ",type(seat_number))


# Getting Passenger Information 
# print("=== Indian Railway Booking System === ")
# passenger_name = input("Enter Passenger Name: ")
# age =int(input("Enter Age: "))
# destination = input("Enter Destination: ")

# # Display Booking Conformation
# print("\n=== Booking Details ===")
# print(f"Passenger: {passenger_name}")
# print(f"Age: {age}")
# print(f"Destination: {destination}")
# print("Booking Confirmed")

# #Arithmetic Operators

# basic_price = 1500
# service_charge = 100
# total_price = basic_price + service_charge
# print(f"Base Price: ₹{basic_price}")
# print(f"Service Charge: ₹{service_charge}")
# print(f"Total Price: ₹{total_price}")

# # Comparison Operators
# passenger_age =25
# senior_citizen_age = 60
# is_senior = passenger_age >= senior_citizen_age

# print(f"\n Is passenger senior citizen? {is_senior}")

# Logical Operator

# has_ticket = True
# has_id_proof = True
# can_board = has_ticket and has_id_proof

# print(f"Can Board Train? {can_board}")

# Control Flow - IF Statments

# Age Based Pricing 

# Age = int(input("Enter Passenger Age: "))

# if Age < 5:
#     price = 0
#     category = "Infant (Free)"
# elif Age < 12:
#     price = 750
#     category = "Child (50% Discount)"
# elif Age >= 60:
#     price = 1200
#     category = "Senior Citizen (20% Discount)"
# else:
#     price = 1500
#     category = "Adult"
    
# print(f"Category: {category}")
# print(f"Ticket Price: ₹{price}")        
    
# For Loop - Display Available trains 

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
 
    
 # While Loop - Booking System
 
# print("\n ==== Booking Menu ====")
# choice = 0

# while choice != 3:
#     print("1. Book Ticket")
#     print("2. Check Status")
#     print("3. Exit")
#     choice = int(input("Enter Your Choice: "))
    
#     if choice == 1:
#         print("Booking ticket .........")
#     elif choice == 2:
#         print("Checking Status")
#     elif choice == 3:
#         print("Thank you for using Indian Railways!")
#     else:
#         print("Invalid Choice!")   
        
# Ticket_price = 1800                                          # Example Ticket Booking System
# name = input("Enter Passenger Name: ")                           # ------ Discount Calculatio
# passenger_age = int(input("Enter Passenger Age: "))
# destination = input("Enter Destination: ") 

# print("\n ===== Passenger Booking Details\n")
# if passenger_age <= 5:
#     print(f"Pasenger Name: {name}")
#     print(f"Destination: {destination}")
#     print("Category: Infant")
#     print(f"Ticket Price: 0")
# elif passenger_age <=18:
#      print(f"Pasenger Name: {name}")
#      print(f"Destination: {destination}")
#      print("Category: Young") 
#      discounted_price = Ticket_price - (Ticket_price * 0.20)  
#      print(f"Base Ticket Price: {Ticket_price} \nDiscounted Ticket Price: {discounted_price}")
# elif passenger_age <= 45:
#     print(f"Pasenger Name: {name}")
#     print(f"Destination: {destination}")
#     print("Category: Adult")  
#     discounted_price = Ticket_price - (Ticket_price * 0.35)  
#     print(f"Base Ticket Price: {Ticket_price} \nDiscounted Ticket Price: {discounted_price}")                   
# elif passenger_age <= 60:
#     print(f"Pasenger Name: {name}")
#     print(f"Destination: {destination}")
#     print("Category: Senior") 
#     discounted_price = Ticket_price - (Ticket_price * 0.50)  
#     print(f"Base Ticket Price: {Ticket_price} \nDiscounted Ticket Price: {discounted_price}")  
# else: 
#     print(f"Pasenger Name: {name}")
#     print(f"Destination: {destination}")
#     print("Category: Old")     
#     discounted_price = Ticket_price - (Ticket_price * 0.70)  
#     print(f"Base Ticket Price: {Ticket_price} \nDiscounted Ticket Price: {discounted_price}")  


# Ticket Price Calculator

# def calculated_ticket_price(distance,class_type):
#     base_rate = 0.5

#     if class_type == "Sleeper":
#         multiplier = 1.0
#     elif class_type == "AC 3 Tier":
#         multiplier = 2.0
#     elif class_type == "AC 2 Tier":
#         multiplier = 2.5
#     elif class_type == "AC 1 Tier":
#         multiplier = 3.0
#     else:
#         multiplier = 1.0
#     price = distance * base_rate * multiplier

#     return round(price,2)

# distance = 500
# Class_type = "Sleeper"
# price = calculated_ticket_price(distance,Class_type)

# print(f"Price for {distance}km in {Class_type} : ₹{price}")


# Ticket Booking ---------------------------------------------------------------------

# def book_ticket(passenger_name,age,destination,class_type = "Sleeper"):
#     Ticket = {
#         "Passenger Name" : passenger_name,
#         "Age" : age,
#         "Destination" : destination,
#         "Booking ID" :f"BK{hash(passenger_name)% 10000:04d}"
#     }
#     return Ticket

# def get_passenger_details(*args,**kwargs):
#     print("Positional arguments : ",args)
#     print("Keyword arguments : ",kwargs)


# ticket1 = book_ticket("Samyak Ubale",22,"Goa","AC 1 tier")
# ticket2 = book_ticket("Priya Singh",21,"Delhi","AC 3 tier")

# print("\nTicket 1 : ",ticket1)
# print("\nTicket 2 : ",ticket2)

# get_passenger_details("Samyak",22,"Goa",class_type = "AC 1 tier",Meal_Preference = "NON-VEG")        
        
# Calculate DIscounts

# calculate_discount = lambda price,discount_percentage : price * (1 - discount_percentage/100)

# original_price = 1500

# dicounted_price = calculate_discount(original_price,20)

# print(f"Original Price: ₹{original_price}, Discounted Price: ₹{dicounted_price}")

# trains = [
#     {"name":"Rajdhani","price":2500,"duration":16},
#     {"name":"Shatabdi","price":1800,"duration":8},
#     {"name":"Duronto","price":2000,"duration":12},
# ]

# # Map ------------

# train_names = list(map(lambda x: x['name'],trains)) 
# print(f"\nTrain Names: {train_names}")

# # Filter ------------------

# affordable_trains = list(filter(lambda x: x['price'] <2200, trains))
# print(f"\nAffordable Train Names: ",[t["name"]for t in affordable_trains])

# # Sorted ----------------------

# sorted_by_price = sorted(trains,key=lambda x: x["price"])
# print("\nSorted by price: ",[t["name"] for t in sorted_by_price])

# OOP Based Train System -------------------------------

# class Train:
    
#     def __init__(self,train_no,train_name,source,destination,total_seats):
#         self.train_no = train_no
#         self.train_name = train_name
#         self.source = source
#         self.destination = destination
#         self.total_seats = total_seats
#         self.available_seats = total_seats
        
#     def display_info(self):
#         print(f"{self.train_no} - {self.train_name}")
#         print(f"Route: {self.source} to {self.destination}")
#         print(f"Available Seats: {self.available_seats}/{self.total_seats}") 
        
#     def book_seats(self):
#         if self.available_seats > 0:
#             self.available_seats -= 1
#             return True
#         return False

# train1 = Train(12301,"Rajdhani Express","Howrah","New Delhi",700)
# train2 = Train(12502,"Deccan Express","CSMT","Pune",500)
# train3 = Train(12701,"Chennai Express","LTT","Chennai",650)

# print(" === Train Information ===")
# train1.display_info()
# print()
# train2.display_info()
# print()
# train3.display_info()

# print("\n === Booking Tickets ===")

# if train1.book_seats():
#    print("Seats Booked Successfully in Rajdhani Express!!")
#    train1.display_info()
 
# class Train:
#     def __init__(self,train_no,train_name,source,destination):
#         self.train_no = train_no
#         self.train_name = train_name
#         self.source = source
#         self.destination = destination
        
#     def get_info(self):
#         return f"{self.train_no} - {self.train_name}"    
                    
# class ExpressTrain(Train):
#     def __init__(self,train_no,train_name,source,destination,max_speed):
#         super().__init__(train_no,train_name,source,destination)
#         self.max_speed = max_speed
        
#     def get_info(self):
#         base_info = super().get_info()
#         return f"{base_info} Max Speed: {self.max_speed} km/h"
    
# class PassengerTrain(Train):
#     def __init__(self,train_no,train_name,source,destination,stops):
#         super().__init__(train_no,train_name,source,destination)
#         self.stops = stops

#     def get_info(self):
#         base_info = super().get_info()
#         return f"{base_info} (Total Stops: {len(self.stops)})"
    
# express = ExpressTrain(12301,"Rajdhani Express","Howrah","New Delhi",135)
# passenger = PassengerTrain(11301,"Sinhagad Express","CSMT","Pune",["CSMT","Kalyan","Karjat","Lonavla","Shivajinagar","Pune"])

# print("=== Train Types ====")
# print(f"Express Train: {express.get_info()}")
# print(f"Passenger Train: {passenger.get_info()}")


# Encapsulation  ---------------------------------------------------------------------

# class BankAccount:
#     def __init__(self, account_no,initial_balance=0):
#         self._account_no = account_no            # Protected Attribute
#         self.__balance = initial_balance         # Private Attribute
    
#     @property
#     def balance(self):
#         return self.__balance   
    
#     @property
#     def account_number(self):
#         return self._account_no
    
#     def deposit(self,amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited Amount: ₹{amount}. Current Balance: ₹{self.__balance}.")
#         else:
#             print("Invalid Amount !!!")  
            
#     def withdraw(self,amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrawl Amount: ₹{amount}. Current Balance: ₹{self.__balance}.")
#         else:
#             print("Insufficient Balance")    
            
# class Ticket:
#     def __init__(self,passenger_name,train_no,seat_number):
#         self.__passenger_name = passenger_name
#         self.__train_no = train_no
#         self.__seat_number = seat_number
#         self.__is_confirmed = False
        
#     def Confirm_ticket(self):
#         self.__is_confirmed = True
        
#     def Details(self):
#         status = "Confirmed" if self.__is_confirmed else "Pending"
#         return{
#             "Passenger: ":self.__passenger_name,
#             "Train: ":self.__train_no,
#             "Seat Number: ":self.__seat_number,
#             "Status: ": status      
#         } 

# print("=== Bank Account ===")

# account = BankAccount("SBI9461820529") 
# account.deposit(5000)
# account.withdraw(1500)
# print("Current Balance: ₹",account.balance)

# print("\n=== Ticket Confirmation")     

# ticket = Ticket("Suraj Thange",12301,"A1")
# print("Before Confirmation: ",ticket.Details())
# ticket.Confirm_ticket()
# print("After Confirmation: ",ticket.Details())  
           
# Polymorphism 

class Paymentmethod:
    def process_payment(self,amount):
        raise NotImplementedError("Subclass must implement abstract method")  
    
class CreditCard(Paymentmethod):
         
      
         

            

 
 
 
 
 
 
 
 