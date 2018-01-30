#Function that requires no input or arguments
def display_success():
    print ("Your request has been successfully processed.")

#Functions can be reusable many times
display_success()

#Using functions inside pythons in-built functions. Watch out for TWO printed outputs
print (display_success())

#Function without parenthesis will print some unreadbale output which is python's way of displaying the value of the function object.
print (display_success)

var_a = 20
var_b = 10

#Functions can take inputs. The inputs are just mentioned with some variable name. Function doesn't gives back (RETURN) anything.
def add_type_1(value_1, value_2):
    result = value_1 + value_2
    print (result)

#The function is being called
#Function should be defined before it is called 
#The inputs that we pass can be with a different variable name. All placeholders should be given.
add_type_1(var_a, var_b)

#Functions that returns something
def add_type_2(value_1, value_2):
    result = value_1 + value_2
    return result

#The below line does nothing until we collect it somewhere 
add_type_2(var_a, var_b)

#Here we collect the output of the function.
var_c = add_type_2(var_a, var_b)

#Here we print that collected value
print (var_c)

#We can default some arguments with some values
def divide(dividend, divisor = 1):
    return dividend/divisor

#We can just give value only for the arguument that is not defaulted 
print (divide(var_a))

#We can overide the default value for defaulted argument
print (divide(var_a, var_b))

#If we are not lazy, we can mention the argument name as defined in the fuction and its values.
#The advantage being that the arguments can be of any order.
print (divide(divisor = var_b, dividend = var_a))

#Function that can take infinite or unpredictable number of arguments
def maximum(*many_arguments):
    bigvalue = 0
    first_check = 'Y'
    for looper in many_arguments:
        if first_check == 'Y':
            bigvalue = looper
            first_check = 'N'
        else:
            if looper > bigvalue:
                bigvalue = looper
            elif looper == bigvalue:
                bigvalue = looper
            else:
                continue
    return bigvalue

#Maximum of a number can be found with 5 arguments
print (maximum(-1, 3, 4, 99, -10, 88))

#Maximum of a number can be found with no arguments
print (maximum())

#Maximum of a number can be found with 2 arguments
print (maximum(-10, -20))
    
print ("End Of Program")