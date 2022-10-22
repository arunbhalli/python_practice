try:
    print('hello world')
    a = int(input('Enter your number:'))
    b = int(input('Enter your another number:'))

    print(a+b)
    print(a/b)
    if a < 99 or b < 99 :
        raise Exception('This is a large no that is not allowed')
except ValueError:
    print('Value error occured')
