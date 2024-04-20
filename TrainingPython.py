import re
# txt = input("Enter text:")
import pywhatkit

# word =input("Enter Word:")
# pa=re.compile(r'\b'+re.escape(word)+r'\b',re.IGNORECASE)
# ms=pa.findall(pa,txt)
# for m in ms:
#     print(m)
#
#
# le = int(input("Enter No."))
# pa = r'\b\w{' + str(le) + r'}\b'
#
# pa = r'\b[A-Z][.?!]*[.?]'
#
# PA = r'\b'+prefix+r'\w*'+suffix+r'\b'

# import pywhatkit
# # pywhatkit.search("Python")
# pywhatkit.playonyt("Python")
# pywhatkit.image_to_ascii_art(r"b1.jpg",r"b1.txt")
# from gtts import gTTS
# obj=gTTS(text="How are you", lang="en", slow=False)
# obj.save("agg1.mp3")
# print("Done")

# import instaloader
# ig=instaloader.Instaloader()
# ig.download_profile("i_am_yeager",profile_pic_only=True)
# print("Done")

# import webbrowser
# webbrowser.open(input("Enter the website"))

# import requests
# # res=requests.get("https://en.wikipedia.org/wiki/Robots.txt").text
# res=requests.get("https://analytics.usa.gov/data/live/browsers.json")
# print(res.json()['totals']['browser'])
# print(res.json()['query']['dateRanges'][0]['startDate'])

from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup
# html=urlopen("https://wikipedia.org/")
# bs=BeautifulSoup(html,"html.parser")
# print(bs)
# nameList=bs.findAll('a',{'class':'link-box'})
# for name in nameList:
#     print(name.get_text())

# bs=BeautifulSoup(urlopen("https://pythonscraping.com/pages/page3.html"),"html.parser")
# imgs=bs.findAll('img',{'src':re.compile('.jpg')})
# for img in imgs:
#     print(img['src']+'\n')

# req = requests.get("https://buffer.com/library/social-media-sites/")
# facelinks=[fa for fa in req if 'https://facebook.com']
# for fa in facelinks:
#     print(fa)

# res =requests.get("https://www.python.org/")
# print("status",res.status_code)
# print("headers",res.headers)
# print("url",res.url)
# print("history",res.history)
# print("encoding",res.encoding)
# print("cookies",res.cookies)
# print("content",res._content)

# res =requests.get("https://www.python.org/")
# soup=BeautifulSoup(res.text,'html.parser')
# upcoming=soup.find('div',class_='shrubbery')
# events=upcoming.findAll('li')
# for event in events:
#     date=event.find('time').text.strip()
#     title=event.find('a').text.strip()
#     print(date+"-"+title)

# res =requests.get("https://www.python.org/psf/donations/")
# soup=BeautifulSoup(res.text,'html.parser')
# a_tags=soup.findAll('a')
# for tags in a_tags:
#     print(tags.text.strip())

# res =requests.get("https://makeawebsitehub.com/social-media-sites/")
# html_content=res.content
# soup=BeautifulSoup(html_content,'html.parser')
# comments=soup.findAll('div',class_='comment-content')
# names=soup.findAll('cite',class_='fn')
# ctexts=[c.get_text(strip=True) for c in comments]
# ntexts=[n.get_text(strip=True) for n in names]
# for na,co in zip(ntexts,ctexts):
#     pa=r'Reply$'
#     print("Name:", na)
#     print("Comment:", re.sub(pa,'',co))
#     print("="*30)


# res=requests.get("https://reqres.in/api/users?page=1")
# li=[]
# li=res.json()['data']
# for i in li:
#     if type(i) is dict:
#         for k,v in i.items():             #items function can handle key value
#             if k=='email':
#                 print(v)

from selenium import webdriver
from selenium.webdriver.common.by import By
# d=webdriver.Chrome()
# d.get('https://aggregateintelligence.com/products')
# heles=d.find_elements(By.TAG_NAME,'h2')
# for h in heles:
#     print("Header Text:", h.text)
# # html=d.page_source
# d.quit()
# soup=BeautifulSoup(html,'html.parser')
# title=soup.title
# print("Title", title)

# ieles=d.find_elements(By.TAG_NAME,"img")
# urls=[ele.get_attribute("src") for ele in ieles]
# for u in urls:
#     print(u)
# d.quit()

# d.get("https://www.google.com/")
# s=d.find_element("name","q")
# s.send_keys("OpenAI")
# s.submit()
# d.implicitly_wait(5)
# res=d.find_elements("css selector","h3")
# for r in res:
#     print(r.text)
# d.quit()

# num=[]
# print(dir(num))
#
# num= {"name":"aa"}
# print(dir(num))
#
# num=1,2
# print(dir(num))
#
# num= {"aa","bb","cc"}
# print(dir(num))
# print("Quot&Div", divmod(10,3))

import sqlite3
conn=sqlite3.connect('item.db')
cursor=conn.cursor()
cursor.execute("create table if not exists item(quantities integer primary key,names text)")
print("Done")

def create_item(quantities,names): # parameter
    try:
        cursor.execute("insert into item(quantities,names) values (?,?)", (quantities,names)) # insert records
        conn.commit() # save permenatly
        print("item Added")
    except sqlite3.IntegrityError:
        print("item already Exists")

def update_item(quantities,names): # parameter
    try:
        cursor.execute("update item set names = ? where quantities = ?", (names,quantities)) # update records
        conn.commit()
        print("item updated")
    except Exception as e:
        print("Error", e)

def readall_item():
    try:
        cursor.execute("select * from item")
        items=cursor.fetchall()
        if items:
            for item in items:
                print(" QTY:", item[0],"Item Name", item[1])
        else:
            print("No records found")
    except Exception as e:
        print("Error", e)

def delete_item(quantities):
    try:
        cursor.execute("delete from item where quantities=?",(quantities))
        items=cursor.fetchone()
        if items:
            print("Qty No:", items[0], "Item Name", items[1])
        else:
            print("No records found")
    except Exception as e:
        print("Error", e)

def display_menu():
    print("\na.Add new item to the inventory.")
    print("d.Display the current inventory.")
    print("b.Update quantity of an existing item.")
    print("c.Remove an item from the inventory.")
    print("e.Exit the program")

def user_choice():
    while True:
        choice=int(input("Enter Choice:"))
        if choice in ["a","b","c","d","e"]:
            return choice
        else:
            print("Invalid choice")

while True:
    display_menu()
    ch=user_choice()
    if ch== "a":
        quantities=int(input("Enter Qty: "))
        names=input("Enter Name : ")
        create_item(quantities,names) # arguments
    elif ch== "d":
        readall_item() # arguments
    elif ch == "b":
        quantities=int(input("Enter Qty: "))
        names=input("Enter Name : ")
        update_item(quantities,names)
    elif ch == "c":
        quantities = int(input("Enter quantities: "))
        delete_item(quantities)  # arguments
    elif ch == "e":
        print("Existing")
        break
    conn.close()