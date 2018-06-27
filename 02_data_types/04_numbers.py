#Beginning of the program
print("Beginning Of the Program")
print("")

from decimal import *

#As always in Python, we can directly assign numeric values to variables
#Both integers and decimal numbers can be provided
#By using type function, we can verify the data type assigned to the variable by Python
x = 5
y = 98765432109876543210
z = 6.9
print(f"x is : {str(x):<20} and its type is {type(x)}")
print(f"y is : {str(y):<20} and its type is {type(y)}")
print(f"z is : {str(z):<20} and its type is {type(z)}")

y = 3

#We can directly perform any mathematical operation with numeric variables
result = x + y
print(f"{x} + {y} = {result}")
result = x - y
print(f"{x} - {y} = {result}")
result = x * y
print(f"{x} * {y} = {result}")

#By default division in Python will result in regular division and answers will have decimal values
result = x / y
print(f"{x} / {y} = {result}")

#We can achieve integer or floor division by using double forward slash(//). We get only the quotient part
result = x // y
print(f"{x} // {y} = {result}")

#We perform modulo division using percentage(%) symbol. We get only remainder part
result = x % y
print(f"{x} % {y} = {result}")

#Using decimal values will result in Python considering the extreme precision value possible
x = (.1 + .1 + .1) - (.3)
print("Where 0 is expected, a high precision number is seen. Value =", x)
x = (.2 + .2 + .2) - (.6)
print("Where 0 is expected, a high precision number is seen. Value =", x)
#The above scenario can be helpful for scientists or astronomers and so on

#If we need Python just to consider the literal value and provide accurate answer, decimal module should be imported
#After importing decimal module, Decimal function should be used to force Python to do exact maths and give backk accurate answer
#Python will not consider precision by following this way
a = Decimal(".1")
b = Decimal(".3")
x = a + a + a - b
print("Value of x is ", x)

#Multiple assignments can be done in Python in single line
a, b = 0, 1
print("Initial valus of a and b are", a, "and",b)

#If we re-assign variables and perform some recursive mathematics, initial values will only be considered
#New values will be effective only after assignment of values to all variables
#In below example, no priority is given to either variable assignments
a, b = b, a + b
print("After 1st re-assignment:", a, b)
a, b = b, a + b
print("After 2nd re-assignment:", a, b)
a, b = b, a + b
print("After 3rd re-assignment:", a, b)

#Useful numeric functions

#The abs function returns absolute or positive value of any given number 
print("Absolute value:", abs(-47))

#The divmod return quotient and remainder of the division as a tuple
print("divmod result is", divmod(22, 7))

#Round function rounds the decimal value (first argument) to provided precision (second argument)
#Precision (second argument) is optional and the default is 0 decimal places
print("Value of pi with 5 decimal places:", round(22/7,5))
print("Value of pi with 0 decimal places:", round(22/7))

#End of the program
print("")
print("End Of the Program")