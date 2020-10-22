gastos = {"pessoal":0, 'trabalho':0, "outros":0, 'lazer':0}

continuar = True
while continuar == True:
  valor_do_gasto =float(input('infome um valor: '))
  categoria = input('informe uma categoria: ').lower()
  if categoria in gastos.keys():
    gastos[categoria] += valor_do_gasto
  else:
    gastos['outros'] = valor_do_gasto
  print('chaves:')
  print(gastos.keys())
  print('valores: ')
  print(gastos.values())
  continuar = input("Continuar?").lower() == 's'

#Passa por todas as categorias e exibe os gastos
for categoria in gastos.keys():
  print("Categoria:", categoria, "Valor:", gastos[categoria])
