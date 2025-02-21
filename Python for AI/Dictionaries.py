dic = {'name':'Ali Raza','age':20,'Mobile':'1234567890'}
print(dic)
print(dic['name'])
print(dic.get('age'))
print(dic.keys())
print(dic.values())
for rec in dic.keys():
    print(dic[rec])

print('Lets try with fstring method')
for rec in dic.keys():
    print(f'The value of key {rec} is {dic[rec]}')

for key,val in dic.items():
    print(f'The {key} is this and the values is {val}.')