
import forca
import advinhacao

def escolhe_jogo():
    print("Escolha o jogo")

    print("(1) Forca, (2) Adivinhação")
    game = int(input("Qual jogo? "))
    if(game == 1): 
        print("Jogando forca")
        forca.jogar()
       
    elif(game == 2):
        print("Jogando adivinhação")
        advinhacao.jogar()
        
    

if (__name__ == "__main__"):
    escolhe_jogo()
