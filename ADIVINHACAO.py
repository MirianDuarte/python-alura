import random

def jogar():

    print("*********************************")
    print("Bem-vindo ao jogo de adivinhação!")
    print("*********************************")

    #variaveis
    numero_secreto = random.randrange(1, 101) # Geração de número aleatorio
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Dificíl")

    nivel = int(input("Defina um nível: "))
    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número de 1 a 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print('O número digitado deve ser entre 1 e 100.')
            continue #continuação do for = pula para a proxima rodada

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos".format(pontos))
            break #sair do laço = fim do jogo
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if (maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
                if(rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
                if(rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))

    print("Fim do jogo!")
    #print("Aqui está o número secreto: {}3".format(numero_secreto))

if(__name__ == "__main__"):
    jogar()
            