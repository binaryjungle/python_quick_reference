#Beginning of the program
print("Beginning Of the Program")
print("")

#Useful string functions

#String assignment. First THE and LAZY is in upper case
a = "THE quick brown fox Jumps over the LAZY dog"

#Capitalize function converts first character to upper case and rest other characters to lower case 
print(a.capitalize())

#Upper function converts all characters to upper case
print(a.upper())

#Lower function converts all characters to lower case
print(a.lower())

#Swapcase function converts upper case characters to lower case and vice versa
print(a.swapcase())

#Title function converts first character of every word to upper case
print(a.title())

#Replace function replaces the old string(mentioned left of comma) with new string(mentioned right of comma)
print(a.replace("brown",  "white"))

#Find function returns the position of first occurence of the searched value. Find is case-sensitive. Positions start from 0
print(a.find("he"))
print(a.lower().find("he"))

#Strip function is called Trim in other programming languages
#Removes the character(s) provided as argument to the function on either ends of the string
#If no argument is provided, spaces will be removed on either ends
#The character(s) in middle of the strings will not be removed
b = "aaaTHE quick brown fox Jumps over the LAZY dogaaa"
print(b.strip("aaa"))
c = "   THE quick brown fox Jumps over the LAZY dog   "
print(c.strip())

#Rstrip function removes the provided character(s) in right end of the string only
print(a.rstrip("dog"))
#Lstrip function removes the provided character(s) in left end of the string only
print(a.lstrip("THE"))

#Isprintable function returns True if all characters are printable character in a string else we get false
print(a.isprintable())
b = "Printable\n\n\n\nCharacters"
print(b.isprintable())

#Isalnum function returns True if all characters are either alphabets or numbers in a string else we get false
#False is seen when space or other symbols are present in the string
b = "abcdefghijklmnopqrstuvwxyz1234567890"
print(b.isalnum())
print(a.isalnum())

#Isalpha function returns True if all characters are alphabets in a string else we get false
#False is seen when numbers, space or other symbols are present in the string
b = "abcdefghijklmnopqrstuvwxyz"
print(b.isalpha())
print(a.isalpha())

#Isnumeric function returns True if all characters are numbers in a string else we get false
#False is seen when alphabets, space or other symbols are present in the string
b="1234567890"
print(b.isnumeric())
print(a.isnumeric())

#Endswith function returns True if a given string ends with the character(s) provided as argument to the function
#Argument is mandatory
b = "file_name.txt"
if b.endswith(".txt"):
    print("Correct Extension")
else:
    print("Incorrect Exteension")

#Split function splits the string based on character(s) provided as argument to the function and returns a LIST
#Default split character is space if no argument is provided 
b = "Sam|New York|IT|Senior Developer"
temp_b = b.split()
print("Output after split is ", temp_b)
print("Type of the splited output is ", type(temp_b))

temp_b = b.split("|")
print("Output after split is ", temp_b)
print("Type of the splited output is ", type(temp_b))

#Join function is used to join each ITERABLE item provided as argument to the function WITH THE STRING preceding the join function 
new_b = ",".join(temp_b)
print("Output after join is ", new_b)
print("Type of joined output is ", type(new_b))

#End of the program
print("")
print("End Of the Program")