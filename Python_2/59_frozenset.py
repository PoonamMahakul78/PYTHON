# s={23,33,43,53,63}
# fs=frozenset(s)
# print(fs)
# print(type(fs))


#CREATING FROZENSET FROM LIST
# l=[23,1,2,3,5,7]
# fs=frozenset(l)
# print(fs)
# print(type(fs))



# fs=frozenset(range(10))
# print(fs)

# fs=frozenset(range(10))
# fs.add(888)
# fs.remove(1)


#APPLYING OTHER NORMAL METHODD WHICH WILL NOT MODIFY FROZENSET
fs1=frozenset([23,33,43,53,63])
fs2=frozenset([11,12,13,23,53])
fs3=frozenset([23,43])
fs5=frozenset([99,100])
# fs4=fs1.copy()
# print(fs4)


# print(fs1.union(fs2))
# print(fs1.intersection(fs2))
# print(fs1.difference(fs2))
# print(fs1.symmetric_difference(fs2))


# print(fs3.issubset(fs1))
# print(fs3.issuperset(fs3))
# print(fs3.isdisjoint(fs3))
# print(fs1.isdisjoint(fs3))

