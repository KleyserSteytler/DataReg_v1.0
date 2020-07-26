from lib import Interface
from lib import Funcionabilidades
import sys

while True:
    resposta = Interface.corpoPrincipal('MENU PRINCIPAL', ['[1] Nova lista', '[2] Editar Listas Existentes', '[3] Info','[4] sair do programa'])
    if resposta == '1':
        Funcionabilidades.criarLista()
    elif resposta == '2':
        Funcionabilidades.editarLista()
    elif resposta == '3':
        Funcionabilidades.infoPrograma()
    elif resposta == '4':
        sys.exit()
