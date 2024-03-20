import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    
    
    while True:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1
        
        if palpite < numero_secreto:
            print("Seu palpite está baixo. Tente novamente!")
        elif palpite > numero_secreto:
            print("Seu palpite está alto. Tente novamente!")
        else:
            print(f"Parabéns! Você acertou o número!")
            break

jogo_adivinhacao()

