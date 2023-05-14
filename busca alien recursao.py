nmr_binario = []
def rec_binar(x):    
    if x==0:
        return nmr_binario
    else:
        y = x%2
        nmr_binario.append(y)
        rec_binar(int(x/2))        
numeros = input().split(' ')
nmr_escolhido = int(input())
qtd_bits = int(input())
bits = False
coordenadas = []
coordenada = str()
for i in range(len(numeros)):
      numeros[i] = int(numeros[i])
for i in range(nmr_escolhido+1):
    if i == nmr_escolhido:
        x = i
rec_binar(x)
if len(nmr_binario) == qtd_bits:
    nmr_binario = nmr_binario
    bits = True
elif len(nmr_binario)< qtd_bits:
    while(len(nmr_binario)<qtd_bits):
        nmr_binario.append(0)
        bits = True
elif len(nmr_binario) > qtd_bits:
    bits = False
nmr_binario.reverse()
if bits == True:
  for i in range(len(nmr_binario)):
    nmr_binario[i] = str(nmr_binario[i])
  nmr_binario = ''.join(nmr_binario)
if nmr_escolhido<numeros[0] or nmr_escolhido>numeros[-1]:
  print('Acho que a Doutora se confundiu, pois é impossível chegar nesse número pois ele é menor que a menor sala ou maior que o maior da sala.')
else:
 while(len(numeros) != 1):
   if len(numeros)%2 == 0:
    for i in range(len(numeros)):
      if i == (len(numeros)/2):
        porta_centro = numeros[i]
        posi_centro = i
   else:
    for i in range(len(numeros)):
      if i == ((len(numeros)-1)/2):
        porta_centro = numeros[i]
        posi_centro = i   
   if nmr_escolhido > porta_centro:
      for j in range(len(numeros)):
        if j<=posi_centro and len(numeros)>1:
          numeros.remove(numeros[0])
      coordenadas.append('Direita')
   elif nmr_escolhido < porta_centro and len(numeros)>1:
      for j in range(len(numeros)):
        if j>=posi_centro:
          numeros.remove(numeros[-1])
      coordenadas.append('Esquerda')   
   if len(numeros) == 1 and nmr_escolhido == numeros[0]:
      coordenadas.append('Meio')
   elif nmr_escolhido == porta_centro:
      porta_achada = True
      coordenadas.append('Meio')
      for j in range(len(numeros)):
            if j<posi_centro:
                numeros.remove(numeros[0])
            elif j>posi_centro:
                numeros.remove(numeros[-1])
 else:
   coordenada = ' -> '.join(coordenadas) 
   if numeros[0] == nmr_escolhido and bits==False:
     print('Consegui encontar a saída, mas não consigo falar pois o número é muito grande para essa quantidade de bits.')
   elif numeros[0] != nmr_escolhido and bits==False:
     print('Busquei muito, mas não achei a sala, que nem posso dizer, já que tenho poucos bits.')
   elif numeros[0] == nmr_escolhido and bits == True:
     print(f'{coordenada}, seguindo por essas coordenadas você vai chegar no número {nmr_binario}.')
   elif numeros[0] != nmr_escolhido and bits==True:
     print(f'{coordenada}, mas não consegui achar.')