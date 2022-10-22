class Vector:
  def __init__(self,l1):
    self.dim = len(l1)
    self.data = l1
    
  def __add__(self,obj):
     myList = []
     for i in range(len(obj.data)):
       myList.append(obj.data[i]+self.data[i])
       
     return Vector(myList)
    
v1 = Vector([1,5,3])
v2 = Vector([1,9,3])
v3=v1+v2
print(v3.data)