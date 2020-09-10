#lista vazia com as temperaturas
temperaturas= [23, 5, -6, 34]
temperaturas=[]

print(temperaturas)

#pede para o usuario digitar 5 temperaturas
contador = 0
while contador < 5:
  temperatura= float(input("informe uma temperatura: "))
  temperaturas.append(temperatura)
  print(temperaturas)
  contador += 1
maior = max(temperaturas)
print("maior valor é: ",maior)
menor = min(temperaturas)
print("menor valor é:", menor)

#calcular valor media pela soma e contagem de elementos
media= sum(temperaturas)/ len(temperaturas)
print("temperatura média: %.2f" % (media)

#colooca a lista em ordem
temperaturas.sort()
print("ordenação crescente")
print(temperaturas)

#ordenação decrescente
temperaturas.sort(reverse=True)
print("ordenasção decrescente")
print(temperaturas)
