## Script de Limpeza de Arquivos Temporários em Python

Este script Python realiza a limpeza de arquivos temporários. Aqui está uma análise detalhada do que o script faz:

1. Importação de Módulos: O script começa importando os módulos necessários - os e tempfile.

2. Definição da Função de Limpeza: A função limpar_temporarios() é definida para realizar a limpeza de arquivos temporários.

3. Obtenção do Diretório Temporário: Dentro da função, a primeira coisa que acontece é a obtenção do diretório temporário usando a função tempfile.gettempdir().

4. Iteração sobre os Arquivos Temporários: Em seguida, o script itera sobre todos os arquivos no diretório temporário.

5. Verificação e Remoção de Arquivos: Para cada arquivo, o script verifica se é realmente um arquivo (e não um diretório) usando a função os.path.isfile(). Se for um arquivo, ele é removido usando a função os.remove().

6. Execução da Função de Limpeza: Finalmente, a função limpar_temporarios() é chamada para iniciar o processo de limpeza.