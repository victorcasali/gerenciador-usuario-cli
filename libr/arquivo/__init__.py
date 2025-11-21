from fileinput import close

from libr.interface import lerinteiros, linha, cor_frase, icone


def arquivoExiste(nome):
    try:
        a=open(nome,'rt')
        a.close()
    except(FileNotFoundError):
        print('Arquivo não existe')
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a=open(nome,'wt+')
        a.close()
    except:
        return False
    else:
        print(f'Foi criado um arquivo {nome}')

def lerArquivo(nome):
    linha()
    print(f"\033[1;97m{'Cod.':<10}{'Nome':<10}\033[m")
    linha()
    try:
        a=open(nome,'rt')
    except:
        print('\033[91mERRO ao ler arquivo\033[m')
    else:
        for l in a:
            if l.strip() == '':
                continue
            dado=l.split(';')
            dado[1]=dado[1].replace('\n','')
            print(f'\033[97m{dado[0]:<10}{dado[1]:<20}\033[m')
        a.close()

def cadastrar(arq, nome='<desconhecido>', idade=0, sexo='N'):
    mat = matricula(arq)

    if mat is None:
        mat = 1
    else:
        mat += 1

    try:
        a = open(arq, 'at')
    except:
        print('ERRO ao abrir o arquivo')
    else:
        try:
            a.write(f'{mat};{nome};{idade};{sexo}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados')
        else:
            print(f'\033[97mNovo cadastro de\033[m \033[4;94m{nome}\033[m \033[97m adicionado\033[m')
        finally:
            a.close()

def contarUsuario(arq):
    try:
        a=open(arq,'rt')
    except(FileNotFoundError):
        return None
    else:
        contador=0
        for l in a:
            contador+=1
        a.close()
    return contador

def matricula(arq):
    maior=0
    try:
        a=open(arq,'rt')
    except(FileNotFoundError):
        print('Lista vazia...')
        return None
    else:
        for l in a:
            if l.strip()=='':
                continue
            dado=l.split(';')
            mat=int(dado[0])
            if mat > maior:
                maior=mat
        a.close()
        return maior

def buscarUsuario(arq):
    busca = str(input(f'{cor_frase('Digite a matricula ou nome do usuário: ')}'))
    linha()
    #1 — Descobrir tipo da busca
    if busca.isdigit():
        tipo='matricula'
        valor=int(busca)
    else:
        tipo='nome'
        valor=busca.lower()

    # 2 — Abrir o arquivo
    try:
        a=open(arq,'rt')
    except:
        print('Erro ao abrir arquivo')
        return None
    else:
        # 3 — Procurar linha por linha
        for l in a:
            #Pular linhas que estão em branco (evita erro)
            if l.strip() == '':
                continue

            dado=l.split(';')
            dado[-1]=dado[-1].replace('\n','')
            mat=int(dado[0])
            nome=dado[1].lower()
            if tipo == "matricula" and mat == valor:
                return dado
            if tipo == "nome" and valor in nome:
                return dado

        return None

def mostrarUsuario(arq):
    dado=buscarUsuario(arq)
    if dado is None:
        print('Usuário não encontrado')
    else:
        print(f'Matricula: {dado[0]}\nNome: {dado[1]}\nIdade: {dado[2]}\nSexo: {dado[3]}')

def removerUsuario(arq):
    dado=buscarUsuario(arq)
    if dado is None:
        print('Usuário não encontrado')
        return

    print(f'Remover usuário \033[94m{dado[1]}\033[m?')
    print('Digite ENTER para voltar')
    confirm=input(f'Digite {icone('S')} para confirmar: ').upper().strip()
    if confirm != 'S':
        print('Remoção CANCELADA')
        return

    try:
        a=open(arq,'rt')
        linhas=a.readlines()
        a.close()
    except:
        print('Erro ao abrir arquivo')
        return

    nova_lista=[]
    for linha in linhas:
        if linha.strip()=='':
            continue

        partes=linha.split(';')

        if partes[0]==dado[0]:
            continue
        nova_lista.append(linha)

    try:
        a=open(arq,'wt')
        for item in nova_lista:
            a.write(item)
        a.close()
        print('Usuário removido com sucesso.')
    except:
        print('Erro ao gravar arquivo durante a remoção')


def editarUsuario(arq):
    dado=buscarUsuario(arq)
    if dado is None:
        print('Usuário não encontrado')
        return

    print(f'\033[1;97mUsuário encontrado: \033[m')
    print(f'\033[94m{"Matricula:":<10}\033[m \033[97m{dado[0]}\033[m')
    print(f'\033[94m{"Nome:":<10}\033[m \033[97m{dado[1]}\033[m')
    print(f'\033[94m{"Idade:":<10}\033[m \033[97m{dado[2]}\033[m')
    print(f'\033[94m{"Sexo:":<10}\033[m \033[97m{dado[3].upper()}\033[m')

    op=(input('Deseja editar esse usuário?[S/N] ')).upper().strip()
    if op == '' or op!='S':
        print('Edição CANCELADA')
        return
    linha()


    print('Oque deseja editar?')
    print(f'{icone('1')} - {cor_frase('Nome')}')
    print(f'{icone('2')} - {cor_frase('Idade')}')
    print(f'{icone('3')} - {cor_frase('Sexo')}')
    print(f'{icone('4')} - {cor_frase('Editar tudo')}')
    print(f'{icone('5')} - {cor_frase('Cancelar')}')
    opc=input('Escolha uma opção para editar: ').strip()

    if opc =='':
        print('Edição CANCELADA')
        return

    elif opc == '1':
        novo_nome = input(f'{cor_frase('Digite o novo nome: ')}').title().strip()
        if novo_nome != '':
            dado[1]=novo_nome
    elif opc == '2':
        nova_idade=lerinteiros('Digite uma nova idade: ')
        dado[2]=nova_idade
    elif opc == '3':
        novo_sexo=input('Digite um novo sexo[M/F]: ').strip()
        if novo_sexo != '':
            dado[3]=novo_sexo
    elif opc == '4':
        novo_nome = input('Digite o novo nome: ').title().strip()
        nova_idade = input('Digite uma nova idade: ').strip()
        novo_sexo = input('Digite um novo sexo[M/F]: ').strip()
        dado[1] = novo_nome
        dado[2] = nova_idade
        dado[3] = novo_sexo
    else:
        print('Opção invalida')
        return

    try:
        a=open(arq,'rt')
        linhas= a. readlines()
        a.close()
    except:
        print('ERRO ao abrir arquivo')
        return
    nova_lista=[]
    for l in linhas:
        if l.strip()=='':
            continue
        partes=l.split(';')
        if partes [0] == dado[0]:
            nova_lista.append(f"{dado[0]};{dado[1]};{dado[2]};{dado[3]}\n")
        else:
            nova_lista.append(l)
    try:
        a=open(arq,'wt')
        for item in nova_lista:
            a.write(item)
        a.close()
        print('\033[92mUsuário atualizado com sucesso\033[m')
    except:
        print('Erro ao gravar arquivo')

