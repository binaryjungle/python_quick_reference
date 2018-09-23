#Beginning of the program
print("Beginning Of the Program")
print("")

#No need to declare variable types unlike many other programming languages

#By assigning values, python decides the variable type
a = 10
b = 3.14
c = "Hello"
d = True
e = None

#To "see" the data type of the variable after assignment, we use type function
#An unique ID is assigned by Python to all objects in the program
print(f"a is : {str(a):<5} and its id is {str(id(a)):<13} its type is {type(a)}")
print(f"b is : {str(b):<5} and its id is {str(id(b)):<13} its type is {type(b)}")
print(f"c is : {c:<5} and its id is {str(id(c)):<13} its type is {type(c)}")
print(f"d is : {str(d):<5} and its id is {str(id(d)):<13} its type is {type(d)}")
print(f"e is : {str(e):<5} and its id is {str(id(e)):<13} its type is {type(e)}")

#To "check" the data type programmatically, we use isinstance function
if isinstance(a, int):
    print("isinstance shows: Integer")
else:
    print("isinstance shows: Not an Integer")

#Prints the assigned variables
print (a)
print (b)
print (c, type(c))
print (d, e)

#Mathematics can be performed using variables
print ("a + b:", a + b)

#Same variables can be "re-assigned". Re-assigning will change the variable's data type.
a = "abc"
b = "def"

#Prints the assigned variables
print(f"a is : {a:<3} and its type is {type(a)}")
print(f"b is : {b:<3} and its type is {type(b)}")

#String manipulation (in this case, "concatenation") can be done using variables.
print ("Concatenation of a and b is", a + b)

#Correct variable types MUST be used to perform intended operations.
#Implicit data type conversion (also called type casting) doesn't happens in Python
#print (a + d);

#Explicit conversion should be done like below.
#In this case, boolean is casted/converted to string using STR function
print ("Concatenation of string and boolean is", a + str(d))

#Multiple assignments to multiple variables at the same time can be done like below
a, b = 100, 200

#Prints the assigned variables
print ("Value of a and b is", a, b)

#To be aware during multiple assignments in single line
#a, b = 100, 200, 300
#a, b, c, d = 100, 200, 300

#Value of one variable can be assigned to another variable
a, b = b, a

#Prints the assigned variables
print ("Value of a and b is", a, b)

#Removing the variable from python memory can be done
del a

#Expect an error because you are printing something that doesn't exists
#print(a)

#End of the program
print("")
print("End Of the Program")