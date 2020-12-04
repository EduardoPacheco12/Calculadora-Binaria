import os
import Menu

#SOMA DE BINÁRIOS 

def soma():

    while(True):

        print('Pra voltar ao MENU INTERATIVO, digite "voltar"\n')

        soma_um = input('Primeiro número binário: ')
        if soma_um.lower() == 'voltar':
            os.system('cls')
            print ('Ate logo!\n')
            os.system('pause')
            os.system('cls')
            Menu.menu_principal()
            return(None)
        elif soma_um.isnumeric() == True:
            for numero_um in str(soma_um):
                if numero_um in '01':
                    binary_um = True
                else:
                    binary_um = False
            if binary_um == False:
                os.system('cls')
                print('Este não é um número binário\n')
                os.system('pause')
                os.system('cls')
                continue
        else:
            os.system('cls')
            print('Digite uma opção válida\n')
            os.system('pause')
            os.system('cls')
            continue

        soma_dois = input('Segundo número binário: ')
        if soma_dois.lower() == 'voltar':
            os.system('cls')
            print ('Ate logo!\n')
            os.system('pause')
            os.system('cls')
            Menu.menu_principal()
            return(None)
        elif soma_dois.isnumeric() == True:
            for numero_dois in str(soma_dois):
                if numero_dois in '01':
                    binary_dois = True
                else:
                    binary_dois = False
            if binary_dois == False:
                os.system('cls')
                print('Este não é um número binário\n')
                os.system('pause')
                os.system('cls')
                continue
            else:
                soma_um = int(soma_um, 2)
                soma_dois = int(soma_dois, 2)
                resultado = soma_um + soma_dois
                os.system('cls')
                print(f'O resultado da soma será {bin(resultado)[2:]}\n')
                os.system('pause')
                os.system('cls')
        else:
            os.system('cls')
            print('Digite uma opção válida\n')
            os.system('pause')
            os.system('cls')
            continue