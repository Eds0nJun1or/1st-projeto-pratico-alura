## Pasta de Scripts

Esta pasta contém vários scripts Python que realizam uma variedade de tarefas, incluindo backup de arquivos, limpeza de arquivos temporários, monitoramento de uso de disco e recursos, verificação e correção de permissões de arquivos, e integração com Cron Jobs.

### Sumário de Assuntos
* Backup de Arquivos
* Limpeza de Arquivos Temporários
* Monitoramento de Uso de Disco
* Monitoramento de Recursos
* Verificação e Correção de Permissões de Arquivos
* Integração com Cron Jobs

### Arquivos
* script_backup.py: Script responsável por realizar backups dos arquivos especificados.
* script_limpeza_temporarios.py: Script responsável por limpar arquivos temporários.
* script_monitoramento_disco.py: Script responsável por monitorar o uso de disco.
* script_monitoramento_recursos.py: Script responsável por monitorar o uso de recursos, como CPU e memória.
* script_verificar_corrigir_permissoes.py: Script responsável por verificar e corrigir as permissões de um arquivo.
* README.md: Este arquivo contém informações sobre a pasta de Scripts Python e instruções de uso.

### Instruções de Uso
* Configure as variáveis de origem e destino no script_backup.py e execute o script para iniciar o processo de backup.
* Execute o script_limpeza_temporarios.py para iniciar o processo de limpeza de arquivos temporários.
* Execute o script_monitoramento_disco.py e script_monitoramento_recursos.py para iniciar o processo de monitoramento de uso de disco e recursos, respectivamente.
* Configure o caminho do arquivo no script_verificar_corrigir_permissoes.py e execute o script para iniciar o processo de verificação e correção de permissões.
* Configure os caminhos dos scripts no Cron Jobs para agendar a execução dos scripts. Certifique-se de que os scripts têm as permissões corretas para serem executados. Verifique o log do Cron Jobs para garantir que os scripts estão sendo executados conforme o esperado.