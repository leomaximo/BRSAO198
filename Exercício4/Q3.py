'''
3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
a - deve ter pelo menos 8 caracteres.
b - deve conter pelo menos um número.
'''

auxx = 0
auxxx = 0
senha = input("Digite a senha:   ")
while(auxx == 0 or auxxx == 0):    
    if len(senha) < 8:
        print("Sua senha é muito curta.")
        auxxx = 0
    else:
        auxxx = 1
    auxx = 0
    for aux in range(len(senha)):
        if senha[aux].isdigit():
            auxx = auxx + 1

    if auxx == 0:
        print("Sua senha não possui numeros.")     

    if(auxx == 0 or auxxx == 0):
        senha = input("Sua senha é inválida, digite outra senha:    ")
