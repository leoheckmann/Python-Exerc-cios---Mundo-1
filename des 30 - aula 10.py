# Crie um programa que leia um número inteiro e mostre na tela
# se ele é PAR ou IMPAR.

n = int(input("Insira seu número e descubra se ele é PAR ou ÍMPAR: "))

new = n % 2

if new == 0:
    print("Esse numero é PAR")
else:
    print("Esse número é ÍMPAR")