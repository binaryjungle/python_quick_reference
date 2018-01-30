#No need to declare variable types unlike many other programming languages
#By assigning values, python decides the variable type
var_a = 100;
var_b = 50;
var_c = 4000;

#Prints the assigned variables
print (var_a);
print (var_b);

#Mathematics can be applied using variables
print (var_a + var_b);

#Same variables can be "re-assigned". Re-assigning will change the variable type.
var_a = "abc";
var_b = "def";

#Prints the assigned variables
print (var_a);
print (var_b);

#String manipulation (in this case, "concatenation") can be done using variables.
print (var_a + var_b);

#Correct variable types MUST be used to perform intended operations. Implicit conversion doesn't happens
#print (var_a + var_c);

#Explicit conversion should be done like below. In this case, integer is casted to string using STR function
print (var_a + str(var_c));

print ("End of Program")