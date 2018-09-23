#form of metaprogramming
#special type of functions that returns wrapper function

def f5():
    print("this is f5")

f5()
x = f5
print(x)
x()

def f6():
    def f7():
        print("this is f2")
    return f7

y = f6()
y()

def f1(f_name):
    def f2():
        print("step 1 from f2")
        f_name()
        print("step 3 from f2")
    return f2

@f1
def f3():
    print("step 2 from f3")

print("hello")
f3()

import time
def elapsed_time(f_name):
    def wrapper(x):
        start_time = time.time()
        print(start_time)
        f_name(x)
        end_time = time.time()
        print(end_time)
        print((end_time - start_time)*1000)
    return wrapper

@elapsed_time
def big_sum(number):
    looper = 1
    while looper < 30000:
        print(f"{number} * {looper} = {number * looper}")
        looper += 1
        
big_sum(5)