isTrue = True
while isTrue:
    try:
        name = input('Type Username(Numbers Only): ')
        num = int(name)
        if num:
            print('Username accepted')
            isTrue = False
            break
    except:
        print('Username must be in numbers.')