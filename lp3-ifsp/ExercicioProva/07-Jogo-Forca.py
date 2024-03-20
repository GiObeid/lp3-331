import random

def escolher_palavra():
    palavras = ["quantico", "brooklin 99", "lucifer", "titanic", "supernatural", "vingadores", "barbie", "avatar", "anyone but You"]
    return random.choice(palavras)

def exibir_palavra_oculta(palavra, letras_corretas):
    oculto = ""
    for letra in palavra:
        if letra in letras_corretas:
            oculto += letra
        else:
            oculto += "_"
    return oculto

def main():
    palavra = escolher_palavra()
    tentativas_maximas = 6
    letras_corretas = []
    letras_erradas = []

    print("Jogo da Forca! O tema é: Série ou Filme")
    print("Adivinhe a palavra secreta.")

    while tentativas_maximas > 0:
        palavra_oculta = exibir_palavra_oculta(palavra, letras_corretas)
        print("\nPalavra secreta:", palavra_oculta)

        if palavra_oculta == palavra:
            print("Parabéns! Você venceu!")
            break

        print("Letras erradas:", " ".join(letras_erradas))
        letra = input("Digite uma letra: ").lower()

        if letra in palavra:
            print("Boa! Esta letra está na palavra secreta.")
            letras_corretas.append(letra)
        else:
            print("Ops! Esta letra não está na palavra secreta.")
            letras_erradas.append(letra)
            tentativas_maximas -= 1

    else:
        print("Você excedeu o número máximo de tentativas. A palavra secreta era:", palavra)
main()
