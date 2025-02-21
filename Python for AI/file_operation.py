# First only read file
# fil_r = open('file_operation.txt','r')
# read = fil_r.read()
# print(read)
# fil_r.close()


# Second write file
# fil_w = open('file_operation.txt','w')
# write = fil_w.write('Just for testing purpose.')
# fil_w.close()


# Third append file
# fil_a = open('file_operation.txt','a')
# app = fil_a.write('Now append is triggered')
# fil_a.close()

# Other method is 'with'
with open('file_operation.txt','a') as fil :
    fil.write('Also add this')
with open('file_operation.txt','r') as fil :
    print(fil.read())