def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return 'Baixo peso'
    elif imc < 25:
        return 'Peso normal'
    elif imc < 30:
        return 'Excesso de peso'
    elif imc < 35:
        return 'Obesidade de classe 1'
    elif imc < 40:
        return 'Obesidade de classe 2'
    else:
        return 'Obesidade de classe 3'

def calcular_peso_ideal(peso, altura):
    peso_ideal = 24.9 * (altura ** 2)
    diferenca_peso = peso_ideal - peso
    return diferenca_peso

peso = float(input("Insira seu peso (kg): "))
altura = float(input("Insira sua altura (m): "))

imc = calcular_imc(peso, altura)
classificacao = classificar_imc(imc)
diferenca_peso = calcular_peso_ideal(peso, altura)

if diferenca_peso > 0:
    print(f"Seu IMC é {imc:.2f}, {classificacao}. Você precisa ganhar {abs(diferenca_peso):.2f} kg para atingir um IMC de 24.9.")
elif diferenca_peso < 0:
    print(f"Seu IMC é {imc:.2f}, {classificacao}. Você precisa perder {abs(diferenca_peso):.2f} kg para atingir um IMC de 24.9.")
else:
    print("Seu peso está dentro da faixa considerada normal para um IMC de 24.9.")