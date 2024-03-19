# Programa calcula Desconto

print("Programa Calcula Desconto \n")

compra = float(input("Digite o valor da compra: "))

if (compra >= 0.01 and compra <= 9.99):
    desconto = 0/100 * compra
    compra = compra - desconto
elif (compra >= 10.0 and compra <= 99.99):
    desconto = 5/100 * compra
    compra = compra - desconto
elif (compra >= 100.0 and compra <= 499.99):
    desconto = 10/100 * compra
    compra = compra - desconto
elif (compra >= 500.0):
    desconto = 15/100 * compra
    compra = compra - desconto

print("O valor do desconto será de:", desconto , " Valor atualalizado: R$", compra)