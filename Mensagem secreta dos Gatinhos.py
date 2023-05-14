def traducao(alfabeto, numero):  
    frase_traduzida = []  
    invalido = False
    for i in range(len(numero)):
        numero[i] = int(numero[i]) 
    for ii in range(len(numero)):
     for j in range(len(alfabeto)):
        if j == numero[ii]:
            frase_traduzida.append(alfabeto[j])
    for i in range(len(numero)):
        if numero[i] > 100:
            print('Infelizmente os números nao dizem nada')
            invalido = True
    for i in range(len(numero)):
        if numero[i] == 100:
            frase_traduzida.insert(i,' ') 
    if invalido == False:  
        print(''.join(frase_traduzida))
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X']
traducao(alfabeto, numero = input().split(' '))


