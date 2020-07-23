# -*- coding:utf8-*-

import re
import requests
import csv
import jieba
import wordcloud
import numpy as np
from PIL import Image


URL = 'https://api.bilibili.com/x/v1/dm/list.so?oid=186803402'

# request
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0'
}

resp = requests.get(URL, headers=headers)

html_doc = resp.content.decode('utf-8')

res = re.compile('<d.*?>(.*?)</d>')
danmu = re.findall(res, html_doc)
print(len(danmu))

for i in danmu:
    with open('./b站彈幕.csv', 'a', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        danmu = []
        danmu.append(i)
        writer.writerow(danmu)


f = open('./b站彈幕.csv', encoding='utf-8')
txt = f.read()
txt_list = jieba.lcut(txt)
print(txt_list)
string = " ".join(txt_list)
print(string)
background = np.array(Image.open('background.jpg'))

w = wordcloud.WordCloud(
    width=1000,
    height=700,
    mask=background,
    background_color='white',
    font_path='SourceHanMono-RegularIt.otf',
    scale=15,
    stopwords={' '},
    contour_width=5,
    contour_color='red',
)

w.generate(string)
w.to_file('./output.png')
