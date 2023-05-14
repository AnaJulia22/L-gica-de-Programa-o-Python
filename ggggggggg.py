n = int(input()) #número de estrelas
dist = int()
dist1 = int() #usada para somar as distâncias
checagem = int() #usada para saber se há uma ou mais de uma distância fora da sequência
num = int() #para parar o laço
eixo_x1 = float()
eixo_y1 = float()
eixo_x2 = float()
eixo_y2 = float()
primo = False
if n <= 0: 
  print('Isso está quebrado, acho que Howard pode me ajudar.')
elif 0<n<3:
   print('Acho que bebi demais, eu juro que tinha mais estrelas!')
else:

  eixo_x1 = float(input())
  eixo_y1 = float(input())
  eixo_x2 = float(input())
  eixo_y2 = float(input())
  while(num < n): 
    num += 1
    if num != n:
     dist = ((int(eixo_x1) - int(eixo_x2))**2 + (int(eixo_y1) - int(eixo_y2))**2)**(1/2)  
     print(f'Distância [star{num} <-> star{num + 1}: {int(dist)}]') 
     eixo_x1 = eixo_x2
     eixo_y1 = eixo_y2           
    if num != n:
     if int(dist) ==  2 or int(dist) ==3 or int(dist) ==5 or int(dist) ==8 or int(dist) ==13 or int(dist) ==21 or int(dist) ==34 or int(dist) ==55 or int(dist) ==89:
          dist1 = dist1 + int(dist)
     else:
        if num != n:
          checagem += 1
          dist1 = dist1 + int(dist)
          
    if num < n - 1:
     eixo_x2 = float(input())
     eixo_y2 = float(input())
  else:
   if checagem == 1:
    print('Oh, não! Eu quase consegui!')
   if dist1 > 1: 
    for i in range(2,dist1): 
     if dist1 % i == 0: #checa se o a soma das distâncias é um número primo
      primo += 1 #se não for, soma um 

   if primo > 0 and checagem == 0:
    print('Yes! Eu consegui!') 
   elif primo > 0 and checagem > 1:
    print('Eu vou acabar como o Stuart :/')
   elif primo == 0 and checagem == 0 and n>0:
    print('Oh my god! Eu vou ganhar o Nobel primeiro que Sheldon!')
   elif primo == 0 and checagem > 1 and n>0:
    print('Pelo menos o programa está funcionando...')