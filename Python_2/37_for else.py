# FOR ELSE
#if for loop id executed succesfully withour having break

# for i in range(10):
#     print(i)
# else:
#     print("i am else block")

for i in range(10):
    if i==6:
        break
    print(i) #if break statement is executed inside for loop ,then it will not be executed else part
else:
    print("i am else block")