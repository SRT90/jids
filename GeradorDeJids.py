import random
import os

os.system('clear')
print('[$] GERADOR DE JIDS BY SALVADOR [$]')
fala = int(input('QUANTOS JIDS VAI GERAR? : '))

for i in range(fala):

    numeros = [1,2,3,4,5,6,7,8,9]
    jids = '@s.whatsapp.net,'
    n1 = str(random.choice(numeros))
    n2 = str(random.choice(numeros))
    n3 = str(random.choice(numeros))
    n4 = str(random.choice(numeros))
    n5 = str(random.choice(numeros))
    n6 = str(random.choice(numeros))
    numer = (n1+n2+n3+n4+n5+n6+jids)
    with open('jids.txt','a') as arquivo:
        arquivo.write(numer)
os.system('clear')
print('$-'*25)
print(' ')
print('{} JIDS GERADOR VERIFIQUE jids.txt BY SALVADOR'.format(fala))
print(' ')
print('$-'*25)

