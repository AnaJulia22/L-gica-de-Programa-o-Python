N = int(input())
matriz1 = []
matriz2 = []
num = int()
contador = int()
counter = int()
soma = False
subtracao = False
multiplicacao = False
multiplicacao_escalar = False
x = []
x1 = []
result = []
while(num<(N*2)): 
    numeros = input().split()
    if counter < N:
        matriz1.append(numeros)
    elif counter >= N:
        matriz2.append(numeros)
    counter+=1
    num+=1
for i in range(len(matriz1)):
        row = [0] * N
        result.append(row)
qtd_op = int(input())
while(contador<qtd_op):
    operacao = input().split()
    contador+=1
    for i in range(len(operacao)):
            if operacao[i] == '+':
                soma = True
            elif operacao[i] == '-':
                subtracao = True
            elif operacao[i] == '.':
                multiplicacao = True
            elif operacao[i] == '*':
                multiplicacao_escalar = True
    if soma == True:        
                soma = False    
                if operacao[2] == 'm1' and operacao[4] == 'm1': 
                  for i in range(len(matriz1)):
                     for j in range(len(matriz1[i])): 
                        if operacao[0] == 'm1':
                            matriz1[i][j] = str(int(matriz1[i][j]) + int(matriz1[i][j])) 
                        elif operacao[0] == 'm2':
                            matriz2[i][j] = str(int(matriz1[i][j]) + int(matriz1[i][j]))
                elif operacao[2] == 'm1' and operacao[4] == 'm2':
                  for i in range(len(matriz1)):
                         for j in range(len(matriz1[i])):
                            if operacao[0] == 'm1':
                                matriz1[i][j] = str(int(matriz1[i][j]) + int(matriz2[i][j])) 
                            elif operacao[0] == 'm2':
                                matriz2[i][j] = str(int(matriz1[i][j]) + int(matriz2[i][j]))
                elif operacao[4] == 'm1' and operacao[2] == 'm2':
                      for i in range(len(matriz1)):
                         for j in range(len(matriz1[i])):
                            if operacao[0] == 'm1':
                                matriz1[i][j] = str(int(matriz1[i][j]) + int(matriz2[i][j])) 
                            elif operacao[0] == 'm2':
                                matriz2[i][j] = str(int(matriz1[i][j]) + int(matriz2[i][j]))
                elif operacao[2] == 'm2' and operacao[4] == 'm2':
                    for i in range(len(matriz1)):
                         for j in range(len(matriz1[i])):
                            if operacao[0] == 'm1':
                                matriz1[i][j] = str(int(matriz2[i][j]) + int(matriz2[i][j])) 
                            elif operacao[0] == 'm2':
                                matriz2[i][j] = str(int(matriz2[i][j]) + int(matriz2[i][j])) 
    elif subtracao == True:
            subtracao = False
            if operacao[2] == 'm1' and operacao[4] == 'm1': 
                  for i in range(len(matriz1)):
                     for j in range(N**2): 
                        if operacao[0] == 'm1':
                            matriz1[i][j] = (int(matriz1[i][j]) - int(matriz1[i][j]))
                        elif operacao[0] == 'm2':
                            matriz2[i][j] = (int(matriz1[i][j]) - int(matriz1[i][j]))
            elif operacao[2] == 'm1' and operacao[4] == 'm2':
                  for i in range(len(matriz1)):
                         for j in range(len(matriz1[i])):
                            if operacao[0] == 'm1':
                                matriz1[i][j] = (int(matriz1[i][j]) - int(matriz2[i][j])) 
                            elif operacao[0] == 'm2':
                                matriz2[i][j] = (int(matriz1[i][j]) - int(matriz2[i][j])) 
            elif operacao[2] == 'm2' and operacao[4] == 'm1':
                  for i in range(len(matriz1)):
                         for j in range(len(matriz1[i])):
                            if operacao[0] == 'm1':
                                matriz1[i][j] = (int(matriz2[i][j]) - int(matriz1[i][j])) 
                            elif operacao[0] == 'm2':
                                matriz2[i][j] = (int(matriz2[i][j]) - int(matriz1[i][j])) 
            elif operacao[2] == 'm2' and operacao[4] == 'm2':
                    for i in range(len(matriz1)):
                         for j in range(len(matriz1[i])):
                            if operacao[0] == 'm1':
                                matriz1[i][j] = (int(matriz2[i][j]) - int(matriz2[i][j]))
                            elif operacao[0] == 'm2':
                                matriz2[i][j] = (int(matriz2[i][j]) - int(matriz2[i][j]))    
    elif multiplicacao == True:
            multiplicacao = False
            if operacao[2] == 'm1' and operacao[4] == 'm1': 
                  for i in range(len(matriz1)):
                     for j in range(len(matriz1[0])): 
                      for k in range(len(matriz1)):                        
                           result[i][j] += (int(matriz1[i][k]) * int(matriz1[k][j]))
                 
                  if operacao[0] == 'm1':              
                                    matriz1 = result
                  elif operacao[0] == 'm2':              
                                    matriz2 = result
            elif operacao[2] == 'm1' and operacao[4] == 'm2':
                  for i in range(len(matriz1)):
                         for j in range(len(matriz2[0])):
                          for k in range(len(matriz2)):                            
                                result[i][j] += (int(matriz1[i][k]) * int(matriz2[k][j])) 
                 
                  if operacao[0] == 'm1':                  
                                        matriz1 = result
                  elif operacao[0] == 'm2':                  
                                        matriz2 = result
            elif operacao[4] == 'm1' and operacao[2] == 'm2':
                  for i in range(len(matriz1)):
                         for j in range(len(matriz1[0])):
                          for k in range(len(matriz2)):                            
                                result[i][j] += (int(matriz1[i][k]) * int(matriz2[k][j]))
                  if operacao[0] == 'm1':
                                        matriz1 = result
                  elif operacao[0] == 'm2':               
                                    matriz2 = result                
            elif operacao[2] == 'm2' and operacao[4] == 'm2':
                    for i in range(len(matriz1)):
                         for j in range(len(matriz1[0])):
                          for k in range(len(matriz2)):                            
                                result[i][j] += (int(matriz2[i][k]) * int(matriz2[k][j]))
                    if operacao[0] == 'm1':
                                 matriz1 = result 
                    elif operacao[0] == 'm2':         
                                matriz2 = result         
    elif multiplicacao_escalar == True:
        multiplicacao_escalar = False
        if operacao[2] == 'm1':
         for i in range(len(matriz1)):
          for j in range(len(matriz1[i])):
             if operacao[0] == 'm1':
                matriz1[i][j] = (int(matriz1[i][j]) * int(operacao[4]))
             elif operacao[0] == 'm2':
                matriz2[i][j] = (int(matriz1[i][j]) * int(operacao[4]))
        elif operacao[2] == 'm2':
         for i in range(len(matriz1)):
          for j in range(len(matriz1[i])):
             if operacao[0] == 'm1':
                 matriz1[i][j] = (int(matriz2[i][j]) * int(operacao[4]))
             elif operacao[0] == 'm2':
                 matriz2[i][j] = (int(matriz2[i][j]) * int(operacao[4]))
        elif operacao[4] == 'm1':
         for i in range(len(matriz1)):
            for j in range(len(matriz1[i])):
             if operacao[0] == 'm1':
                 matriz1[i][j] = (int(matriz1[i][j]) * int(operacao[2]))
             elif operacao[0] == 'm2':
                 matriz2[i][j] = (int(matriz1[i][j]) * int(operacao[2]))
        elif operacao[4] == 'm2':
         for i in range(len(matriz1)):
          for j in range(len(matriz1[i])):
             if operacao[0] == 'm1':
                 matriz1[i][j] = (int(matriz2[i][j]) * int(operacao[2]))
             elif operacao[0] == 'm2':
                 matriz2[i][j] = (int(matriz2[i][j]) * int(operacao[2]))        
else:   
      if operacao[0] == 'm1':
        for a in range(len(matriz1)):
          for b in range(len(matriz1[a])):
            matriz1[a][b] = str(matriz1[a][b])
        for i in range(len(matriz1)):
                print(' '.join(matriz1[i]))
      elif operacao[0] == 'm2':
        for a in range(len(matriz1)):
          for b in range(len(matriz1[a])):
            matriz2[a][b] = str(matriz2[a][b])
        for i in range(len(matriz2)):
                print(' '.join(matriz2[i]))       
    
