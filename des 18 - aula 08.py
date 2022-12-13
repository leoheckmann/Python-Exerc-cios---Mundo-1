#Faça um programa que leia um ângulo qualquer e mostre na tela o valor seno, cosseno e tangente desse ângulo.

import math
ang = float(input("Digite o angulo que você deseja: "))
seno = math.sin(math.radians(ang))
print("O angulo {} tem o SENO de {:.2f}".format(ang, seno))
cosseno = math.cos(math.radians(ang))
print("O ãngulo de {} tem o COSSENO de {:.2f}".format(ang, cosseno))
tangente = math.tan(math.radians(ang))
print("O ângulo de {} tem a TANGENTE de {:.2f}".format(ang, tangente))