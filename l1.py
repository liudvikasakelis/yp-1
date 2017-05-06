#!/usr/bin/python3

from lxml import html
import requests


def scraper(url):
    results = [None] * 12
    results[0] = sys.argv[1]  # URL
    page = requests.get(results[0])
    tree = html.fromstring(page.content)
    
    try:
        results[1] = tree.xpath('//div[@class="sales-info"]/h1/text()')[0] # business name
    except IndexError:
        results[1] = 'not found'
    
    try:
        results[2] = tree.xpath('//p[@class="address"]/span/text()')[0:3] # address
    except IndexError:
        results[1] = 'not found'
        
    return(results)
    
