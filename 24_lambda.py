
#def func(x):
#    return x+5
#print(func(34))

#func2 = lambda x: x+5
#print(func2(34))

def func(x):
    func2 = lambda x: x + 7
    return func2(x) + 13

print(func(23))


func3 = lambda x,y=3: x + y
print(func3(6, 7))
print(func3(6))

a = [1,2,3,4,5,6,7,8,9,10]
newA = list(map(lambda x: x**3, a))
print(newA)

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newB = list(filter(lambda x: x % 3 == 0, a))
print(newB)


