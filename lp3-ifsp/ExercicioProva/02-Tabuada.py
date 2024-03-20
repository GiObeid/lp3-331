numero = input("Digite um número para exibir a tabuada: ")

if numero.isdigit():
    numero = int(numero)
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
else:
    print("Por favor, digite um número válido.")



