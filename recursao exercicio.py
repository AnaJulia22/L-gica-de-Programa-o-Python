def rec_produto(numero1,numero2):
    if numero1==1:
       return numero2
    else:
        return numero2 + rec_produto(numero1-1,numero2)
x = rec_produto(2,3)
print(x)
