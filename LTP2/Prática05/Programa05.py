#Criar um log de temperaturas
#Ler N Temperatura
#Calcular a temperatura media
#Encontrar todas as instalações acima da mídia
#Encontrar a maior temperatura
#Encontrar a menor temperatura
temperatura  = []

quantidade  =  int ( input ( 'Quantidade:' ))

enquanto  len ( temperaturas ) <  quantidade :
  temperatura  =  flutuante ( entrada ( 'Informe temp .:' ))
  temperaturas . anexar ( temperatura )

#Cálcula o valor da temperatura média
media  =  sum ( temperatura ) /  len ( temperatura )
#Cria uma lista vazia para guardar as atualizações acima da mídia
temp_acima_da_media  = []
para  temperatura  em  temperatura :
  se  temperatura  >  mídia :
    temp_acima_da_media . anexar ( temperatura )

maior  =  max ( temperatura )
menor  =  min ( temperatura )

imprimir ( 'Temperaturas Informadas:' )
imprimir ( temperaturas )
imprimir ( 'Temp. Media:' , media )
print ( 'Temps acima da media:' , temp_acima_da_media )
print ( 'Temp. Maxima:' , maior )
imprimir ( 'Temp. Minima:' , menor )
