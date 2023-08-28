test = 10

def addNum():
    global test
    test = test + 45
    return test


print(test)
print(addNum())
print(test)