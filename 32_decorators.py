
""" def func(string):
    def wrapper():
        print('Started')
        print(string)
        print('Ended')

    return wrapper

x = func('hello')
print(x)
x() """
def func(f):
    def wrapper(*args, **kwargs):
        print('Started')
        f(*args, **kwargs)
        print('Ended')

    return wrapper

@func
def func2(x):
    print('1 am func2...')

@func
def func3():
    print('1 am func3...')

x = func(func2)
print(x)
x()

#func3 = func(func3)
func3()

