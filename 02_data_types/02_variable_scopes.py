#Beginning of the program
print("Beginning Of the Program")
print("")

#Variable declaration below
a = "I am a local variable OUTSIDE function"

#Prints locally declared variable (outside function)
print(a)

#Defining a function
def alpha():
    a = "I am a local variable INSIDE function"
    print(a)

alpha() #Prints locally declared variable after its value being changed within function

#Prints locally declared variable (outside function)
print(a)

def beta():
    #Declaring a variable to be GLOBAL and changing its value within function
    global a
    a = "I am a global variable"
    print(a)

beta() #Prints globally declared variable after its value being changed within function

#Prints local variable after it is made global
print(a)

#End of the program
print("")
print("End Of the Program")