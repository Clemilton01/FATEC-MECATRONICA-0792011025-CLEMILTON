temperaturas = []

quantidade = int(input("quantidade de temperaturas:"))
while len(temperaturas) < quantidade:
  temperatura= float(input("valor:"))
  temperaturas.append(temperatura)

media = sum(temperaturas) / len(temperaturas)
temp_acima_da_media  = []
for temperatura in temperaturas :
  if temperatura > media :
    temp_acima_da_media.append(temperatura)

maior = max(temperaturas)
menor = min(temperaturas)

print('temperaturas informadas:', temperaturas)
print("temperatura media:", media)
print('temperaturas acima da media:', temp_acima_da_media)
print('maior temperatura:', maior)
print("menor temperatura:", menor)
temperaturas.sort()
print('temperaturas em ordem:', temperaturas)
