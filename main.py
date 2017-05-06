#!/usr/bin/python3

import l1
import sys
import csv

q_url = sys.argv[1]
results = []

urls = l1.q_scraper(q_url)

for url in urls:
    if url[1:11] != 'nationwide':
        r = l1.scraper('https://www.yellowpages.com' + url) 
        if r:
            print(url)
        results.append(r)
        
with open('test.csv', 'w') as csvout:
    w = csv.writer(csvout, delimiter=',')
    for r in results:
        w.writerow(r)
        

    

