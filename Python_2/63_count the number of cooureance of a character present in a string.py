# s='mama'
# d={}
# for i in s:
#     d[i]=d.get(i,0)+1 #creating iteams as well as updation

# print(d)



# s='mamaij'
# d={}
# for i in s:
#     d[i]=d.get(i,0)+1 #creating iteams as well as updation

# print(d)



# s='ss aa bb cc 123 11 23'
# d={}
# for i in s:
#     d[i]=d.get(i,0)+1 #creating iteams as well as updation

# print(d)


s='mamamij'
d={}
for i in s:
    d[i]=d.get(i, 0)+1 #creating iteams as well as updation

print(d)

for i,j in d.items():
    print(f'{i} is present {j} times')  #{'m': 3, 'a': 2, 'i': 1, 'j': 1}
# m is present 3 times
# a is present 2 times
# i is present 1 times
# j is present 1 times