usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'vitoria'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
  print('Usuário logado com sucesso!')
else:
  print('Usuário ou senha incorretos.')