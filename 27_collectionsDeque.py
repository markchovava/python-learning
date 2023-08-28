from collections import deque

d = deque('hello')
print(d)

d.append(23)
print(d)

d.appendleft(25)
print(d)

d.pop()
print(d)

d.popleft()
print(d)

d.clear()
print(d)

d.extend('try again')
print(d)
d.extendleft('123')
print(d)

d.rotate(2)
print(d)

e = deque('hello', maxlen=5)
e.extend([1,2,3])
print(e)