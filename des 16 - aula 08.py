# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira!
# Ex:
# Digite um número: 6.127
# O número 6.127 tem a parte inteira 6

import math
n1 = float(input("Digite um valor: "))
print("O valor de {} e sua porção inteira é: {}".format(n1 , math.trunc(n1)))

