#Beginning of the program
print("Beginning Of the Program")
print("")

import sys

get_input = input("enter single digit number: ")

if len(get_input) > 1:
    #creates custom error messages and aborts program
    raise ValueError("Only single digit number allowed")
else:
    try: #accepts the error and looks for any exception handling
        get_input = int(get_input) ** 2
    except ValueError as error_mess: #creates the type of error and stores in variable
        print("Only numbers allowed")
        print(sys.exc_info()[1])
        print(error_mess)
    else: #if no error is caught, then else will execute
        print(get_input)
        print("Thanks for trying")

#End of the program
print("")
print("End Of the Program")