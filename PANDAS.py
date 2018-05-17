#Importar la libreria pandas
import numpy as np
import pandas as pd
#Tipos de arrays
#Datos, índices y tipos
a= pd.Series ([1,2,3,4,5], index=['a','b','c','d','e'], dtype="int16")
print (a)
#Si no pasas el tipo de índice, por defecto lo hace de 1 en 1
b = pd.Series ([1,2,3,4,5])
print (b) 
#diccionario-Si se pasa el índice, los valores del diccionario son asociados a los índices
c= {'Melanie': 29., 'Melinda': 25., 'Macarena': 20., 'Mirella': 18.}
#Hay que convertirlo en lista para que se pueda "jugar" con ella
listanombres = list(c.values())
print (listanombres)
#indexar
c1= {'Melanie': 29., 'Melinda': 25., 'Macarena': 20., 'Mirella': 18.}
#crear una serie a partir de un diccionario
posicion= pd.Series(c1, index=['Mirella','Melanie','Macarena','Melinda'])
print (posicion)




