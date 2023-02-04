# l=[10,20,30,40,50]
# s=['surendra','priyanka',999,888,777]
# r=l+s
# print(r)


# l=[10,20,30,40,50]
# s=['surendra','priyanka',999,888,777]
# a=[12.3,45.7,True,False]
# r=l+s+a
# print(r)

#WE CAN NOT JOINT LIST INTEGER
# l=[10,20,30,40,50]
# s=[100]
# r=l+s
# print(r)


#REPETITION OF LIST
# l=[10,20,30,40,50]
# r=l*5
# print(r)

# l=[10,20,30,40,50]
# r=l*5.7      #TYPE ERROR
# print(r)



#MEMBERSHIP OPERATOR(in,not in)

# l=[10,20,30,40,50]
# print(20 in l)
# print(20 not in l)
# print(999 in l)
# print(999 not in l)

#WAP TO CHECK WEATHER YOUR LUCKY NUMBER IS PRESENT INSIDE LIST OR NOT

# l=[1,2,3,5,6,7,9,11,12,17,18,23,25,67,92,99]
# choice=int(input('Enter ur lucky number'))

# if choice in l:
#     print("Yes ur lucky number is available")
# else:
#     print("Sry lucky number is not available")

#WAP TO CHECK YOUR LUCKY NUMBER UNTIL MATCH YOUR LUCKY NUMBER WITH LIST ELEMEMT

l=[1,2,3,5,6,7,9,11,12,17,18,23,24,25,67,92,99]

choice=int(input("Enter ur lucky number :"))

while True:
    if choice in l:
        print("yes ur lucky number is present")
        break
    else:
        print("sry ur lucky number is not present")
        choice=int(input("Enter ur lucky number :"))