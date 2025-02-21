sets = {'set',1,1,0,0,2,3,2,3,2,4,5,2,8,6,4.3,'set','abcd'}
print(sets)
set1 = {3,'s2',1,3,4,5,6,'s1'}
for x in set1:
    print(x)
print('Set Methods')
c1 = {'Rio','Madrid','Dubai','Moscow'}
c2 = {'Berlin','Rio','Oslo','Dubai'}
print(c1.union(c2))
print(c1.intersection(c2))
print(c1.symmetric_difference(c2))
print('Difference',c1.difference(c2))
c1.update(c2)
print(c1)
c1.difference_update(c2)
print(c1)

c3 ={'Tokyo','Delhi','Macca'}
c4 ={'Tehran','Karbla','Madina'}
c5 ={'Tehran','Karbla','Tokyo'}
c6 ={'Delhi','Macca','Tehran','Karbla','Tokyo'}
print(c3.isdisjoint(c4))
print(c3.isdisjoint(c5))
print(c6.issuperset(c5))
print(c5.issubset(c6))