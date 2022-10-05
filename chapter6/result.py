
sub1 = int(input('enter your marks'))
sub2 = int(input('enter your marks'))
sub3 = int(input('enter your marks'))

total = (sub1+sub2+sub3)
percentage = (total*100)/300

if (sub1 < 33 or sub2 < 33 or sub3 < 33 or percentage < 40):
    print('Your are failed in exam')
else:
    print('Your are successful in exam')
