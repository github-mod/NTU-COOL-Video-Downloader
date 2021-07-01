#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests


# load titles
path = 'C:\\Users\\user\\Desktop\\Crawler\\titles.txt'
fh_titles = open(path, 'r')
titles = []
for aline in fh_titles:
    titles.append(aline.strip('\n'))
fh_titles.close()

# load video_links
path = 'C:\\Users\\user\\Desktop\\Crawler\\video_links.txt'
fh_video_links = open(path, 'r')
videos = []
for aline in fh_video_links:
    videos.append(aline.strip('\n'))
fh_video_links.close()

# start download
result_path = 'C:\\Users\\user\\Desktop\\Crawler\\videos\\'

for video_index in range(len(videos)):

    print( "Downloading file:%s" % titles[video_index])

    r = requests.get(videos[video_index], stream = True)

    with open(result_path + titles[video_index] +".mp4",'wb') as f:
        for chunk in r.iter_content(chunk_size = 1024*1024):
                if chunk:
                    f.write(chunk)
        f.close()
    print( "'%s' successfully downloaded!\n"% titles[video_index] )
