# 2d and 3d vectors 

class Vector2d:
  def __init__(self,i,j):
    self.i = i
    self.j = j
  def printVector(self):
    print(f'{self.i}i+{self.j}j')
    
class Vector3d(Vector2d):
  def __init__(self,i,j,k):
    super().__init__(i,j)
    self.k = k
    
  def printVector(self):
    print(f'{self.i}i+{self.j}j+{self.k}k')
  
    
v2 = Vector2d(1,5)
v3 = Vector3d(1,5,6)
v2.printVector()
v3.printVector()