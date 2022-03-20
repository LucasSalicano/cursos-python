import random

from numpy.core.defchararray import isnumeric

print("*************************")
print("Bem Vindo")
print("*************************")

numero_secreto = random.randrange(0, 10)
total_tentativas = 3


def checaNumeroSecreto(numero):
    if numero == numero_secreto:
        print("\n\nVocê acertou :)")
        finalizar()
    else:
        print("Você errou, numero digitado {} ".format(numero))

    isUltimaTentativa()


def isUltimaTentativa():
    if total_tentativas == 0:
        print("\nO jogo será finalizado, o numero correto era: {} ".format(numero_secreto))


def checaNumeroTentativas(total_tentativas):
    total_tentativas -= 1
    if total_tentativas == 0:
        print("essa é ultima tentativa.")

    return total_tentativas

def finalizar():
    print("\n*************************")
    print("Jogo Finalizado")
    print("*************************")
    exit()


nivel = input("Digite um numero de dificuldade \n1 - Fácil | 2 - Médio | 3 - Difícil: ")
nivel_escolhido = int(nivel)

if nivel_escolhido == 1:
    total_tentativas = 10
elif nivel_escolhido == 2:
    total_tentativas = 5
else:
    total_tentativas = 2

print("Configurado\n***************")

while total_tentativas > 0:
    total_tentativas = checaNumeroTentativas(total_tentativas)

    chute_str = input("Digite um numero entre 1 e 10: ")
    chute_str = int(chute_str) if isnumeric(chute_str) else exit("valor informado é incorreto")

    if int(chute_str) < 0:
        exit("Valor fora do permitido.")

    checaNumeroSecreto(chute_str)
finalizar()
