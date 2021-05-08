from bs4 import BeautifulSoup
import requests as req
from time import perf_counter
from time import sleep

def main(address):

    t1=perf_counter()

    url="https://www.blockchain.com/btc/address/"+address
    page=req.get(url)


    soup = BeautifulSoup(page.content, 'html.parser')

    a=soup.find_all('span',class_="sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC")  # span had changed 

    count=0
    for i in a:
        for j in i:
            count+=1
            if(count==6):
                # print(i.contents[0].split(" ")[0])

                print("balance is "+i.contents[0].split(" ")[0]+ " for "+address)
                if float(i.contents[0].split(" ")[0]):  #comment lines 26 and 27 if u dont want to stop if the balance of that particular address is greater than 0
                    input("continue ??") 
    t2=perf_counter()

    print("{0} time elaspsed".format(str(t2-t1)))
    # print(a)


with open("address.txt","r+") as r:
    count2=0
    for k in r.readlines():
        # print(k.strip().split(" ")[0])
        # break
        count2+=1
        main(k.strip().split(" ")[0])
        sleep(0.5) #timeout
        
        
        print("count :"+str(count2))
    
        
