# use input function for user name
name = input('please enter your name ')
print(name)

# 

date=input('Please enter the date \n')

template= '''Dear<|name|>, you are selected for the test on the date <|date|> '''
print(template.replace('<|name|>',name).replace('<|date|>',date))