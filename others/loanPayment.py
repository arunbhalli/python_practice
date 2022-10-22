

money_owe = float(input('how much do owe to the lander?\n'))
apr = float(input('enter you percentage per annual?\n'))
payment = float(input('what will you pay per month'))
months = int(input('how many months '))

monthly_rate = apr/100/12
for i in range(months):
    interest_paid = money_owe*monthly_rate
    money_owe = money_owe+interest_paid

    if (money_owe-payment < 0):
        print(f'the last payment is,{money_owe}', end='')
        print(f'you paid off the loan in {i+1} Month')
        break
    money_owe = money_owe-payment
    print(f'Paid {payment} of which {interest_paid} was interest')
    print(f'now i owe,{money_owe}')
