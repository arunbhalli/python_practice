
class StringInfo():
  
  def __init__(self, name,language):
   self.name = name
   self.language = language
   
arun = StringInfo('Arun','python')
rahul = StringInfo('Rahul','python')
gaurav = StringInfo('Gaurav','python')

print(arun.name)
print(rahul.name)
print(gaurav.name)
print(arun.language)