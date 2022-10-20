total = 0
expense = []
num_expenses = int(input('Enter no of your expense:- '))
for i in range(num_expenses):
  expense.append(float(input('enter your expense amount')))
total = sum(expense)
print('you spent $', total, sep='')