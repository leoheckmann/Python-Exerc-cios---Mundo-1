# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada.
import random

no1 = input("1: ")
no2 = input("2: ")
no3 = input("3: ")
no4 = input("4: ")
c = (no1, no2, no3, no4)
random.shuffle(c)
print(c)