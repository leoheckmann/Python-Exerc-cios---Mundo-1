# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros.
m = float(input('Quantos metros? '))
cm = m * 100
mm = m * 1000
dec = m * 10
km = m / 1000
hc = m / 100
dam = m / 10
print('A media de {}m corresponde a:\n{:.0f}cm\n{:.0f}mm\n{}dec\n{}km\n{}hc\n{}dam'.format(m, cm, mm, dec, km, hc, dam))

