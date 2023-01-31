import csv
import os
import sys
from Scrape_functions.Scrape import *


class Citas:

    quotes = []

    if os.path.exists("quotes.csv"):
        with open ("quotes.csv", 'r') as file:
            data = csv.DictReader(file)
            for quote in data:
                #La lista es una cadena, hay que reevaluarla
                quote['tags'] = eval(quote['tags']) # Interpeta cadenas en crudo a codigo python
                quotes.append(quote)

    @staticmethod
    def scrapear():
        Citas.quotes = scrap_site(limit= sys.maxsize)

        # Guardamos las citas scrapeadas en un ficher CSV

        with open("quotes.csv", 'w') as file:
            writer = csv.DictWriter(file, fieldnames=['text', 'author', 'tags'])

            writer.writeheader()

            for quote in Citas.quotes:
                writer.writerow(quote)
    
    @staticmethod
    def listar(limite = 10):
        for quote in Citas.quotes[:limite]:
            print(quote['text'])
            print(quote['author'])

            for tag in quote['tags']:
                print(tag, end= " ")

        print('\n')
    
    @staticmethod
    def etiqueta(nombre = ""):
        for quote in Citas.quotes:
            if nombre in quote["tags"]:
                print(quote['text'])
                print(quote['author'])

                for tag in quote['tags']:
                    print(tag, end= " ")

                print('\n')
    
    @staticmethod
    def autor(nombre = ""):
        for quote in Citas.quotes:
            if nombre in quote["author"]:
                print(quote['text'])
                print(quote['author'])

                for tag in quote['tags']:
                    print(tag, end= " ")

                print('\n')
            