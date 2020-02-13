import re
string = """Runoob 的网页地址为：https://www.runoob.com
Google 的网页地址为：https://www.google.com
Keyman 的博客地址为：http://www.s-keyman.site
baidu  的网页地址为：https://www.baidu.com
bilibili 的地址为：https://www.bilibili.com/"""
url = re.findall(r'https?://(?:[\w.]|(?:[\S]))*', string)
print("Urls:", url)