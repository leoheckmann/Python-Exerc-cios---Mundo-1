#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. / Considere US$1.00 = R$3,27

n1 = float(input("Quantos REAIS você tem: "))

a1 = n1 / 3.27

print("Você pode comprar: {:.2f} USD$".format(a1))