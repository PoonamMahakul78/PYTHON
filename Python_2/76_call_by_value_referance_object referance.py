#CALL BY VALUE
# def fun(a):
#     print('inside fun',a)
#     print('inside fun',id(a))
    
    
# a=23
# print('outside fun',a)
# fun(a)
# print('outside fun',a)
# print('outside fun',id(a))



# def fun(x):
#     print('inside fun',x)
#     print('inside fun',id(x))
    
    
# a=23
# print('outside fun',a)
# fun(a)
# print('outside fun',a)
# print('outside fun',id(a))

#CALL BY VALUE
#PASS INTEGER(immutable in nature)
# def fun(a):
#     print(a)
#     print('inside fun before modification : ',a)
#     print('inside fun before modification : ',id(a))
#     a=1000
#     print('inside fun after modification : ',a)
#     print('inside fun after modification : ',id(a))
    
    
    
# a=23
# print('outside fun before calling:',a)
# print('outside fun before :',id(a))
# fun(a)
# print('outside fun after calling:',a)
# print('outside fun after calling: ',id(a))


#CALL BY REFERANCE
#pass int(mutable object)
# def fun(l):
#     print('inside fun',l)
#     print('inside fun',id(l))
#     l.append(1000)
#     print('inside fun',l)
#     print('inside fun',id(l))
    
    
    
# l=[23,33,43]
# print('outside fun',l)
# print('outside fun',id(l))
# fun(l)
# print('outside fun',l)
# print('outside fun',id(l))






