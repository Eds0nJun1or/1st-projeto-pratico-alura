import shutil
import os
import datetime

def fazer*backup(origem, destino):
    agora = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    destino_backup = destino + '*' + agora
    shutil.copytree(origem, destino_backup)

origem = '/caminho/para/origem'
destino = '/caminho/para/destino'
fazer_backup(origem, destino)