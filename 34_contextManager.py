""" file = open('text/file.txt', 'w')
try:
    file.write('Hello')
finally:
    file.close() """

#CONTEXT MANAGER
with open('text/file.txt', 'w') as file:
    file.write('hello')
    print('Saved...')