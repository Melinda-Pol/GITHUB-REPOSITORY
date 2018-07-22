# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 21:09:14 2018

@author: Usuario
"""
#LIMPIEZA DE DATOS PY
#EJEMPLO BASE.Cargar texto
nombrearchivo= 'metamorphosis_clean.txt'
archivo= open(nombrearchivo, 'rt')
texto = archivo.read()
archivo.close()
#Ejemplo 1. Separación de palabras con un espacio
#Ojo!, aquí no separa si no están con espacio, ejemplo si va separado con un guión, no hace la diferencia y lo cuenta solamente con una palabra.
palabras = texto.split()
print(palabras[126:226:1])

#Ejemplo ALPHANUMÉRICO:Volver a subir texto pero seleccionando un alphanumérico
#Separa todo. Oj: Los apóstrofes no los diferencia y lo separa de la propia palabra.
import re
palabras = re.split(r'\W+', texto)
print(palabras[125:225:1])

#Truco: Para saber el listado de caracteres que podemos separar
import string
print(string.punctuation)
#Ejemplo 3.Subimos el texto, lo dividimos por espacios y lo traducimos para evitar los signos de puntuación
nombrearchivo= 'metamorphosis_clean.txt'
archivo= open(nombrearchivo, 'rt')
texto = archivo.read()
archivo.close()
palabras = texto.split()
import string
tabla = str.maketrans('','',string.punctuation)
stripped = [p.translate(tabla) for p in palabras]
print(stripped[126:226:1])

#Ejemplo4. NORMALIZAR.Convertir todo en minúsculas
nombrearchivo= 'metamorphosis_clean.txt'
archivo= open(nombrearchivo, 'rt')
texto = archivo.read()
archivo.close()
palabras = texto.split()
palabras = [palabra.lower() for palabra in palabras]
print(palabras[126:226:1])

#Instalar NLTK y utilizando el paquete que más nos guste

import nltk
nltk.download()

filename = 'metamorphosis_clean.txt'
file= open(filename, 'rt')
text = file.read()
file.close()
#separar en frases
from nltk import sent_tokenize
sentences= sent_tokenize(text)
print(sentences[0])

#Separador de palabras: Word_tokenize nos deja dividir en tokes (palabras nominales)
#Lo identizican por los espacios y los signos de puntuación. 
#Esta me sirve para separar text, pero cuidado separa todos los signos de puntuación, tendría que diferenciar.
filename = 'metamorphosis_clean.txt'
file= open(filename, 'rt')
text = file.read()
file.close()
#separar en palabras
from nltk.tokenize import word_tokenize
tokens= word_tokenize(text)
print(tokens[:100]) 
#FILTROS DE PUNTUACIÓN
#1.isalpha función para filtar
filename = 'metamorphosis_clean.txt'
file= open(filename, 'rt')
text = file.read()
file.close()
#separar en palabras
from nltk.tokenize import word_tokenize
tokens= word_tokenize(text)
#quitar todas las palabras que no son alpfabéticas
words=[word for word in tokens if word.isalpha()]
print (words[:550])
#2.Filtros STOP WORDS: Se tratan de palabras que no añaden significado a la frase por ejemplo "a","the", "is" etc
#Se pueden seleccionar en diferentes lenguas.
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
print (stop_words)
#tupla sirve para eliminar duplicados
stop_wordst=tuple(stop_words)
#Ejemplo completo
filename = 'metamorphosis_clean.txt'
file = open(filename,'rt')
text=file.read()
file.close()
#separamos
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)
#convierto en minúsculas
tokens=[w.lower() for w in tokens]
#quitamos las puntuaciones de cada palabra
import string
table = str.maketrans('','',string.punctuation)
stripped= [w.translate(table) for w in tokens]
#quitamos los que no sean alpfabéticos
words = [word for word in stripped if word.isalpha()]
#filtramos las palabras que no aportan significado
from nltk.corpus import stopwords
stop_words= set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]
print(words[:300])
#Reducir las palabras a su raíz con PORTERSTEMMER
#Cargamos la data
filename='metamorphosis_clean.txt'
file = open(filename, 'rt')
text= file.read()
file.close()
#dividir las palabras
from nltk.tokenize import word_tokenize
tokens= word_tokenize(text)
#stemming of words
from nltk.stem.porter import PorterStemmer
porter= PorterStemmer()
stemmed=[porter.stem(word)for word in tokens]
print(stemmed[:100])



