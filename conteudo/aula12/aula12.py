"""
OPERADORES LÓGICOS

and, or, not
in e not in
"""

a = 2
b = 2
c = 3
nome = input('Qual seu nome? ')

print(a == b and b < c) # Só retorna verdadeiro, se ambas forem verdadeiras
print(a == b or b == c) # Retorna verdadeiro se uma ou outra for verdadeira

if not b > a:
  print('B é menor do que A.')
else:
  print('A é maior do que B')

if 'i' in nome:
  print('A letra i existe no seu nome')
else:
  print('A letra i não existe no seu nome')