from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.worldometers.info/coronavirus/').text

soup = BeautifulSoup(source,'lxml')

table = soup.find('table',id="main_table_countries_today")

table_header = table.find('thead').find_all('th')


with open('results.csv','w',newline='') as f:

    writer = csv.writer(f)

    header = []
    new_list = []

    for th in table_header:
        header.append(th.text)

    for element in header:
        new_list.append(element.strip())

    # remove \xa0 from the word
    new_list[8] = new_list[8].replace(u'\xa0', ' ')

    # remove \n from the word
    new_list[11] = new_list[11].replace('\n',' ')

    writer.writerow(new_list)

    for row in table.find_all('tr'):
        csvRow = []
        for data in row.find_all('td'):
            csvRow.append(data.text)
        
        for i in range(len(csvRow)):
            csvRow[i] = csvRow[i].replace('\n','')

        writer.writerow(csvRow)

f.close()