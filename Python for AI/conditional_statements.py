x = int(input('Enter your age: '))
if(x>0):
    print('Only if')


if(x>18):
    print('if else')
else:
    print('Nope')


if(x>20):
    print('if else')
elif(x==20):
    print('In elif')
else:
    print('Nope')


if(x>0):
    if(x>18):
        print('nested if else')
    else:
        print('Nope')
else:
    print('Nope')