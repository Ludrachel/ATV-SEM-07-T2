x = input("digite um número entre 100 e 999 : ")
contagem = 0
for n in x:
    if int(n) % 2 == 0:
        contagem = contagem + 1
print(contagem)
