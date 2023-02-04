#While with else block

i=1
while i<=10:
    print(i)
    i=i+1
#if the while part is fully executed then only it will exicute else part
else:
    print('This is else block')


i=1
while i<=10:
    if i==6:
        break #here if we will use break then else part will be not executed
    print(i)
    i=i+1
else:
    print('This is else block')