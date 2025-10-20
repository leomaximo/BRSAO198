import requests
import re # Módulo para expressões regulares, útil para limpar o CEP

def consultar_cep():
    """
    Busca informações de endereço (logradouro, bairro, cidade, estado) 
    a partir de um CEP usando a API ViaCEP.
    """
    # 1. Obter e Limpar Input
    cep_input = input("Digite o CEP para consulta (ex: 01001-000): ")
    
    # Remove caracteres não numéricos
    cep = re.sub(r'\D', '', cep_input)

    if len(cep) != 8:
        print("\n❌ ERRO: O CEP deve conter exatamente 8 dígitos numéricos.")
        return

    # 2. Definir o Endpoint da API
    API_URL = f"https://viacep.com.br/ws/{cep}/json/"
    
    print(f"Buscando informações para o CEP {cep}...")

    try:
        # 3. Fazer a requisição HTTP GET
        response = requests.get(API_URL, timeout=10) # Timeout para evitar espera infinita

        # 4. Verificar o Status da Resposta HTTP
        if response.status_code == 200:
            dados = response.json()
            
            # 5. Verificar erro interno da API (CEP inexistente)
            if 'erro' in dados and dados['erro'] == True:
                print(f"\n❌ Falha: O CEP {cep_input} não foi encontrado na base de dados.")
                return

            # 6. Extrair e Exibir as informações
            print("\n--- Informações do Endereço ---")
            print(f"CEP: {cep}")
            print(f"Logradouro: {dados.get('logradouro', 'Não Informado')}")
            print(f"Bairro: {dados.get('bairro', 'Não Informado')}")
            print(f"Cidade (Localidade): {dados.get('localidade', 'Não Informada')}")
            print(f"Estado (UF): {dados.get('uf', 'Não Informado')}")
            print("-------------------------------\n")
            
        else:
            # Lida com erros HTTP genéricos (ex: 404, 500)
            print(f"\n❌ Falha na requisição. A API retornou o código de status: {response.status_code}.")

    # 7. Lida com Erros de Conexão
    except requests.exceptions.RequestException as e:
        print("\n❌ ERRO DE CONEXÃO!")
        print("Não foi possível conectar à API. Verifique sua conexão com a internet.")
        # Opcional: print(f"Detalhe do erro: {e}")

# --- Execução do Programa ---
if __name__ == "__main__":
    consultar_cep()