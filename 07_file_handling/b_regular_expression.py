#Beginning of the program
print("Beginning Of the Program")

import re

ip_file_name = "ip_data.dat"
ip_file = open(ip_file_name, "rt")

print("\nRE Search:\n")
for ip_record in ip_file.readlines():
    #searches for the string and prints the full record
    if re.search("(John|Alex)", ip_record): print(ip_record.strip())

ip_file_name = "ip_data.dat"
ip_file = open(ip_file_name, "rt")
print("\nRE substitute:\n")
for ip_record in ip_file.readlines():
    #substitute one word with another word
    print(re.sub("(John|Alex)", "Frank", ip_record.strip()))

ip_file_name = "ip_data.dat"
ip_file = open(ip_file_name, "rt")
print("\nRE simple patttern:\n")
for ip_record in ip_file.readlines():
    #pattern stores the search regular expression in memory which can then be used multiple times
    #below is just a simple search of the words John or Alex 
    pattern = re.search("(John|Alex)", ip_record)
    if pattern: print(pattern.group())

ip_file_name = "ip_data.dat"
ip_file = open(ip_file_name, "rt")
print("\nRE simple complie:\n")
for ip_record in ip_file.readlines():
    #compile can be used to add more search logic and store it in the pattern and use it later
    #below is the simple search as did earlier
    #watch for lower case alex
    pattern = re.compile("(John|alex)")
    if re.search(pattern, ip_record): print(ip_record.strip())

ip_file_name = "ip_data.dat"
ip_file = open(ip_file_name, "rt")
print("\nRE compile use case:\n")
for ip_record in ip_file.readlines():
    #below is the little more complex search (ignoring case)
    #watch for lower case alex
    pattern = re.compile("(John|alex)", re.IGNORECASE)
    if re.search(pattern, ip_record): print(ip_record.strip())

ip_file_name = "ip_data.dat"
ip_file = open(ip_file_name, "rt")
print("\nRE pattern use case:\n")
for ip_record in ip_file.readlines():
    #pattern storing the full search regular expression
    pattern = re.compile("(John|alex)", re.IGNORECASE)
    #1. pattern used in IF search
    #2. same pattern used in substitute
    if re.search(pattern, ip_record): print(pattern.sub("Frank",ip_record), end="")

#End of the program
print("\n")
print("End Of the Program")