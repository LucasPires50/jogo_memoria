import forca
import adivinhacao


def escolha_jogo():

    print("*********************************")
    print("*********Escolha um jogo!********")
    print("*********************************")

    print("(1)Forca (2)Adivinhação")

    jogo = int(input("Qual jogo?"))

    if (jogo == 1):
        print("Jogo da Forca")
        forca.jogar_forca()
    elif(jogo == 2):
        print("Jogo da Adivinhação")
        adivinhacao.jogar_adivinhacao()

if(__name__ == "__main__"):
    escolha_jogo()
