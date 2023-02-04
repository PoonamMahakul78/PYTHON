num=int(input('Enter a number(if u want to exit plz enter -1)'))
np=0
mn=0
nz=0
while num!=-1:
    if num>0:
        np=np+1
    elif num<0:
        nm=np+1
    else:
        nz=nz+1
    num=int(input('Enter a number(if u want to exit plz enter -1)'))

print('Number of positive',np)
print('Number of Negative',np)
print('Number of zeros',nz)
