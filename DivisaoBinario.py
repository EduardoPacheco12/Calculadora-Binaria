import os
import Menu

#DIVISÃO DE BINÁRIOS

def divisão():

    while(True):
            
        print('Pra voltar ao MENU INTERATIVO, digite "voltar"\n')

        divisao_um = input('Primeiro número binário: ')
        if divisao_um.lower() == 'voltar':
            os.system('cls')
            print ('Ate logo!\n')
            os.system('pause')
            os.system('cls')
            Menu.menu_principal()
            return(None)
        elif divisao_um.isnumeric() == True:
            for numero_um in str(divisao_um):
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

        divisao_dois = input('Segundo número binário: ')
        if divisao_dois.lower() == 'voltar':
            os.system('cls')
            print ('Ate logo!\n')
            os.system('pause')
            os.system('cls')
            Menu.menu_principal()
            return(None)
        elif divisao_dois.isnumeric() == True:
            for numero_dois in str(divisao_dois):
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
                divisao_um = int(divisao_um, 2)
                divisao_dois = int(divisao_dois, 2)
                resultado = divisao_um // divisao_dois
                os.system('cls')
                print(f'O resultado da divisão será {bin(resultado)[2:]}\n')
                os.system('pause')
                os.system('cls')
        else:
            os.system('cls')
            print('Digite uma opção válida\n')
            os.system('pause')
            os.system('cls')
            continue             
