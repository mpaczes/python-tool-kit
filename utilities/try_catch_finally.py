# Using Try/Except Blocks for Error Handling

try:
    f = open('testfilewrong.txt')
    # f = open('testfile.txt')
    if f.name == 'testfilewrong.txt':
        raise Exception
except FileNotFoundError:
    print('this file does not exist')
except Exception:
    print('something went wrong')
else:   # uruchomi sie jesli nie bylo wyjatku
    print(f.read())
    f.close()
finally: # wykonuje sie zawsze
    print('executing finally')