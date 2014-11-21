# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 13:56:22 2014
Terminated on Wed Sep 24 02:58:00 2014
@author: ASSI Maixent Gemeri
"""

url='http://business.abidjan.net/PJ/'
from lxml import html
import requests
page = requests.get('http://business.abidjan.net/PJ/')
tree = html.fromstring(page.text)
content1=tree.xpath('//div[@id="module"]//a/text()')
link1=tree.xpath('//div[@id="module"]//a/@href')
length1=len(link1)
for i in range(0,length1):
    page=requests.get(url+link1[i])
    tree = html.fromstring(page.text)
    content2=tree.xpath('//div[@id="module"]//a[@href]//b/text()')
    link2=tree.xpath('//div[@id="module"]//a/@href')
    length2=len(link2)
    for j in range(0,length2):
        page=requests.get(url+link2[j])
        tree = html.fromstring(page.text)
        content3=tree.xpath('//div[@id="module"]//a[@href]/text()')
        link3=tree.xpath('//div[@id="module"]//a[@href]/@href')
        length3=len(link3)
        for k in range(0,length3):
            page=requests.get(url+link3[k])
            tree = html.fromstring(page.text)
            nomEnt=str(tree.xpath('//div[@id="module"]/p/font/b/text()'))
            activEnt=str(tree.xpath('//div[@id="module"]/p[2]/text()'))
            adrGeoEnt=str(tree.xpath('//div[@id="module"]//table/tr[1]/td[2]//font/text()'))
            adrPosEnt=str(tree.xpath('//div[@id="module"]//table/tr[2]/td[2]//font/text()'))
            villeEnt=str(tree.xpath('//div[@id="module"]//table/tr[3]/td[2]//b/text()'))
            telEnt=str(tree.xpath('//div[@id="module"]//table/tr[4]/td[2]//font/text()'))
            faxEnt=str(tree.xpath('//div[@id="module"]//table/tr[5]/td[2]//font/text()'))
            emailEnt=str(tree.xpath('//div[@id="module"]//table/tr[6]/td[2]//a/text()'))
            sitewebEnt=str(tree.xpath('//div[@id="module"]//table/tr[7]/td[2]//a/text()'))
            anneeCreaEnt=str(tree.xpath('//div[@id="content_left"]/table//tr[1]/td[2]//font/text()'))
            regComEnt=str(tree.xpath('//div[@id="content_left"]/table//tr[2]/td[2]//font/text()'))
            
            print (url+link3[k])+'|'+ nomEnt+'|'+activEnt+'|'+adrGeoEnt+'|'+adrPosEnt+'|'+villeEnt+'|'+telEnt+'|'+faxEnt+'|'+emailEnt+'|'+sitewebEnt+'|'+anneeCreaEnt+'|'+regComEnt
