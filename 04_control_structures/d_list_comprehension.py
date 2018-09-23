#Beginning of the program
print("Beginning Of the Program")
print("")

#Variable assignment
current_salary = [12000, 8500, 10000, 7500, 8000]
hike = 0.07

#New salary calculation using list comprehension
new_salary = [(looper+(looper*hike)) for looper in current_salary]
print(new_salary)

#list comprehension along with condition checking using if statements
marks = [50, 67, 54, 34, 90, 83, 45, 50, 66, 79]
print(len(marks))
pass_marks = [looper for looper in marks if looper >= 50]
print(len(pass_marks))
print(pass_marks)

#create a list of tuples using the final outputs of list comprehension
new_salary = [(looper, (looper+(looper*hike))) for looper in current_salary]
print(new_salary)

#create a dictionary using the final outputs of list comprehension
new_salary = {looper: (looper+(looper*hike)) for looper in current_salary}
print(new_salary)

#End of the program
print("")
print("End Of the Program")