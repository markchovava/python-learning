def myFunc(a, b=1):
    if b == 1:
        print('B is running on default.')
        print(f'A is running on {a}.')
    else:
        print(f'A is running on {a}.')
        print(f'B is running on {b}.')

    return f'{int(a) + int(b)} hertz in total'


c = myFunc(12, 23)
print(c)