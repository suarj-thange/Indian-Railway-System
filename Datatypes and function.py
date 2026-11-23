# List ----------------------------------------------------------------------------

# states = ["Maharastra","Kerla","Punjab","Tamil Nadu","Gujrat"]
# print("Original List: ",states)

# states.append("Karnataka")
# states.insert(2,"Rajasthan")
# print("After Append & Insert: ",states)

# states.extend(["Goa","Bihar"])
# print("After Extend: ",states)

# states.remove("Bihar")
# popped = states.pop()
# print("Removed Elements: ",popped)
# print("After Remove & pop: ",popped)

# # Sorting And Reverse

# states.sort()
# print("Sorted List: ",states)
# states.reverse()
# print("Reversed List: ",states)

# print("Index of Kerla: ", states.index("Kerla"))
# print("Count of kerla: ", states.count("Kerla"))

# copy_states = states.copy()
# print("Copied List: ", copy_states)
# states.clear()
# print("Cleared List: ", states)

# Tuple -------------------------------------------------------

# cities = ("Mumbai","Delhi","Bengluru","Chennai","Kolkata","Mumbai","Pune")
# print ("Tuple: ", cities)

# # Count
# print("Count of Mumbai: ", cities.count("Mumbai"))

# # Index 
# print("Index of Kolkata: ",cities.index("Kolkata"))

# # Length
# print("Length: ",len(cities))

# # Membership
# print("Delhi in tuple?","Delhi" in cities)

# # Min & Max (Alphabetically)
# print("Min: ", min(cities))
# print("Max: ",max(cities))

# Dictonary -----------------------------------------------------

# capitals = {
#     "Maharashtra": "Mumbai",
#     "Kerala": "Thiruvananthapuram",
#     "Tamil Nadu": "Chennai",
#     "Gujrat": "Gandhinagr"
# }
# print("Dictonary:", capitals)

# # Get & Access 

# print("Capital of Maharashtra: ",capitals.get("Maharashtra"))

# # keys, Values, Items

# print("States: ", capitals.keys())
# print("Capitals: ", capitals.values())
# print("Pairs: ", capitals.items())

# #Update & Add

# capitals.update({"Goa": " Panji"})
# capitals["punjab"]= "Chandigarh"
# print("After Update: ",capitals)

# #Remove 
# capitals.pop("Tamil Nadu")
# capitals.popitem()
# print("After Pop & Popitem: ",capitals)

# # Copy & Clar 
# Copy_caps = capitals.copy()
# capitals.clear()
# print("Copie: ", Copy_caps)
# print("Cleared: ", capitals)

# SET  ---------------------------------------------

# languages = {"Marathi","Hindi","English","Tamil","Telugu"}
# print("Original Set:", languages)

# # Add & Remove

# languages.add("Gujrati")
# languages.discard("English")
# print("After Add & Discard: ",languages)

# languages.remove("Telugu")

# # Set Operations 

# south = {"Tamil","Telugu","Kannada"}
# print("Union: ",languages.union(south))
# print("Intersection: ",languages.intersection(south))
# print("Difference: ",languages.difference(south))
# print("Symmetric Difference: ",languages.symmetric_difference(south))

# # Copy & Clear

# copy_lang = languages.copy()
# languages.clear()
# print("Copied: ", copy_lang)
# print("Cleared: ",languages)

# String -----------------------------------------------------

# movie = "Sholay is A Classic Bollywood Movie"
# print("Original: ",movie)

# #Case

# print(movie.upper())
# print(movie.lower())
# print(movie.title())
# print(movie.capitalize())
# print(movie.swapcase())

# # Check
# print(movie.startswith("Sholay"))
# print(movie.endswith("Movie"))
# print("Is Alpha?", movie.isalpha())
# print("Is Digit?",movie.isdigit())

# # Find & Replace 

# print("Find 'Classic':",movie.find("Classic"))
# print(movie.replace("Classic", "Legendray"))

# # Split & Join 

# words = movie.split()
# print("Split: ",words)
# joined = "-".join(words)
# print("Joined: ",joined)

# # Strip 

# line = "    Jai Hind    "
# print("Stripped: ",line.strip())
# print("Left Strip: ", line.lstrip())
# print("Right Strip: ", line.rstrip())

# # Count  & Index 

# print("Count of 'o' : ", movie.count("o"))
# print("Index of 'Bollywood' : ",movie.index("Bollywood"))

# # Length

# print("Length: ",len(movie))

# Date & Time --------------------------------------------------------------

# import datetime

# # Current date & time

# now = datetime.datetime.now()
# print("Now: ", now )

# # Today

# today = datetime.date.today()
# print("Today: ",today)

# # Specific Date 
# birth_date = datetime.date(2005,3,10)
# print("Birth Date: ",birth_date.strftime("%d-%B-%Y"))

# # Time Difference 

# diff = today - birth_date
# print("Days Since Birth: ",diff.days)

# #Current Components

# print("Year: ",now.year)
# print("Month: ",now.month)
# print("Day: ",now.day)
# print("Hour: ",now.hour)
# print("Minute: ",now.minute)
# print("Second: ",now.second)

# # Create a time object 

# t = datetime.time(10, 30, 15)
# print("Custom Time: ",t)

# # Combine date & time 

# dt = datetime.datetime.combine(today,t)
# print("Combined Datetime: ", dt)

# # Formating 
# print("Formatted: ", now.strftime("%A, %d %B %Y %I:%M %p"))





