text = input('Enter your text:')
if ('make a lot of money' in text):
    spam = True
elif ('Buy now' in text):
    spam = True
elif ('Subscribe now' in text):
    spam = True
elif ('click this' in text):
    spam = True
else:
    spam = False

if (spam):
    print('This is a spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam')
else:
    print('This is a not a spam')
