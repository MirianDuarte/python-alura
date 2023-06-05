import ADIVINHACAO
import FORCA

def escolha_jogo():
    print("***********************************")
    print("********Escolha o seu jogo!********")
    print("***********************************")

    print("(1) Adivinhacao (2) Forca")

    jogo = int(input("Qual jogo?"))

    if(jogo == 1):
        print("Jogando adivinhacao")
        ADIVINHACAO.jogar()
    elif(jogo == 2):
        print("Jogando forca")
        FORCA.jogar()
    
if(__name__ == "__main__"):
    escolha_jogo()