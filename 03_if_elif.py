age = input('What is your age? ')
ageInt = int(age)


if ageInt < 18:
    print('You are not allowed.')
elif ageInt > 30:
    print('You are in the wrong domain')
else:
    print(f'Welcome, you are {ageInt} years old...')