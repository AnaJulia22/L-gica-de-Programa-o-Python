estoque = {'trigo':(5,3), 'fermento':(5,2), 
                'ovos':(5,2), 'batata':(5,4),
                'arroz':(5,3), 'siri':(5,8), 
                'pao':(5,2), 'tomate':(5,2),
                'alface':(5,1), 'picles':(5,3), 
                'queijo':(5,5), 'manteiga':(5,6)}
cardapio = {'hamburguer de siri':24, 'pizza de siri':42,
            'siri frito':15, 'siri a parmegiana':24}
ingrediente_cardapio = {'hamburguer de siri':('siri', 'pao', 'alface', 'tomate', 'queijo','picles'),
                        'pizza de siri': ('siri', 'trigo', 'fermento', 'ovos', 'queijo'),
                        'siri frito': ('siri', 'manteiga'),
                        'siri a parmegiana':('siri', 'trigo', 'ovos', 'queijo', 'tomate')}
pedidos_negados = {'hamburguer de siri': 0, 'pizza de siri':0, 'siri frito':0, 'siri a parmegiana':0}
pedidos_aceitos = {}
ingred = ()
mais_vendido = str()
preco = int()
falta = False
counter = int()
caixa = int(40)
lucro = int()
teste = True
while(teste == True):
 try:
  pedido = input()
  falta = False
  if pedido not in cardapio:
    if pedido in pedidos_negados:
        for key,value in pedidos_negados.items():
            if key == pedido:
                value = value + 1
                pedidos_negados[key] = value
                if value > 2:
                    ingredientes = input().split(' ')
                    ingred = tuple(ingredientes)
                    print(f'Atendendo demandas, {pedido} é a mais nova adição ao cardápio do Siri Cascudo.')
                    ingrediente_cardapio[pedido] = ingred
                    for a,b in estoque.items():
                     for i in ingred:
                        if a==i:
                            preco = preco + b[1]
                    cardapio[pedido] = preco + 5
                    preco = 0
                    pedidos_aceitos[pedido] = 0
                    pedidos_negados[pedido] = 0          
                else:
                    print(f'{pedido} ainda não é uma opção disponível.')
    else:
        print(f'{pedido} ainda não é uma opção disponível.')
        falta = True
        pedidos_negados[pedido] = 1
  else:
    for key, value in ingrediente_cardapio.items():
        if key == pedido:
            for i in range(len(value)):
              for j in estoque.keys():
                if value[i] == j:
                    for a, b in estoque.items():
                        if a == j:
                         if b[0] > 0:
                            b = (b[0]-1,b[1])
                            estoque[a] = b
                         elif b[0] == 0:
                            caixa = caixa - b[1]*4
                            b = (3,b[1])
                            estoque[a] = b
    for key, value in cardapio.items():
        if key == pedido:
            caixa = caixa + value
    if pedido in pedidos_aceitos.keys():
     for key, value in pedidos_aceitos.items():
        if key == pedido:
            value = value + 1
            pedidos_aceitos[key] = value
    else:
        pedidos_aceitos[pedido] = 1
    print(f'{pedido} saindo...')
 except EOFError:
  teste = False
  print('##### Fim do expediente #####')
  caixa = caixa - 40
  print(f'O lucro obtido no dia de hoje foi de R${caixa}.')
  for key, value in pedidos_aceitos.items():
        if counter == 0:
            maior_valor = value
            mais_vendido = key
        if counter > 0:
            if value > maior_valor:
                 maior_valor = value 
                 mais_vendido = key  
            elif value == maior_valor:
                maior_valor = maior_valor 
        counter+=1
  if mais_vendido == 'hamburguer de siri':
        print('O bom e tradicional hambúrguer de siri, líder em vendas, nunca será superado!')
  else:
        mais_vendido = mais_vendido.capitalize()
        print(f'{mais_vendido} está fazendo sucesso entre os clientes, ultrapassando até mesmo o lendário hambúrguer de siri.')