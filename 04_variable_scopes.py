#Defining a function
def alpha():
    var_a = "I am a local variable INSIDE function"
    print (var_a)

def beta():
    #Below GLOBAL definition makes use of the variable that was originally declared outside
    global var_a
    var_a = "I am a global variable"
    print (var_a)
    
#Variable declaration below
var_a = "I am a local variable OUTSIDE function"

#Prints locally declared variables (outside fuction)
print (var_a)

#Prints locally declared variables (inside function)
alpha()

#Proof that both var_a still have thier original values
print (var_a)

#Prints the global variable
beta()

#Because beta function changed the variable value by using GLOBAL keyword, the variable outside function gets its new value
print (var_a)

#Removing the variable from python memory can be done
del var_a

#Expect an error because you are printing something that doesn't exists
#print (var_a)

print ("End of Program")