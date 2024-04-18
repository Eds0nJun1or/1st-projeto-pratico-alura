## Script de Backup em Python

Este script Python realiza o backup de arquivos e diretórios importantes. Aqui está uma análise detalhada do que o script faz:

1. Importação de Módulos: O script começa importando os módulos necessários - shutil, os e datetime.

2. Definição da Função de Backup: A função fazer_backup(origem, destino) é definida para realizar o backup. Ela aceita dois argumentos - origem e destino.

3. Criação do Nome do Diretório de Backup: Dentro da função, a primeira coisa que acontece é a criação de um nome de diretório de backup único.

4. Realização do Backup: A função shutil.copytree() é usada para copiar todo o diretório de origem para o diretório de backup.

5. Execução da Função de Backup: Finalmente, a função fazer_backup() é chamada com o diretório de origem e o diretório de destino especificados.

