#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import packages
import requests
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
import time


# load urls
path = 'C:\\Users\\user\\Desktop\\Crawler\\links.txt'
fh_links = open(path, 'r')
links = []
for aline in fh_links:
    links.append(aline.strip('\n'))
fh_links.close()

# load titles
path = 'C:\\Users\\user\\Desktop\\Crawler\\titles.txt'
fh_titles = open(path, 'r')
titles = []
for aline in fh_titles:
    titles.append(aline.strip('\n'))
fh_titles.close()

####webdriver

username = input("Please type in username:")
password = input("Please type in password:")

# driver setup
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get("https://cool.ntu.edu.tw/")
time.sleep(1.5)

# click and go to login
commit = driver.find_element_by_css_selector('#saml')
commit.click()
time.sleep(2)

# type in username
context = driver.find_element_by_css_selector('#ContentPlaceHolder1_UsernameTextBox')
context.send_keys(username)
time.sleep(0.3)

# type in password
context = driver.find_element_by_css_selector('#ContentPlaceHolder1_PasswordTextBox')
context.send_keys(password)
time.sleep(0.3)

# click login
commit = driver.find_element_by_css_selector("#ContentPlaceHolder1_SubmitButton")
commit.click()
time.sleep(2)

# start crawling
count = 0
video_links = []
for a_link in links:
    # go to the course pages
    driver.get(a_link)
    time.sleep(2)

    # change to iframe
    driver.switch_to.frame('tool_content')
    time.sleep(1)

    # get the elements
    video = driver.find_element_by_id('vjs_video_3_html5_api')
    src = video.get_attribute('src')
    video_links.append(src)
    print("Getting video:" + str(count))
    count+=1


# write the video links
result_path = 'C:\\Users\\user\\Desktop\\Crawler\\'
fh_video_links = open(result_path+"video_links.txt", 'w')
for a_link in video_links:
        fh_video_links.write(a_link)
        fh_video_links.write('\n')
fh_video_links.close()
