# Read code line by line
# file = open('File Operations Data.txt','r')
# while True:
#     data = file.readline()
#     if not data:
#         break
#     m1 = data.split(',')[0]
#     m2 = data.split(',')[1]
#     m3 = data.split(',')[2]
#     print(f'Math marks is {m1}')
#     print(f'Physics marks is {m2}')
#     print(f'English marks is {m3}')
#     print(data)

# Write code into file
# file2 = open('File Operations Data.txt','a')
# lines = ['Line 1\n','Line 2\n','Line 3\n','Line 4\n','Line 5\n']
# file2.writelines(lines)
# file2.close()

# Seek function in the file
# file3 = open('File Operations Data.txt','r')
# file3.seek(14)
# print(file3.read(6))
# print(file3.tell())
# file3.close()

# Truncate function in the file
file4 = open('File Operations Data.txt','w')
file4.write('12345This is only for testing ')
file4.truncate(8)
file4.close()
