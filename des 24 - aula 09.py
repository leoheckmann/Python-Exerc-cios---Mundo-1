# Crie um programa que leia o nome de uma cidade e diga se ela
# começa ou não com o nome "SANTO".

nome = str(input("Decubra se começa com SANTO, digite o nome: ")).strip()

print(nome[:5].upper == "Santo")