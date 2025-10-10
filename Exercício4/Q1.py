'''1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).'''

def soma(n1,n2):
    print(n1+n2)
    return 

def subtração(n1,n2):
    print(n1-n2)
    return

def mult(n1,n2):
    print(n1*n2)
    return

def div(n1,n2):
    print(n1/n2)
    return



aux = 1
while (aux): 
    n1 = float(input("Digite o primeiro numero: "))
    n2 = float(input("Digite o segundo numero: "))
    operacao = float(input("Se quer somar os numeros aperte 1 \nSe quer subtrair digite 2 \nSe quer multiplicar digite 3\nSe quer dividir digite 4 \n"))
    if (operacao == 1):
        soma(n1,n2)
    
    elif(operacao == 2):
        subtração(n1,n2)
        
    elif(operacao == 3):
        mult(n1,n2)
    
    elif(operacao == 4):
        div(n1,n2)
    
    else:
        print("Operação inválida")
    aux = float(input("Se quiser parar de usar a calculadora digite 0 se não aperte qualquer outro numero"))
