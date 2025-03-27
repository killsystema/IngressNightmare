Shodan Vulnerability Scanner
Este script utiliza a API do Shodan para procurar por alvos vulneráveis com base em um filtro de país e realizar um teste de vulnerabilidade (simulado). Caso um alvo vulnerável seja encontrado, ele será salvo em um arquivo de texto para posterior análise.

Funcionalidades
Busca de Alvos: Realiza uma busca no Shodan por dispositivos/servidores que atendem a um filtro baseado no país e outras condições.

Testes de Vulnerabilidade: Testa possíveis vulnerabilidades nos alvos encontrados (este teste é simulado no momento e pode ser substituído por uma lógica real).

Armazenamento de Alvos Vulneráveis: Alvos que se mostram vulneráveis são armazenados em um arquivo de texto.

Requisitos
Python 3.x

Bibliotecas Python:

shodan

colorama

Você pode instalar as dependências usando o pip:

```
pip install shodan colorama
```
Configuração
Obter a API Key do Shodan:

Crie uma conta no Shodan e obtenha a sua API Key.

Substitua a chave da variável SHODAN_API_KEY no script com sua chave API.

Como Usar
Clone este repositório ou baixe o arquivo scanNightmare.py.

(git clone https://github.com/killsystema/IngressNightmare.git)

Execute o script, passando o país como argumento:

```python3 scanNightmare.py "Brazil" ```
O script fará a busca no Shodan usando o filtro de país e testará os alvos encontrados para possíveis vulnerabilidades.

Exemplo de Saída:


```
[+] Procurando por: ssl:"Issuer: O=nil1" port:8443 country:"Brazil"
[+] Testando vulnerabilidade em 192.168.1.1:8443
[*] Possível alvo encontrado: 192.168.1.1:8443 - Admission Webhook: https://192.168.1.1:8443/admission
[-] 192.168.1.1:8443 não parece vulnerável.
[+] Testando vulnerabilidade em 192.168.1.2:8443
[!] 192.168.1.2:8443 pode estar vulnerável!
[+] Alvo vulnerável salvo: 192.168.1.2:8443 - Admission Webhook: https://192.168.1.2:8443/admission
```

Arquivo de Saída
Os alvos vulneráveis serão salvos no arquivo alvos_vulneraveis.txt:

``` 
192.168.1.2:8443 - Admission Webhook: https://192.168.1.2:8443/admission
```
