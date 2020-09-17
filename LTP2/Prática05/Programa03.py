numeros = []
quantidade =int(input('quantidade de valores que deseja informar: '))
while len(numeros)< (quantidade):
  numero = int(input('valor: '))
  numeros.append(numero)
  
print("valores informados:", numeros)
pares = []
impares = []
for numero in numeros:
  if numero % 2 == 0:
    pares.append(numero)
  else:
    impares.append(numero)

print('pares: ', pares)
print("impares:", impares)
