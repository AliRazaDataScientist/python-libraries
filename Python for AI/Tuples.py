tup = (0,1,2,3,4,5,6,7,8,8,10,0)
tup2 = (11,12,13,14,15)
print(type(tup))
print(tup[2:8])
print(tup[-8:-3])

if 5 in tup:
    print('Yes In Tup')
else:
    print('No In Tup')

print('Here we are starting Tuple methods')
print(len(tup))
print(sorted(tup,reverse=True))
print(tup+tup2)
print(tup.count(0))
print(tup.index(5))