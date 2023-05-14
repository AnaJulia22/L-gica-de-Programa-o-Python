def mod11(n):
  if n == 0:
    return 0
  else:
    return n%11
def fatorial (n):
  if n == 0:
    return 1
  else:
    return n * fatorial(n-1)
def fibonacci(n):
  if n == 0 or n == 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n-2)
senha_alter = list(input())
num = int()
igual = int()
palavra = []
lista_fat = []
lista_fib = []
qtd_pal = int(input())
posi_alfab = int()
while(num < qtd_pal):
  num+=1
  palavra_teste = list(input())
  for i in range(len(palavra_teste)):
    if palavra_teste[i] == 'a':
      posi_alfab = 0
    elif palavra_teste[i] > 'a':
      posi_alfab = ord(palavra_teste[i]) - ord('a')
    posi_mod11 = mod11(posi_alfab)
    for j in range(posi_mod11):
        fat = fatorial(j)
        lista_fat.append(fat)
    for k in range(posi_mod11):
      if len(lista_fib) == 0:
            lista_fib.append(0)
      if len(lista_fib) != posi_mod11:
        fib = fibonacci(k)
        lista_fib.append(fib)
    if posi_mod11%2 != 0:
     for i in range(len(lista_fat)):
        multi = (int(lista_fat[i]) * int(lista_fib[i])) + ord('a')
        convert = chr(multi)
        palavra.append(convert)
    elif posi_mod11 == 0:
     palavra.append(1)
    else:
        for i in range(len(lista_fat)):
         soma = (int(lista_fat[i]) + int(lista_fib[i])) + ord('a')
         convert = chr(soma)
         palavra.append(convert)
    lista_fat.clear()
    lista_fib.clear()
  if palavra == senha_alter:
        igual +=1
  elif palavra != senha_alter:
        igual = igual
  palavra.clear()
else:
    if igual > 0:
        print('Achamos! Achamos a senha.')
    else:
        print('É... Temos que procurar mais.')