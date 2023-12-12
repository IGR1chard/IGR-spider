# IGR-spider
小说/爬虫【个人练习】
# 声明
----本代码为个人练习使用，请勿用作商业用途----

----本代码基于Jack-Cherish/python-spider进行修改----
----原代码网址https://github.com/Jack-Cherish/python-spider

需要几个必要的库，使用pip install安装下列库：

bs4
cn2an

本身代码也非常简单，本人初学者，0爬虫基础花了一个下午吧
简单讲讲如何根据不同网站修改： 
# 针对biquge20231212.py
1.查看request默认的编码, 确定req.encoding是gbk还是utf-8

req=requests.get(url=target)

req.encoding = 'utf-8'

2.查看soup, 找到你需要看的那本书的目录位于哪个div class/id是什么

list_tag=soup.find_all('div', class_="layout layout-col1")

dt_elements = list_tag[1].find_all('dt') # 这个地方需要用于确定你的目录到底是class下的第几个

3.找到了目录dt_elements，通常为你要看的小说名字或者+正文两个字，找到所有章节标题

sb = dt_elements[1].find_all_next('dd')

4.遍历每个标题里面的href，相当于把每个章节打开一次，最关键的是这句：

chapter_soup = BeautifulSoup(chapter_req.text, "html.parser")

建议print(chapter_soup)先看看你的正文是啥格式的
5.遍历每一行正文

content_tag = chapter_soup.find_all('p') # 找到每一行正文

content_text = '\n'.join([p_tag.get_text(strip=True) for p_tag in content_tag]) #提取每一行正文并拼接为一个整体
6.输出txt到你想要的文件夹

# 针对 mergestory.py
由于上面的代码是按章节输出的，需要整合为一个txt，因此本人写了这个小程序。

下面解释一下函数作用

1.normalize_file_names(input_directory) # input_directory为txt文件目录

此函数用于将txt名称转化为阿拉伯数字用于排序，例如：

第1章 开篇

第2章 中间

第4章 后记

第三章 最后

windows 文件夹排序是先数字后汉字，因此将第三章改为第3章，这样可以获得以下排序，用于后续合并
第1章 开篇

第2章 中间

第3章 最后

第4章 后记

2.extract_arabic_number(file_name) 

此函数用于提取章节序号（阿拉伯数字）

3.merge_files(input_directory, output_file_path) # input_directory为txt文件目录output_file_path为输出文件

此函数将txt文件按章节排序（PS：可以添加章节缺失检测），整合为一个整体，并且每章前添加章节名称，导入各种阅读软件时自动生成目录
