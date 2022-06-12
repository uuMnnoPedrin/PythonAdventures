#pip install art==5.6

#imports
from art import text2art as arte
from random import randint as aleatorio
import time
import os

#variaveis

#controle de jogo
winStat = 0 #0 = padrao, 1 = ganhou , 2 = morreu
continueGame = 0 #0 = padrao, 1 = continuar, 2 = sair, 3 = game over
gameReset = 0
aumentarPoder = 0
aumentarVida = 0
aumentarVidaInimigo = 0
aumentarDanoInimigo = 0

#personagem
personagem = ""
vida = 0
maxVida = 0
barraVida = ""
poder = 0
maxPoder = 0
barraPoder = ""

defesa = 0
recover = 0

acoes = ["1 - Atacar", "2 - Defender", "3 - Curar", "4 - Descansar"]
acao = 0

#inimigo
inimigo = ""
vidaInimigo = 0
maxVidaInimigo = 0
poderInimigo = 0
maxPoderInimigo = 0
barraVidaInimigo = ""
danoInimigo = 0

defesaInimigo = 0

inimigos = ["PHP", "JS", "C#"]
inimigoAcoes = ["atacar","defender"]

#imprimindo o titulo do jogo
os.system("clear")
title = arte("Python Adventures", font="slant")
print(title)

print("\n\nEscolha seu personagem:\n")

while True: #Escolha de personagem
    print("1 - Guerreiro\n")
    print("2 - Mago\n")
    escolha = input("Digite o número correspondente ao seu personagem\n-> ")
    if escolha == "1":
        print("\nVocê escolheu o Guerreiro\n")
        personagem = "Guerreiro"
        break
    elif escolha == "2":
        print("\nVocê escolheu o Mago\n")
        personagem = "Mago"
        break
time.sleep(1.5)
os.system("clear")

#Introducao do jogo
print(f"Você é Python, um {personagem} iniciante que decidiu entrar em uma aventura pelo mundo da programação.")
time.sleep(2)
print("Você conhece um lugar onde as linguagens de programação vão para encontrar desafios e se tornarem mais fortes, o Processador.")
time.sleep(2)
print("Um lugar com várias salas diferentes com todos os tipos de perigos.")
time.sleep(3)
print("Chegando lá você pensa em voz alta 'Eu estou pronto para me tornar a linguagem de programação mais forte do mundo!' e adentra no Processador para começar sua aventura.")
time.sleep(4)

#Luta

