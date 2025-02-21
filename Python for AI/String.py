name = 'Ali Raza'
print('Hello',name)

print('We can write anything in the string like "this"')
print('But we should to use Escape for the same quotation like \'this\'')

multiline = '''
I
can
write
anything
also spaces
like this.
'''
print(multiline)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

print('Slice Start Here')
silly = 'Do Testing on it.'
print(silly[3:11])
print(silly[:3])
print(silly[11:])
print('Negtive Slice Start Here')
print(silly[-6:-1])
nm = 'harrY broke OR borke harrY ???'
print(nm[-5:-1])
print('String Methods')
print(nm.upper())
print(nm.lower())
print(nm.rstrip('?'))
print(nm.replace('harrY','Cricket'))
print(nm.split(' '))
print(nm.capitalize())


string = 'Welcome to my code.'
print(len(string))
print(string.center(50))
print(nm.count('harrY'))
print(string.endswith('code.',5,19))
print(string.find('co'))
print(string.index('co'))


age = 10
name = 'Ali Raza'
resp = (f"My name is {name} and my age is {age} and My name is {name} and my age is {age} and My name is {name} and my age is {age}")
print(resp)