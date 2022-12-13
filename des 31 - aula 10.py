# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de
# até 200Km e R$0,45 para viagens mais longas

print("Digite a distância e faça o calculo da gasolina!!")
dis = float(input("KMs: "))
if dis <= 200:
    gast1 = dis * 0.50
    print("Total de gastos com gasoline para essa distãncia: {:.2f}".format(gast1))
else:
    gast2 = dis * 0.45
    print("Total de gastos com gasoline para essa distãncia: {:.2f}".format(gast2))

