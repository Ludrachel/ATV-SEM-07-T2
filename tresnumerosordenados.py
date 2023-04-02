valor_a = int(input())
valor_b = int(input())
valor_c = int(input())

auxiliar = 0

if valor_a < valor_b:
    if valor_b < valor_c:
        pass
        if valor_b < valor_c:
            pass
if valor_c < valor_a:
    auxiliar = valor_c
    valor_c = valor_a
    valor_a = auxiliar
    if valor_c < valor_b:
        auxiliar = valor_c
        valor_c = valor_b
        valor_b = auxiliar
if valor_b < valor_a:
    auxiliar = valor_b
    valor_b = valor_a
    valor_a = auxiliar
print(valor_a)
print(valor_b)
print(valor_c)
