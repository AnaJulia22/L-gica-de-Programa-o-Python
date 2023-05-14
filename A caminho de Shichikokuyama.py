silaba_separada = []
teste_palavra_junta = []
si_hospital = []
silaba_correta = []
posicao = []
palavra_completa = False
teste = False
palavra_junta = []
silaba_juntas = []
todas_silabas = []
quantidade_silabas = int()
hospital = ['shi', 'chi', 'ko', 'ku', 'ya', 'ma']
while (palavra_completa == False):
  palavra = list(input())
  for i in range(len(palavra)):
      if palavra[i] != 'i' and palavra[i] != 'o' and palavra[i] != 'u' and palavra[i] != 'a' and palavra[i] != 'e':
                silaba_separada.append(palavra[i])
      elif palavra[i] == 'i' or palavra[i] == 'o' or palavra[i] == 'u' or palavra[i] == 'a' or palavra[i] == 'e':
                silaba_separada.append(palavra[i])
                silaba_juntas.append(''.join(silaba_separada))
                if silaba_juntas[0] in hospital:
                 if silaba_juntas[-1] not in todas_silabas:
                    quantidade_silabas+=1 
                    silaba_correta.append(silaba_juntas[0])                                         
                silaba_separada.clear()  
                silaba_juntas.clear()      
  if quantidade_silabas == 1:
    if silaba_correta[-1] not in todas_silabas:
       todas_silabas.append(silaba_correta[-1])
       print(f'Lembrei! A sílaba {silaba_correta[-1]} está no nome do hospital. Obrigada, Totoro!')
    else:
        print('Infelizmente nenhuma dessas sílabas me lembrou do nome do hospital, Totoro.') 
    quantidade_silabas = 0
  elif quantidade_silabas == 0:
      print('Infelizmente nenhuma dessas sílabas me lembrou do nome do hospital, Totoro.')  
  elif quantidade_silabas >= 2:
       quantidade_silabas = 0 
       while(teste == False):
           if silaba_correta[0] in todas_silabas:  
               silaba_correta.pop(0)
           else:
                teste = True
       for z in range(len(silaba_correta)):
         if silaba_correta[z] not in todas_silabas:
                todas_silabas.append(silaba_correta[z])
       teste = False 
       for j in range(len(silaba_correta)):
            for a in range(len(hospital)):
                if silaba_correta[j] == hospital[a]:
                        posicao.append(a)
       for ii in range(0,1):
            for i in range(len(palavra)):
                if palavra[i] != 'i' and palavra[i] != 'o' and palavra[i] != 'u' and palavra[i] != 'a' and palavra[i] != 'e':
                    silaba_separada.append(palavra[i])
                elif palavra[i] == 'i' or palavra[i] == 'o' or palavra[i] == 'u' or palavra[i] == 'a' or palavra[i] == 'e':
                    silaba_separada.append(palavra[i])
                    silaba_juntas.append(''.join(silaba_separada))
                    silaba_separada.clear()            
       if posicao[ii+1] == posicao[ii] + 1 and silaba_juntas == silaba_correta:                                 
                    palavra_junta.append(''.join(silaba_correta))
                    print('A palavra', ', '.join(palavra_junta), 'está toda no nome do hospital. Acertou em cheio, Totoro!')                
       else:   
                    for iii in range(len(posicao)):
                        for aa in range(len(hospital)):
                            if posicao[iii] == aa:
                                si_hospital.append(hospital[aa])
                    print('Lembrei! As sílabas:', ', '.join(si_hospital), 'estão no nome do hospital. Obrigada, Totoro!')
                    si_hospital.clear()
       posicao.clear()
       silaba_juntas.clear()
  if len(todas_silabas) == 6:
            palavra_completa = True
else:
   print('Conseguimos lembrar o nome do hospital shichikokuyama, agora é só pegar o Catbus e ir até lá!')