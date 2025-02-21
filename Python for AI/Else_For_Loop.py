print('For Loop')
for x in range(1,6):
    print('The answer is',x)
    if(x==3):
        break
else:
    print('Now x is empty')

print('While Loop')
i = 1
while(i<=10):
    print('The i values is',i)
    i = i+1
    if(i==4):
        break
else:
    print('Now the i is also empty')