from bs4 import BeautifulSoup

import requests
import csv  

source = requests.get('https://isap.sejm.gov.pl/isap.nsf/ByYear.xsp?type=WDU&year=2021').text
soup = BeautifulSoup(source, 'lxml')

#zapis do csv
csv_file = open('C:\\Users\\Wiktoria\\Desktop\\inżynierka\\dane_strona_2021.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['index_nazwa', 'tytul', 'link'])

for links in soup.find_all('a', class_='doc-details-link'):
    indeks_do_bazy = links.text
    adres = links['href'].split('?')[1]
    pelen_adres = f'https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?{adres}'
    kopia_do_pdf = adres.split('=')[1]

    new_source = requests.get(pelen_adres).text
    soup_link = BeautifulSoup(new_source, 'lxml')
    tytul = soup_link.find('h2').text
   #print(tytul)

    for pdf in soup_link.find_all('div', class_='row') : 
        for ten in pdf.find_all(class_='icon-after doc-link'):
        
            test = ten['href'].split('/')[4]
            if test == 'O':
                test = ten['href'].split('/')[5] 
                link_do_pdf = f'https://isap.sejm.gov.pl/isap.nsf/download.xsp/{kopia_do_pdf}/O/{test}'
              #  print(link_do_pdf)
              #  print(pelen_adres)
                csv_writer.writerow([indeks_do_bazy,  tytul, link_do_pdf])
    
    
  #  print(indeks_do_bazy)
csv_file.close()
