dicionario = {}
descricao = []
entrada = ()
while(True): 
 try:
  entrada = input().split(' ')
  if entrada[0] == 'ADD':
    desc = input()
    #for key in :
    if entrada[-1] in dicionario.keys():
      print('Pokémon já adicionado na Pokédex')
    else:
      dicionario[entrada[-1]] = desc
      descricao.append(desc)
      print('Pokémon adicionado com sucesso')
  elif entrada[0] == 'DESC':
    if entrada[-1] in dicionario.keys():
     for key,value in dicionario.items():
      if entrada[-1] == key:
        print(value) 
    else:
      print('Ainda não há registro desse Pokémon')
 except EOFError:
    break