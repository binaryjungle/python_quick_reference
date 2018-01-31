#Variable assignment
num_a = 100
num_b = 200

#Single decision making. Also called branching
if num_a < num_b:
    print (str(num_a) + " is lesser than " + str(num_b))

#Variable assignment
num_a = 300
num_b = 200

#Decisioning and assigning variable
if num_a < num_b:
    display_message = str(num_a) + " is lesser than " + str(num_b)

#This will get printed only if above IF condition passes else python will fail to recognize the variable.
#print (display_message)

#Below IF performs 2 decisions.
if num_a < num_b:
    display_message = str(num_a) + " is lesser than " + str(num_b)
else:
    display_message = str(num_a) + " is greater than " + str(num_b)

#Just a print of above variable
print (display_message)

#Assigning same values to variables
num_a = 200
num_b = 200

#Using ELSE might result in wrong values being pushed to last bucket
if num_a < num_b:
    display_message = str(num_a) + " is lesser than " + str(num_b)
else:
    display_message = str(num_a) + " is greater than " + str(num_b)

#Watch for the wrong message
print (display_message)

#Taking care of all decisioning is programmers responsibility
if num_a < num_b:
    display_message = str(num_a) + " is lesser than " + str(num_b)
elif num_a > num_b:
    display_message = str(num_a) + " is greater than " + str(num_b)
else:
    display_message = str(num_a) + " is equal to " + str(num_b)

#Right message will be displayed as per values given to variables
print (display_message)

#Variable assignment
fruit_1 = "apple"
fruit_2 = "apple"

#Ternary operator. IF and ELSE in same line. Will work only for 2 decisions
string_match = "SAME FRUITS" if fruit_1 == fruit_2 else "NOT SAME FRUITS"

#Printing the result
print (string_match)

#If lines inside a function is just one line, it can be placed after the COLON itself
if fruit_1 != "apple": print ("Mango not found")
else: print ("appple found")

print ("End Of Program")