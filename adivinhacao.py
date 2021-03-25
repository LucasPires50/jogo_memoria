import random


def jogar_adivinhacao():
    
    print("*********************************")
    print("Bem Vindo ao jogo de adivinhação!")
    print("*********************************")

    # função rondom para gerar número aleatórios
    nomero_secreto = round(random.randrange(1, 101))
    total_de_tentativas = 3
    pontos = 1000

    print("Escolha um nivel de dificuldade: ")
    print("(1)Fácil (2)Médio (3)Difícil")

    nivel = int(input("Escolha um nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 3

    for rodada in range(1, total_de_tentativas + 1):
        # Interpolção de string
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        # Função para o usuário para usuário inserir a informação solicita
        chute_usuario = input("Digiteo um número entre 1 e 100: ")

        # Função para converter a string para inter
        numero_chute = int(chute_usuario)

        if (numero_chute < 1 or numero_chute > 100):
            print("Você deve digitar um número entre 1 e 100.")
            # sai dessa interação, e continua o loop
            continue

        print("Você digitou: ", numero_chute)

        # Colocar a condição do if em uma variável
        acertou = nomero_secreto == numero_chute
        chute_maior = numero_chute > nomero_secreto
        chute_menor = numero_chute < nomero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!!".format(pontos))
            break
        else:
            if(chute_maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif(chute_menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
            # Função abs() sempre deixa o número positivo
            pontos_perdidos = abs(numero_chute - nomero_secreto)
            pontos = pontos - pontos_perdidos

    print("*********************************")
    print("Fim do jogo!")
    print("*********************************")
