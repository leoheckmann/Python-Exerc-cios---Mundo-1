# Escreva um programa que pergunte o salário de um funcionário e calcule
# o valor do seu aumento.

# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input("Insira o seu salário: "))

if sal > 1250:
    n1 = sal * 1.10
    print("\033[1;33mSeu salário teve um aumento para R${:.2f}".format(n1))
else:
    n2 = sal * 1.15
    print("\033[1;33mSeu salário teve um aumento para R${:.2f}".format(n2))