# FOR, WHILE, (break,continue)
# for in -0 -- final

for letra in "Ola mundo":
    print(letra)

prontuarios = ["SP01", "SP02", "SP03"]
               
for prontuario in prontuarios:
    print(prontuario)

# range(5) => 0, 1, 2, 3, 4
# RANGE
for i in range(5):
    print(i)

#Range (START, STOP, STEP)
for i in range(0, 12, 2):
    print(i)

lista = list(range(1, 101))
print(lista)

#while
contador = 0
while contador < 5:
    print(contador)
    contador +=1

# break
comando = ''
while True:
    comando = input('Digite um comando')

    if comando == 'sair':
        break
    if comando == '1':
        print('um')
    if comando == '2':
        print('dois')

# CONTINUE
numeros = [3, -1, 2, 0, -4, 5]
for numero in numeros:
    if numero <= 0:
        continue
    print(numero)

for numero in numeros:
    if numero > 0:
        print(numero)

# compreensão de listas 
numeros = [3, -1, 2, 0, -4, 5]

positivos = []

for numero in numeros:
    if numero > 0:
        positivos.append(numero)


# expressao for item in lista if condicao
positivos = [numero for numero in numeros if numero > 0]
elevad_quad = [numero ** 2 for numero in numeros]