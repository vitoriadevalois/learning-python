"""
VARIÁVEIS:
Iniciam com letra, podem conter números, separar _, letras minúsculas.
"""

nome = 'Vitória'
idade = 18 # int
altura = 1.75 #float
e_maior = idade >= 18 #bool
peso = 57
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos e seu imc é ', imc)