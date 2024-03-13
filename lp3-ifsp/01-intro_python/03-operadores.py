## Operadores aritméticos
# +, -, *, /, %, **

nota1 = 3.0
nota2 = 5.5

media = (nota1 + nota2)/2

#  2 elevado ao quadrado
potencia = 2**2

# 2 elevado ao cubo  
potencia = 2 ** 3
numero = 2 * 2 * 2

# operadores de atribuição
# =, +=, -=...
idade = 20

idade += 10

# operadores lógicos
# and, or, not

resultado = True or False
print(type(resultado))
print(resultado)

# entra a lógica do AND e OR

#operadores de comparação

idade = 17 

if idade >= 18:
    print('Maior de idade')
else:
    print('Menor')


# operador is
# os valores do objeto e se ocupam o mesmo espaço de memória

a = [1,2,3]
b = [1,2,3]

print(a is b) ##false

z = [1,2,3]
x = z
print(z is x)

# operador in e not in
# verificar se um objeto está ou não dentro de uma sequência (str, list, tuple)

print('a' in 'Java')
print('Maria' in ['Pedro', 'Ana'])

alunos = ['Pedro', 'Ana']
aluno = 'Maria'
print (aluno not in alunos)
print (aluno in alunos)