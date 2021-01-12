from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import requests
import os
#from pymongo import MongoClient

def DoSearch():
    search = input("Please enter term you wanna search:")
    params={"q" : search}
    dir_name=search.replace(" ","_").lower()
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)

    r= requests.get("https://divar.ir/s/tehran",params=params)

    soup= BeautifulSoup(r.text,"html.parser")
    #print(soup.prettify())
    results= soup.find("div",{"class" : "browse-post-list"})
    links = results.findAll("a",{"class" : "col-xs-12 col-sm-6 col-xl-4 p-tb-large p-lr-gutter post-card"})

    #print(links)

    for item in results :
        try:
            item_name = item.find("div",{"class" : "subtitle-16 post-card__title"}).text
            item_price= item.find("div",{"class" : "body-12 post-card__description"}).text
            img_obj = requests.get(item.find("img",{"class": "post-card__image"}).attrs["src"])
            print("getting image",item.find("img",{"class": "post-card__image"}).attrs["src"])
            title = item.find("img",{"class": "post-card__image"}).attrs["src"].split("/")[-1]
            img=Image.open(BytesIO(img_obj.content))
            img.save("./"+dir_name+"/"+title, img.format)
        #item_link = item.find("href")
       # print(item)
            print(item_name)
            print(item_price)
            #client = MongoClient()
            #db = client.amin
            #itm = db.items

            #itm.insert({"Search_Name":search,"Item_name" : item_name,"Item_Price" :item_price,"Image_Title": title,"Folder_path":"./"+dir_name})
        except:
             print("An exception occurred")

    DoSearch()

DoSearch()






