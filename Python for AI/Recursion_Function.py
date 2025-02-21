num = int(input('Enter the number: '))
def factorial(n):
    if n in [0,1]:
        return n
    return n * factorial(n-1)
print(factorial(num))

# Fibonacci Sequence
# num = int(input('Enter the number: '))
# def factorial(n):
#     if(n == 0):
#         return 0
#     elif (n == 1):
#         return 1
#     else:  
#         def fiboni(n1):
#             if(n1>1):
#                 sum = (n1 -1)+(n1 -2)
#                return sum + fiboni(n)
# print(factorial(num))