print('Break Statement')
for num in range(1,13):
    print('5 *',num,'=',5*num)
    if(num == 10):
        break


print('Continue Statement')
for num in range(1,13):
    if(num%2 == 0):
        continue
    print('5 *',num,'=',5*num)