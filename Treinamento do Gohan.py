N = int(input())
gohan = {}
piccolo = {}
sequencia1 = input().split(' ')
sequencia2 = input().split(' ')
def comp(sequencia,dicionario):
 distancia_igual = int()
 for i in range(len(sequencia)):
    numero = sequencia[i]
    for j in range(len(sequencia)):
        if sequencia[j] == numero:
            distancia_igual+=1
    if sequencia[i] not in dicionario.keys():
        dicionario[sequencia[i]] = distancia_igual
    distancia_igual = 0
 return dicionario
gohan = comp(sequencia1,gohan)
piccolo = comp(sequencia2,piccolo)
if gohan == piccolo:
        print('Dale Gohan!')
else:
        print('Ih, nao foi agora, Gohan! Vamos tentar de novo semana que vem.')