#Beginning of the program
print("Beginning Of the Program")
print("")

#Boolean results for unique values in various data types
x = True
y = False
a = None #Testing will result in boolean result of False
b = 0 #Testing will result in boolean result of False
c = "" #Testing will result in boolean result of False

#Below will display the value and it's real data type
print(f"value of x is {str(x):<5} and its type is {type(x)}")
print(f"value of y is {str(y):<5} and its type is {type(y)}")
print(f"value of a is {str(a):<5} and its type is {type(a)}")
print(f"value of b is {str(b):<5} and its type is {type(b)}")
print(f"value of c is {c:<5} and its type is {type(c)}")
print("")

#Below kind of test is possible. If a/b/c have valid values then the result is True else False
if a: #Value None to variable a will result in Boolean False
    print("Value Exists")
else:
    print("Value Doesn't Exists")

if b: #Value 0 to variable b will result in Boolean False
    print("Value Exists")
else:
    print("Value Doesn't Exists")

if c: #Value "" (empty string) to variable c will result in Boolean False
    print("Value Exists")
else:
    print("Value Doesn't Exists")

if True: #We can just pass True
    print("This is true")
else:
    print ("This is false")

#End of the program
print("")
print("End Of the Program")