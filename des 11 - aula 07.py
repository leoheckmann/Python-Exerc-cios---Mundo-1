# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessário para pintá-la, sabendo que cada litro de tinta, pinta uma aré de 2mquadrado

n1 = float(input("Qual é a largura da parede que você deseja pintar? "))
n2 = float(input("Qual é a altura da parede que você deseja pintar? "))
m2 = n1 * n2
res = m2 / 2

print("Você precisará de {} litros de tinta para pintar {} metros quadrado de parede".format(res,m2))
