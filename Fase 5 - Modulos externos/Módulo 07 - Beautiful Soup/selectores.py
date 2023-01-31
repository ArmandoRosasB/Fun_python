import requests
from bs4 import BeautifulSoup
import re

req = requests.get("https://es.wikipedia.org/wiki/Python").text

soup = BeautifulSoup(req, features="html.parser")

# Obtenemos el titulo de la pagina
title = soup.select("title")[0].getText()
print(title, '\n')

# Obtener el primer parrafo de la pagina

resumen = soup.select("p")[0].getText()
print(resumen, '\n')

# Obtener el indice
# tag con id = 'toc'

toc = soup.select("#toc")[0]

for a in toc.select("a"):
    print(a.getText())

print()
# Extraer solo enlaces de primer nivel

for a in toc.select("a"):
    text = a.getText()
    if re.match(r"\d+ ", text): # Al menos un numero y despues un espacio
        print(text)

# Formatear segundo y tercer nivel

for a in toc.select("a"):
    text = a.getText()
    if re.match(r'\d+ ', text):
        print(text)
    elif re.match(r'\d+.\d+ ', text):
        print(" ", text)
    elif re.match(r'\d+.\d+.\d+ ', text):
        print("     ", text)
    
print()

# Extraer la caja de informacion
# class: infobox

tr_tags = soup.select(".infobox tr") # Extraemos la tr de la tabal con la clase infobox

for tr_tag in tr_tags:
    print(tr_tag.getText())

print()
# Mejora a la implementacion

for tr_tag in tr_tags:
    th_tags = tr_tag.select("th")
    td_tags = tr_tag.select("td")

    if len(th_tags) > 0 and len(td_tags) > 0:
        print(f"{th_tags[0].getText().strip()}: {td_tags[0].getText().strip()}")

# Extraer el logo de python
print()

imagen = soup.select(".infobox img")[0]
src = imagen['src']

print(imagen)

print()

print(src)

# Para guardar la imagen

response = requests.get(f"https:{src}")

if response.status_code == 200: # Si hacemos la peticion y descargamos el contenido
    with open("Python_logo.png", 'wb') as f:
        f.write(response.content)



