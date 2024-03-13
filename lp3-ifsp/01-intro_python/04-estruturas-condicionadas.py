#if, if/else, if/elif/else, ternario e match

# if 
# if condicao:
#   corpo
#   corpo
#   corpo

idade = 20
if idade >= 18:
    print('Maior de idade')
else:
    print('Menor de idade')

print('agora acaboui')

# criança(0-12), adolescente(13-17), adulto(18-59) ou idoso(60+)
if idade <= 12:
    print('Crianca')
elif idade <= 17:
    print('Adolescente')
elif idade <=59:
    print('Adulto')
else:
    print('idoso')

# if aninhado (EVITAR)
email = 'joao@gmail.com'
senha = '123456'

if email == 'joao@gmail.com':
    if senha == '123456':
        print('Acesso liberado')
    else:
        print('Email ou senha incorretos')
else:
    print('email ou senha incorretos')


if email == 'joao@gmail.com' and senha == '123456':
    print('acesso liberado')
else:
    print('email ou senha incorretos')

#condicao complexa no if
# permitir a entrada se:
# o usuário não estiver bloqueado E
# o usuário for um funcionário E
# a hora atual entre 08 E 18
# OU
# o usuário é admin

usuario_bloqueado = False
usuario_funcionario = True
hora_atual = 19
usuario_admin = False

if (not usuario_bloqueado and usuario_funcionario and hora_atual >= 8 and hora_atual <=18) or usuario_admin:
    print('liberado')
else:
    print('nao liberado')

horario_comercial = hora_atual >=8 and hora_atual <=18
usuario_ativo = usuario_funcionario and not usuario_bloqueado
liberado = (usuario_ativo and horario_comercial) or usuario_admin

if liberado:
    print('liberado')
else:
    print('não liberado')

#entrada: hora_atual
#saida: hora_atual esta dentro do horario comercial (bool)
 
def dentro_horario_comercial(hora_atual):
    return hora_atual >=8 and hora_atual <= 18

#operador ternario

if idade >= 18:
    status = 'maior'
else:
    status = 'menor'

status = 'maior' if idade >= 18 else 'menor'

#usuario passa o dia (int)
#devolve string nome 
# 1 - domingo, 2 - segunda... 7 - sabado

dia = 4

dias ={
    1: 'DOmingo',
    2: 'segunda',
    3: 'terça',
    4: 'quarta',
    5: 'quinta',
    6: 'sexta',
    7: 'sábado',
}


if dia in dias:
    print(dias(dia))

dia = 2
match dia:
    case 1: 
        print('Domingo')
    case 2: 
        print('segunda')
    case 3: 
        print('terça')
    case 4: 
        print('quarta')
    case 5: 
        print('quinta')
    case 6: 
        print('sexta')
    case 7: 
        print('sábado')
    case _: 
        print('inválido')

match dia:
    case 1 | 7:
        print('Fim de semana')
    case 2 | 3 | 4 | 5 | 6:
        print('dia útil')
    case _:
        print('inválido')