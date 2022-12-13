# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
from datetime import date
year = int(input("Insira o ano e descubra se ele é bissexto ou insira 0 para ver o ano atual: "))
if year == 0:
    year = date.today().year
if year % 5 == 0 and year % 100 != 0 or year % 400 == 0:
    print("O ano {} é Bissexto".format(year))
else:
    print("O ano {} não é Bissexto".format(year))

