#Beginning of the program
print("Beginning Of the Program")
print("")

#Range is created using range function
#Range gives sequence of numbers from 0 incrementing by 1 until the value we provide as argument to the function
#The sequence will NOT include the argument we provide or in other words, range will stop at one position before the provided argument
#This is called exclusive or non-inclusive of the last number
#When 1 argument is provided, the range will start from 0 and stop at the argument we provide
series1 = range(30)

#When 2 arguments are provided, the range will start at first argument and stop at second argument
series2 = range(10, 30)

#When 3 arguments are provided, the range will start at first argument and stop at second argument incrmenting or stepping the sequence by thrid argument
series3 = range(6, 30, 3)

#Range values cannot be seen as such and hence cannot be printed. Ranges are often used as iterables
print(f"series1 is : {series1} and its type is {type(series1)}")
print(f"series2 is : {series2} and its type is {type(series2)}")
print(f"series3 is : {series3} and its type is {type(series3)}")

#Ranges are also iterables and iterables can be used in for loop
#We can access individual item from the range using for loop 
for looper in series1:
    print(looper, end=" ")
print("")

for looper in series2:
    print(looper, end=" ")
print("")

for looper in series3:
    print(looper, end=" ")
print("")

#End of the program
print("")
print("End Of the Program")