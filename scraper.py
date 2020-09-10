# beautiful soup
from bs4 import BeautifulSoup
import requests as req
from time import perf_counter

t1=perf_counter()

url="https://www.blockchain.com/btc/address/1CVkuxTHDozNTg46An1FbvJnC2WXwivvFi"

page=req.get(url)


soup = BeautifulSoup(page.content, 'html.parser')

a=soup.find('span',class_="sc-1ryi78w-0 gCzMgE sc-16b9dsl-1 kUAhZx u3ufsr-0 fGQJzg")

print(a)

# for i in a.find_all('span',class_='grey'):
#     print(float(i.contents[0]))
#     break


t2=perf_counter()


print("{0} time elaspsed".format(str(t2-t1)))
# print(a)
