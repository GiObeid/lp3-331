# Programa verifica código de funcionários de uma empresa
import re

print("Programa Verifica Codigo de Funcionarios  \n")

def verificar_codigo(codigo):
    padrao = r'^BR\d{4}X$'
    
    if re.match(padrao, codigo):
        return True
    else:
        return False

codigo = input("Digite o codigo do funcionario: ")

if verificar_codigo(codigo):
    print('Codigo Valido')
else:
    print('Codigo Invalido')