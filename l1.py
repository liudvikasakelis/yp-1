#!/usr/bin/python3

from lxml import html
import requests

def scraper(url):    
    results = [None] * 9
    results[0] = url 
    try:
        page = requests.get(url)
    except requests.exceptions.ConnectionError:
        return 0
        
    tree = html.fromstring(page.content)
    
    try:
        results[1] = tree.xpath('//div[@class="sales-info"]/h1/text()')[0] # business name
    except IndexError:
        results[1] = 'not found'
    
    try:
        results[2] = tree.xpath('//p[@class="phone"]/text()')[0]
    except IndexError:
        results[2] = 'not found'
        
    try:
        results[3] = ';'.join(tree.xpath('//dd[@class="categories"]/span/a/text()')) # categories
    except IndexError:
        results[3] = 'none found'    
    
    try:
        results[4] = tree.xpath('//p[@class="address"]/span/text()')[0] # street address
    except IndexError:
        results[4] = 'not found'
    
    try:
        results[5] = tree.xpath('//p[@class="address"]/span/text()')[1] # city
    except IndexError:
        results[5] = 'not found'
        
    try:
        results[6] = tree.xpath('//p[@class="address"]/span/text()')[3] # zip code
    except IndexError:
        results[6] = 'not found'
    
    try:
        results[7] = tree.xpath('//p[@class="address"]/span/text()')[2] # state
    except IndexError:
        results[7] = 'not found'
    
    try:
        results[8] = tree.xpath('//a[@class="secondary-btn website-link"]/@href')[0] # website
    except IndexError:
        results[8] = 'not found'
        
    for i in range(len(results)):
        results[i] = results[i].replace(',', '')
    
    return(results)

def q_scraper(url):
    results = []
    page = requests.get(url)
    tree = html.fromstring(page.content)
    for i in tree.xpath('//div[@class="search-results organic"]//a[@class="business-name"]/@href'):
        if i[0] == '/':
            results.append(i)
    return results
        