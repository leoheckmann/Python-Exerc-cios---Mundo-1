# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Ex: Dígite um número: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

n1 = int(input("Digite um número de 0 a 9999: "))
a = n1 // 1 % 10
b = n1 // 10 % 10
c = n1 // 100 % 10
d = n1 // 1000 % 1000
print("Anlisando: {}".format(n1))
print("Unidade: {}".format(a))
print("Dezena: {}".format(b))
print("Centena: {}".format(c))
print("Milhar: {}".format(d))