#CHECKING STARTING AND ENDING OF STRING

s="hello python programming language"
print(s.startswith('hello'))
print(s.startswith('Hello'))
print(s.endswith('language'))
print(s.endswith('abc'))


#CHECKING WHAT TYPE OF CHAR IS PRESENT IN GIVEN STRING
s="hello python programming language"
print(s.isalpha()) #because of space it will shows error


s="hello pythonprogramminglanguage"
print(s.isalpha())


s="hello python"
print(s.isalpha())


s="hello python"
print(s.isalpha())


s="1Hello python"
print(s.isalpha())




s="Hellopython"
print(s.isalnum())


s="1111"
print(s.isalnum())




s="1*2"
print(s.isalnum())

s="123"
print(s.isdigit())

s="123hello"
print(s.isdigit())


s="123hello"
print(s.islower())


s="123Hello"
print(s.islower())


s="123hEllo"
print(s.isupper())


s="ABC"
print(s.isupper())



s="Poonam"
print(s.istitle())

s="sRENDRA"
print(s.isspace())


# CHANGE CASE

s="Hello python language"
print(s.upper())
print(s)


s="Hello python language"
s1=s.upper()
print(s)
print(s1)

print(id(s))
print(id(s1))


s="Hello python language"
print(s.swapcase())


s="Hello python language"
print(s.title())


s="Hello python language"
print(s.capitalize())



#FIND OUT THE LENGTH ND COUNT
s="Hello python language"
print(len(s))

s="Hello python language"
print(s.count('a'))

s="Hello python language"
print(s.count('a',18))


#REPLACE
s='python is bad programming'
print(s.replace('bad','good'))
print(s)
