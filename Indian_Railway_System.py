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
print("=== Indian Railway Booking System === ")
passenger_name = input("Enter Passenger Name: ")
age =int(input("Enter Age: "))
destination = input("Enter Destination: ")

# Display Booking Conformation
print("\n=== Booking Details ===")
print(f"Passenger: {passenger_name}")
print(f"Age: {age}")
print(f"Destination: {destination}")
print("Booking Confirmed")