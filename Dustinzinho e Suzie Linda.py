matriz = int(input())
elementos_matriz = []
lista_linha = []
lista_coluna = []
lista_diagonal = []
lista_pares = []
soma_linha = []
soma_coluna = []
soma_diagonal = []
num = int()
soma = int()
while (num < matriz):
    N = input().split(' ')
    elementos_matriz.append(N)
    num+=1
for i in range(len(elementos_matriz)):
    for j in range (len(elementos_matriz[i])):
        elementos_matriz[i][j] = int(elementos_matriz[i][j])

for i in range(len(elementos_matriz)):
    for j in range (len(elementos_matriz[i]) - 1):
        soma = elementos_matriz[i][j] + elementos_matriz[i][j+1]
        soma_linha.append(soma)
        lista_linha.append(elementos_matriz[i][j])
        lista_linha.append(elementos_matriz[i][j+1])
posicao_max = soma_linha.index(max(soma_linha))
for i in range (len(lista_linha)):
    if i == posicao_max*2:
        lista_pares.append(lista_linha[i])
    elif i == (posicao_max*2)+1:
        lista_pares.append(lista_linha[i])
for j in range(len(elementos_matriz)):
    for i in range(len(elementos_matriz)-1):
        soma = elementos_matriz[i][j] + elementos_matriz[i+1][j]
        soma_coluna.append(soma)
        lista_coluna.append(elementos_matriz[i][j])
        lista_coluna.append(elementos_matriz[i+1][j])
posicao_max = soma_coluna.index(max(soma_coluna))
for i in range(len(lista_coluna)):
    if i == posicao_max*2:
        lista_pares.append(lista_coluna[i])
    elif i == (posicao_max*2)+1:
        lista_pares.append(lista_coluna[i])
for i in range(len(elementos_matriz)-1):
    for j in range(len(elementos_matriz[i])-1):
        if i == j:
            soma = elementos_matriz[i][j] + elementos_matriz[i+1][j+1]
            soma_diagonal.append(soma)
            lista_diagonal.append(elementos_matriz[i][j])
            lista_diagonal.append(elementos_matriz[i+1][j+1])
posicao_max = soma_diagonal.index(max(soma_diagonal))
for i in range(len(lista_diagonal)):
    if i == posicao_max*2:
        lista_pares.append(lista_diagonal[i])
    elif i == (posicao_max*2)+1:
        lista_pares.append(lista_diagonal[i])
print('Falei que era fácil Dustinzinho...')
print('Pegando todas os números que formam as combinações dos pares de cada sentido temos...')
for i in range(len(lista_pares)):
    lista_pares[i] = str(lista_pares[i])
print('Password:',''.join(lista_pares))
