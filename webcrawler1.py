# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 21:32:59 2015

WARNING: you may be illegal to crawl a webpage.
Use this code at your own risks.

@author: Neo
"""

#import urllib2
from bs4 import BeautifulSoup
import requests

def findAllRestaurantInfo(url):
    r = requests.get(url)
    
    ## if you want to messy stuffs, uncomment the below line
    #print r.content
    
    soup = BeautifulSoup(r.content)
    ## if you want to messy stuffs, uncomment the below line
    #print soup.prettify()
    
    ## find all the links
    #print soup.find_all("a") # in a list
    #for link in soup.find_all("a"):         
    #    try:
    #        print link.text, link.get("href")
    #    except:
    #        pass
    #    ## if you want to print it in the orignal way as in HTML
    #       #print "<a href='%s'>%s</a>" %(link.get("href"), link.text)
          
          
    g_data = soup.find_all("div", {"class": "info"})
    print "------------------------------------------"
    for item in g_data:
        try:
            print item.contents[0].find_all("a", {"class": "business-name"})[0].text
        except:
            print "NO BUSINESS NAME"
        try:
            print item.contents[1].find_all("span", {"itemprop":"streetAddress"})[0].text
        except:
            print "NO ADDRESS INFO"
        try:
            print item.contents[1].find_all("span", {"itemprop":"addressLocality"})[0].text.strip(),
        except:
            print "NO LOCALITY INFO",
        try:
            print item.contents[1].find_all("span", {"itemprop":"addressRegion"})[0].text,
        except:
            print "NO REGION INFO",
        try:
            print item.contents[1].find_all("span", {"itemprop":"postalCode"})[0].text
        except:
            print "NO POSTALCODE INFO"
        try:
            print item.contents[1].find_all("div", {"itemprop":"telephone"})[0].text
        except:
            print "NO PHONE INFO"
            
        print "------------------------------------------"
    

url = ""

findAllRestaurantInfo(url)