def naturalidade(estado_civil,nome):
    if estado_civil == 1:
        conjuge = input("digite o nome do(a) seu(a) cônjuge : ").upper().strip()
        return len(nome) + len(conjuge)
    elif estado_civil == 2:
        return len(nome)
nome = input("digite seu nome : ").upper().strip()
x = int(input("digite 1 se você for casado ou 2 se for solteiro"))
print(naturalidade(x,nome))
