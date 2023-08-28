import collections
from collections import Counter

a = Counter('gallant')
b = Counter(['a', 'a', 'b', 'b', 'c', 'c'])
c = Counter({'a':2, 'b': 5})
d = Counter(cats=3, dogs=6)
#print(a)
#print(b)
#print(c)
#print(d)
#print(d['cats'])
#print(list(c.elements()))
#print(a.most_common(1))

""" a = Counter(a=4, b=2, c=3, d=6)
b = ['a', 'a', 'b', 'b', 'c']
a.subtract(b)
print(a)
a.update(b)
print(a) """


a = Counter(a=4, b=2, c=3, d=6)
b = Counter(['a', 'a', 'b', 'b', 'c'])
print(a+b)
print(a-b)
print(a & b) # intersect
print(a | b) # union



