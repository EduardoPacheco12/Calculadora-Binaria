import os
import Conversao
import SomaBinario
import SubtracaoBinario
import MultiplicacaoBinario
import DivisaoBinario

def menu_principal():
    
    while(True):
        print("BEM VINDO A CALCULADORA BINÁRIA\n")
        print("===== MENU INTERATIVO =====")
        print("O QUE DESEJA FAZER?\n")
        print("[1]Converter um número decimal para binário")
        print("[2]Soma")
        print("[3]Subtração")
        print("[4]Multiplicação")
        print("[5]Divisão")
        print("Se quiser encerrar o programa digite 'sair'")
        opcao = input("OPÇÃO: ")
        os.system('cls')

        if opcao.lower() == 'sair':
            print("\nFim do Programa!")
            exit(0)

        elif opcao == '1': #CONVERSÃO DE DECIMAIS
            Conversao.conversao_decimais()

        elif opcao == '2': #SOMA DE BINÁRIOS
            SomaBinario.soma()

        elif opcao == '3': #SUBTRAÇÃO DE BINÁRIOS
            SubtracaoBinario.subtracao()

        elif opcao == '4': #MULTIPLICAÇÃO DE BINÁRIOS
            MultiplicacaoBinario.multiplicacao()

        elif opcao == '5': #DIVISÃO DE BINÁRIOS
            DivisaoBinario.divisão()

        else: #QUALQUER OUTRA OPÇÃO DIGITADA SERÁ INVÁLIDADA PARA O BOM USO DO CÓDIGO
            print("Opção inválida, tente novamente\n")
            os.system('pause')
            os.system('cls')
            continue