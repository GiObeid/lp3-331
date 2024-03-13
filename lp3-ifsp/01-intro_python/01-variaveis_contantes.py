# Indentificadores

# letra, numero e ...
# nao pode ser palavra reservada: if, nome, true, false 
# case sensitive 
    nome = "Pedro"
    Nome = "Pedro"

# variaveis 

# tudo em minusculo 
# separador _
# snake_case 
    idade = 20
    pessoa_fisica = "Marcio"
    pessoa_juridica = 'Paula LTDA'
    imposto_renda = 2200.45

# e o tipo?

# java 
# string nome = "pedro"
# int idade = 20
# no python temos inferência de tipo
# o tipo será definido com base no valor (literal)
idade = 20 # int
nome = "Pedro" # string

# constantes 

# nao existe constante em python 
# convenção: nome em maiusculo
PI = 3,14

# comentarios

# comentarios de uma unica linha (#)
# comentarios de multiplas linhas (''')

# docstring (comentario de documentaçao)
# documentar classe, modulos, funções, ...

static somar(double numero1, double numero2){
    return numero1 + numero2
}

def somar(numero1, numero2):
    '''
    funcao que soma dois numeros 
    :param numero1: primeiro numero
    :param numeros: segundo numero
    :return: a soma dos numeros
    '''

    return numero1 + numero2
    