while True: #game loop
    #começo de jogo
    #Preparar Player
    if personagem == "Guerreiro":
        maxPoder = aleatorio(5, 10)
        maxPoder+= aumentarPoder
        poder = maxPoder
    else:
        maxPoder = aleatorio(7, 15)
        poder = maxPoder
    maxVida = 10
    maxVida += aumentarVida
    vida = maxVida

    #Preparar Inimigo
    inimigo = inimigos[aleatorio(0, 2)]
    maxVidaInimigo = 20
    maxVidaInimigo += aumentarVidaInimigo
    vidaInimigo = maxVidaInimigo
    danoInimigo = 3 + aumentarDanoInimigo
    inimigoArt = arte(inimigo, font="tarty1")

    if continueGame == 2:
        os.system("clear")
        print(title)
        print("Obrigado por jogar!")
        time.sleep(1.5)
        break
    elif continueGame == 1:
        gameReset += 1 #Quantidade de Continues
        continueGame = 0 #Reseta o Continue pra não entrar em um if
        aumentarVida = 5 * gameReset #Aumenta a vida do personagem de acordo com a quantidade de continues
        aumentarPoder = 3 * gameReset #Aumenta o poder do personagem de acordo com a quantidade de continues
        aumentarVidaInimigo = 10 * gameReset #Aumenta a vida do inimigo de acordo com a quantidade de continues
        aumentarDanoInimigo = 3 * gameReset #Aumenta o dano do inimigo de acordo com a quantidade de continues
        continue
    elif continueGame == 3:
        os.system("clear")
        print(title)
        print(arte("Game Over", font="small"))
        break

    #iniciar batalha
    print(f"\nVocê estava andando pelo Processador quando você encontra um {inimigo} selvagem!")
    time.sleep(2)
    print(f"\nVocê se prepara para a batalha!")
    time.sleep(2.5)
    os.system("clear")


    while True:#batalha loop
        #Verificar Vida Player
        if vida <= 0:
            os.system("clear")
            print("Você morreu!")
            winStat = 2
            break
        #Montar Barras

        #Consertar Valores
        if poder < 0:
            poder = 0
        if vida < 0:
            vida = 0
        if vidaInimigo < 0:
            vidaInimigo = 0
        
        if poder > maxPoder:
            poder = maxPoder
        if vida > maxVida:
            vida = maxVida
        if vidaInimigo > maxVidaInimigo:
            vidaInimigo = maxVidaInimigo
        
        #Tirar defesa
        if defesa == 1:
            defesa = 0
            print("\n\nVocê baixou a guarda!")
            time.sleep(1.5)
        

        #barras Player
        barraPoder = ""
        barraVida = ""
        
        while len(barraPoder) < poder:
            barraPoder += "#"

        while len(barraPoder) < maxPoder:
            barraPoder += "."

        while len(barraVida) < vida:
            barraVida += "#"
        while len(barraVida) < maxVida:
            barraVida += "."

        #barras Inimigo
        barraVidaInimigo = ""
        while len(barraVidaInimigo) < vidaInimigo:
            barraVidaInimigo += "#"
        while len(barraVidaInimigo) < maxVidaInimigo:
            barraVidaInimigo += "."

        #Print Padrão
        os.system("clear")
        print(f"\n{vidaInimigo}/{maxVidaInimigo}\n\n[{barraVidaInimigo}]\n")
        print (inimigoArt)
        print("\nO que você fará?")
        print(f"\nPWR [{barraPoder}] {poder}/{maxPoder}  |  VIT[{barraVida}] {vida}/{maxVida}]\n")
        #Turno Player
        while True:
            for x in acoes:
                print(x)
            
            acao = input("\nDigite o número correspondente à ação que deseja realizar\n-> ")
            if acao == '':
                continue
            acao = int(acao)
            if acao >= 1 and acao <= 4:
                break
        print(f"\nVocê escolheu: {acoes [acao - 1]}")

        str(acao)
        if acao == 1:#acao atacar
            if poder < 2:
                    print("\nVocê tenta atacar mas está cansado e não consegue\n")
            else:
                poder -= 2
                if defesaInimigo == 0:
                        if personagem == "Guerreiro":
                            dano = aleatorio(3, 10)
                            vidaInimigo -= dano
                            print(f"\nVocê ataca o {inimigo} e causa {dano} de dano\n")
                        else:
                            dano = aleatorio(0, 8)
                            vidaInimigo -= dano
                            print(f"\nVocê ataca o {inimigo} e causa {dano} de dano\n")
                else: 
                    print("\nO inimigo bloqueou o ataque")
                    defesaInimigo = 0
        elif acao == 2:#acao defender
            if personagem == "Mago":
                poder-=1
            defesa = 1
            print("\nVocê prepara para defender um ataque")
        elif acao == 3:#acao curar
            if poder < 2:
                print("\nVocê tenta curar mas está cansado e não consegue\n")
            else:
                poder-=2
                if personagem == "Guerreiro":
                    vida+= 1
                    print("\nVocê se sente revitalizado.\n1 de vida recuperado")
                else:
                    vida+= 2
                    print("\nVocê se sente revitalizado.\n2 de vida recuperado")
        elif acao == 4:#acao descansar
            recover = aleatorio(1, 5)
            print(f"\nVocê recua por um momento,coloca a mão no peito e respira profundamente.\nVocê sente seu fôlego voltar um pouco.\n{recover} de poder restaurado")
            poder+= recover

        time.sleep(2.5)

        #Turno Inimigo
        if vidaInimigo <= 0:
            os.system("clear")
            print(f"\nVocê derrotou {inimigo}!")
            winStat = 1
            break
        #Montar Barras

        #Consertar Valores
        if poder < 0:
            poder = 0
        if vida < 0:
            vida = 0
        if vidaInimigo < 0:
            vidaInimigo = 0
        
        if poder > maxPoder:
            poder = maxPoder
        if vida > maxVida:
            vida = maxVida
        if vidaInimigo > maxVidaInimigo:
            vidaInimigo = maxVidaInimigo

        #barras Player
        barraPoder = ""
        barraVida = ""
        while len(barraPoder) < poder:
            barraPoder += "#"

        while len(barraPoder) < maxPoder:
            barraPoder += "."

        while len(barraVida) < vida:
            barraVida += "#"
        while len(barraVida) < maxVida:
            barraVida += "."

        #barras Inimigo
        barraVidaInimigo = ""
        while len(barraVidaInimigo) < vidaInimigo:
            barraVidaInimigo += "#"
        while len(barraVidaInimigo) < maxVidaInimigo:
            barraVidaInimigo += "."
        
        #Print Padrão
        os.system("clear")
        print(f"\n{vidaInimigo}/{maxVidaInimigo}\n\n[{barraVidaInimigo}]\n")
        print (inimigoArt)
        print(f"\nTurno do {inimigo}")
        print(f"\nPWR [{barraPoder}] {poder}/{maxPoder}  |  VIT[{barraVida}] {vida}/{maxVida}]\n")

        time.sleep(1.2)

        #Acao Inimigo
        if defesaInimigo == 1:
            defesaInimigo = 0
            print("\n\nO inimigo baixou a guarda!")
            time.sleep(1.5)

        acaoInimigo = aleatorio(1, 2)
        if acaoInimigo == 1:
            if defesa == 0:
                print(f"\n{inimigo} atacou você com {danoInimigo} de dano")
                vida -= danoInimigo
            else:
                print("\nVocê bloqueou o ataque")
                defesa = 0
        elif acaoInimigo == 2:
            print(f"\n{inimigo} preparou para defender")
            defesaInimigo = 1
        time.sleep(2.5)
    
    if winStat == 1:
        print("\nVocê deseja continuar jogando?")
        escolha = input("1 - Sim\n2 - Não\n-> ")
        if escolha == "1":
            continueGame = 1
            continue
        elif escolha == "2":
            continueGame = 2
    elif winStat == 2:
        continueGame = 3