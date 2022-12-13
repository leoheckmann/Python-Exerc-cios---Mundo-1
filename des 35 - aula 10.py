# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
# se elas podem ou não formar um triângulo
print("Insira três números de um reta para ver forma um triângulo!")

n1 = float(input("Primeiro número: "))
n2 = float(input("Segundo número: "))
n3 = float(input("Terceiro número: "))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print("As retas acima podem formar um triângulo!")
else:
    print("As retas acima não formam um triângulo!") \

