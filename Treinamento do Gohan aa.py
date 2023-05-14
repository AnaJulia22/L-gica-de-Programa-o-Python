N = int(input())
gohan = {}
piccolo = {}
distancia_igual = int()
sequencia1 = input().split(' ')
sequencia2 = input().split(' ')
for i in range(len(sequencia1)):
  sequencia1[i] = int(sequencia1[i])
for i in range(len(sequencia2)):
  sequencia2[i] = int(sequencia2[i])
for j in range(len(sequencia1)-1,0,-1):
 for i in range(j):
    if sequencia1[i+1] < sequencia1[i]:
        sequencia1[i+1] = sequencia1[i]
        sequencia1[i] = sequencia1[i+1] 
for j in range(len(sequencia2)-1,0,-1):
 for i in range(j):
    if sequencia2[i+1] < sequencia2[i]:
        x = sequencia2[i]
        sequencia2[i] = sequencia2[i+1] 
        sequencia2[i+1] = x
gohan['sequencia'] = sequencia1
piccolo['sequencia'] = sequencia2
if gohan == piccolo:
    print('Dale Gohan!')
else:
    print('Ih, nao foi agora, Gohan! Vamos tentar de novo semana que vem.')