import inspect

def func(x):
    if x == 1:
        def rv():
            print('X is equal to 1')
    else:
        def rv():
            print('X is NOT equal to 1')

    return rv

newFunc = func(1)
#print(inspect.getsource(newFunc()))
newFunc()