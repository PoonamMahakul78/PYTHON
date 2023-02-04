#WITH OUT SET COMPREHENSION
#create a set from list
# l=[23,33,43,53,63]
# s=set()

# for i in l:
#     s.add(i)
# print(s)


#WITH SET COMPREHENSION
#create a set from list

# l=[23,33,43,53,63]

# s={i for i in l}
# print(s)

#EXAMPLE

# l=[23,33,43,53,63]

# s={i*2 for i in l}
# print(s)


#WORK WITH RANGE

# s={i for i in range(100,111)}
# print(s)


# s={i**2 for i in range(11)}
# print(s)


#CREATE A SET BY ADDING ALL THE ELEMENT FROM 20 TO 40 WHICH IS DIVISIBLE BY 4

# s={i for i in range(20,41) if i%4==0}
# print(s)


#CREATE A SET FROM LIST CALLED AS NAME BY ADDING THE FIRST CGAR OF EACH ELEMENT
# names=['surendra','priyanka','rahul','zini']
# s={i[0] for i in names}
# print(s)


# names=['surendra','priyanka','rahul','zini']
# s={i[0].upper() for i in names}
# print(s)


#CREATE A SET FROM S LIST (NAMES) BY ADDING ALL THE ELEMENTS BUT IF THE ELEMENT IS PRIYANKA THEN INSTREADE OF PRIYANKA ADD ANJALI


names=['surendra','priyanka','rahul','zini']

s={i if i!='priyanka' else'anjali'for i in names}
print(s)
