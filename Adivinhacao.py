###neste arquivo, vamos melhor a linguagem em relacao a 1 versao####
import random  #usei para importar a funcao random#

def jogar():

    print("********************************")
    print("bem vindo ao jogo de adivinhacao")
    print("********************************")

    numero_secreto = random.randrange(1,100)   #0.0 1.0
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?") #coloquei no n.secreto para aparecer qual seria o numero, mas tenho
    #que deixar sem o numero secreto ""print("Qual nível de dificuldade?")""
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas =20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}". format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100; ")  ##input recebe oque era impresso no console, igual o print     print("voce digitou", chute_str)
        print("Você digitou", chute_str)
        chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")


        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

    if (acertou):
        print("você acertou e fez {} pontos!".format(pontos))


    else:
        if (maior):
            print("você errou! O seu chute foi maior que o número secreto.")
        elif (menor):  ## elif = neste caso, so para dividir, mas podemos usar o o else mesmo, tem a mesma funcao
            print("Você errou! O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute) #40-60 = -20 #neste caso usei a funcao abs para desconsiderar o
             #sinal negativo no numero resultado.
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")
if (__name__ == "__main__"):
    jogar()
