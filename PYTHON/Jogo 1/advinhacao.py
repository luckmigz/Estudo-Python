
import random 
def jogar():
    
    
    print("* Bem vindo ao jogo de Advinhação *");
    print("Dificuldades (1) Fácil, (2) Médio, (3) Difícil")
    dif = int(input("Selecione a dificuldade:"))

    if(dif == 1): 
        tot = 15
        score = 1000
        print("A dificuldade: Fácil")
    elif(dif == 2):
        tot = 7
        score = 2000
        print("A dificuldade:  Médio")
    elif(dif == 3):
        tot = 4 
        score = 4000
        print("A dificuldade: Difícil")
        
    random.seed(100)
    numero_secreto = int(random.randint(1,101))

    for num_ten in range(1,tot+1):
        chute = int(input("Digite seu número entre 1 e 100: "))
        if (chute == numero_secreto): 
            print("Você digitou ", chute)
            break
        if(chute < 1 or chute >100):
            print("Digite um número entre 1 e 100")
            continue
        else:
            if(numero_secreto == chute):
                print("Você acertou e fez {} pontos!".format(score))
            else:
                if(chute > numero_secreto):
                    print("Errou! seu chute foi maior")
                elif(chute < numero_secreto):
                    print("Errou! seu chute foi menor")
            lost_pt = abs(numero_secreto - chute)
            score = score - lost_pt
            
            print("Tentativa {} de {} \n".format(num_ten,tot))
        
    print("Você fez {} pontos!".format(score)) 
    print("Fim de jogo \n")

if(__name__ == "__main__"):
    jogar()