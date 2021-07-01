#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import packages
from bs4 import BeautifulSoup

# deal with original list of titles
path = 'C:\\Users\\user\\Desktop\\Crawler\\titles_html.txt'

fh = open(path, 'r', encoding="utf-8")
text = fh.read()
fh.close()

# use bs to cleanse
soup = BeautifulSoup(text, 'html.parser')
LinkElements = soup.find_all('a', class_="ig-title title item_link")

# get titles
titles = [e.text for e in LinkElements]
for i in range(len(titles)):
    titles[i] = titles[i].strip('\n')
    titles[i] = titles[i].strip(' ')
    titles[i] = titles[i].strip('\n')

# get links
links = [t['href'] for t in LinkElements]

# get rid of empty items at end
titles = titles[:-1]
links = links[:-1]

# save results as txts
result_path = 'C:\\Users\\user\\Desktop\\Crawler\\'

fh_titles = open(result_path+"titles.txt", 'w')
for title in titles:
        fh_titles.write(title)
        fh_titles.write('\n')
fh_titles.close()

fh_links = open(result_path+"links.txt", 'w')
print(result_path+"links.txt")
print()
for link in links:
    fh_links.write("https://cool.ntu.edu.tw/" + link)
    fh_links.write("\n")
fh_links.close()
