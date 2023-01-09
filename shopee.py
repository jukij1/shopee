from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time
import streamlit as st

def create_driver():
    opsi = webdriver.ChromeOptions()
    opsi.add_argument('--headless')
    servis = Service('chromedriver.exe')
    driver = webdriver.Chrome(service=servis, options=opsi)
    return driver

def link_loop(jumlah,url):
    links= []
    for page in range(0,jumlah):
        web_link = url.format(page)
        links.append(web_link)
    return links

def analytics(driver,base_url,links):
    driver.set_window_size(1300,800)
    driver.get(links)
    rentang = 500
    for i in range(1,7):
        akhir = rentang * i 
        perintah = "window.scrollTo(0,"+str(akhir)+")"
        driver.execute_script(perintah)
        print("loading ke-"+str(i))
        time.sleep(1)
    time.sleep(5)
    driver.save_screenshot("home.png")
    content = driver.page_source
    driver.quit()
    data = BeautifulSoup(content,'html.parser')
    i = 1
    base_url = base_url
    list_nama,list_harga,list_link,list_terjual=[],[],[],[]
    for area in data.find_all('div',class_="col-xs-2-4 shopee-search-item-result__item"):
        print('proses data ke-'+str(i))
        nama = area.find('div',class_="ie3A+n bM+7UW Cve6sh").get_text()
        harga = area.find('span',class_="ZEgDH9").get_text()
        link = base_url + area.find('a')['href']
        terjual = area.find('div',class_="r6HknA uEPGHT")
        if terjual != None:
            terjual = terjual.get_text()
        list_nama.append(nama)
        list_harga.append(harga)
        list_link.append(link)
        list_terjual.append(terjual)
        i+=1
        print("------")
    df = pd.DataFrame({'Nama':list_nama,'Harga':list_harga,'Link':list_link,'Terjual':list_terjual})
    return df


st.image('Shopee_Logo.png',width=200)
st.title("SHOPEE DATA SCRAPER (REAL-TIME)") 
st.caption("Tahalu Indo")
st.warning("Only for Marketing Purpose !")
Website = "https://shopee.co.id"
product = st.text_input("Product: ")
jumlah_halaman = int(st.slider("Masukkan jumlah halaman yang akan di scrape: ",0,10))
url="https://shopee.co.id/search?keyword="+str(product)+"&page={}"

j = 0
l = link_loop(jumlah_halaman,url)

while j < jumlah_halaman:
    d = create_driver()
    df = analytics(d,Website,l[j])
    st.header(product+" page "+str(j+1))
    st.write(df)
    j+=1

