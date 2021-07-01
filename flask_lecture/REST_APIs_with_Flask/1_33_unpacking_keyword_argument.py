def named(**kwargs):
    print(kwargs)

def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

print_nicely(name='Bob', age=25)

def myfunction(**kwargs):
    print(kwargs)

test_dict = {'name': 'jinoh', 'age': 28}

myfunction(**test_dict)