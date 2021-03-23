print("*********************************")
print("Bem Vindo ao jogo de adivinhação!")
print("*********************************")

nomero_secreto = 42

# Função para o usuário para usuário inserir a informação solicita
chute_usuario = input("Digiteo seu número: ")

# Função para converter a string para inter
numero_chute = int(chute_usuario)

print("Você digitou: ", numero_chute)

if nomero_secreto == numero_chute:
    print("Você acertou!!")
else:
    if(numero_chute > nomero_secreto):
        print("Você errou! O seu chute foi maior do que o número secreto.")
    elif(numero_chute < nomero_secreto):
        print("Você errou! O seu chute foi menor do que o número secreto.")

print("*********************************")
print("Fim do jogo!")
print("*********************************")