import os

def verificar_corrigir_permissões(caminho_arquivo): # Verificar as permissões atuais do arquivo
    permissões_atuais = os.stat(caminho_arquivo).st_mode & 0o777
    print("Permissões atuais:", oct(permissões_atuais))

Corrigir permissões para 755 (rwxr-xr-x)
os.chmod(caminho_arquivo, 0o755)
print("Permissões corrigidas para 755")

caminho_arquivo = '/caminho/para/arquivo.txt'
verificar_corrigir_permissões(caminho_arquivo)