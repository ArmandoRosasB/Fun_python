import requests
from bs4 import BeautifulSoup

req = requests.get("https://example.com")

soup = BeautifulSoup(req.text, features="html.parser") # Transformamos el texto en un objeto dinamico 

titles = soup.select('title') # Devuelve una lista con las etiquetas correspondientes
print("Etiquetas title:", titles)

title = titles[0].getText() # Extraemos el texto de dicha etiqueta
print("Texto de la primera etiqueta title:", title)

h1_s = soup.select('h1')
p_s = soup.select('p')

# Acceder a <a></a> dentro de p_s[1]
a = p_s[1].select('a')[0]
print("link a dentro de la etiqueta p:", a)


#Las etiquetas tienen valores especiales llamados atributos, como la dirección `href` de un enlace. 
#
#Estos se almacenan como un diccionario del objeto, es muy cómodo acceder a ellos:

direccion_a = a['href']

print("Direccion de a:",direccion_a)

# Acceder a todos los atributos de a

print("Diccionario de a:", a.attrs.items())


#Script que recupere todos los atributos de los metadatos de la pagina

print("Atributos de los metadatos")
for meta in soup.select('meta'):
    for atributo, valor in meta.attrs.items():
        print(f'{atributo}: {valor}')