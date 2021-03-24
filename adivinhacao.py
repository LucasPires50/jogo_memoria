print("*********************************")
print("Bem Vindo ao jogo de adivinhação!")
print("*********************************")

nomero_secreto = 42
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    # Interpolção de string
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    # Função para o usuário para usuário inserir a informação solicita
    chute_usuario = input("Digiteo seu número: ")

    # Função para converter a string para inter
    numero_chute = int(chute_usuario)

    print("Você digitou: ", numero_chute)

    # Colocar a condição do if em uma variável
    acertou = nomero_secreto == numero_chute
    chute_maior = numero_chute > nomero_secreto
    chute_menor = numero_chute < nomero_secreto

    if acertou:
        print("Você acertou!!")
    else:
        if(chute_maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif(chute_menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")

    rodada = rodada + 1

print("*********************************")
print("Fim do jogo!")
print("*********************************")
