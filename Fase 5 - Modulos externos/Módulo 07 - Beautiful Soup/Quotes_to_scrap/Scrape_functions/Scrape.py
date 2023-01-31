import requests
from bs4 import BeautifulSoup

def scrap_quotes(url = ""):
    domain = 'https://quotes.toscrape.com/'
    req = requests.get(f"{domain}{url}")

    soup = BeautifulSoup(req.text, features='html.parser')


    # Lista para almacenar diccionarios que contendran datos de las citas
    quotes = []

    quote_tags = soup.select("div.quote")

    for quote_tag in quote_tags:
        quote = {}

        # Almacenamso los diferentes campos en el diccionario
        quote['text'] = quote_tag.select("span.text")[0].getText()
        quote['author'] = quote_tag.select("small.author")[0].getText()
        quote['tags'] = []

        for tag in quote_tag.select("div.tags a.tag"):
            quote['tags'].append(tag.getText())

        # Agregamos al diccionario
        quotes.append(quote)

        # Buscamos el enlace en el tag li con clase next
        next_url = None
        link_tag = soup.select("li.next a")

        if len(link_tag) > 0:
            next_url = link_tag[0]['href']

    print(f"Pagina {domain}{url}, {len(quotes)} citas scrapeadas.")

    return quotes, next_url

def scrap_site(limit = 2):
    # Lista global para todas las citas
    all_quotes = []

    next_url = ""

    while True:
        quotes, next_url = scrap_quotes(next_url)
        all_quotes+= quotes

        limit -= 1

        if limit == 0 or next_url == None:
            return all_quotes


