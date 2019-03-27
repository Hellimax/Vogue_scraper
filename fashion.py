import requests
from bs4 import BeautifulSoup as bs
from PIL import Image
from io import BytesIO
import os
dirname = "Downloaded_Images"
try:
    os.mkdir(dirname)
    print("folder "+dirname+" created")
except FileExistsError:
    print("folder "+dirname+" already existed")
r = requests.get("https://www.vogue.com/fashion-shows/fall-2019-ready-to-wear")
soup = bs(r.text,"html.parser")
div = soup.find("div",{"class":"carousel--wrap"})
ancher = div.findAll("a")
for item in ancher:
    r = requests.get(item.attrs["href"])
    soup = bs(r.text,"html.parser")
    div = soup.find("div",{"class":"review-gallery-cta--single"})
    link = div.find("a")
    name = soup.find("span",{"class":"article-content--title"})
    count = soup.find("span",{"class":"gallery-marker--count"})
    print(count.text)
    path = dirname+"/"+name.text
    try:
        os.mkdir(path)
        print("folder "+name.text+" created")
    except FileExistsError:
        print("folder "+name.text+" already existed")
    f_link = "https://www.vogue.com"+link.attrs["href"]
    r2 = requests.get(f_link)
    soup2 = bs(r2.text,"html.parser")
    for i in range(0,20):
        fig = soup2.find("div",{"data-index":i})
        im = fig.find("img",{"class":"gallery--center-module--image"})
        obj = requests.get(im.attrs["srcset"])
        title = im.attrs["srcset"].split("/")[-1]
        imga = Image.open(BytesIO(obj.content))
        imga.save(dirname+"/"+name.text+"/" + title, imga.format)
