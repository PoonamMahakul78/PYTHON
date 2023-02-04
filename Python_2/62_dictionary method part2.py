#LIST METHODS PART()
#keys()

# d={23:'surendra',24:'priyanka',25:'rahul',26:'zini'}


# print(d.keys())#keys method is besically used to return all the key from the dictionary


# d={23:'surendra',24:'priyanka',25:'rahul',26:'zini'}


# for i in d.keys():
#     print(i)



#VALUES()

# d={23:'surendra',24:'priyanka',25:'rahul',26:'zini'}


# print(d.values())


# d={23:'surendra',24:'priyanka',25:'rahul',26:'zini'}

# for i in d.values():
#     print(i)


#SETDEFAULT()
# d={23:'surendra',24:'priyanka',25:'rahul',26:'zini'}

# print(d)
# print(d.setdefault(999,'anjali'))
# print(d)



# d={23:'surendra',24:'priyanka',25:'rahul',26:'zini'}

# print(d)
# print(d.setdefault(23,'anjali'))
# print(d)#if the key is present then it will return the corresponding value


# d={23:'surendra',24:'priyanka',25:'rahul',26:'zini'}

# print(d)
# print(d.setdefault(23))
# print(d)


# d={23:'surendra',24:'priyanka',25:'rahul',26:'zini'}

# print(d)
# print(d.setdefault(999))  #by default it will give none 
# print(d)


#UPDATE()  adding modification kind of things

# d1={23:'surendra',24:'priyanka',25:'rahul',26:'zini'}

# d2={1:'college',2:'university'}

# d1.update(d2)
# print(d1)
# print(d2)



# d1={23:'surendra',24:'priyanka',25:'rahul',26:'zini'}
    #23: 'college',
# d2={23:'college',2:'university'}

# d1.update(d2)
# print(d1)
# print(d2)

#COPY()
# d1={23:'surendra',24:'priyanka',25:'rahul',26:'zini'}

# d2={}

# d2=d1.copy()

# # print(d1)
# # print(d2)

# print(id(d1))
# print(id(d2))

# d1[24]='anjali'

# print(d1)
# print(d2)


# d1={23:'surendra',24:'priyanka',25:'rahul',26:'zini'}

# d2=d1

# d2=d1
# print(d1)
# print(d2)

# print(id(d1))
# print(id(d2))

# d1[24]='anjali'

# print(d1)
# print(d2)



#CLEAR()
# d={23:'surendra',24:'priyanka',25:'rahul',26:'zini'}

# d.clear()
# print(d)


#FORMKEYS()
# l=[23,33,43,53,63]
# d=dict.fromkeys(l)
# print(d)


# t=(23,33,43,53,63)
# d=dict.fromkeys(t)
# print(d)


# l=(23,33,43,53,63)
# d=dict.fromkeys(l,'hello')
# print(d) #{23: 'hello', 33: 'hello', 43: 'hello', 53: 'hello', 63: 'hello'}


# d=dict.fromkeys(range(5),[1,2,3])
# print(d) #{0: [1, 2, 3], 1: [1, 2, 3], 2: [1, 2, 3], 3: [1, 2, 3], 4: [1, 2, 3]}


# d=dict.fromkeys([],[])  #{}
# print(d)


# d=dict.formkeys([1],[1])
# print(d) #AttributeError: type object 'dict' has no attribute 'formkeys'. Did you mean: 'fromkeys'?


# l=[23,33,43,53,63]
# d={}.fromkeys(1)
# print(d)  #iterable object










