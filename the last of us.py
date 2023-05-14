quantidade_mochila = int(input())
lista_tamanhos = []
lista_mochilas = []
lista_inicial = []
nomes = input().split(' ')
num = int()
num1 = int()
num2 = int()
cheio = False
checar = False
acao = ()
while (num < quantidade_mochila):
    tamanho_mochila = input()
    lista_tamanhos.append(tamanho_mochila)
    num+=1
else:
    for i in range(len(lista_tamanhos)):
        lista_inicial = ['Lanterna', 'Omega 3 da top therm']
        lista_mochilas.append(lista_inicial)
    numero_itens = int(input())
    if numero_itens <= 0:
        checar = False
    else:
        checar = True
    if checar == True:
        while(num1 < numero_itens):
            nome_item = input()
            numero_mochila = int(input())
            num1+=1
            for i in range(len(lista_tamanhos)):
             if i == numero_mochila:
                 if len(lista_mochilas[i]) == int(lista_tamanhos[i]): 
                     print('Mochila cheia. Não vai dar para levar.')
                 else:
                    lista_mochilas[i].append(nome_item)                
while (num2 == 0):
            acao = input()
            if acao == 'CHEGAMOS NO CIN!':
                num2+=1
            elif acao != 'Guardar na mochila' and acao!= 'Tirar da mochila':
                print('Ação inválida.')
            else:
              nome_item = input()
              numero_mochila = int(input())
              if acao == 'Tirar da mochila':
                for i in range(len(lista_mochilas)):
                 if i == numero_mochila:
                    if nome_item in lista_mochilas[i]:
                        lista_mochilas[i].remove(nome_item)
                        print(f'{nome_item} usado com sucesso da mochila {i}.')
                    else:
                        print(f'Você não tem {nome_item} na mochila {i}.')    
              elif acao == 'Guardar na mochila':
                for i in range(len(lista_mochilas)):
                 if i == numero_mochila:
                    if len(lista_mochilas[i]) == lista_tamanhos[i]:
                        print(f'Mochila {i} cheia!')
                    else:
                        lista_mochilas[i].append(nome_item)
                        print(f'{nome_item} adicionado na mochila {i}.')
                
else:
                for i in range(len(nomes)):
                    print(f'Mochila de {nomes[i]} chegou assim:')
                    for elementos in lista_mochilas[i]:
                        print(elementos)
                   
           