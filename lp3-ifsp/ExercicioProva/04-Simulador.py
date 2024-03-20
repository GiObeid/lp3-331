def main():
    candidatos = {"Candidato 1": 0, "Candidato 2": 0, "Candidato 3": 0}
    numero_maximo_votos = 5 

    print("Bem-vindo à votação!")

    votos = 0
    while votos < numero_maximo_votos:
        print("\nEscolha seu candidato:")
        print("1 - Candidato 1")
        print("2 - Candidato 2")
        print("3 - Candidato 3")

        voto = input("Digite o número do candidato em que deseja votar: ")

        if voto.isdigit() and 0 < int(voto) <= len(candidatos):
            candidato = f"Candidato {voto}"
            candidatos[candidato] += 1
            votos += 1
            print("Voto registrado com sucesso!")
        else:
            print("Opção inválida! Por favor, escolha um número válido para votar.")

    print("\nResultado da votação:")
    for candidato, votos in candidatos.items():
        print(f"{candidato}: {votos} votos")

    vencedor = max(candidatos, key=candidatos.get)
    print(f"\nO vencedor da eleição é {vencedor}!")

    if __name__ == "__main__":
      main()