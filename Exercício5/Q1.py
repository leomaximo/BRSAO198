'''
1 - Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de
gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
Parâmetros:
a - valor_conta (float): O valor total da conta
b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
c - retorna: float: O valor da gorjeta calculada
'''


conta = float(input("Digite o valor da conta:  "))
percgort = float(input("Digite a porcentagem da gorjeta:  "))
print("O valor da gorjeta vai ser de ", conta * (percgort/100))
