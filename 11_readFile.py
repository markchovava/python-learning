file = open('text/file.txt', 'r')
f = file.readlines()
file.close()

newList = []
""" for line in f:
    if line[-1] == '\n':
        newList.append(line[:-1])
    else:
        newList.append(line) """

for line in f:
    newList.append(line.strip())
   


print(newList)

