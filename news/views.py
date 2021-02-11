from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

#get the source news website for scraping
onion_r=requests.get("https://theonion.com")

#get all the content from the html page using BeautifulSoup
onion_soup=BeautifulSoup(onion_r.content,'html5lib')

#from the parsed content, get all h4 
onion_headings=onion_soup.find_all('h4')

onion_news=[]

#append the fetched news text in onion_news 
for news in onion_headings:
    onion_news.append(news.text)

def index(req):
    return render(req, 'index.html',{'onion_news':onion_news})