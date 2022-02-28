from contextlib import contextmanager


@contextmanager
def read_file(name):
    try:
        file = open(name, 'r')
        print(file.read().count('\n'))
        yield file
    except:
        print('We had an error')
    finally:
        file.close()


with read_file('log.txt') as f:
    pass
