from bs4 import BeautifulSoup
import requests as req
from time import perf_counter
from time import sleep

def main(address):

    try:
        t1=perf_counter()

        url="https://www.blockchain.com/btc/address/"+address
        page=req.get(url)


        soup = BeautifulSoup(page.content, 'html.parser')

        a=soup.find_all('span',class_="sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC")

        count=0
        for i in a:
            for j in i:
                count+=1
                if(count==6):
                # print(i.contents[0].split(" ")[0])
                    print("balance is "+i.contents[0].split(" ")[0]+ " for "+address)
                    if float(i.contents[0].split(" ")[0]):  # comment line 26 and 27 if u dont want to stop if balance is greater than 0 for an address
                        input("continue ??")
                    t2=perf_counter()

        print("{0} time elaspsed".format(str(t2-t1)))
    except KeyboardInterrupt:
        print("crtl + c pressed exiting")   #crtl + c stops script
        exit()


with open("address.txt","r+") as r:
    count2=0
    for k in r.readlines():
        # print(k.strip().split(" ")[0])
        # break
        count2+=1
        main(k.strip().split(" ")[0])
        sleep(0.5) #timeout
        
        
        print("count :"+str(count2))
    
        
