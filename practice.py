# for i in range(1,11,2):
#     print(i)

# for i in range(1,21):            # even no
#     if i %2 ==0:
#      print(i)    
         
# for i in range(1,21):           # odd no
#     if i %2 !=0:
#      print(i) 


# num = 5
# for i in range(1,11):
#     print(num, "x", i, "=", num*i)
     
# total = 0
# for i in range (1,11):
#     total = total + i
# print("Total: ",total)     
     
# num = 5 
# fact = 1

# for i in range(1,num + 1):
#     fact = fact * i
# print("Factorial: ",fact)      


# chars = "Python"

# for char in chars:
#     print(char)

# names =["Suraj","Tejas","Om","Yash"]
# for name in names:
#     print(name)    
    
# num  = [10,30,20,45,40,200,60,202,756]

# largest = num[0]
# for i in num:
#     if i > largest:
#         largest = i 
# print("The Largest Number: ",largest)        

# text = "python programming"
# count = 0
# for char in text:
#     if char in "aeiou":
#         count +=1
# print("Number Of Vowels: ",count)        
              
# While loop----------

# i = 1

# while i <= 10:
#     print(i)
#     i+=1
    
# i=1
# total=0
# while i <= 10:
#     total += i
#     i += 1 
    
# print("Total: ",total) 

# num = 12345                    -- Reverse
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
    
for i in range(20):      
    if i == 12:
        continue 
    print(i)   




                           