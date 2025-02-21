x= 5
print(f'X value is {x}')
def testfun():
    x = 3
    print(f'X value is {x}')
testfun()

print(f'X value is {x}')

def testfun1():
    global x
    x = 1
    print(f'X value is {x}')
testfun1()

print(f'X value is {x}')