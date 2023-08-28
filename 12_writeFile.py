# Writing a file in Python

file = open('text/file2.txt', 'w')
file.write('Hi There \n')
file.write('I am writing this file in Python. \n')
file.write('Goodbye.')
file.close()

print('File written successful.')