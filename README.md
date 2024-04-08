# Processo de Automatização de Tarefas

Este repositório foi criado para apresentar minha experiência com as primeiras aulas da Alura e como fiz o primeiro projeto prático proposto pelos mentores. Este projeto demonstrou como a combinação de atividades teóricas e práticas podem criar uma solução poderosa para sistemas automatizados.

## A. Identificação de Tarefas:

Nesta etapa, identificamos as tarefas comuns que podem ser automatizadas no ambiente Linux. Isso pode incluir uma variedade de atividades, como backup de arquivos, limpeza de temporários, monitoramento de recursos do sistema, gerenciamento de permissões de arquivos, atualização de pacotes do sistema e notificação em caso de eventos importantes. O objetivo é identificar tarefas que consomem tempo e podem ser realizadas de forma mais eficiente e consistente através da automação.

## B. Desenvolvimento de Scripts:

Após identificar as tarefas a serem automatizadas, desenvolvemos scripts Python para realizar cada uma delas. Cada script é projetado para executar uma tarefa específica de forma automatizada. Por exemplo, um script de backup pode fazer uma cópia de segurança de determinados arquivos ou diretórios importantes para um local especificado, enquanto um script de limpeza de temporários pode remover arquivos temporários que não são mais necessários. É importante garantir que os scripts sejam robustos, eficientes e seguros.

## C. Integração com Cron Jobs:

Para garantir que as tarefas automatizadas sejam executadas regularmente, integramos os scripts com tarefas cron. O cron é um utilitário de agendamento de tarefas no Linux que permite programar a execução de comandos ou scripts em intervalos específicos. Configuramos entradas no arquivo crontab para especificar quando e com que frequência os scripts devem ser executados. Isso garante a automação contínua das tarefas, ajudando a manter o sistema funcionando de forma eficiente e confiável ao longo do tempo.

## Identificação de Tarefas:

1. Backup de arquivos e diretórios importantes.
2. Limpeza automática de arquivos temporários.
3. Monitoramento de uso de disco.
4. Monitoramento de uso de CPU e memória.
5. Verificação e correção de permissões de arquivos.
6. Atualização automática de pacotes do sistema.
7. Notificação por e-mail em caso de eventos importantes, como falhas no sistema ou espaço em disco insuficiente.

## Desenvolvimento de Scripts em Python:

1. Script de Backup:

#   
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

2. Script de Limpeza de Arquivos Temporários:

#
    import os
    import tempfile

    def limpar_temporarios():
    pasta_temporaria = tempfile.gettempdir()
    for arquivo in os.listdir(pasta_temporaria):
    caminho_arquivo = os.path.join(pasta_temporaria, arquivo)
    if os.path.isfile(caminho_arquivo):
    os.remove(caminho_arquivo)

    limpar_temporarios()

3. Script de Monitoramento de Uso de Disco:

#
    import psutil

    def monitorar_uso_disco():
    uso_disco = psutil.disk_usage('/')
    print("Uso de disco:")
    print("Total:", uso_disco.total)
    print("Usado:", uso_disco.used)
    print("Livre:", uso_disco.free)

    monitorar_uso_disco()

4. Monitoramento de uso de CPU e memória:

# 
    import psutil

    def monitorar_recursos(): # Monitoramento de uso de CPU
    uso_cpu = psutil.cpu_percent(interval=1)
    print("Uso de CPU:", uso_cpu, "%")

        Monitoramento de uso de memória
        uso_memoria = psutil.virtual_memory().percent
        print("Uso de memória:", uso_memoria, "%")

    monitorar_recursos()

5. Verificação e correção de permissões de arquivos:

#
    import os

    def verificar_corrigir_permissões(caminho_arquivo): # Verificar as permissões atuais do arquivo
    permissões_atuais = os.stat(caminho_arquivo).st_mode & 0o777
    print("Permissões atuais:", oct(permissões_atuais))

        Corrigir permissões para 755 (rwxr-xr-x)
        os.chmod(caminho_arquivo, 0o755)
        print("Permissões corrigidas para 755")

    caminho_arquivo = '/caminho/para/arquivo.txt'
    verificar_corrigir_permissões(caminho_arquivo)

6. Atualização automática de pacotes do sistema:

#
    import os

    def atualizar_pacotes():
    os.system('sudo apt update && sudo apt upgrade -y')

    atualizar_pacotes()

7. Notificação por e-mail em caso de eventos importantes:
#

    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    def enviar_email(destinatario, assunto, corpo_mensagem): # Configurações do servidor SMTP
    smtp_host = 'smtp.example.com'
    smtp_porta = 587
    email_rem = 'seu_email@example.com'
    senha = 'sua_senha'

        Configurar mensagem
        mensagem = MIMEMultipart()
        mensagem['From'] = email_rem
        mensagem['To'] = destinatario
        mensagem['Subject'] = assunto
        mensagem.attach(MIMEText(corpo_mensagem, 'plain'))

        Conectar ao servidor SMTP e enviar e-mail
        server = smtplib.SMTP(smtp_host, smtp_porta)
        server.starttls()
        server.login(email_rem, senha)
        server.sendmail(email_rem, destinatario, mensagem.as_string())
        server.quit()

### Exemplos de como usar:

#
    destinatario = 'destinatario@example.com'
    assunto = 'Alerta: Falha no sistema!'
    corpo_mensagem = 'O sistema encontrou uma falha crítica. Por favor, verifique imediatamente.'
    enviar_email(destinatario, assunto, corpo_mensagem)

## Integração com Cron Jobs:

#
    0 1 * * * /usr/bin/python3/caminho/para/script_backup.py
    0 2 * * * /usr/bin/python3/caminho/para/script_limpeza_temporarios.py
    0 3 * * * /usr/bin/python3/caminho/para/script_monitoramento_disco.py
### Isso agendará a execução dos scripts de backup, limpeza de temporários e monitoramento de disco para 1h, 2h e 3h da manhã, respectivamente, todos os dias. Certifique-se de substituir "/caminho/para/" pelos caminhos reais dos seus scripts.

# 
    _/5 _ * * * /usr/bin/python3/caminho/para/script_monitoramento_recursos.py
### Agendar a execução a cada 5 minutos

#
    0 3 * * * /usr/bin/python3/caminho/para/script_verificar_corrigir_permissoes.py
### Agendar a execução diária às 3 da manhã

#
    0 2 * * * /usr/bin/python3/caminho/para/script_atualizar_pacotes.py
### Agendar a execução semanalmente às segundas-feiras às 2 da manhã

#
    0 8 * * * /usr/bin/python3/caminho/para/script_notificacao_email.py
### Agendar a execução diária às 8 da manhã