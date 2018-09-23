def bmi(**kwargs):
    for looper in kwargs:
        bmi_value = (int(looper) / (kwargs[looper] ** 2))
        #Generator logic works here
        yield bmi_value

weight_height_dict = {"70": 1.6, "55": 1.5, "80": 1.5}

'''the below bmi function provides many values and for statement loopers
through all the values provided by the function'''

for looper in bmi(**weight_height_dict):
    print(looper)