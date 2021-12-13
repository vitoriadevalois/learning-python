"""
Criar variáveis para nome (str), idade (int), altura (float) e peso (float) de uma pessoa
Criar variável com o ano atual (int)
Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
Obter o IMC da pessoa com 2 casas decimais (peso e altura da peso)
Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""

nome = 'Vitória'
idade = 18
altura = 1.73
peso = 57.4
ano_atual = 2021
ano_nasc = ano_atual - idade
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos, possui {altura} de altura, seu peso é de {peso}, o seu ano de nascimento é {ano_nasc} e seu IMC é de {imc:.2f}')