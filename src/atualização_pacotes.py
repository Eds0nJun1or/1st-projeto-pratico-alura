import os

def atualizar_pacotes():
    os.system('sudo apt update && sudo apt upgrade -y')

atualizar_pacotes()