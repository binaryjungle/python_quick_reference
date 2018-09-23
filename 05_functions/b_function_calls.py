#Beginning of the program
print("Beginning Of the Program")
print("")

#For standard data types, function is called by values
#original value and value inside function is totally independent
def func1(a):
    a = 5
    print(a)
    
x = 7
#value for x is 7
print(x)
#value for a is 7 and that is changed to 5
func1(x)
#but value of x is still 7
print(x)

#For lists and dictionaries, function is called by references
#If functions alters the value, the original variables also changes its value

#Example to demonstrate using lists 
def func4(a):
    a[0] = 9
    a[1] = 8
    a[2] = 7
    print(a)

x = [2, 3, 4]
print(x)
func4(x)
print(x)

#Example to demonstrate using dictionaries
def func5(a):
    a["cat"] = "cub"
    print(a)
    
x = {"dog": "puppy", "cat": "kitten"}
print(x)
func5(x)
print(x)

#End of the program
print("")
print("End Of the Program")