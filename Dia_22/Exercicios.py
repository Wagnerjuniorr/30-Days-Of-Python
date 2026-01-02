# Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').
import requests, json
from bs4 import BeautifulSoup
url  = 'https://www.bu.edu/president/boston-university-facts-stats/'
response  = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# lista vazia para criar os dados limpos
lista_of_fact_about_boston = []

# itera sobre as tags e extrai apenas o que vc quer
for h3 in soup.find_all('h3'):
    titulo = h3.get_text(strip= True) # extrai o texto e remove espaços extras
    # Criamos um dicionário simples( que Json aceita)
    lista_of_fact_about_boston.append({'nome':titulo})

# Dess jeito  n funciona pq json só aceita dict
# with open('./Dia_22/boston_university_content.json','w', encoding= 'utf=8') as f:
    # json.dump(soup.content, f, ensure_ascii=False, indent= 4)
with open('./Dia_22/boston_university_content.json','w', encoding= 'utf=8') as f:
    json.dump(lista_of_fact_about_boston, f, ensure_ascii=False, indent= 4)

# Extract the books in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file
url = 'https://books.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


list_of_books = []
for h3 in soup.find_all('h3'):
    titulo = h3.get_text(strip=True)
    list_of_books.append({'book':titulo})

with open('./Dia_22/List_of_books.json', 'w', encoding='utf=8') as f:
    json.dump(list_of_books, f, ensure_ascii=False, indent= 4)

# Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). The table is not very structured and the scrapping may take very long time.
# Alguns sites tem um sistema de segurança que bloqueia acessos automatizado que não se identificam
# para entrar necessário criar um dicionário chamado headers dentro da função get
# a wikipedia pede especificamente um nome para o projeito e se possível um email
url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
headers ={
    'User-Agent': 'MeuProjetoEscolar/1.0 (contato: wagner.juniorr669@gmail.com)'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

tabela = soup.find('table',{'class':'wikitable'})

data = []

# itera sobre as linhas pulando o cabeçalho
for linha in tabela.find_all('tr'):
    colunas = linha.find_all(['td', 'th'])
    
    if len(colunas) >= 5:
        try:
            # Pegamos o nome (geralmente na coluna 2 ou 3 dependendo da linha)
            # Na Wikipedia, o nome costuma estar dentro de um <b> ou um <a>
            nome = colunas[2].text.strip().split('[')[0]
            
            # Só adicionamos se o nome não for o cabeçalho "President"
            if nome != "President":
                data.append({
                    "nome": nome
                })
        except IndexError:
            # Se ainda assim der erro em uma linha específica, ele pula e continua
            continue
with open('./Dia_22/presidentes_USA.json','w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)