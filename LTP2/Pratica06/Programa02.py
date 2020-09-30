valores = []

quantidade = int(input("quantidade: "))
while len(valores) < quantidade:
  valor= float(input("valor:"))
  valores.append(valor)

media = sum(valores) / len(valores)
temp_acima_da_media  = []
for valor in valores :
  if valor > media :
    temp_acima_da_media.append(valor)

maior = max(valores)
menor = min(valores)

print('valores informados:', valores)
print(" media:", media)
print(' acima da media:', temp_acima_da_media)
print('maior valor :', maior)
print("menor valor :", menor)
valores.sort()
print('valores em ordem:', valores)
