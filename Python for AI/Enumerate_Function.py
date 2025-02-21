marks = [2,45,55,12,44,77]
for index,mark in enumerate(marks):
    print(f'The index is {index} and the values is {mark}')

# we can start it according to our given number

for index,mark in enumerate(marks,start=1):
    print(f'The index is {index} and the values is {mark}')