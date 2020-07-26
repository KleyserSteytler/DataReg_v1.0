from lib import Interface
import os
from time import sleep

def criarLista():
    while True:
        c = 1
        Interface.cabecalho('ARQUIVO')
        nomeLista = input('Nome do arquivo: ').upper()
        arquivo = open(f'arqs\{nomeLista}', 'wt+')
        Interface.cabecalho('CADASTRO')
        while True:
            nome = input(f'N*{c} Nome: ')
            idade = input(f'N*{c} Idade: ')
            arquivo.write(f'O Trabalhador da area da {nomeLista} "{nome}" tem {idade}anos de idade\n')
            choose = input('Deseja continuar?[S/N]: ').upper()
            c = c + 1
            if choose == 'N':
                c = 1
                arquivo.close()
                break
        Interface.cabecalho('OQUE DESEJA EFECTUAR?')
        choose = input('[1] Criar novo arquivo\n[2] Sair para MENU: ')
        if choose == '2':
            break

def infoPrograma():
    Interface.cabecalho('INFORMACOES DO SISTEMA')
    print("""
    {NOME DO PROGRAMADOR} = {KLEYZER STEYTLER}
    {ANO} = {2020}
    {VERSAO} = {v1.0}""")
    sleep(2)
    choose = input('deseja sair?[S]: ').upper()
    if choose == 'S':
        pass

def editarLista():
    i = 0
    arquivos = []
    areas = []
    for arquivos in os.walk('arqs/'):
        pass
    for areas in arquivos:
         pass
    Interface.cabecalho('LISTAS')
    while True:
        if len(areas) > 0:
            for i in areas:
                print(i)
            Interface.linha()
            nomeLista = input('Digite o nome da lista que deseja abrir: ').upper()
        else:
            print('Sem arquivos no momento')
            Interface.linha()

        try:
            arquivo = open('arqs/'+nomeLista, 'rt')
        except FileNotFoundError:
            print('Arquivo nao encontrado!')
        except UnboundLocalError:
            pass
        else:
            Interface.cabecalho(f'PESSOAS NA AREA {nomeLista.upper()}')
            print(arquivo.read())
            arquivo.close()
            Interface.cabecalho('OQUE DESEJA EFECTUAR?')
            choose = input(
                f'[1] Verificar outro arquivo\n[2] Sair para MENU\n[3] Eliminar arquivo\n[4] Eliminar pessoas da area {nomeLista}')
            Interface.linha()
            if choose == '2':
                break
            elif choose == '3':
                son = input('CONFIRMAR? [S/N]: ').upper()
                if son == 'S':
                    os.remove('arqs/'+nomeLista)

                print(f'O arquivo {nomeLista} foi removido com sucesso...')
                break
            elif choose == '4':
                continue

        finally:
            print('Processando...')
            sleep(3)
            break


        sleep(1)
        print()
        print()
