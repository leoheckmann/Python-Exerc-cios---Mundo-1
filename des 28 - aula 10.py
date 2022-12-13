# Escreva um programa que faça o computador "Pensar" em um número
# inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual
# foi o número escokhido pelo computador

# O programa deverá escrever na tela se o usuário venceu ou perdeu

import random

n0 = 0
n1 = 1
n2 = 2
n3 = 3
n4 = 4
n5 = 5

sort = [n0, n1, n2, n3, n4, n5]
win = random.choice(sort)

esc = int(input("Insira seu número da sorte: "))

if esc == win:
    print("Você acertou, que sortudo você é :)")
else:
    print("Poxa não foi dessa vez, tente novamente!")
