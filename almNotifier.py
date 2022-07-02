import requests
from bs4 import BeautifulSoup
from datetime import datetime

# daily check website
# retrieve information
# check for timeslot september (start)
# when exists collect title, price, date and link for details
# optional: send notification

AIDA_LAST_MINUTE_URL = 'https://aida.de/kreuzfahrt/angebote/last-minute'
AIDA_BASE_URL = 'https://aida.de'

page = requests.get(AIDA_LAST_MINUTE_URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find_all('div', class_='cruise-teaser')

for i in results:
    range = i.find('div', class_='dates')
    tmp = range.text
    dates = tmp.split(' bis ')
    start = datetime.strptime('01.08.2022', '%d.%m.%Y')
    end = datetime.strptime('30.09.2022', '%d.%m.%Y')

    datetimeStart = datetime.strptime(dates[0], '%d.%m.%Y')
    datetimeEnd = datetime.strptime(dates[1], '%d.%m.%Y')

    accaptable = start <= datetimeStart and end >= datetimeEnd

    if accaptable:
        header = i.find('div', class_='moreInfo')
        name = i.find('p', class_='name')
        date = i.find('div', class_='dates')
        price = i.find('span', class_='price-label')
        link = i.find('a', class_='details')
        print(link)

        print(header.text, name.text, date.text,
              price.text, AIDA_BASE_URL + link['href'], sep=' - ')
