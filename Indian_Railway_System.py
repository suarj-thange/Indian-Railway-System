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

def calculated_ticket_price(distance,class_type):
    base_rate = 0.5

    if class_type == "Sleeper":
        multiplier = 1.0
    elif class_type == "AC 3 Tier":
        multiplier = 2.0
    elif class_type == "AC 2 Tier":
        multiplier = 2.5
    elif class_type == "AC 1 Tier":
        multiplier = 3.0
    else:
        multiplier = 1.0
    price = distance * base_rate * multiplier

    return round(price,2)

distance = 500
Class_type = "Sleeper"
price = calculated_ticket_price(distance,Class_type)

print(f"Price for {distance}km in {Class_type} : ₹{price}")


# Ticket Booking

def book_ticket(passenger_name,age,destination,class_type = "Sleeper"):
    Ticket = {
        "Passenger Name" : passenger_name,
        "Age" : age,
        "Destination" : destination,
        "Booking ID" :f"BK{hash(passenger_name)% 10000:04d}"
    }
    return Ticket

def get_passenger_details(*args,**kwargs):
    print("Positional arguments : ",args)
    print("Keyword arguments : ",kwargs)


ticket1 = book_ticket("Samyak Ubale",22,"Goa","AC 1 tier")
ticket2 = book_ticket("Priya Singh",21,"Delhi","AC 3 tier")

print("\nTicket 1 : ",ticket1)
print("\nTicket 2 : ",ticket2)

get_passenger_details("Samyak",22,"Goa",class_type = "AC 1 tier",Meal_Preference = "NON-VEG")        
        


            


 
 
 
 
 
 
 
 