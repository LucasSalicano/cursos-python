import random

def jogar():
    imprime_mensagem_abertura()
    palavras = realiza_leitura_txt()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    letras_acertadas = inserir_underscore_cada_letra(palavra_secreta)

    enforcou = acertou = False
    erros = 0

    print(letras_acertadas)

    while not enforcou and not acertou:
        chute = valor_entrada()
        erros = verifica_letra_existe(chute, erros, letras_acertadas, palavra_secreta)

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    retorna_mensagem_tentativas(acertou, palavra_secreta)


def retorna_mensagem_tentativas(acertou, palavra_secreta):
    if acertou:
        print("Você ganhou!!")
    else:
        print("Você perdeu!! A palavra correta era: " + palavra_secreta)


def valor_entrada():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute


def verifica_letra_existe(chute, erros, letras_acertadas, palavra_secreta):
    if chute in palavra_secreta:
        index = 0
        for letra in palavra_secreta:
            if chute == letra:
                letras_acertadas[index] = letra
            index += 1
    else:
        erros += 1
    return erros


def inserir_underscore_cada_letra(palavra_secreta):
    return ["_" for letra in palavra_secreta]


def realiza_leitura_txt():
    palavras = []
    arquivo = open("palavras.txt", "r")
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    return palavras


def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


if __name__ == "__main__":
    jogar()
