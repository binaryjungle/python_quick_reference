#Beginning of the program
print("Beginning Of the Program")
print("")

#Variable assignment
fruit_1 = "apple"
fruit_2 = "apple"

#Ternary operator. IF and ELSE in same line. Will work only for 2 decisions
string_match = "SAME FRUITS" if fruit_1 == fruit_2 else "NOT SAME FRUITS"

print (string_match)

#above example in usual way

if fruit_1 == fruit_2:
    string_match = "SAME FRUITS"
else:
    string_match = "NOT SAME FRUITS"

print (string_match)

#We can chain ternary operations one after another 

marks = 77

grade = "A" if marks >= 80 else "B" if marks >= 70 and marks < 80 else "C" if marks >= 60 and marks < 70 \
else "D" if marks >= 50 and marks < 60 else "E"

print(grade)

#above example in usual way

if marks >= 80: grade = "A" 
elif marks >= 70 and marks < 80: grade = "B"
elif marks >= 60 and marks < 70: grade = "C"
elif marks >= 50 and marks < 60: grade = "D"
else: grade = "E"

print(grade)

#End of the program
print("")
print("End Of the Program")