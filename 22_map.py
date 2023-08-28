li = [1,2,3,4,5,6,7,8,9]

def func(x):
    return x**x

# the map function
newLi = list(map(func, li))
newLi2 = [func(x) for x in li]
newLi3 = [func(x) for x in li if x % 2 == 0]

print(newLi)
print(newLi2)
print(newLi3)