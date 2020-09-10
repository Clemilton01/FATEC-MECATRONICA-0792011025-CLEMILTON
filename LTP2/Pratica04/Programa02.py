#Cria uma lista vazia para os nomes
nomes = []


#Cria uma repeticao que pergunta se o usuario deseja continuar
continuar = True


while continuar == True:
  nome = input('Informe um nome:')
  #Coloca o nome no final da lista
  nomes.append(nome)
  #Exibe a parcial da lista com os nomes
  print(nomes)
  if input('Deseja continuar (s/n)?: ') == 's':
   continuar = True
  else:
   continuar = False

nomes = ['a', 'b', 'c', 'z', 'w', 'bb']
nomes.sort()
nome = input("quem voce deseja procurar")
if nome in nomes:
  print('encontrei na posiçao:', nomes.index(nome))
else:
  print('nao encontrado')
