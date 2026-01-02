# What is Web Scrapping
# The internet is full of huge amount fo data which can be used do different purposes
# To collect this data we need to know how to scrape data from a website
# web scrapping is the process of extraction and collecting data from websites and storing it on local machine or in a database
# In this section, we wil use beatifulsoup and requests package to scrape data
# the package version we are using is beatifulsoup 4

# to scrape data grom websites, basic undersating of HTML tags and CSS selectors is needed
# We targets content from a website using HTML tags, classes or/and ids
import requests
from bs4 import BeautifulSoup

# Let us declare url variable for the website which we are going to scrape
url = 'https://books.toscrape.com/'

# Let use the requests get method to fetch the data from url
response = requests.get(url)
status = response.status_code
print(status)

# Using beatifulSoup to parse content from the page
content = response.content # we get all the content from the website (cru)
soup = BeautifulSoup(content, 'html.parser') # beatiful soup will give a chance to parse (analisar)
print(soup.title) # <title> All products | Books to Scrape - Sandbox </title>
print('Apenas do titulo:', soup.title.get_text())
print('Nos da a página inteira', soup.body)

# tables = soup.find_all('stock', {'cellpadding':'3'})
## We are targeting the table with cellpadding attribute with the value of 3
## We can select using id, class or HTML tag
# table = tables[0] # the result is a list, we are taking out data from it
# for td in table.find('tr').find_all('td'):
    # print(td.text)
