# -*- coding:utf-8 -*-
"""
@author: momochong0
@software: PyCharm
@file: gitee.py
@time: 2023-03-30 20:58
@desc:
"""
# from DrissionPage import ChromiumPage
#
# # 创建页面对象，并启动或接管浏览器
# page = ChromiumPage()
# # 跳转到登录页面
# page.get('https://gitee.com/login')
#
# # 定位到账号文本框，获取文本框元素
# ele = page.ele('#user_login')
# # 输入对文本框输入账号
# ele.input('momochong0@163.com')
# # 定位到密码文本框并输入密码
# page.ele('#user_password').input('jianghe032')
# # 点击登录按钮
# page.ele('@value=登 录').click()
#
# from DrissionPage import SessionPage
#
# # 创建页面对象
# page = SessionPage()
#
# # 爬取3页
# for i in range(1, 4):
#     # 访问某一页的网页
#     page.get(f'https://gitee.com/explore/all?page={i}')
#     # 获取所有开源库<a>元素列表
#     links = page.eles('.title project-namespace-path')
#     # 遍历所有<a>元素
#     for link in links:
#         # 打印链接信息
#         print(link.text, link.link)

from DrissionPage import WebPage

# 创建页面对象
page = WebPage()
# 访问网址
page.get('https://gitee.com/explore')
# 查找文本框元素并输入关键词
page('#q').input('DrissionPage')
# 点击搜索按钮
page('t:button@tx():搜索').click()
# 等待页面加载
page.wait.load_start()
# 切换到收发数据包模式
page.change_mode()
# 获取所有行元素
items = page('#hits-list').eles('.item')
# 遍历获取到的元素
for item in items:
    # 打印元素文本
    print(item('.title').text)
    print(item('.desc').text)
    print()