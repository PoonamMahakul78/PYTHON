#PRINT THIS STAR IN REVERSE ORDER
"""
*  *  *  *
*  *  *
*  *
*
"""

n=int(input())

for i in range(n, 0, -1):
    # print(i)
    for j in range(i):
        print("*",end=" ")
    print()
