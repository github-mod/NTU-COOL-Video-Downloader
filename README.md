# NTU COOL 影片下載器
# NTU COOL Video Downloader
---------------------------------------------------------------


### 簡介 Introduction
嗨，這是一個用來下載[NTU COOL](https://cool.ntu.edu.tw)上課程資料的實驗性工具。
我使用[python3](https://python.org)進行開發，並使用[BeautifulSoup](https://code.launchpad.net/beautifulsoup/)和[Selenium](https://www.selenium.dev/)套件及WebDriver進行網頁互動。
其使用到的Chrome 是Version 91。

Hi, this is an experimental project intended to help download the course contents on [NTU COOL](https://cool.ntu.edu.tw).
It was completely developed using [python3](https://python.org), while packages such as [BeautifulSoup](https://code.launchpad.net/beautifulsoup/),  [Selenium](https://www.selenium.dev/) and WebDriver are also used.
Chrome used in this project is of version 91.

### 責任聲明 Legal Notice
請注意，NTU COOL 上之內容仍受中華民國司法管轄，**擅自散布、再製及其他不法行為可能使行為人受偵訊甚至被逮捕**。
本程式之開發本於學習及交流，並不鼓勵任何人從事任何不法行為。

若須使用本程式或對其進行優化(下述可能的改進方向)，無須經過我的同意，但可以的話可以聯絡[我](https://github.com/github-mod)讓我知道一聲，謝謝。

Please be reminded that contents on and the website itself, NTU COOL, are under the jurisdiction of the Republic of China.
Illegal distribution or reproduce may lead to arrest. The entire development of this project does not encourage illicit activities but serves for the purpose of learning solely.

Should you intend to use this project or optimize it, my consent is not needed, however, I would like to know your usage if possible, thank you.

### 程式說明 Code Breakdown

本程式分為三個步驟：
1. `get_title_links.py` 將讀到的課程網頁原始碼進行整理，得到影片標題及影片(播放)連結。
2. `get_video_links.py` 將影片(播放)連結中的影片資源連結爬出。
3. `download_videos.py` 將整理好的影片資源連結下載至電腦。

The project is broken down into three steps:
1. `get_title_links.py` Cleanse the source of the course page, and getting the titles for the videos and video (playbak) links.
2. `get_video_links.py` Crawl the links of the media resources.
3. `download_videos.py` Download the sorted resources to local computer.


### 可能的改進方向 Possible Improvments

1. 影片下載時預設為720p。可透過點按畫質設定的方式取得更高畫質之連結。
2. 目前只能對影片連結進行互動，未來或可加入其他種類資源連結之爬取。


1. The default quality of the videos are 720p. It could be changed by clicking quality settings on the webpage, but was not included in this version of the project.
2. Currently only videos are available for dowload. We look forward to adding other type of resources to this project.
