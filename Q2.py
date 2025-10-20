import requests
import json # Não estritamente necessário, mas bom para manipulação de JSON

def buscar_usuario_aleatorio():
    # URL da API Random User Generator para um usuário aleatório
    API_URL = "https://randomuser.me/api/"
    
    print(f"Tentando conectar à API em: {API_URL}...")

    try:
        # 1. Faz a requisição HTTP GET
        response = requests.get(API_URL, timeout=10) # Define um timeout para evitar espera infinita

        # 2. Verifica se a requisição foi bem-sucedida (código 200)
        if response.status_code == 200:
            # Converte a resposta JSON em um dicionário Python
            dados = response.json()
            
            # O usuário está na primeira posição da lista 'results'
            usuario = dados['results'][0]
            
            # 3. Extrai as informações
            nome_primeiro = usuario['name']['first']
            nome_ultimo = usuario['name']['last']
            email = usuario['email']
            pais = usuario['location']['country']
            
            # 4. Exibe o resultado
            print("\n--- Usuário Fictício Encontrado ---")
            print(f"Nome: {nome_primeiro} {nome_ultimo}")
            print(f"E-mail: {email}")
            print(f"País: {pais}")
            print("------------------------------------\n")

        else:
            # 5. Lida com outros erros HTTP (ex: 404, 500)
            print(f"\n❌ Falha na busca do usuário. A API retornou o código de status: {response.status_code}.")
            print("Verifique se o endpoint da API está correto.")

    # 6. Lida com erros de conexão (ex: timeout, DNS, falta de internet)
    except requests.exceptions.RequestException as e:
        print("\n❌ ERRO DE CONEXÃO!")
        print(f"Não foi possível conectar à API. Verifique sua conexão com a internet ou o status do serviço.")
        # Opcional: print(f"Detalhe do erro: {e}")

# --- Execução do Programa ---
if __name__ == "__main__":
    buscar_usuario_aleatorio()