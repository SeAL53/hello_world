def add_one(x):
    return x + 1

def add_one_to_everything(a):
    for number in a:
        bigger_number = add_one(number)
        print bigger_number

y = 1
name = "Sean"
array = [1, 2, 3, 4, 5]

add_one_to_everything(array)
