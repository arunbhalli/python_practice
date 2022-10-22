try :
  print('hello world')
  a =int(input('Enter your number:'))
  b =int(input('Enter your another number:'))
  print(a+b)
  
except Exception as e :
  print(f"the proble occured: {e}")
  
print('there were no errors')