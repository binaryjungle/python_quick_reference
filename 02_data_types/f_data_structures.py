#Beginning of the program
print("Beginning Of the Program")
print("")

#Range is created using range function
#Range gives sequence of numbers from 0 until the value we provide as argument to the function
series = range(10)

#List is created using square brackets
flights = ["AA001", "AA002", "AA003"]

#Tuple is created using parenthesis
gender = ("Male", "Female", "Transgender")

#One more example of tuple
planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto")

#Dictionary is created using curly/set brackets
flight_class_price = {"Economy":10, "Economy + Leg Space":15, "Business":30}

#Printing the assigned values of various data structures
print(f"flights are : {flights} and its type is {type(flights)}")
print(f"gender is : {gender} and its type is {type(gender)}")
print(f"planets are : {planets} and its type is {type(planets)}")
print(f"flight_class_price is : {flight_class_price} and its type is {type(flight_class_price)}")

#Data structures can be used as iterables and iterables can be used in for loop
#We can access individual item from the data structures using for loop 
for looper in series:
    print("Range values are:", looper)

for looper in flights:
    print("Flight ID:", looper)

for looper in gender:
    print("Genders are:", looper)
    
for looper in planets:
    print("Planets are:", looper)

for looper_key, looper_value in flight_class_price.items():
    print(f"{looper_key} : {looper_value}")

#Conversion of one data structure to another structure is easy using functions like list, tuple and so on
#List is converted to tuple
tupled_flights = tuple(flights)

#Tuple is converted to list
listed_gender = list(gender)

#Range is converted to tuple
tupled_series = tuple(range(9))

#Range is converted to list
listed_series = list(range(9))

#Dictionary keys are converted to list
listed_dict_keys = list(flight_class_price.keys())

#Dictionary keys are converted to tuple
tupled_dict_keys = tuple(flight_class_price.keys())

#Dictionary values are converted to list
listed_dict_values = list(flight_class_price.values())

#Dictionary values are converted to tuple
tupled_dict_values = tuple(flight_class_price.values())

#Printing the assigned values of various data structures
print(f"tupled_flights are : {tupled_flights} and its type is {type(tupled_flights)}")
print(f"listed_gender is : {listed_gender} and its type is {type(listed_gender)}")
print(f"tupled_series is : {tupled_series} and its type is {type(tupled_series)}")
print(f"listed_series is : {listed_series} and its type is {type(listed_series)}")
print(f"listed_dict_keys are : {listed_dict_keys} and its type is {type(listed_dict_keys)}")
print(f"tupled_dict_keys are : {tupled_dict_keys} and its type is {type(tupled_dict_keys)}")
print(f"listed_dict_values are : {listed_dict_values} and its type is {type(listed_dict_values)}")
print(f"tupled_dict_values are : {tupled_dict_values} and its type is {type(tupled_dict_values)}")

#End of the program
print("")
print("End Of the Program")