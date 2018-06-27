#Empty function

def empty_function():
    pass

print(empty_function())

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

#Function that can take infinite or unpredictable number of arguments. This is called argument lists_and_tuples
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

#Passing a tuple is possible by preceding tuple name with an asterisk
many_args = (1, 2, 3, 4, 5)
print(maximum(*many_args))

#Dictionary can also be passed as arguments. This is called keyword arguments.
#More than 2 values per loop is processed.
def max_bmi(**kwargs):
    bigvalue = 0
    Weight = "00"
    Height = 0.0
    first_check = 'Y'
    if len(kwargs) > 0:
        for looper in kwargs:
            bmi_value = (int(looper) / (kwargs[looper] ** 2))
            if first_check == 'Y':
                bigvalue = bmi_value
                Weight = looper
                Height = kwargs[looper]
                first_check = 'N'
            else:
                if bmi_value > bigvalue:
                    bigvalue = bmi_value
                    Weight = looper
                    Height = kwargs[looper]
                elif bmi_value == bigvalue:
                    bigvalue = bmi_value
                    Weight = looper
                    Height = kwargs[looper]
                else:
                    continue
    return bigvalue, Weight, Height

#print(max_bmi(a = 1.6, b = 1.4, c = 1.5))

weight_height_dict = {"70": 1.6, "55": 1.4, "80": 1.5, "80": 1.4}
print(max_bmi(**weight_height_dict))

print ("End Of Program")