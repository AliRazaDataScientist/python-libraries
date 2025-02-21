# Map function
liz = [2,5,2,6,8,5,3,1,5]
def sq(x):
    return x*x
newliz = list(map(sq,liz))
print(newliz)
# via lambda function
newliz1 = list(map(lambda y:y*y*2,liz))
print(newliz1)

# Filter
lis = [4,3,5,2,8,1,3,1,6]
def bol(z):
    return z>3
newlis = list(map(bol,lis))
print(newlis)
# via lambda function
newlis1 = list(map(lambda a:a<=3,lis))
print(newlis1)

# reduce
from functools import reduce
liste = [1,2,3,4,5,6]
newliste = reduce(lambda m,n:m+n,liste)
print(newliste)

def sum(a,b):
    return a+b
newliste1 = reduce(sum,liste)
print(newliste1)