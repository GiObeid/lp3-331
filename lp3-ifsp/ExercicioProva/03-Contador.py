def contar_vogais_consoantes(frase):
    vogais = 'aeiou'
    total_vogais = 0
    total_consoantes = 0

    for letra in frase:
        if letra.isalpha():
            if letra in vogais:
                total_vogais += 1
            else:
                total_consoantes += 1

    return total_vogais, total_consoantes

frase = input("Digite uma frase: ")

num_vogais, num_consoantes = contar_vogais_consoantes(frase)

print(f"Número de vogais: {num_vogais}")
print(f"Número de consoantes: {num_consoantes}")
