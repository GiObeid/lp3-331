def verifica_palindromo(texto):
    texto = texto.lower().replace(" ", "")  
    return texto == texto [::-1]  

def main():
    palavra = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")
    if verifica_palindromo(palavra):
        print(f"{palavra} é um palíndromo!")
    else:
        print(f"{palavra} não é um palíndromo.")
main()
