



import requests

from bs4 import BeautifulSoup
headers = {'user-agent': 'Mozilla/5.0'}

url = ('https://shopee.com.br/')

pagina = requests.get(url)

teste = BeautifulSoup(pagina.text, 'html.parser')


estoque = teste.find("div", class_="p-2 flex-1 flex flex-col justify-between")

print(estoque)






  
    
    
    