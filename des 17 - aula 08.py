# Faça um programa que leia o comprimento do catero oposto e do cateto adjacente de um triângulo retangulo, cacule e
# mostre o comprimento da hipotenusa.

co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = (co ** 2 + ca ** 2) ** (1/2)
print("A hipotenusan vai medir {:.2f}".format(hi))

import math
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = math.hypot(co, ca)
print("a hipotenusa vai medir {:.2f}".format(hi))

from math import hypot
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = hypot(co, ca)
print("a hipotenusa vai medir {:.2f}".format(hi))