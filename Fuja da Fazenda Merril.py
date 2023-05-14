nome_personagem = input()
movimentop = ()
movimentod = ()
linhas = []
moved = False
num = int()
for i in range(8):
  linha = input()
  linhas.append(list(linha))
for i in range(len(linhas)):
  for j in range(len(linhas[i])):
    if linhas[i][j] == 'p': #descobrindo a posição de p
        posi_pi = i
        posi_pj = j
    elif linhas[i][j] == 'd': #descobrindo a posição de d
        posi_di = i
        posi_dj = j

while (num==0):
      if linhas[posi_pi][posi_pj-1] == 'o' and posi_pj != 0 or linhas[posi_pi][posi_pj+1] == 'o' or linhas[posi_pi-1][posi_pj] == 'o' or linhas[posi_pi+1][posi_pj] == 'o':
            #para o loop quando o 'o' está do lado do p
            num+=1
      elif linhas[posi_di][posi_dj-1] == 'o' or linhas[posi_di][posi_dj+1] == 'o' or linhas[posi_di-1][posi_dj] == 'o' or linhas[posi_di+1][posi_dj] == 'o':
            #para o loop quando o 'o' está do lado do d
            num+=1
      elif linhas[posi_pi][posi_pj-1] != '.' and linhas[posi_pi][posi_pj+1] != '.' and linhas[posi_pi-1][posi_pj] != '.' and linhas[posi_pi+1][posi_pj] != '.':
            num+=1
      
      elif linhas[posi_pi][posi_pj+1] == '.' or linhas[posi_pi][posi_pj-1] == '.' or linhas[posi_pi+1][posi_pj] == '.' or linhas[posi_pi-1][posi_pj] == '.':
        if linhas[posi_pi][posi_pj+1] == '.' and movimentop != 'esquerda': #se houver um espaço livre a sua direita, movo para direita
            #caso o último movimento foi seu oposto, então não faz esse movimento
          if linhas[posi_pi][posi_pj+2] == 'd': #verifica se o próximo movimento vai por p em cima do d
            if linhas[posi_pi+1][posi_pj] == '.' and linhas[posi_pi][posi_pj+1] != 'o':
                linhas[posi_pi][posi_pj] = '.'
                linhas[posi_pi+1][posi_pj] = 'p'
                posi_pi = posi_pi + 1
                movimentop = 'baixo'
                if moved == True:
                    for ii in range(len(linhas)):
                        print(' '.join(linhas[ii]))
            elif linhas[posi_pi-1][posi_pj] == '.' and linhas[posi_pi][posi_pj+1] != 'o':
               linhas[posi_pi][posi_pj] = '.' 
               linhas[posi_pi-1][posi_pj] = 'p'
               posi_pi = posi_pi - 1
               movimentop = 'cima'
               if moved == True:
                    for ii in range(len(linhas)):
                        print(' '.join(linhas[ii]))
            elif linhas[posi_pi][posi_pj-1] == '.' :
               linhas[posi_pi][posi_pj] = '.'
               linhas[posi_pi][posi_pj-1] = 'p'
               posi_pj = posi_pj - 1
               movimentop = 'esquerda'
               if moved == True:
                    for ii in range(len(linhas)):
                        print(' '.join(linhas[ii]))
          else:                                                                 
            linhas[posi_pi][posi_pj] = '.'
            linhas[posi_pi][posi_pj+1] = 'p'
            posi_pj = posi_pj + 1
            movimentop = 'direita' #se o p se mover, então o movimento realizado é atribuído à variável movimento
            if moved == True:
                    for ii in range(len(linhas)):
                        print(' '.join(linhas[ii]))                     
        elif linhas[posi_pi+1][posi_pj] == '.' and movimentop != 'cima' and linhas[posi_pi][posi_pj+1] != 'o':
          if linhas[posi_pi+2][posi_pj] == 'd': 
                if linhas[posi_pi][posi_pj+1] == '.':
                       linhas[posi_pi][posi_pj] = '.'
                       linhas[posi_pi][posi_pj+1] = 'p'
                       posi_pj = posi_pj + 1 
                       movimentop = 'direita'
                       if moved == True:
                        for ii in range(len(linhas)):
                          print(' '.join(linhas[ii]))
                elif linhas[posi_pi-1][posi_pj] == '.' and linhas[posi_pi][posi_pj+1] != 'o':
                       linhas[posi_pi][posi_pj] = '.' 
                       linhas[posi_pi-1][posi_pj] = 'p'
                       posi_pi = posi_pi - 1
                       movimentop = 'cima'
                       if moved == True:
                        for ii in range(len(linhas)):
                         print(' '.join(linhas[ii]))
                elif linhas[posi_pi][posi_pj-1] == '.':
                       linhas[posi_pi][posi_pj] = '.'
                       linhas[posi_pi][posi_pj-1] = 'p'
                       posi_pj = posi_pj - 1
                       movimentop = 'esquerda'
                       if moved == True:
                        for ii in range(len(linhas)):
                         print(' '.join(linhas[ii]))              
          else:    
            linhas[posi_pi][posi_pj] = '.'
            linhas[posi_pi+1][posi_pj] = 'p'
            posi_pi = posi_pi + 1
            movimentop = 'baixo'  
            if moved == True:
                    for ii in range(len(linhas)):
                        print(' '.join(linhas[ii]))                     
        elif linhas[posi_pi-1][posi_pj] == '.' and movimentop != 'baixo' and linhas[posi_pi][posi_pj+1] != 'o':
          if linhas[posi_pi-2][posi_pj] == 'd':
                if linhas[posi_pi][posi_pj+1] == '.':
                       linhas[posi_pi][posi_pj] = '.'
                       linhas[posi_pi][posi_pj+1] = 'p'
                       posi_pj = posi_pj + 1 
                       movimentop = 'direita'
                       if moved == True:
                        for ii in range(len(linhas)):
                         print(' '.join(linhas[ii]))
                elif linhas[posi_pi+1][posi_pj] == '.' and linhas[posi_pi][posi_pj+1] != 'o':
                       linhas[posi_pi][posi_pj] = '.'
                       linhas[posi_pi+1][posi_pj] = 'p'
                       posi_pi = posi_pi + 1
                       movimentop = 'baixo' 
                       if moved == True:
                        for ii in range(len(linhas)):
                          print(' '.join(linhas[ii]))
                elif linhas[posi_pi][posi_pj-1] == '.':
                       linhas[posi_pi][posi_pj] = '.'
                       linhas[posi_pi][posi_pj-1] = 'p'
                       posi_pj = posi_pj - 1
                       movimentop = 'esquerda' 
                       if moved == True:
                        for ii in range(len(linhas)):
                          print(' '.join(linhas[ii]))           
          else:    
            linhas[posi_pi][posi_pj] = '.' 
            linhas[posi_pi-1][posi_pj] = 'p'
            posi_pi = posi_pi - 1
            movimentop = 'cima' 
            if moved == True:
                    for ii in range(len(linhas)):
                        print(' '.join(linhas[ii]))                         
        elif linhas[posi_pi][posi_pj-1] == '.' and movimentop != 'direita':
           if linhas[posi_pi][posi_pj-2] == 'd':
                if linhas[posi_pi][posi_pj+1] == '.':
                       linhas[posi_pi][posi_pj] = '.'
                       linhas[posi_pi][posi_pj+1] = 'p'
                       posi_pj = posi_pj + 1 
                       movimentop = 'direita'
                       if moved == True:
                        for ii in range(len(linhas)):
                         print(' '.join(linhas[ii]))
                elif linhas[posi_pi+1][posi_pj] == '.' and linhas[posi_pi][posi_pj+1] != 'o':
                       linhas[posi_pi][posi_pj] = '.'
                       linhas[posi_pi+1][posi_pj] = 'p'
                       posi_pi = posi_pi + 1
                       movimentop = 'baixo'
                       if moved == True:
                        for ii in range(len(linhas)):
                         print(' '.join(linhas[ii]))
                elif linhas[posi_pi-1][posi_pj] == '.' and linhas[posi_pi][posi_pj+1] != 'o':
                       linhas[posi_pi][posi_pj] = '.' 
                       linhas[posi_pi-1][posi_pj] = 'p'
                       posi_pi = posi_pi - 1
                       movimentop = 'cima' 
                       if moved == True:
                        for ii in range(len(linhas)):
                         print(' '.join(linhas[ii]))
           else:              
            linhas[posi_pi][posi_pj] = '.'
            linhas[posi_pi][posi_pj-1] = 'p'
            posi_pj = posi_pj - 1
            movimentop = 'esquerda'  
            if moved == True:
                    for ii in range(len(linhas)):
                        print(' '.join(linhas[ii]))                                 
        if linhas[posi_di][posi_dj+1] == '.' and movimentod != 'esquerda': #faz os movimentos do d        
              linhas[posi_di][posi_dj] = '.'
              linhas[posi_di][posi_dj+1] = 'd'
              posi_dj = posi_dj + 1    
              movimentod = 'direita'          
              for ii in range(len(linhas)): #imprime os mapa dps que p e d se movimentaram
                    print(' '.join(linhas[ii]))
        elif linhas[posi_di+1][posi_dj] == '.' and movimentod != 'cima': 
              linhas[posi_di][posi_dj] = '.'
              linhas[posi_di+1][posi_dj] = 'd'
              posi_di = posi_di + 1        
              movimentod = 'baixo'      
              for ii in range(len(linhas)):
                    print(' '.join(linhas[ii]))
        elif linhas[posi_di-1][posi_dj] == '.' and movimentod != 'baixo': 
              linhas[posi_di][posi_dj] = '.' 
              linhas[posi_di-1][posi_dj] = 'd'
              posi_di = posi_di - 1
              movimentod = 'cima'
              for ii in range(len(linhas)):
                    print(' '.join(linhas[ii]))
        elif linhas[posi_di][posi_dj-1] == '.' and movimentod != 'direita': 
              linhas[posi_di][posi_dj] = '.'
              linhas[posi_di][posi_dj-1] = 'd'
              posi_dj = posi_dj - 1   
              movimentod = 'esquerda'          
              for ii in range(len(linhas)):
                    print(' '.join(linhas[ii]))            
