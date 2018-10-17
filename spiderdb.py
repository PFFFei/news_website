#coding:utf-8
import os
import django
from bs4 import BeautifulSoup
import requests

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")
django.setup()

def spider_Information():
    global new
    from tool.models import Information
    first = BeautifulSoup(str(new[0]),'html.parser')
    first_new = first.find_all('tr')
    for i in range(20):
        first_new_td = BeautifulSoup(str(first_new[i+1]),'html.parser')
        first_new_item = first_new_td.find_all('td')
        Information.objects.create(title=first_new_item[1].text,number=first_new_item[0].text,clicks=first_new_item[2].text,time=first_new_item[3].text)

def spider_Military():
    global new
    from tool.models import Military
    second = BeautifulSoup(str(new[1]),'html.parser')
    second_new = second.find_all('tr')
    for i in range(20):
        second_new_td = BeautifulSoup(str(second_new[i+1]),'html.parser')
        second_new_item = second_new_td.find_all('td')
        Military.objects.create(title=second_new_item[1].text,number=second_new_item[0].text,clicks=second_new_item[2].text,time=second_new_item[3].text)

def spider_Sports():
    global new
    from tool.models import Sports
    third = BeautifulSoup(str(new[2]),'html.parser')
    third_new = third.find_all('tr')
    for i in range(20):
        third_new_td = BeautifulSoup(str(third_new[i+1]),'html.parser')
        third_new_item = third_new_td.find_all('td')
        Sports.objects.create(title=third_new_item[1].text,number=third_new_item[0].text,clicks=third_new_item[2].text,time=third_new_item[3].text)

def spider_Entertainment():
    global new
    from tool.models import Entertainment
    forth = BeautifulSoup(str(new[3]),'html.parser')
    forth_new = forth.find_all('tr')
    for i in range(20):
        forth_new_td = BeautifulSoup(str(forth_new[i+1]),'html.parser')
        forth_new_item = forth_new_td.find_all('td')
        Entertainment.objects.create(title=forth_new_item[1].text,number=forth_new_item[0].text,clicks=forth_new_item[2].text,time=forth_new_item[3].text)

def spider_Finance():
    global new
    from tool.models import Finance
    fifth = BeautifulSoup(str(new[4]),'html.parser')
    fifth_new = fifth.find_all('tr')
    for i in range(20):
        fifth_new_td = BeautifulSoup(str(fifth_new[i+1]),'html.parser')
        fifth_new_item = fifth_new_td.find_all('td')
        Finance.objects.create(title=fifth_new_item[1].text,number=fifth_new_item[0].text,clicks=fifth_new_item[2].text,time=fifth_new_item[3].text)

if __name__ == "__main__":
    url = 'http://news.ifeng.com/hotnews/'
    req = requests.get(url)
    html = req.content.decode('utf-8')
    div_bf = BeautifulSoup(html,'html.parser')
    new = div_bf.find_all('div',class_='boxTab clearfix')
    spider_Information()
    print('Information Done!')
    spider_Military()
    print('Military Done!')
    spider_Sports()
    print('Sports Done!')
    spider_Entertainment()
    print('Entertainment Done!')
    spider_Finance()
    print('Finance Done!')
    print('All Done!')
