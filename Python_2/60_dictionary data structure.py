# myinfo={
#     'name':'Poonam Mahakul',
#     'email':'mahakulpoonam59@email.com',
#     'address':'Rourkela',
#     'mobile':7656008266
# }

# print(myinfo['name'])
# print(myinfo)








#DUPLICATE KEYS ARE NOT ALLOWED
# myinfo={
#     'name':'Poonam Mahakul',
#     'name':'Surendra',
#     'email':'mahakulpoonam59@email.com',
#     'address':'Rourkela',
#     'mobile':7656008266
# }
# print(myinfo['name'])






#DIFFERENT WAYS FOR CREATING DICT
#empty dict
#d={}
#print(d)
#print(type(d))

#CREATE EMPTY DICT RHEN ADD ITEM
# d={}
# d['name']='Poonam'
# d['address']='bonei'
# d['email']='poonammahakul59@email.com'
# print(d)




#CREATE DICT DIRECTLY

# roll={1:'poonam',2:'priyanka',3:'rahul',4:'Zini'}
# print(roll)








# roll={1:'poonam',2:'priyanka',3:'rahul',4:'Zini'}
# print(roll[11])



# roll={0:'poonam',2:'priyanka',3:'rahul',4:'Zini'}
# print(roll[0])



#CHECK THE KEY IS EXIST OR NOT
#has_key()


# roll={1:'poonam',2:'priyanka',3:'rahul',4:'Zini'}
# print(roll.has_key(2))



#WHAT IS THE SOLUTION
#use in operator


# roll={1:'poonam',2:'priyanka',3:'rahul',4:'Zini'}
# print(2 in roll)
# print(2 not in roll)



#CREATE A DICTIONARY DYNAMICALLY BY TAKING USER INPUT

# d={}

# while True:
#     key=input('Enter the key : ')
#     val=input('Enter the value : ')
#     d[key]=val

#     choice=input('DO YOU WANT TO ENTER MORE[Y/N] : ').upper()

#     if choice=='N':
#         break

# print(d)


#TRAVERSING A DICT
# roll={1:'poonam',2:'priyanka',3:'rahul',4:'Zini'}


#PRINT ONLY KEYS
# for i in roll:
#     print(i)


#PRINT KEY AND VALUE
# roll={1:'poonam',2:'priyanka',3:'rahul',4:'Zini'}

# for i in roll:
#     print(i, roll[i])



#ADD ITEM IN DICT
# d=roll={1:'poonam',2:'priyanka',3:'rahul',4:'Zini'}
# print(d)
# d[27]='anjali'
# print(d)



#MODIFY
# d=roll={1:'poonam',2:'priyanka',3:'rahul',4:'Zini'}
# print(d)
# d[24]='anjali'
# print(d)


# d[1024]='hello'
# print(d)



#DELETE ITEM
# d={23:'surendra',24:'priyanka',25:'rahul',26:'zini'}
# print(d)
# del d[123]
# print(d)


#DELETE ALL THE ITEM
# d={23:'surendra',24:'priyanka',25:'rahul',26:'zini'}
# print(d)
# d.clear()
# print(d)


#HOW TO DELETE ENTIRE DICT
# d={23:'surendra',24:'priyanka',25:'rahul',26:'zini'}
# print(d)
# del d
# print(d)



#DICT KEY IMMUTABLE 
# IN NATURE HENCE WE CANT USE LIST,SET,DICT AS A DICT KEY BUT WE CAN USE NUMBER,TUPLE,FROZENSET AS A DICT KEY OTHERWISE WE WILL GET TYPEERROR

# d={[21,22,23]:'surendra',24:'priyanka',25:'rahul',26:'zini'}
# print(d)

# d={(21,22,23):'surendra',24:'priyanka',25:'rahul',26:'zini'}
# print(d)


# l=[21,22,23]
# d={l:'surendra',24:'priyanka',25:'rahul',26:'zini'}
# print(d)

# l.append(100)



# s=set((10,20,30))
# d={s:'surendra',24:'priyanka',25:'rahul',26:'zini'}
# print(d)

# s.add(100)


# s=set((10,20,30))
# d={frozenset(s):'surendra',24:'priyanka',25:'rahul',26:'zini'}
# print(d)

# s=set((10,20,30))
# d={frozenset(s):'surendra',24:'priyanka',25:'rahul',26:'zini'}
# print(d[frozenset({10,20,30})])


# d={12+13j:'surendra',24:'priyanka',25:'rahul',26:'zini'}
# print(d)


# d={True:'surendra',24:'priyanka',25:'rahul',26:'zini'}
# print(d)


# d={{1:'one'}:'surendra',24:'priyanka',25:'rahul',26:'zini'}
# print(d)






