def Call():
    print('My name is Ali')
    print('I am zoho dev')
Call()
print('Call Once Again')
Call()

def NewFun():
    pass

# Default Arguments
def total(a=5,b= 7):
    print('A is',a,'& b is',b)
    print('The Sum is',a+b)

total(3)

# Keyword Arguments
total(b=3, a=2)


# Required Arguments
def req_Fun(x,y):
    print('Both x =',x,'and y =',y,'is required if i didn\'t call it then throw error')
req_Fun(2,5)


# Variable Arguments
# Tuple
def average(*number):
    print(type(number))
    avg = 0
    for all_num in number:
        avg = avg + all_num
    print('The average is', avg/len(number))
average(5,5,5,5,10)
# Dict = Map
def map(**name):
    print(type(name))
    print('My first name is',name['firstname'],', middle name is',name['middlename'],'and the last name is',name['lastname'])
map(firstname = 'Ali', middlename = 'nothing', lastname = 'Raza')