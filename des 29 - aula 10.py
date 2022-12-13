# Escreva um progrma que leia a velocidade de um carro.

# Se ele ultrapassar 80KM/H, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada KM acima do limite

vel = float(input("Velocidade do Carro: "))

if vel > 80:
    print("Você estava acima da velocidade de 80Km/h e foi multado")
    multa = 7.00 * (vel - 80)
    print("Valor da multa: R${:.2f}".format(multa))
else:
    print("Você estava dentro da velocidade permitida!")
