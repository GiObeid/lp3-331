# LP3 331 IFSP

Repositorio para organizar os códigos da disciplina de Linguagem de Programação 3

## Instruções Lab de Info

Ao chegar no laboratório:

Configurar o usuário no git

'''bash 
git config --global user.name "seu.nome"
git config --global user.email "seu.email"

Fazer o clone do seu repositório no GitHub

'''bash 
git clone https://github.com/txminxtz/lp3-331.git

Abrir o repositorio no vscode 

'''bash
code lp3-331
'''

Criar um token para realizar os pushs 
Settings -> Developer settings -> Personal acces tokens -> Tokens (classic)
Generate new token, selecionar a opção Generate new token classic, marcar a opção scope repo

## Antes de sair do lab

1- Remover configurações de usuário do git local 

'''bash 
git config --global --unset user.name
git config --global --unset user.email
'''  