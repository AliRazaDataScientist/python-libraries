import random
new_list = []
client_list = []
print('Snake = 0, Water = 1, Gun = 2')
for x in range(1,4):
    new_list.append(random.randint(0,2))
    number = int(input(f'Enter you {x} number : '))
    while(True):
        if(number in [0,1,2]):
            break
        else:
            number = int(input(f'Enter {x} valid number : '))
    client_list.append(number)
print(new_list)
print(client_list)
a = 0
b = 0
c = 0
answer = []
for col in new_list:
    r = []
    for row in client_list:
        r.append(col*row)
        if(row == col):
            a+=1
        elif(row>col):
            b+=1
        else:
            c+=1
    answer.append(r)
print(a)
print(b)
print(c)
if(a>b and a>c):
    print('You Lose')
elif(b>a and b>c):
    print('You Win')
else:
    print('Draw')
for row in answer:
    print(row)