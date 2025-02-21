x = int(input('Enter the Number : '))

match x:
    case 0:
        print('You enter zero')
    case 18:
        print('You enter Eighteen')
    case 30:
        print('You enter thirty')
    case _:
        print('You enter',x)

print('Now we are on another case')

def switch_case_if_elif(x):
    if 10 > x:
        print("You are Todler")
    elif 18 > x >= 10:
        print("You are Children")
    elif 30 > x >= 18:
        print("You are Young Man")
    elif 45 > x >= 30:
        print("You are Man")
    else:
        print("You are Old Man")

switch_case_if_elif(x)