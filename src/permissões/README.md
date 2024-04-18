## Verificação e Correção de Permissões de Arquivos em Python

Este script Python realiza a verificação e correção das permissões de um arquivo. Aqui está uma análise detalhada do que o script faz:

1. Importação de Módulos: O script começa importando o módulo necessário - os.

2. Definição da Função de Verificação e Correção: A função verificar_corrigir_permissões(caminho_arquivo) é definida para realizar a verificação e correção das permissões de um arquivo.

3. Verificação das Permissões Atuais: Dentro da função, a primeira coisa que acontece é a verificação das permissões atuais do arquivo usando a função os.stat(caminho_arquivo).st_mode & 0o777.

4. Impressão das Permissões Atuais: Em seguida, o script imprime as permissões atuais do arquivo.

5. Correção das Permissões para 755: O script então corrige as permissões do arquivo para 755 (rwxr-xr-x) usando a função os.chmod(caminho_arquivo, 0o755).

6. Impressão das Permissões Corrigidas: O script imprime que as permissões foram corrigidas para 755.

7. Execução da Função de Verificação e Correção: Finalmente, a função verificar_corrigir_permissões(caminho_arquivo) é chamada com o caminho do arquivo especificado para iniciar o processo de verificação e correção.