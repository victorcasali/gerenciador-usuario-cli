from time import sleep

def lerinteiros(msg):
    while True:
        try:
            n=int(input(msg))
        except(ValueError,TypeError,KeyboardInterrupt):
            print('\033[91mERRO! Digite um valor valido.\033[m\033[97m')
            sleep(0.4)
            continue
        else:
            return n

def linha(tam=40):
    print('\033[1;96m-\033[m'*tam)

def titulo(title):
    linha()
    print(title.center(50))
    linha()

def menu(lista):
    titulo('\033[1;96mGERENCIADOR DE USUÁRIO\033[m')
    c=1
    for b in lista:
        print(f'{icone(c)} \033[94m- {cor_frase(b)}')
        c+=1
    linha()
    op=lerinteiros('\033[94mSua opção:\033[m ')
    return op

def menuLista(lista):
    linha()
    print('Opções:')
    for b in lista:
        print(f'{b}')
    linha()
    op=input(f'{cor_frase('Sua opção: ')}')
    if op =='':
        return
    if op.isdigit():
        return int(op)

    return None


def icone(msg):
    return f'\033[94m[\033[m\033[97m{msg}\033[m\033[94m]\033[m'

#Branco
def cor_frase(msg):
    return f'\033[97m{msg}\033[m'
