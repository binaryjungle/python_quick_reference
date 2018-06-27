#Beginning of the program
print("Beginning Of the Program")
print("")

#Strings are values enclosed by quotes
#In below example, string is enclosed by double quotes
string1 = "String enclosed by double quotes"
#In below example, string is enclosed by single quotes
string2 = 'String enclosed by single quotes'

#Multi lined values can be assigned by enclosing the value by 3 quotes
#In below example, string is enclosed by 3 double quotes
string3 = """Multi line string
enclosed by 3 double quotes"""
#In below example, string is enclosed by 3 single quotes
string4 = '''Multi line string
enclosed by 3 single quotes'''
#To avoid newlines to be created in multi-lined values, backslash(\) can be used  
string5 = '''\
Multi \
line
string \
with
some avoided newlines'''

#Prints the assigned variables
print(string1)
print(string2)
print(string3)
print(string4)
print(string5)

#Special characters can be mentioned using the character's special representation
#In below example, newline or line break will be created because of \n (representation for newline)
print("This will create \na new line")
#In below example, tab will be created because of \t (representation for tab)
print("This will insert\ta single tab")
#To use the representation characters as such or in other words to escape the
#special characters, we enclose the string and precede it with "r"
#r notation is called as raw string notation
print(r"This will NOT create \na new line")
print(r"This will NOT insert\ta single tab")

#String concatenation donein one of below 3 ways
#1. Just placing the strings next to each other
#The space between strings is just to tidy up the program and doesn't gets included in final result
string6 = "Python" "Programmer1"; print(string6) #using strings in variables
print("Python" "Programmer1") #using strings directly

#2. Having plus(+) symbol between strings
#The spaces on either side of plus(+) symbol are just to tidy up the program and doesn't gets included in final result
string7 = "Python" + "Programmer2"; print(string7) #using strings in variables
print("Python" + "Programmer2") #using strings directly

#3. Having comma(,) symbol between strings
#The spaces on either side of comma(,) symbol are just to tidy up the program and doesn't gets included in final result
#This method includes one space between strings being concatenated
string8 = "Python"; string9 = "Programmer3"; print(string8 , string9) #using strings in variables
print("Python" , "Programmer3") #using strings directly

#End of the program
print("")
print("End Of the Program")