import forca
import adivinhacao

print("*********************************")
print("*********Escolha um jogo!********")
print("*********************************")

print("(1)Forca (2)Adivinhação")

jogo = int(input("Qual jogo?"))

if (jogo == 1):
    print("Jogo da Forca")
elif(jogo == 2):
    print("Jogo da Adivinhação")    