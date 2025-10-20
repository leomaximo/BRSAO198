import random
import string

def gerar_senha(tamanho):
    letras = string.ascii_letters
    numeros = string.digits
    simbolos = string.punctuation
    todos_caracteres = letras + numeros + simbolos
    if tamanho < 3:
        print("O tamanho da senha deve ser no mínimo 3 para garantir pelo menos um caractere de cada tipo.")
        return None
    senha = []
    senha.append(random.choice(letras))
    senha.append(random.choice(numeros))
    senha.append(random.choice(simbolos))
    comprimento_restante = tamanho - 3
    for _ in range(comprimento_restante):
        senha.append(random.choice(todos_caracteres))
    random.shuffle(senha)
    return "".join(senha)
if __name__ == "__main__":
    while True:
        try:
            tamanho_senha = int(input("Digite o tamanho da senha desejada (ex: 12): "))
            
            if tamanho_senha > 0:
                senha_gerada = gerar_senha(tamanho_senha)
                if senha_gerada:
                    print("\n--- Senha Segura Gerada ---")
                    print(f"Tamanho: {tamanho_senha}")
                    print(f"Senha: {senha_gerada}")
                    print("---------------------------\n")
                    break
            else:
                print("Por favor, digite um número inteiro positivo.\n")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.\n")