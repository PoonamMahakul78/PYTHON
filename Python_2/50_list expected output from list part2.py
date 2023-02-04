# l=['Surendra','Priyanka','Rahul','Zini']

# new_list=[]

# for i in l:
#     new_list.append(i[0]+i[-1])
# print(new_list)



l=['Surendra','Priyanka','Rahul','Zini']

new_list=[]

for i in l:
    n=len(i)
    new_list.append(i[0]+i[n-1])
print(new_list)