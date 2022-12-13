# Crie um programa que leia o nome completo de uma pessoa e mostre:
# > O nome com todas as letras maiúsculas.
# > O nome com todas minúsculas.
# > Quantas letras ao todo (sem considerar os espaços)
# > Quantas letras tem o primeiro nome dela

nome = str(input("Insira o seu nome aqui e descubra as características dele: ")).strip()
print("Seu nome em maiúsculo: ", nome.upper())
print("Seu nome em minúsculo: ", nome.lower())
print("A quantidade de letras que seu nome completo tem é: {}".format(len(nome) - nome.count(" ")))
div = nome.split()
print("O seu primeiro nome é: {} e tem {} letras".format(div[0], len(div[0])))
