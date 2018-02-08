try:
    print(1)
    try:
        print(a)
    except IndexError:
        print('except inside')
    finally:
        print('finally inside')
except:
    print('except')
else:
    print('else')
finally:
    print('finally')