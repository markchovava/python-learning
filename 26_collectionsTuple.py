import collections
from collections import namedtuple

Point = namedtuple('Point', 'x y z')
newP = Point(3,7,5)
print(newP)
print(newP._fields)
print(newP.x, newP.y)
print(newP[0])

newP = newP._replace(x=6)
print(newP)
newP = newP._make(['a', 'b', 'c'])
print(newP)