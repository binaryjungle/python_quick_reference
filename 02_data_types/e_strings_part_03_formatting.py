#Beginning of the program
print("Beginning Of the Program")
print("")

#Assigning values to variables
x, y = 2, 7
z = 4

#By default, curly braces prints as such in Python
print("x is {} and y is {}")

#Using format function, in different ways, we can pass values to the placeholders in the original string
#We use open and close curly braces as placeholders in Python
#The placeholders will be replaced by values provided as arguments to the format function
print("x is {}".format(2))

#Variables can be passed as arguments to format function
print("x is {}".format(x))

#Instead of direct values, expressions that will result in single value can be provided as arguments to format function
print("result after multiplying is {}".format(2 * 7))
print("result after multiplying is {}".format(x * y))

#Multiple values/variables can be provided as comma seperated arguments to format function
print("x is {} and y is {}".format(2, 7))
print("x is {} and y is {}".format(x, y))

#Less number of arguments provided will not be executed
#print("x is {} and y is {}".format(x))

#More number of arguments will ignore the unused arguments
print("x is {} and y is {}".format(x, y, z))

#Each argument have an index starting from 0
#We can mention the index within curly braces to replace the value of the argument
print("x is {0} and y is {1}".format(x, y))

#Using index, the order of the argument can change within the string
print("x is {1} and y is {0}".format(x, y))

#Using index, the same argument can be used multiple times within the string
print("x is {1} and y is {0}. Again x is {1}".format(x, y))

#Instead of default indexing, we can assign the values/variables to another variables
#This have same advantages as index. We can mention the new variables within curly braces to replace the value of the argument
print("x is {a} and y is {b}".format(a = x, b = y))

#Using the new variables, the order of the argument can change within the string
print("x is {b} and y is {a}".format(a = x, b = y))

#Using the new variables, the same argument can be used multiple times within the string
print("x is {b} and y is {a}. Again x is {b}".format(a = x, b = y))

x, y = 2876, 7
a, b = "word", 7
#Below examples will do some real formatting to the strings instead of just replacing the placeholders
#Colon(:) is used to tell Python about the formatting we do
#In right side of the colon, we specify the formatting rules
#Left angle brackets followed by number does left justification of the replaced value
#If the value is less than the provided number, spaces are padded to the right of the value   
#Right angle brackets followed by number does right justification of the replaced value
#If the value is less than the provided number, spaces are padded to the left of the value
print("x = {0:<10}; and y = {1:<10};".format(x, y))
print("a = {0:<10}; and b = {1:<10};".format(a, b))

print("x = {0:>10}; and y = {1:>10};".format(x, y))
print("a = {0:>10}; and b = {1:>10};".format(a, b))

#Providing ZERO between angle bracket and the number will pad the values with zero instead of space
#Angle brackets are optional for numbers but mandatory for alphabets 
print("x = {0:010}; and y = {1:010};".format(x, y))
print("a = {0:>010}; and b = {1:010};".format(a, b))

#For padding with any other character, mention the character before angle bracket
#Angle bracket is mandatory even for numbers when using other characters for padding
#Hence, it is good to use angle brackets always for clarity
print("x = {0:*>10}; and y = {1:010};".format(x, y))
print("a = {0:*>10}; and b = {1:>010};".format(a, b))

#If plus(+) or minus(-) sign needs to be printed, we can mention the required symbol instead of angle brackets
#If angle brackets are used, padding will happen, instead of printing plus/minus sign
#This doesn't works with strings.   
print("x = {0:+010}; and y = {1:>010};".format(x, y))
#print("a = {0:+010}; and b = {1:>010};".format(a, b)) --Will fail

#If numbers needs comma seperators, comma(,) should be meentioned after colon
#This needs only numbers and not strings
z = 9876543210
print("z = {:,}".format(z))
#print("z = {:,}".format(a)) --Will fail

#For decimal numbers, we can mention the number of decimal places to print using period(.) followed by the number of decimal places, after the colon
#Will work only for numbers and not for strings
z = 22/7
print("z = {:.15f}".format(z))
#print("a = {:.15f}".format(a)) --Will fail

#We can find the different notation of hexadecimal, octal and binary for a given number
#For hexadecimal, x identifier is used after colon
#For octal, o identifier is used after colon
#For binary, b identifier is used after colon
z = 92
print("z in hexadeimal is {:x}".format(z))
print("z in octal is {:o}".format(z))
print("z in binary is {:b}".format(z))

#F string is 100% same as format function
#F string is just short cut for format function that saves some typing for us
#Taking similar examples from format function, below is the f string notation
#COloring of curly braces will vary for F string and format function between IDEs

#Assigning values to variables
x, y = 2, 7
z = 4

#The placeholders will be replaced by values provided as arguments to the format function
print(f"x is {2} and y is {7}")
print(f"x is 2 and y is 7")

#Variables can be passed within the curly braces
#Multiple values/variables can also be provided similar to format function
print(f"x is {x} and y is {y}")

#Instead of direct values, expressions that will result in single value can be provided
print(f"result after multiplying is {2 * 7}")
print(f"result after multiplying is {x * y}")

x, y = 2876, 7
a, b = "word", 7

#Below examples will do some real formatting to the strings instead of just replacing the placeholders
#Colon(:) is used to tell Python about the formatting we do
#In right side of the colon, we specify the formatting rules
#Left angle brackets followed by number does left justification of the replaced value
#If the value is less than the provided number, spaces are padded to the right of the value   
#Right angle brackets followed by number does right justification of the replaced value
#If the value is less than the provided number, spaces are padded to the left of the value
print(f"x = {x:<10}; and y = {y:<10};")
print(f"a = {a:<10}; and b = {b:<10};")

print(f"x = {x:>10}; and y = {y:>10};")
print(f"a = {a:>10}; and b = {b:>10};")

#Providing ZERO between angle bracket and the number will pad the values with zero instead of space
#Angle brackets are optional for numbers but mandatory for alphabets 
print(f"x = {x:010}; and y = {y:010};")
print(f"a = {a:>010}; and b = {b:010};")

#For padding with any other character, mention the character before angle bracket
#Angle bracket is mandatory even for numbers when using other characters for padding
#Hence, it is good to use angle brackets always for clarity
print(f"x = {x:*>10}; and y = {y:>010};")
print(f"a = {a:*>10}; and b = {b:>010};")

#If plus(+) or minus(-) sign needs to be printed, we can mention the required symbol instead of angle brackets
#If angle brackets are used, padding will happen, instead of printing plus/minus sign
#This doesn't works with strings.   
print(f"x = {x:+010}; and y = {y:>010};")
#print(f"a = {a:+010}; and b = {b:>010};") --Will fail

#If numbers needs comma seperators, comma(,) should be meentioned after colon
#This needs only numbers and not strings
z = 9876543210
print(f"z = {z:,}")
#print(f"a = {a:,}") --Will fail

#For decimal numbers, we can mention the number of decimal places to print using period(.) followed by the number of decimal places, after the colon
#Will work only for numbers and not for strings
z = 22/7
print(f"z = {z:.15f}")
#print(f"a = {a:.15f}") --Will fail

#We can find the different notation of hexadecimal, octal and binary for a given number
#For hexadecimal, x identifier is used after colon
#For octal, o identifier is used after colon
#For binary, b identifier is used after colon
z = 92
print(f"z in hexadecimal is {z:x}")
print(f"z in octal is {z:o}")
print(f"z in binary is {z:b}")

#End of the program
print("")
print("End Of the Program")