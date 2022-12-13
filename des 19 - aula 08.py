# Um professor quer sortear um dos seus quatros alunos para apagar o quadro. Faça um programa que ajude ele, lendo o
# nome deles e escrevendo o nome escolhido.

import random

no1 = input("1: ")
no2 = input("2: ")
no3 = input("3: ")
no4 = input("4: ")
c = (no1, no2, no3, no4)
random.shuffle(c)
print(c)