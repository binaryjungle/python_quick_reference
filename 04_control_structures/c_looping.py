#Beginning of the program
print("Beginning Of the Program")
print("")

#Variable assignment
stop_at = 10
looper = 1
number = 5

#while statement is used to loop same set of code until some condition is met
while looper <= stop_at: #
    print(f"{number} * {looper} =", number * looper)
    looper = looper + 1

#continue will jump into the next loop or iterable
#break will quit the loop completely
#else executes after completion of all the loops

words_to_ignore = ("pass", "next", "proceed", "skip")
words_to_abort = ("exit", "quit", "x", "q")
any_word = ""

#Word game

while any_word.lower() != "finish":
    any_word = input("enter any word: ")
    if any_word.lower() in words_to_ignore:
        continue
    if any_word.lower() in words_to_abort:
        break
    if any_word.lower() != "finish":
        print(any_word.lower(), any_word.lower(), any_word.lower())
else:
    print("Good Bye. Thanks for trying.")

#for statement is used to loop same set of code for items in containers/iterables
for looper in range(1, 11):
    print(f"{number} * {looper} =", number * looper)

print(looper)

#Another example of for and range
n = int(input("Enter the number for which factorial needs to be found: "))
n_factorial=1
for looper in range(1, n + 1):
    n_factorial = n_factorial * looper

print(n_factorial)

#End of the program
print("")
print("End Of the Program")