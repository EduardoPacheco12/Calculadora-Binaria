import os
import Menu

#SUBTRAÇÃO DE BINÁRIOS

def subtracao():

    while(True):

        print('Pra voltar ao MENU INTERATIVO, digite "voltar"\n')

        subtracao_um = input('Primeiro número binário: ')
        if subtracao_um.lower() == 'voltar':
            os.system('cls')
            print ('Ate logo!\n')
            os.system('pause')
            os.system('cls')
            Menu.menu_principal()
            return(None)
        elif subtracao_um.isnumeric() == True:
            for numero_um in str(subtracao_um):
                if numero_um in '10':
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

        subtracao_dois = input('Segundo número binário: ')
        if subtracao_dois.lower() == 'voltar':
            os.system('cls')
            print ('Ate logo!\n')
            os.system('pause')
            os.system('cls')
            Menu.menu_principal()
            return(None)
        elif subtracao_dois.isnumeric() == True:
            for numero_dois in str(subtracao_dois):
                if numero_dois in '10':
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
                subtracao_um = int(subtracao_um, 2)
                subtracao_dois = int(subtracao_dois, 2)
                resultado = subtracao_um - subtracao_dois
                os.system('cls')
                print(f'O resultado da subtração será {bin(resultado)[2:]}\n')
                os.system('pause')
                os.system('cls')
        else:
            os.system('cls')
            print('Digite uma opção válida\n')
            os.system('pause')
            os.system('cls')
            continue