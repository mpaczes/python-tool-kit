# Import Modules and Exploring The Standard Library

print('imported my_module ...')

test = 'test string'

def find_index(to_search, target):
    ''' find the index of a value in a sequence '''
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1
