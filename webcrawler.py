# -*- coding: utf-8 -*-
"""
Created on Mon Nov 02 21:51:57 2015

WARNING: you may be illegal to crawl a webpage.
Use this code at your own risks.

@author: Neo
"""

import urllib
from bs4 import BeautifulSoup

url = raw_input("Enter your URL: ")
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve a list of the anchor tags
# Each tag is like a dictionary of HTML attributes
tags = soup('a')
for tag in tags:
    print tag.get('href', None)