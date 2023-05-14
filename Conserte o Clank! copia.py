#def soma_parent(x,y):
 #     if:
  #    else:
n = int(input())
num = int()
while(num < n):
    num+=1
    exp = list(input())
    parenteses_1 = 0
    parenteses_2 = 0
    for i in range(len(exp)):
        if exp[0] == '(':
            parenteses_1 += 1
            exp.pop(0)
        elif exp[0] == ')': 
            parenteses_2 += 1
            exp.pop(0)
        else:
            exp.pop(0)
    x = parenteses_1
    y = parenteses_2
    if x == y:
        print('Essa sentença está com os parênteses balanceados, HOORAY!')
    elif x > y:
        print('A quantidade de parênteses \'(\' está maior que a de \')\', vamos descartá-la')
    elif x < y:
        print('A quantidade de parênteses \')\' está maior que a de \'(\', vamos descartá-la')
    
      