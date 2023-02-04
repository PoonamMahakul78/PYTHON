#MERGING OF COLLECTION
#list merging
# l=[10,20,30,40,50]
# s=[100,200,'surendra']
# z=l+s
# print(z)

#list merging
# l=[10,20,30,40,50]
# s=[100,200,'surendra']
# z=[*l,*s]
# print(z)




# # TUPLE MERGING
# l=(10,20,30,40,50)
# s=(100,200,'surendra')
# z=l+s
# print(z)

#SET MERGING
# s1={10,20,30,40,50}
# s2={50,'surendra',100}
# s3=s1+2
# print(s3)


#solution
# s1={10,20,30,40,50}
# s2={50,'surendra',100}
# s3={*s1,*s2}
# print(s3)


# d1={1:'surendra',2:'priyanka'}
# d2={3:'rahul',4:'zini'}

# d3={*d1,*d2}
# print(d3)


#SOLUTION
d1={1:'surendra',2:'priyanka'}
d2={3:'rahul',4:'zini'}

d3={**d1,**d2}
print(d3)