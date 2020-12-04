import os
import Menu

#CONVERSÃO DE DECIMAIS

def conversao_decimais():

    while(True):

        print("Pra voltar ao MENU INTERATIVO, digite 'voltar'\n")

        num = input("digite um número inteiro: ")
        if num.lower() == 'voltar':
            os.system('cls')
            print("Até logo\n")
            os.system('pause')
            os.system('cls')
            Menu.menu_principal()
            return(None)
        elif num.isnumeric() == False:
            os.system('cls')
            print("Por favor digite um valor válido\n")
            os.system('pause')
            os.system('cls')
            continue
        else:
            num = int(num)
            os.system('cls')
            print (f"O {num} convertido para binário é: {bin(num)[2:]}\n ")
            os.system('pause')
            os.system('cls')