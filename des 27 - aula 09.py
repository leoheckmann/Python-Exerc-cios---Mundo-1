# Faça um programa que leia o nome completo de uma pessoa, mostrando
# em seguida o primeiro e o último nome separadamente.
# EX: Ana Maria de Souza
# Primeiro: Ana
# Último: Souza

nome = str(input("Insira seu nome: ")).strip()
div = nome.split()
print(div[0], div[len(div)-1])
