d={}
while True:
    bf=input('Enter the bf name :')
    gf=input('Enter your gf name :')
    d[bf]=gf

    choice=input('Do u want to add more item[Y/N]')

    if choice=='N':
        break

while True:
    bf=input('Enter bf name to get gf name :')
    gf=d.get(bf,0)

    if gf==0:
        print('Sry bf name is not available')
    else:
        print(f'Hi{bf} your gf name is {gf}')

    choice=input('Do u want to search more item[Y/N]')

    if choice=='N':
        break






