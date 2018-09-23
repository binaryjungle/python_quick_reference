#a_dict = {"a":1, "b":2, "c":3, "d":4, "e":5}
#a_set = {1, 2, 3, 4, 5}
#print(a_list, a_tuple, a_dict, a_set)

#Beginning of the program
print("Beginning Of the Program")
print("")

#tuples are enclosed wiithin parenthesis or values seperated by commas or both
#parenthesis is required only for empty tuples otheriwse it is optional
#commas are required always except for empty tuples
#below is not a tuple because it is not empty and no comma is present
a_tuple = (1)
print(f"Values: {a_tuple} and its type is {type(a_tuple)}")

#below is a tuple because even for single element a comma is present
a_tuple = (1,)
print(f"Values: {a_tuple} and its type is {type(a_tuple)}")

#below is a tuple because even for single element a comma is present.
#Parenthesis is optional for non-empty tuples
a_tuple = 1,
print(f"Values: {a_tuple} and its type is {type(a_tuple)}")

#below is a tuple because it is empty and enclosed within parenthesis
#Parenthesis is mandatory for empty tuples
a_tuple = ()
print(f"Values: {a_tuple} and its type is {type(a_tuple)}")

a_tuple = (1, 2, 3, 4, 5)
b_tuple = (6, 7, 8, 9)

#We can get individual items in the tuple using for loop, indexing or slicing
#Tuples are also iterables and iterables can be used in for loop
#We can access individual item from the tuple using for loop
for looper in a_tuple:
    print(looper, end=" ")
print("")

#If we know the position of the individual item we can use index to get that item
#Index position is mentioned within square brackets
print("Item at position 0 is", a_tuple[0])

#To get partial items from the tuple, slicing needs to be done
#Colon to be used for slicing. Left side of colon indicates the starting item
#Right side of colon indicates the ending item
#tuples are exclusive at ending position. So, we get up until one position before the ending number
print("Items from 1 to 3 are", a_tuple[1:4])

#slices from 0th index until 2nd index. 3rd index is exclusive
print(a_tuple[0:3])

#slices from 0th index until the end and skip the last 2 elements (not index)
print(a_tuple[0:-2])

#slices 4th element (not index) from the last until the 2nd index. 3rd index is exclusive.
print(a_tuple[-4:3])

#slices from 0th index until 3rd index in steps of 2. 4th index is exclusive
print(a_tuple[0:4:2])

#negative step means step back by specified value.
#If you start from 0th index, stepping back is not so useful
print(a_tuple[0:4:-1]) #Not so useful

#If you start from last index, stepping ahead is not so useful
print(a_tuple[4:0:1]) #Not so useful

#starting from last index, step back by 1 position. This is a literal reversing.
print(a_tuple[4:0:-1])

#Missing to provide any indexes will start from the first index and/or continue till last index 
print(a_tuple[4::-1])
print(a_tuple[::-1])

#finding length of the tuple in other words counts the number of elemenets in the tuple
print(len(a_tuple)) #len is not a method to the tuple object

#Ccounts the number of occurence of the PROVIDED VALUE in the tuple
print(a_tuple.count(2))

#searching. based on value. Returns the index where the value is found
print(a_tuple.index(4))

a_tuple = ("a", "b", "c", "d", "e")

#joining all the elements in the tuple with some common string
print(",".join(a_tuple))

#reverses the placement of the elements in the tuple
print(tuple(reversed(a_tuple))) #reversed is not a method to the tuple object

a_tuple = (1, 2, 3, 4, 5)

#performs addition individual elements in the tuple

print(sum(a_tuple))

#add individual elements in the tuple and add additional elements we provide
print(sum(a_tuple, 10))
print(sum(a_tuple, a_tuple[1]))

#maximum of the numeric elements in the tuple
print(max(a_tuple))

#maximum of the numeric elements in the tuple
print(min(a_tuple))

#True if any one item in the tuple is True (not "", 0 or None)
print(any(a_tuple))

#False if any one item in the tuple is False (not "", 0 or None)
#all means all MUST be true, if not then its false
print(all(a_tuple))

#ZIP uses 2 tuples to create key, value pair in the dictionary
name_tuple = ("Sam", "John")
city_tuple = ("New York", "Seatle")
zipped_tuple = zip(name_tuple, city_tuple)
print(zipped_tuple) #object of zip class

final_dict = {}
for looper1, looper2 in zipped_tuple:
    #prepares the dictionary using the zip object
    final_dict[looper1] = looper2
print(final_dict)

#End of the program
print("")
print("End Of the Program")
