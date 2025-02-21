def greet(fx):
    def mfx():
        print('Good Morning Sir!')
        fx()
        print('Thank you Sir!')
    return mfx

@greet
def hello():
    print('Hello World!')
hello()

# Test Once
def doc(fx):
    def mfx(*ab,**abc):
        print('Hello')
        fx(*ab,**abc)
        print('Bye')
    return mfx

@doc
def sum(x,y):
    print('The sum is : ',x+y)
sum(2,2)