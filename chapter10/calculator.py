import math
class  Calculator():
  def __init__(self,number):
    self.number = number
    
  def square(self):
    return self.number * self.number
  
  def cube(self):
    return self.number * self.number*self.number
  def squareroot(self):
    return math.sqrt(self.number)
  def greet(self):
    return 'hello Arun'
    
two = Calculator(2)
print(two.greet())
print(two.number)
print(two.square())
print(two.cube())
print(two.squareroot())