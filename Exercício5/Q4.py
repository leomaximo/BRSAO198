   

from datetime import date
from datetime import datetime

def calcular_dias_de_vida():
    """
    Calcula a diferença em dias entre a data de nascimento e a data atual.
    """
    print("--- Calculadora de Dias de Vida ---")
    
    # 1. Obter a data de nascimento do usuário
    while True:
        data_nascimento_str = input("Digite sua data de nascimento (DD/MM/AAAA): ")
        try:
            # Tenta converter a string para um objeto date, usando o formato DD/MM/AAAA
            data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y").date()
            break
        except ValueError:
            print("Formato de data inválido. Use o formato DD/MM/AAAA.")
            
    # 2. Obter a data atual
    data_atual = date.today()
    
    # 3. Validação: A data de nascimento não pode ser no futuro
    if data_nascimento > data_atual:
        print("\nOps! Sua data de nascimento não pode ser no futuro. Tente novamente.")
        return

    # 4. Cálculo da Diferença
    # A subtração de dois objetos date resulta em um objeto timedelta
    diferenca = data_atual - data_nascimento
    
    # O atributo '.days' de timedelta retorna a diferença em dias
    dias_vividos = diferenca.days
    
    # 5. Saída do Resultado
    print("\n--- Resultado ---")
    print(f"Data de Nascimento: {data_nascimento.strftime('%d de %B de %Y')}")
    print(f"Data Atual: {data_atual.strftime('%d de %B de %Y')}")
    print("---------------------------------")
    print(f"Você está vivo há exatamente {dias_vividos:,} dias!")

# Execução da função principal
if __name__ == "__main__":
    calcular_dias_de_vida()