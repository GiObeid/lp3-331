# Função verifica código de funcionários de uma empresa
import re

def verificar_codigo(codigo):
    
    padrao = r'^BR\d{4}X$'
    
    if re.match(padrao, codigo):
        return True
    else:
        return False