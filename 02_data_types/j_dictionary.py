#Beginning of the program
print("Beginning Of the Program")
print("")

#dictionaries are created by key values pair seperated by commas and enclosed within curly braces
#key and values are seperated by colon
#key and values can be of any data types
#keys must be unique
#if duplicate keys are present, latest key will be chosen
a_dict = {"a":1, "b":2, "c":3, "d":4, "e":5}
print (a_dict)
a_dict = {"a":1, "b":2, "c":3, "d":4, "e":5, "e":7}
print (a_dict)

#1 way of creating dictonaries
flight_class_price = {"Economy":10, "Economy + Leg Space":15, "Business":30}
print(flight_class_price)

#2nd way of creating dictonaries
flight_class_price = dict(Economy=10, Economy_Leg_Space=15, Business=30)
print(flight_class_price)

#dictionaries can be assigned to another dictionary
#type 1
dup_flight = flight_class_price
print(dup_flight)

#type 2
dup_flight = {**flight_class_price}
print(dup_flight)

#type 2 used practically to create another dictionary in addition to new values
dup_flight = {"Premium":12, **flight_class_price}
print(dup_flight)

#retriving from dictionaries can be done using for loops
#variable for key can be used in for loop
for looper in flight_class_price: print(looper, ":", flight_class_price[looper])

#item method is used to assign both keys and values to variables of for loop
for k, v in flight_class_price.items(): print(k, ":", v)

#keys method is used to get only the keys
for looper in flight_class_price.keys(): print(looper)

#values method is used to get only the values
for looper in flight_class_price.values(): print(looper)

#sorted function can be used to sort the keys or values
for looper in sorted(flight_class_price.keys()): print(looper)
for looper in sorted(flight_class_price.values()): print(looper)

#Values of specific key can be retrieved by providing the key within square brackets
print(flight_class_price["Economy"])

#Values of specific key can also be retrieved using get method
print(flight_class_price.get("Economy"))
#if key is not available, None is returned
print(flight_class_price.get("Premium"))
#if key is not available, None can be overridden with custom value/message
print(flight_class_price.get("Premium", "Not_Available"))

#get can be used for comparison
#when key is not found
if flight_class_price.get("Standard") != None:
    print("Class Exists")
else:
    print("No such class found")
#when key is found
if flight_class_price.get("Economy") != None:
    print("Class Exists")
else:
    print("No such class found")

#in operator can also be used for comparing the keys
if "Standard" in flight_class_price:
    print("Class Exists")
else:
    print("No such class found")

#Removing can be done using the key
del dup_flight["Premium"]
print(dup_flight)

#updates the value of the key if the key exists
flight_class_price["Economy"] = 11
print(flight_class_price)

#adds new key if the key doesn't exists
flight_class_price["Premium"] = 20
print(flight_class_price)

#End of the program
print("")
print("End Of the Program")