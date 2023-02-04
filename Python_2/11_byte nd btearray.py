a=[10,20,30,40]  #List
b=bytes(a) #List to byte
# print(b[0])
# print(b[4])
# print(b[-2])


# for i in b:
#      print(i)


a=[10,20,30,40,50]
b=bytearray(a) #convert list to bytearray
# print(b[1])
# print(b[-1])

#modify 1st index value

b[1]=200
b[2]=245
for i in b:
    print(i)