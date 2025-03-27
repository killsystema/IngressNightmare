import shodan
import sys
import os
from colorama import Fore, init

# Inicializa o colorama para suportar cores no terminal
init(autoreset=True)

# Substitua pela sua API Key do Shodan
SHODAN_API_KEY = "SUA_CHAVE_API_AQUI"

# Consultas para encontrar possíveis alvos (filtro de país)
def generate_query(country):
    return f' ssl:"Issuer: O=nil1" port:8443 country:"{country}"'

def test_vulnerability(ip, port):
    try:
        print(Fore.YELLOW + f"[+] Testando vulnerabilidade em {ip}:{port}")
        # Simulação de teste de vulnerabilidade (substitua com lógica real)
        return True  # Substitua por lógica real de detecção
    except Exception as e:
        print(Fore.RED + f"[-] Erro ao testar {ip}:{port} - {e}")
        return False

def save_vulnerable_target(ip, port, admission_url):
    try:
        file_path = "alvos_vulneraveis.txt"
        mode = "a" if os.path.exists(file_path) else "w"
        with open(file_path, mode) as f:
            f.write(f"{ip}:{port} - Admission Webhook: {admission_url}\n")
        print(Fore.GREEN + f"[+] Alvo vulnerável salvo: {ip}:{port} - Admission Webhook: {admission_url}")
    except Exception as e:
        print(Fore.RED + f"[-] Erro ao salvar alvo vulnerável: {e}")

def search_shodan(api, query):
    try:
        print(Fore.YELLOW + f"[+] Procurando por: {query}")
        results = api.search(query)
        
        for result in results['matches']:
            ip = result['ip_str']
            port = result['port']
            admission_url = f"https://{ip}:{port}/admission"  # Supondo uma URL padrão
            print(Fore.CYAN + f"[*] Possível alvo encontrado: {ip}:{port} - Admission Webhook: {admission_url}")
            
            if test_vulnerability(ip, port):
                print(Fore.RED + f"[!] {ip}:{port} pode estar vulnerável!")
                save_vulnerable_target(ip, port, admission_url)
            else:
                print(Fore.GREEN + f"[-] {ip}:{port} não parece vulnerável.")
            
    except shodan.APIError as e:
        print(Fore.RED + f"[-] Erro na API do Shodan: {e}")
    except Exception as e:
        print(Fore.RED + f"[-] Erro inesperado: {e}")

if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            print(Fore.RED + "Uso: python3 shodan_scan.py <país>")
            sys.exit(0)
        
        country = sys.argv[1]  # Recebe o país como argumento
        query = generate_query(country)

        api = shodan.Shodan(SHODAN_API_KEY)
        
        # Busca no Shodan usando o país como filtro
        search_shodan(api, query)
        
    except KeyboardInterrupt:
        print(Fore.YELLOW + "[!] Interrompido pelo usuário.")
    except Exception as e:
        print(Fore.RED + f"[-] Erro crítico: {e}")
