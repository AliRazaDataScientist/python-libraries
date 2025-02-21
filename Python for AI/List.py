marks = [5,6,7,8,9,10]
print(marks)
print(marks[0])
print(marks[1])
print(marks[2])

# we can get data from negtive index
print('With Negtive index',marks[-4]) 
#  Use List as forloop
if 7 in marks:
    print('Yes Existed')
else:
    print('Nope')

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l']
print(alphabet)
print(alphabet[4:10])
print(alphabet[4:10:2])
print('Now Try with negtive indexes')
print(alphabet[-10:-2])
print(alphabet[-10:-2])
print(alphabet[-10:-2:3])


print('List Comprehension')
liz = [i for i in range(5)]
print(liz)
liz1 = [i for i in range(11) if i%2==0]
print(liz1)