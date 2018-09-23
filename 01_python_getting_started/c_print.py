#Beginning of the program
print("Beginning Of the Program")
print("")

#The below code prints a string
print("Hello World.! I am enclosed in double quotes")
print('Hello World.! I am enclosed in single quotes')

#Escaping the special characters can be done in below ways
#1. To use one enclosing character in the print, use the other ennclosing character to enclose
print("I'm a Python programmer")
print('I am a "Python" programmer')
#2. Use the backslash character to escape the "immediate next" character following the backslash.
#This will prevent Python to see the next character with its special meaning in Python
print('I\'m a Python programmer')
print("I am a \"Python\" programmer")
print("Newline within prints can be mentioned using \\n.")

#Numeric values (integers and decimals) should not be enclosed by any quotes
print("Sample numeric value:", 100)

#Concatenation of strings can be done by using the plus(+) symbol. No space will be included between strings
print("Plus Concatenation Example: " + "Hello" + " Python " + "Programmer...!!!")

#Concatenation of strings can also be done using commas. Space between strings will be automatically included.
print("Comma Concatenation Example:", "Python", "Programming")

#Mathematics with numeric values can be performed inside print
#Mathematics using only integers
print("Integer + Integer:", 100 + 900)

#Mathematics using only decimal values (or floating point values)
print("Float + Float:", 12.5 + 17.5)

#Mathematics using integers and decimal values (or floating point values)
print("Integer + Float:", 13 + 16.5)

#Print function terminates the printed string with newline
print("Hello")
print("World")

#To terminate the printed strings using different character, we can use "end" keyword within print function
print("Hello", end='')
print(" World")

#End of the program
print("")
print("End Of the Program")