# Faça um programa que leia três números e
# mostre qual é o maior e qual é o menor.


print("Descubra qual número é maior!!!")
n1 = int(input("Insira o primeiro número: "))
n2 = int(input("O segundo número: "))
n3 = int(input("O terceiro número: "))

menor = n1
if n1 < n2 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print("O menor valor é {}".format(menor))
print("O maior valor é {}".format(maior))
