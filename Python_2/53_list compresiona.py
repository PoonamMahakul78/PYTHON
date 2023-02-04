# l=[i for i in range(11)]
# print(l)


# l=[i*i for i in range(11)]
# print(l)


# l=[i*i*i for i in range(11)]
# print(l)


# l=[i+10 for i in range(11)]
# print(l)

#WITH USING LIST C CONCEPT

# l=[i for i in range(1,21) if i%2 == 0]
# print(l)

#WITHOUT USING LIST C CONCEPT

# l=[]
# for i in range(1,21):
#     if i%2==0:
#         l.append(i)
# print(l)


# name=['surendra','priyanka','rahul','zini']
#expected output :['s','p','r','z']


# names=['surendra','priyanka','rahul','zini']
# l=[i[0] for i in names]
# print(l)


# names=['surendra','priyanka','rahul','zini']
# l=[i[0:4] for i in names]
# print(l)

#CREATE A NEW LIST BY ADD THE ELEMENT WHICH IS CONTANING LETTER A

# names=['surendra','priyanka','rahul','zini']
# l=[i for i in names if 'a' in i]
# print(l)


# names=['surendra','priyanka','rahul','zini']

# l=[i if i!='priyanka'else 'hello' for i in names]
# print(l)


#CREATE A LIST FROM TUPLE

# t=(10,20,30,40,50)
# l=[i for i in t if i%6==0] 
# print(l)


#CREATE A LIST FROM STRING

# name="surendra"
# l=[i for i in name]
# print(l)



#CREATION OF MATRIX USING LIST COM...

# m=[i for i in range(3)]
# print(m)

# m=[[j for j in range(3)] for i in range(3)]
# print(m)

# m=[[j for j in range(5)] for i in range(5)]
# print(m)

# m=[[i for j in range(3)] for i in range(3)]
# print(m)

m=[[i*j for j in range(3)] for i in range(3)]
print(m)






