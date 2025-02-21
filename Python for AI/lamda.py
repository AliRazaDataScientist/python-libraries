res = lambda x,y: (x+y)/2
print(res(2,4))
res1 = lambda : 'Hello World!'
print(res(2,4))
print(res1())
print(res(2,4))
print(res1())
print(res(2,4))

# pass function as a parameters
cube = lambda x :x*x*x
squar = lambda y:y*y
print(cube(2))
def fun(fx, value):
    return 6 + fx(value)
print(fun(cube,2))

def fun2(m,sq,n):
    return sq(m)+n
print(fun2(4,squar,9))