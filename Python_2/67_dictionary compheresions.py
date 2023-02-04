#DICTIONARY COMPREHENSION

# d={i for i in range(1,6)}
# print(d)
# print(type(d)) #<class 'set'>



# d={i:i for i in range(1,6)}
# print(d)
# print(type(d)) 



# d={i:i*i for i in range(1,6)}
# print(d)
# print(type(d)) 

#WORING WITH LIST TO CREATE DICTIONARY

# l=[2.3,4.2,5.6,7.8]
# d={i:3.12*i*i for i in l}
# print(d)






# names=['surendra','priyanka','rahul','zini']
# d={i:len(i)for i in names}
# print(d)

# names=['surendra','priyanka','rahul','zini']
# d={i:len(i)for i in names if len(i)>6}
# print(d)


names=['surendra','priyanka','rahul','zini']
d={i:len(i)for i in names}
print(d)

