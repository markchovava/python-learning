isTrue = True

while isTrue:
    name = input('What is your name? ')
    age = input('How old are you? ')
    gender = input('Gender: [Male / Female] ')
    text = f'Hi {name}, {age} years old, you have grown, {gender} you need an opposite gender now'
    print(text)
    if name == 'stop' or age == 'stop' or gender == 'stop':
        isTrue = False
        break



