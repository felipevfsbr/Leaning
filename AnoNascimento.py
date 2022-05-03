#Author: Neris
from datetime import date
idade=input('qual sua data de nascimento? (ano-mes-dia)')
resultado= 2022-int(idade)
data=date.today()
date=data.strftime("%d/%m/%Y")
print ('O ano que voce nasceu:') 
print (resultado)
print (date)
