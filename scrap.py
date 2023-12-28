import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
'Accept-Language': 'en-US, en;q=0.5'
}
base_url = f'https://www.ebay.com/b/Cell-Phones-Smartphones/9355/bn_320094'

item=[]
name=[]
price =[]
shipping_cost = []
sold_pieces=[]

for i in range(1,4):
    print(f'Processing {i}...'+ base_url + f'_pgn={i}')
    response = requests.get(base_url + '_pgn=2{0}'.format(i),headers=headers)
    soup = BeautifulSoup(response.content,'html.parser')

    n = soup.find_all('h3',attrs={'class':'s-item__title'})
    for item in n:
       name.append(item.text)
    sleep(1.5)

       
    p = soup.find_all('span',attrs={'class':'s-item__price'})
    for item in p:
       price.append(item.text)
    sleep(1.5)

    s = soup.find_all('span',attrs={'class':'s-item__shipping s-item__logisticsCost'})
    for item in s:
       shipping_cost.append(item.text)
    sleep(1.5)

    '''sp = soup.find_all('span',attrs={'class':'s-item__hotness s-item__itemHotness'})
    for item in sp:
       sold_pieces.append(item.text)
    sleep(1.5)'''

data_dict={'Item_name':name,
           'Price':price,
           'Shipping_cost':shipping_cost,
           }
#'Sold_Pieces':sold_pieces
print(data_dict)


df=pd.DataFrame(data_dict)
print(df)
df.to_excel(f'ebay.xlsx')