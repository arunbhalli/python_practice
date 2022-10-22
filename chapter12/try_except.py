try :
  print('hello world')
  a =int(input('Enter your number:'))
  b =int(input('Enter your another number:'))
  print(a+b)
  print(a/b)
  
  
except ValueError:
  print('value error occured')
except ZeroDivisionError:
  print('this is zero divison error')
except Exception as e :
  print(f"the problem occured: {e}")
  
print('there were no errors')