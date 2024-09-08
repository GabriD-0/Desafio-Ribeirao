# 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

# IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

def contador_letra_a(s):
    count_min = s.count('a')
    count_mai = s.count('A')
    total = count_min + count_mai
    return count_min, count_mai, total

string = "Hoje andei de cArro e encontrei uma velhA senhora almoçando."

count_min, count_mai, total = contador_letra_a(string)

if total > 0:
    print(f"A letra 'a' aparece {total} vezes na string, sendo {count_min} vezes minúscula e {count_mai} vezes maiúscula.")
else:
    print("A letra 'a' não foi encontrada na string.")
