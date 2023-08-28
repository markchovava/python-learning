start = True
drive = True
stop = False
brake = True

if start and drive and not stop:
    print('Condition met, car is driving')
    if brake:
        print('Brakes applied.')
else:
    print('conditions no met')