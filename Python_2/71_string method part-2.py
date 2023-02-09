#LIST METHODS PART 2
#split()

s='surendra kumar panda'
print(s.split())



s='surendra kumar panda'
print(s.split('a'))
['surendr', ' kum', 'r p', 'nd', '']


s='surendra kumar panda'
print(s.split('u'))
['s', 'rendra k', 'mar panda']



s='surendra kumar pandau'
print(s.split('u'))
['s', 'rendra k', 'mar panda', '']


dob='1-1-2000'
print(dob.split('-'))  #['1', '1', '2000']


dob='1-1-2000'
print(dob.split('*')) #['1-1-2000']

#JOIN

l=['surendra','priyanka','rahul','zini']
s='+'.join(l)
print(s)
# surendra+priyanka+rahul+zini


l=['surendra','priyanka','rahul','zini']
s='*'.join(l)
print(s)
#surendra*priyanka*rahul*zini

l=['surendra','priyanka','rahul','zini']
s=''.join(l)
print(s)
#surendrapriyankarahulzini


l=['surendra','priyanka','rahul','zini']
s=' '.join(l)
print(s)
#surendra priyanka rahul zini

l=['surendra','priyanka','rahul','zini']
s='.'.join(l)
print(s)
#surendra.priyanka.rahul.zini

#REMOVING SPACE FROM THE STRING
# rstrip()
s='surendra       '
print(len(s))
print(len(s.rsplit()))


#LSTRIP()
s='               surendra'
print(len(s))
print(len(s.strip()))


#FILL CHAR()
#z fill

s='surendra'
print(s.zfill(15))


s='Poonam Mahakul'
print(s.zfill(40))


s='Poonam Mahakul'
print(s.zfill(13))


#RJUST()

s='hello'
print(s.rjust(10))


s='Poonam'
print(s.rjust(10))


s='Poonam'
print(s.rjust(50))

s='Poonam'
print(s.rjust(50, '*'))

#LJUST()
s='surendra'
print(s.ljust(10, '*'))

s='surendra'
print(s.ljust(14, '*'))

# CENTER()
s='surendra'
print(s.center(20))

s='surendra'
print(s.center(20, '*'))

s='surendra'
print(s.center(21, '*'))

#MIN()
s='surendra' #a
print(min(s))

s='surendra' 
print(max(s))

s='surendra' 
print(sorted(s))

s='surendra' 
print(sorted(s,reverse=True))

#ISIDENTIFIRE()

s='123abc'
print(s.isidentifier())

s='abc'
print(s.isidentifier())

s='True'
print(s.isidentifier())

s='***aaa'
print(s.isidentifier())

s='surendra'
for i in enumerate(s):
    print(i)


s='surendra'
for i,j in enumerate(s):
    print(i,j)





