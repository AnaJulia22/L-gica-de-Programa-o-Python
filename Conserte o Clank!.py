parenteses = []
def rec(exp):        
         if len(exp) == 0:
               return parenteses
         elif exp[0] == '(' or exp[0] == ')':
           parenteses.append(exp[0])
           return rec(exp[1:])
         else:
            return rec(exp[1:])
n = int(input())
num = int()
while(num < n):
    parenteses_1 = 0
    parenteses_2 = 0
    num+=1
    exp = list(input())
    z = rec(exp)
    for i in range(len(z)):
        if z[i] == '(':
            parenteses_1+=1
        elif z[i] == ')':
            parenteses_2+=1
    a = parenteses_1
    b = parenteses_2
    if a == b:
        print('Essa sentença está com os parênteses balanceados, HOORAY!')
    elif a > b:
        print('A quantidade de parênteses \'(\' está maior que a de \')\', vamos descartá-la')
    elif a < b:
        print('A quantidade de parênteses \')\' está maior que a de \'(\', vamos descartá-la')
    parenteses.clear()