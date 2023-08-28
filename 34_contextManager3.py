from contextlib import contextmanager

@contextmanager
def file(filename, method):
    print('enter')
    file = open(filename, method)
    yield file
    file.close()
    print('exit')

with file('text/file.txt', 'w') as f:
    print('middle')
    f.write('Hello again form Context')