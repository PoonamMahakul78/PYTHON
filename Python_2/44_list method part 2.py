#EXTEND()

# l=[10,20,30,40,50]
# s=[100,200,300]
# l.extend(s)
# print(l)

#SORT()
# l=[10, 2, 20, 3, 6, 1, 8]
# l.sort()
# print(l)


# l=[10, 2, 20, 3, 6, 1, 8]
# l.sort(reverse=True)
# print(l)


# l=['surendra','rahul',23,33,43,54]
# l.sort()
# print(l)


# l=[2, 1, 4, 3,  6,  8, 5]
# print(l)
# l.clear()
# print(l)



# l=[2, 1, 4, 3,  6,  8, 5]
# print(l)
# del l
# print(l)



#COPY()

# l=[10,20,30,40,50]
# s=l.copy()  #cloning

# print(l)
# print(s)


# print(id(l)) #2448799858496
# print(id(s)) #2448801359104


# s[2]=9999

# print(l)
# print(s)

#ASSIGN CONCEPT

l=[10,20,30,40,50]
s=l  #assign

print(l)
print(s)

     #SAME MEMORY LOCATION
print(id(l)) #2695211089728
print(id(s)) #2695211089728

s[2]=9999

print(l)
print(s)
