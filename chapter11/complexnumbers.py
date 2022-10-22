
class Complex:
  def __init__(self,a,b):
    self.a = a
    self.b = b
    
  def __add__(self,obj):
    return Complex(self.a + obj.a, self.b + obj.b)
  
c1 = Complex(5,7)
c2 = Complex(20,8)
c3 = c1+c2
  
print(c3.a,c3.b)
  