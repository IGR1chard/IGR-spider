# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os

"""
从www.hbcjlp.com爬取小说，
就参照原教程，爬取了该网的内容。
    2023-12-12
"""

if __name__=='__main__':
    #所要爬取的小说主页，每次使用时，修改该网址即可，同时保证本地保存根路径存在即可
    target="https://www.hbcjlp.com/hb50919/"
    # 本地保存爬取的文本根路径
    save_path = 'D:/Download/2077'
    #网站根路径
    index_path='https://www.hbcjlp.com'

    req=requests.get(url=target)
    #查看request默认的编码，发现与网站response不符，改为网站使用的gdk
    print('++',req.encoding)
    req.encoding = 'utf-8'
    #解析html
    soup=BeautifulSoup(req.text,"html.parser")
    # print(soup)
    list_tag=soup.find_all('div', class_="layout layout-col1")
    # print('list_tag:',list_tag)
    #获取小说名称
    dt_elements = list_tag[1].find_all('dt')
    # print(dt_elements)
    story_title = dt_elements[1].string
    print(story_title)
    # 根据小说名称创建一个文件夹,如果不存在就新建
    dir_path=save_path+'/'+story_title
    if not os.path.exists(dir_path):
        os.path.join(save_path,story_title)
        os.mkdir(dir_path)
    #开始循环每一个章节，获取章节名称，与章节对应的网址
    sb = dt_elements[1].find_all_next('dd')
    # print(sb)
    for dd_tag in sb:
        #章节名称
        chapter_name=dd_tag.string
        # print('--20',chapter_name)
        #章节网址
        chapter_url=index_path+dd_tag.a.get('href')
        # print(chapter_url)
        #访问该章节详情网址，爬取该章节正文
        chapter_req = requests.get(url=chapter_url)
        # print(chapter_req)
        chapter_req.encoding = 'utf-8'
        chapter_soup = BeautifulSoup(chapter_req.text, "html.parser")
        # print(chapter_soup)
        #解析出来正文所在的标签
        # content_tag = chapter_soup.div.find(id="content1")
        content_tag = chapter_soup.find_all('p')
        # print(content_tag)
        content_text = '\n'.join([p_tag.get_text(strip=True) for p_tag in content_tag])
        
        #获取正文文本，并将空格替换为换行符
        # content_text = str(content_tag.text.replace('\xa0','\n'))
        # print(content_text)
        # #将当前章节，写入以章节名字命名的txt文件
        with open(dir_path+'/'+chapter_name+'.txt', 'w', encoding='utf-8') as f:
            # f.write('本文网址:'+chapter_url)
            f.write(content_text)