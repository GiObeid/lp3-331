def contar_palavras(frase):
    frase = frase.lower()
    for pontuacao in ",.;:!?":
        frase = frase.replace(pontuacao, "")

    palavras = frase.split()

    contagem = {}
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1

    return contagem

while True:
    texto = input("Digite uma frase (ou digite 'sair' para encerrar): ")
    if texto.lower() == 'sair':
        break
    resultado = contar_palavras(texto)
    print("\nContagem de palavras:")
    for palavra, quantidade in resultado.items():
        print(f"'{palavra}': {quantidade}")
