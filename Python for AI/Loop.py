from typing import Any


class Magic:
    def __init__(self,name):
        self.n = name
    def __str__(self):
        return f'Name is {self.n}'
    def __repr__(self):
        return f'Name is {self.n} repr'
    def __call__(self):
        print('Hahahahaha')
# print('For Loop')
# x = ["apple", "banana", "cherry"]
# for num in x:
#     print(num)
#     for a in num:
#         print(a)

# print('Range Starts Here')
# numb = int(input('Enter the number: '))
# for x in range(numb):
#   print(x+1) 
# numb = int(input('Enter the number: '))
# for x in range(1,numb,2):
#   print(x) 

# print('While Loop')
# rec = 5
# while (rec > 0):
#    print(rec)
#    rec = rec-1

# rec = 1
# while (rec <= 10):
#    print(rec)
#    rec = rec+1
# else:
#    print('Now condition is false')
# print('Do While Loop')
# do = 0
# while(do <= 20):
#     do = int(input('Enter the number: '))
#     print(do)