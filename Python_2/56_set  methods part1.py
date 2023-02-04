#SER METHODS
#add()

# s={23,33,43,53,63}
# s.add('surendra')
# print(s)


# s={23,33,43,53,63}
# s.add(43)
# print(s)

#UPDATE
# s={23,33,43,53,63}
# print(s)
# l=[1,2,3,4,5]
# t=('surendra','priyanka',23,24)
# s.update(l,t)
# print(s)



# s={23,33,43,53,63}
# print(s)
# l=[1,2,3,4,5]
# t=('surendra','priyanka',23,24)
# s.update(l,t, range(99,109))
# print(s)


# s={23,33,43,53,63}
# s.add(999)
# print(s)


# s={23,33,43,53,63}
# s.add(999,888)
# print(s)

# s={23,33,43,53,63}
# s.update({999,888})
# print(s)


# s={23,33,43,53,63}
# s.update(range(20),range(100,120))
# print(s)



#REMOVE

# s={23,33,43,53,63}
# s.remove(88) #KeyError: 88
# print(s)


#DISCARD()

# s={23,33,43,53,63}
# s.discard(43)
# print(s)


# s={23,33,43,53,63}
# s.remove(111)
# print(s)


#POP()
# s={23,33,43,53,63}
# s.pop()
# print(s)


# s={23,33,43,53,63}
# print(s.pop())


# s={}
# print(s.pop())

# s=set() #empty set
# print(s.pop()) #KeyError: 'pop from an empty set

#COPY()
# s1={23,33,43,53,63}  #ASSIGN
# s2=s1.copy()
# print(s1)
# print(s2)
# print(id(s1))
# print(id(s2))

# s1.add(999999)

# print(s1)
# print(s2)


# s1={23,33,43,53,63}  #COPY
# s2=s1
# print(s1)
# print(s2)
# print(id(s1))
# print(id(s2))

# s1.add(999999)

# print(s1)
# print(s2)


#CLEAR
# s={23,33,43,53,63}
# s.clear()
# print(s)
# s.clear()
# print(s)

#ENUMURATAE()

# s={23,33,43,53,63}
# for i in enumerate(s):
#     print(i)


# s={23,33,43,53,63}
# for i, j in enumerate(s):
#     print(i,' ',j)

#MIN & MAX()
# s={23,33,43,53,63}
# print(min(s))
# print(max(s))



# s={23,33,43,53,63}
# print(sum(s))


#SORTES()
s={23,33,43,53,63}
s={1,3,2,6,4}
print(sorted(s))
print(sorted(s,reverse=True))