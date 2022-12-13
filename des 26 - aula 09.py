# Faça um programa que leia uma frase pelo teclado e mostre:
# > Quantas vezes aparece a letra "A"
# > Em que posição ela aparece a primeira vez.
# > Em que posição ela aparece a última vez.

word: str = str(input("Insira a palavra: ")).upper()

print("Quantas vezes aparece a letra A: `{}".format(word.count("A")))
print("A letra A aparece na {} posição".format(word.find("A")+1))
print("A última letra A aparece na {} posição".format(word.rfind("A")+1))