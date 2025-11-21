from libr.interface import *
from  libr.arquivo import *

arquivo='usuarios_cadastrados.txt'
if not arquivoExiste(arquivo):
    criarArquivo(arquivo)


while True:
    arquivoExiste(arquivo)
    resposta=menu(['Cadastrar Usuário', 'Listar Usuário','Sair'])
    #OPÇÃO 1
    if resposta == 1:
        nome=str(input('\033[97mNome: ')).title().strip()
        idade=lerinteiros('Idade: ')
        while True:
            sexo=input('Sexo [M/F]: \033[m').upper().strip()
            if sexo not in ('M','F'):
                print('\033[91mERRO digite uma opção valida M ou F.\033[97m')
            else:
                break
        cadastrar(arquivo,nome, idade, sexo)
    #OPÇÃO 2
    elif resposta == 2:
        lerArquivo(arquivo)
        respostarLerusuario=menuLista([f'{icone('1')} - {cor_frase('Verificar dados completo ou editar')}',f'{icone('2')} - {cor_frase('Remover usuário')} ',f'\033[37mENTER para voltar\033[m'])

        if respostarLerusuario == 1:
                editarUsuario(arquivo)
                input(f'\n\033[37mAperte ENTER para voltar\033[m')

        elif respostarLerusuario == 2:
                removerUsuario(arquivo)


    #OPÇÃO 3
    elif resposta == 3:
        print('Opção 3')
    else:
        print('ERRO! Digite uma opção valida... ')