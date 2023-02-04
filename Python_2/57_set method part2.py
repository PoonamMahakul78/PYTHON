#UNION()....
# A={23,33,43,53,63}
# B={11,12,13,23,53}
# print(A.union(B))
# print(A | B)


#INTERSECTION()
# A={23,33,43,53,63}
# B={11,12,13,23,53}
# print(A.intersection(B))
# print(A | B)


#DIFFERENCE()
# A={23,33,43,53,63}
# B={11,12,13,23,53}
# print(A.difference(B))
# print(A | B)


#SYMMETRIC DIFFERENCE()
# A={23,33,43,53,63}
# B={11,12,13,23,53}
# print(A.symmetric_difference(B))
# print(A | B)


#SUBSET()
# A={1,2,3,4,5,6,7,8,9}
# B={3,4,5,6}
# print(B.issubset(A))
# print(A.issubset(B))



# A={1,2,3,4,5,6,7,8,9}
# B={3,4,5,6}
# print(A.issuperset(B))
# print(B.issubset(A))


#DISJOINT
A={1,2,3,4,5,6,7,8,9}
B={11,12,13}
print(A.isdisjoint(B))
print(B.isdisjoint(A))