x = input("digite um número entre 10 e 99 :")
contagem = 0
loop = 1
for n in x:
    if not int(n) % 2 == 0:
        contagem = contagem + 1
    if loop == 2 and contagem == 0:
        print("Nenhum dígito é ímpar.")
    if loop == 2 and contagem == 1:
        print("Apenas um dígito é ímpar.")
    if loop == 2 and contagem == 2:
        print("Os dois dígitos são ímpares.")
    loop = loop + 1
