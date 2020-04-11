from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.worldometers.info/coronavirus/').text

soup = BeautifulSoup(source,'lxml')

table = soup.find('table',id="main_table_countries_today")

table_header = table.find('thead').find_all('th')


with open('results.csv','w') as f:

    writer = csv.writer(f)

    header = []

    for th in table_header:
        header.append(th.text)

    header.replace('\n')    

    print(header)


    for row in table.find_all('tr'):
        csvRow = []
        for data in row.find_all('td'):
            csvRow.append(data.text)
        writer.writerow(csvRow)

f.close()