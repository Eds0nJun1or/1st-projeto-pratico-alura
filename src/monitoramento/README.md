## Monitoramento de Uso de Disco em Python

Este script Python realiza o monitoramento do uso de disco. Aqui está uma análise detalhada do que o script faz:

1. Importação de Módulos: O script começa importando o módulo necessário - psutil.

2. Definição da Função de Monitoramento: A função monitorar_uso_disco() é definida para realizar o monitoramento do uso de disco.

3. Obtenção do Uso de Disco: Dentro da função, a primeira coisa que acontece é a obtenção do uso de disco usando a função psutil.disk_usage('/').

4. Impressão do Uso de Disco: Em seguida, o script imprime o total, o usado e o livre do uso de disco.

5. Execução da Função de Monitoramento: Finalmente, a função monitorar_uso_disco() é chamada para iniciar o processo de monitoramento.

## Monitoramento de Recursos em Python

Este script Python realiza o monitoramento de recursos, incluindo o uso de CPU e memória. Aqui está uma análise detalhada do que o script faz:

1. Importação de Módulos: O script começa importando o módulo necessário - psutil.

2. Definição da Função de Monitoramento: A função monitorar_recursos() é definida para realizar o monitoramento de recursos.

3. Monitoramento de Uso de CPU: Dentro da função, a primeira coisa que acontece é o monitoramento do uso de CPU usando a função psutil.cpu_percent(interval=1).

4. Monitoramento de Uso de Memória: Em seguida, o script monitora o uso de memória usando a função psutil.virtual_memory().percent.

5. Impressão do Uso de Recursos: O script então imprime o uso de CPU e memória.

6. Execução da Função de Monitoramento: Finalmente, a função monitorar_recursos() é chamada para iniciar o processo de monitoramento.