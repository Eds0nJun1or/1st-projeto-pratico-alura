import os
import tempfile

def limpar_temporarios():
    pasta_temporaria = tempfile.gettempdir()

for arquivo in os.listdir(pasta_temporaria):
caminho_arquivo = os.path.join(pasta_temporaria, arquivo)
if os.path.isfile(caminho_arquivo):
os.remove(caminho_arquivo)

limpar_temporarios()