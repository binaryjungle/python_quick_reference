#Beginning of the program
print("Beginning Of the Program")
print("")

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
fruit = "apple"

#If lines inside a function is just one line, it can be placed after the COLON itself
if fruit == "apple": print ("Its apple")
else: print ("Not an apple")

#End of the program
print("")
print("End Of the Program")