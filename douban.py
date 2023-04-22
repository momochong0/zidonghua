# -*- coding:utf-8 -*-
"""
@author: momochong0
@software: PyCharm
@file: douban.py
@time: 2023-04-09 21:52
@desc:
"""
from DrissionPage import ChromiumPage

# 创建页面对象
page = ChromiumPage()
# 访问目标网页
page.get('https://book.douban.com/tag/小说?start=0&type=T')

# 爬取4页
for _ in range(4):
    # 遍历一页中所有图书
    for book in page.eles('.subject-item'):
        # 获取封面图片对象
        img = book('t:img')
        # 保存图片
        img.save(r'.\imgs')

    # 点击下一页
    page('后页>').click()
    page.wait.load_start()
