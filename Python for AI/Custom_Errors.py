# x = int(input('Enter the value between 18 to 30 : '))
# if(17 > x or  x >= 30):
#     raise ValueError('Here is the error value should between 18 to 30')
# else:
#     print('Its ok')


st = input('For Quiz Enter String value ')
print(type(st))
if(st != 'quite'):
    print('working ok now in if')
    raise ValueError('You are entering wrong value')
else:
    print('Now you enter right value')