import os
import Menu

#MULTIPLICAÇÃO DE BINÁRIOS

def multiplicacao():

    while(True):

        print('Pra voltar ao MENU INTERATIVO, digite "voltar"\n')

        multiplicacao_um = input('Primeiro número binário: ')
        if multiplicacao_um.lower() == 'voltar':
            os.system('cls')
            print ('Ate logo!\n')
            os.system('pause')
            os.system('cls')
            Menu.menu_principal()
            return(None)
        elif multiplicacao_um.isnumeric() == True:
            for numero_um in str(multiplicacao_um):
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

        multiplicacao_dois = input('Segundo número binário: ')
        if multiplicacao_dois.lower() == 'voltar':
            os.system('cls')
            print ('Ate logo!\n')
            os.system('pause')
            os.system('cls')
            Menu.menu_principal()
            return(None)
        elif multiplicacao_dois.isnumeric() == True:
            for numero_dois in str(multiplicacao_dois):
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
                multiplicacao_um = int(multiplicacao_um, 2)
                multiplicacao_dois = int(multiplicacao_dois, 2)
                resultado = multiplicacao_um * multiplicacao_dois
                os.system('cls')
                print(f'O resultado da multiplicação será {bin(resultado)[2:]}\n')
                os.system('pause')
                os.system('cls')
        else:
            os.system('cls')
            print('Digite uma opção válida\n')
            os.system('pause')
            os.system('cls')
            continue

