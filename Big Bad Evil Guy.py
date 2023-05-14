adversarios = {'Vingador': 30,
            'Tiamat': 20,
            'Vingador das Sombras': 14}
personagens = {'Bobby': [8 , 1],
'Diana': [12, 3],
'Eric': [8, 0],
'Hank': [6, 1],
'Presto': [4, 3],
'Sheila': [6, 3],
'Uni': [2, 3]}
fim_batalha = False
num = int()
adversario = input()
if adversario in adversarios:
    for key, value in adversarios.items():
        if adversario == key:
            vida = value
else:
    vida = 9
turnos = int(input())
while(fim_batalha == False):
  num +=1
  personagem = input()
  if personagem == 'Mestre dos Magos':
    vida = 0
  elif personagem in personagens:
    for key, value in personagens.items():
        if personagem == key:
            vida = vida - value[0]
            turnos = turnos - value[1]
  if vida <= 0:
        fim_batalha = True
  elif turnos <= 0 or num==turnos:
        fim_batalha = True
else:
    if personagem == 'Mestre dos Magos':
        print('Muito obrigado amigo, que nos vejamos novamente um dia')
    elif vida > 0:
        print(f'Oh nao, {adversario} e muito forte, este e o fim!')
    else:
        print(f'{personagem} executou o ultimo golpe em {adversario}, estamos livres!')