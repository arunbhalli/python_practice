class Employee:
  def __init__(self,salary,increment)-> None:
    self.salary = salary
    self.increment = increment
    
  @property
  def salaryIncrement(self):
      return (self.salary +(self.salary*self.increment)/100)
  
  @salaryIncrement.setter
  def salaryIncrement(self):
    self.salary = (self.salary +(self.salary*self.increment)/100)
eml1 = Employee(12000,10)
print(eml1.salaryIncrement)


    