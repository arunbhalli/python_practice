
num = int(input('Enter your number to check it is prime or not:-'))

prime = True
for i in range(2, num):
    if (num % i == 0):
        prime = False
        break
if prime:
    print('This is a prime number')
else:
    print('This is not a prime number')