else:
  if linhas[posi_pi][posi_pj+1] == 'o': #faz o p sair do labirinto quando chega no 'o'
    linhas[posi_pi][posi_pj] = '.'
    for ii in range(len(linhas)):
        print(' '.join(linhas[ii]))
    print(f'UFA!!! Você e {nome_personagem} conseguiram escapar do demodog e incendiar o subsolo, agora a Eleven vai conseguir fechar o portal.')
  elif linhas[posi_pi+1][posi_pj] == 'o':
        linhas[posi_pi][posi_pj] = '.'
        for ii in range(len(linhas)):
          print(' '.join(linhas[ii]))
        print(f'UFA!!! Você e {nome_personagem} conseguiram escapar do demodog e incendiar o subsolo, agora a Eleven vai conseguir fechar o portal.')
  elif linhas[posi_pi-1][posi_pj] == 'o':
        linhas[posi_pi][posi_pj] = '.'
        for ii in range(len(linhas)):
          print(' '.join(linhas[ii]))
        print(f'UFA!!! Você e {nome_personagem} conseguiram escapar do demodog e incendiar o subsolo, agora a Eleven vai conseguir fechar o portal.')
  elif linhas[posi_pi][posi_pj-1] == 'o':
        linhas[posi_pi][posi_pj] = '.'
        for ii in range(len(linhas)):
          print(' '.join(linhas[ii]))
        print(f'UFA!!! Você e {nome_personagem} conseguiram escapar do demodog e incendiar o subsolo, agora a Eleven vai conseguir fechar o portal.')
  elif linhas[posi_di][posi_dj+1] == 'o': #faz o d sair do labirinto quando chega no 'o' primeiro que o p
    linhas[posi_di][posi_dj] = '.'
    for ii in range(len(linhas)):
          print(' '.join(linhas[ii]))
    print(f'Ah não, você e {nome_personagem} não foram rápidos o bastante e o demodog passou pelo portal.')
  elif linhas[posi_di+1][posi_dj] == 'o':
        linhas[posi_di][posi_dj] = '.'
        for ii in range(len(linhas)):
              print(' '.join(linhas[ii]))
        print(f'Ah não, você e {nome_personagem} não foram rápidos o bastante e o demodog passou pelo portal.')
  elif linhas[posi_di-1][posi_dj] == 'o':
        linhas[posi_di][posi_dj] = '.'
        for ii in range(len(linhas)):
              print(' '.join(linhas[ii]))
        print(f'Ah não, você e {nome_personagem} não foram rápidos o bastante e o demodog passou pelo portal.')
  elif linhas[posi_di][posi_dj-1] == 'o':
        linhas[posi_di][posi_dj] = '.'
        for ii in range(len(linhas)):
              print(' '.join(linhas[ii]))
        print(f'Ah não, você e {nome_personagem} não foram rápidos o bastante e o demodog passou pelo portal.')
  elif  linhas[posi_pi][posi_pj-1] == 'd' and linhas[posi_pi][posi_pj+1] != '.' and linhas[posi_pi-1][posi_pj] != '.' and linhas[posi_pi+1][posi_pj] != '.':
    #serve pra fazer o movimento de d quando ele pega o p
    linhas[posi_pi][posi_pj] = 'd'  
    linhas[posi_pi][posi_pj-1] = '.'  
    for ii in range(len(linhas)):
                    print(' '.join(linhas[ii]))
    print(f'Ah não, você e {nome_personagem} foram pegos pelo demodog e agora ele vai atravessar o portal e talvez a eleven não consiga salvar todos.')  
  elif  linhas[posi_pi][posi_pj+1] == 'd' and linhas[posi_pi][posi_pj-1] != '.' and linhas[posi_pi-1][posi_pj] != '.' and linhas[posi_pi+1][posi_pj] != '.':
        linhas[posi_pi][posi_pj] = 'd' 
        linhas[posi_pi][posi_pj+1] = '.' 
        for ii in range(len(linhas)):
                    print(' '.join(linhas[ii]))
        print(f'Ah não, você e {nome_personagem} foram pegos pelo demodog e agora ele vai atravessar o portal e talvez a eleven não consiga salvar todos.')    
  elif  linhas[posi_pi+1][posi_pj] == 'd' and linhas[posi_pi-1][posi_pj] != '.' and linhas[posi_pi][posi_pj-1] != '.' and linhas[posi_pi][posi_pj+1] != '.':
        linhas[posi_pi][posi_pj] = 'd' 
        linhas[posi_pi+1][posi_pj] = '.' 
        for ii in range(len(linhas)):
                    print(' '.join(linhas[ii]))
        print(f'Ah não, você e {nome_personagem} foram pegos pelo demodog e agora ele vai atravessar o portal e talvez a eleven não consiga salvar todos.')  
  elif  linhas[posi_pi-1][posi_pj] == 'd' and linhas[posi_pi+1][posi_pj] != '.' and linhas[posi_pi][posi_pj-1] != '.' and linhas[posi_pi][posi_pj+1] != '.':
        linhas[posi_pi][posi_pj] = 'd'  
        linhas[posi_pi-1][posi_pj] = '.'
        for ii in range(len(linhas)):
                    print(' '.join(linhas[ii]))
        print(f'Ah não, você e {nome_personagem} foram pegos pelo demodog e agora ele vai atravessar o portal e talvez a eleven não consiga salvar todos.')  
                