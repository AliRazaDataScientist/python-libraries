num = input('Enter the number: ')
try:
    for x in range(6):
        print(f'{num}*{x}={x*int(num)}')
except Exception as e:
    print('Error is occured',e)

print('Simple Try Except')


print('Try Except')

def testcode(x):
    try:
        mylist = [4,5,2,3,7]
        answer = mylist[int(x)]
        return answer
    except:
        print('Error is occured in the code')
        return 'Error'
    print('I am always execute') #Here we can see after return print is disable so that why we should to use finally
ans = testcode(num)
print(f'The return is {ans}')


print('Try Except and Finally')

def testcode(x):
    try:
        mylist = [4,5,2,3,7]
        answer = mylist[int(x)]
        return answer
    except:
        print('Error is occured in the code')
        return 'Error'
    finally:
        print('I am always execute')
ans = testcode(num)
print(f'The return is {ans}')