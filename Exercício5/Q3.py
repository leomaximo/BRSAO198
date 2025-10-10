'''
3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
b - Preço final: Determina o novo preço após o desconto.
c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.

'''


prec = float(input("Digite o preço   "))
desc = float(input("Digite a porcentagem do desconto   "))
print("O valor final do produto é ", round((prec - ( prec * (desc/100))),2))