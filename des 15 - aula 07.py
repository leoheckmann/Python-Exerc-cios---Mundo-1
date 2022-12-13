print("""Escreva um programa que pergunte a quantida de KM percorridos por um carro alugado e a quantidade de dias pelos quais 
ele foi aligado. Calcule o preço a pagar, sabendo que o carro custa R$ por dia e R$0.15 por KM rodado""")

dias = int(input("Quantos dias alugados? "))
km = float(input("Quanto Km rodados? "))
pago = (dias * 60) + (km * 0.15)
print("O total a pagar é de R${:.2f}".format(pago))