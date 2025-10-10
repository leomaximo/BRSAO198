'''

2 - Criar um código que registre as notas de alunos e calcular a média da turma.
'''
import numpy as np

qntd = int(input("digite a qunatidade de alunos"))
sala = []
aux = 0
for aux in range(qntd):
    nota = float(input("Digite a nota do aluno:   "))
    sala.append(nota)

print("A média da sala é ", np.mean(sala))
