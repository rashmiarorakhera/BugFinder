#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup as bs
import csv

def findFiles(link,cassandra):
    url = 'https://github.com'+link
    page = requests.get(url)
    soup = bs(page.content,'html.parser')
    results = soup.find(id='files')
    data = results.find_all('a')
    print('\n\n Here is the files for (' +str(cassandra)+')\n\n')
    print('link: '+url+'\n\n')
    for d in data:
        result = d.text.strip()
        if '.java' in result:
            print('- ',result)
            print()
 
if __name__ == '__main__':
    my_csv_file = 'data.csv'
    with open(my_csv_file) as f:
        reader = csv.reader(f)
        cassandra_code = tuple([int(code[0]) for code in reader])
    tuple_length = len(cassandra_code)

    while tuple_length:
        url1 = 'https://github.com/apache/CASSANDRA/search?q='
        cassandra = cassandra_code[tuple_length-1]
        url = url1+str(cassandra)+'&type=commits'
        page = requests.get(url)
        soup = bs(page.content,'html.parser')
        try:
            results = soup.find(id='commit_search_results')
            data = results.find('a',class_='sha')
            if data is  None:
                print('No commit')
            else:
                link = data['href']
                findFiles(link,cassandra)
        except Exception as e:
            print('No commit')
        tuple_length -= 1
            
    

