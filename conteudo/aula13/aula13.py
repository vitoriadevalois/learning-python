"""
Quantidade de caracteres - LEN
"""
usuario = input('Digite seu usuário: ')
senha = input('Digite sua senha: ')
qtd_caracteres = len(senha)

if qtd_caracteres < 8:
  print('Você precisa digitar pelo menos 8 caracteres.')
else:
  print('Cadastro efetuado com sucesso.')
