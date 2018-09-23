#Beginning of the program
print("Beginning Of the Program")
print("")

proceed_flag = True

while proceed_flag:
    which_table = int(input("Enter multiplication table:"))
    
    class multiplication_table1:
        def __init__(self, *args ):
            self._which_table = args[0]
            self._until_what= args[1]
            self._start = 0
            self._next = self._start
        
        #below method will be used to make the object iterable (eg: if for loop is required)
        def __iter__(self):
            return self
        
        def __next__(self):
            if self._next == self._until_what:
                raise StopIteration
            else:
                self._next += 1
                return f"{self._which_table} * {self._next} = {self._which_table * self._next}"
    
    #below for loop is possible because of __iter__ method
    for looper in multiplication_table1(which_table, 15):
        print(looper)
    
    proceed = input("do u want to continue:")
    if proceed.lower() == "n":
        proceed_flag = False

print("good bye")

#End of the program
print("")
print("End Of the Program")