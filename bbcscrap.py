import requests
from bs4 import BeautifulSoup


data = requests.get('https://www.afro.who.int/health-topics/coronavirus-covid-19')
view = data.content

soup = BeautifulSoup(view,"html.parser")

links = []

for link in soup.find_all('a'): 
    links.append(link.get('href'))
    print(links)




# soup = BeautifulSoup(view,"html.parser")
# print(soup.prettify())

# africa = requests.get('https://www.africanews.com/2020/05/04/coronavirus-in-africa-breakdown-of-infected-virus-free-countries/')
# a_view = africa.content
