string="a1b2c3d4e5f6g7h8 "

# string.replace("d","x")
# print(string)
# print(string.capitalize())
# print(string.count("a"))
# print(string.isalpha())



alpha,num="",""

for i in string:
    if i.isdecimal():
        num +=i
    else:
        alpha +=i
print(int(num),alpha)