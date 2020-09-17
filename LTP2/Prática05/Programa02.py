numeros = []
quantidade =int(input('quantidade de valores que deseja informar: '))
while len(numeros)< (quantidade):
  numero = int(input('valor: '))
  numeros.append(numero)
  
print("valores informados:")
print(numeros)

for numero in numeros:
  if (numero > 0) and (numero % 2 == 0):
    print(numero)
