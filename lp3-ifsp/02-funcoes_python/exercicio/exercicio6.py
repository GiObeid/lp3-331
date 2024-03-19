def calcular_volume(comprimento, altura, largura):
    volume = (comprimento * altura * largura) / 1000
    return volume

def calcular_potencia(volume, temperatura_desejada, temperatura_ambiente):
    potencia = volume * 0.05 * (temperatura_desejada - temperatura_ambiente)
    return potencia

def calcular_filtragem(volume):
    filtragem = volume * 3
    return filtragem

comprimento = float(input("Digite o comprimento (cm): "))
altura = float(input("Digite a altura (cm): "))
largura = float(input("Digite a largura (cm): "))
temperatura_desejada = float(input("Digite a temperatura desejada em °C: "))
temperatura_ambiente = float(input("Digite a temperatura ambiente em °C: "))

volume = calcular_volume(comprimento, altura, largura)
potencia_termostato = calcular_potencia(volume, temperatura_desejada, temperatura_ambiente)
filtragem_necessaria = calcular_filtragem(volume)

print(f"O volume do aquário é de {volume} litros")
print(f"A potência do termostato necessária é de {potencia_termostato} watts")
print(f"A quantidade de filtragem por hora necessária é {filtragem_necessaria} litros por hora.")