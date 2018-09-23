#Beginning of the program
print("Beginning Of the Program")
print("")

#Lists are mutable and so items in the list can be added, modified or removed

#Lists are created using square brackets. Each item is seperated by comma
a_list = [1, 2, 3, 4, 5]
print(f"Values: {a_list} and its type is {type(a_list)}")

#Even for having single item in the list, we need to use square brackets
a_list = [1]
print(f"Values: {a_list} and its type is {type(a_list)}")

#Below is an example of empty list
a_list = []
print(f"Values: {a_list} and its type is {type(a_list)}")

a_list = [1, 2, 3, 4, 5]
b_list = [6, 7, 8, 9]

#We can get individual items in the list using for loop, indexing or slicing
#Lists are also iterables and iterables can be used in for loop
#We can access individual item from the list using for loop
for looper in a_list:
    print(looper, end=" ")
print("")

#If we know the position of the individual item we can use index to get that item
#Index position is mentioned within square brackets
print("Item at position 0 is", a_list[0])

#To get partial items from the list, slicing needs to be done
#Colon to be used for slicing. Left side of colon indicates the starting item
#Right side of colon indicates the ending item
#lists are exclusive at ending position. So, we get up until one position before the ending number
print("Items from 1 to 3 are", a_list[1:4])

#slices from 0th index until 2nd index. 3rd index is exclusive
print(a_list[0:3])

#slices from 0th index until the end and skip the last 2 elements (not index)
print(a_list[0:-2])

#slices 4th element (not index) from the last until the 2nd index. 3rd index is exclusive.
print(a_list[-4:3])

#slices from 0th index until 3rd index in steps of 2. 4th index is exclusive
print(a_list[0:4:2])

#negative step means step back by specified value.
#If you start from 0th index, stepping back is not so useful
print(a_list[0:4:-1]) #Not so useful

#If you start from last index, stepping ahead is not so useful
print(a_list[4:0:1]) #Not so useful

#starting from last index, step back by 1 position. This is a literal reversing.
print(a_list[4:0:-1])

#Missing to provide any indexes will start from the first index and/or continue till last index 
print(a_list[4::-1])
print(a_list[::-1])

#Extend function adds new items to the list from the argument passed to the function
#Argument passed should be iterable
b_list.extend(a_list[0:2])
#b_list.extend(95) --Will fail
print("b_list with new items from a_list is", b_list)

#appending (at the last position)
a_list.append(6)
print(a_list)

#inserting (at 0th position place the value 55)
a_list.insert(0, 55)
print(a_list)

#removing. based on index
del a_list[3]
print(a_list)

#removing. based on slicing
del a_list[0:4:2]
print(a_list)

#based on value
a_list.remove(6)
print(a_list)

#pop removes the PROVIDED INDEX and stores the removed VALUE at the same time
#if no INDEX is provided to pop, last element is removed
what_value = a_list.pop()
print(a_list)
print(what_value)

#pop with index provided
a_list.pop(1)
print(a_list)

a_list = [1, 2, 3, 4, 5]
b_list = [6, 7, 8, 9]

#finding length of the list in other words counts the number of elemenets in the list
print(len(a_list)) #len is not a method to the list object

#Ccounts the number of occurence of the PROVIDED VALUE in the list
print(a_list.count(2))

#searching. based on value. Returns the index where the value is found
print(a_list.index(4))

a_list = ["a", "b", "c", "d", "e"]

#joining all the elements in the list with some common string
print(",".join(a_list))

#reverses the placement of the elements in the list
print(list(reversed(a_list))) #reversed is not a method to the list object

a_list = [0, 2, 3, 4, 5]

#performs addition individual elements in the list

print(sum(a_list))

#add individual elements in the list and add additional elements we provide
print(sum(a_list, 10))
print(sum(a_list, a_list[1]))

#maximum of the numeric elements in the list
print(max(a_list))

#maximum of the numeric elements in the list
print(min(a_list))

#True if any one item in the list is True (not "", 0 or None)
print(any(a_list))

#False if any one item in the list is False (not "", 0 or None)
#all means all MUST be true, if not then its false
print(all(a_list))

#ZIP uses 2 lists to create key, value pair in the dictionary
name_list = ["Sam", "John"]
city_list = ["New York", "Seatle"]
zipped_list = zip(name_list, city_list)
print(zipped_list) #object of zip class

final_dict = {}
for looper1, looper2 in zipped_list:
    #prepares the dictionary using the zip object
    final_dict[looper1] = looper2
print(final_dict)

#End of the program
print("")
print("End Of the Program")
