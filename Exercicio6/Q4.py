import requests
import datetime

def consultar_cotacao():
    """
    Consulta informações de cotação de uma moeda em relação ao Real (BRL) 
    usando a Awesome API e exibe os dados.
    """
    # 1. Obter e Validar Input
    moeda_input = input("Digite a sigla da moeda para consulta (ex: USD, EUR, BTC): ")
    moeda = moeda_input.upper().strip()
    
    if len(moeda) != 3 or not moeda.isalpha():
        print("\n❌ ERRO: Por favor, digite uma sigla de moeda válida (3 letras).")
        return

    # 2. Definir o Endpoint da API (Moeda-BRL)
    API_URL = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    
    print(f"Buscando cotação de {moeda} em relação ao BRL...")

    try:
        # 3. Fazer a requisição HTTP GET
        response = requests.get(API_URL, timeout=10) # Timeout para evitar espera infinita

        # 4. Verificar o Status da Resposta HTTP
        if response.status_code == 200:
            dados = response.json()
            
            # 5. Verificar erro interno da API (Moeda inexistente)
            # A Awesome API retorna um dicionário vazio {} para moedas inexistentes
            if not dados:
                print(f"\n❌ Falha: A moeda '{moeda_input}' ou o par '{moeda}-BRL' não foi encontrado na base de dados da API.")
                return

            # A chave da cotação é dinâmica (ex: 'USDBRL')
            chave_moeda = list(dados.keys())[0]
            cotacao = dados[chave_moeda]
            
            # 6. Extrair e Exibir as informações
            
            # Converte o timestamp Unix para data e hora legíveis
            timestamp_unix = int(cotacao.get('timestamp', 0))
            data_atualizacao = datetime.datetime.fromtimestamp(timestamp_unix).strftime('%d/%m/%Y %H:%M:%S')

            print("\n--- Cotação da Moeda ---")
            print(f"Par de Moedas: {cotacao.get('codein', 'N/A')}")
            print(f"💰 Valor Atual (Compra - bid): R$ {float(cotacao.get('bid', 0)):.4f}")
            print(f"🔼 Valor Máximo (High):       R$ {float(cotacao.get('high', 0)):.4f}")
            print(f"🔽 Valor Mínimo (Low):        R$ {float(cotacao.get('low', 0)):.4f}")
            print(f"🕒 Última Atualização:        {data_atualizacao}")
            print("--------------------------\n")
            
        else:
            # Lida com erros HTTP genéricos (ex: 404, 500)
            print(f"\n❌ Falha na requisição. A API retornou o código de status: {response.status_code}.")

    # 7. Lida com Erros de Conexão
    except requests.exceptions.RequestException:
        print("\n❌ ERRO DE CONEXÃO!")
        print("Não foi possível conectar à API. Verifique sua conexão com a internet ou o status do serviço.")

# --- Execução do Programa ---
if __name__ == "__main__":
    consultar_cotacao()