# Shodan Scan Script

Este script realiza uma busca na API do Shodan para encontrar servidores expostos a determinadas vulnerabilidades. O script utiliza consultas específicas para buscar máquinas vulneráveis e verifica se elas possuem algum tipo de vulnerabilidade configurada.

## Funcionalidade

O script realiza as seguintes ações:
1. Realiza uma busca na base de dados do Shodan com uma consulta personalizada, onde você pode definir o país e outros parâmetros de busca.
2. Verifica se as máquinas encontradas possuem vulnerabilidades (por exemplo, APIs de Kubernetes expostas).
3. Salva as máquinas vulneráveis em um arquivo de log (`alvos_vulneraveis.txt`), para que possam ser monitoradas ou investigadas mais a fundo.

## Pré-requisitos

1. **Python 3.x** - O script foi desenvolvido para rodar com o Python 3. Certifique-se de ter o Python instalado na sua máquina.
2. **Bibliotecas Python** - O script usa as bibliotecas `shodan` e `colorama` para interagir com a API do Shodan e exibir mensagens coloridas no terminal.

Para instalar as bibliotecas necessárias, execute o seguinte comando:

```bash
pip install shodan colorama

Chave da API do Shodan - Você precisará de uma chave de API do Shodan para usar o script. Se você ainda não tem, pode obter uma chave gratuita aqui.
https://www.shodan.io/

Como Usar
Obtenha sua chave de API do Shodan:

Acesse o site do Shodan e crie uma conta.

Após criar a conta, vá até Dashboard, onde você encontrará a chave da API.

Configure o Script:

Abra o script scanNightmare.py e substitua a chave da API na variável SHODAN_API_KEY:

