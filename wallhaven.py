# -*- coding:utf-8 -*-
"""
@author: momochong0
@software: PyCharm
@file: wallhaven.py
@time: 2023-03-30 21:34
@desc:
"""
# -*- coding:utf-8 -*-
from DrissionPage import WebPage
import os
from typing import List

least_stars = 600


# 创建页面对象
page = WebPage()
# # 控制浏览器访问百度
page.get('https://wallhaven.cc/search?'
         'categories=110&purity=110&topRange=6M'
         '&sorting=toplist&order=desc&page=2')  # 使用页面对象访问

thumbs_ele = page.ele('#thumbs')
href_eles = thumbs_ele.s_eles('tag:li')
# print(href_eles)

img_src_small: List[str] = []
img_src_full: List[str] = []
for href in href_eles:
    # judge stars
    if int(href.ele('xpath://figure/div/a').text) > least_stars:
        # get small src
        img_src_small.append(href.ele('tag:img').attr('data-src'))

print(img_src_small)
for img_src in img_src_small:
    img_src = img_src.replace('small', 'full')
    img_src = img_src.replace('th.wall', 'w.wall')  # 防止误匹配
    src_end = img_src.split('/')[-1]
    img_src = img_src.rstrip(src_end)+'wallhaven-'+img_src.split('/')[-1]
    img_src_full.append(img_src)
    print(img_src)

for img_src in img_src_full:
    ret = page.download(file_url=img_src, goal_path=os.path.abspath(os.path.dirname(__file__)+'/pic'),
                        rename=None, file_exists='skip', show_msg=True)

    if ret[0] is False:
        img_src = img_src.strip('jpg') + 'png'
    page.download(file_url=img_src, goal_path=os.path.abspath(os.path.dirname(__file__)+'/pic'),
                  rename=None, file_exists='skip', show_msg=True)
