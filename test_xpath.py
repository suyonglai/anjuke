import requests
import lxml.html
import re
html=requests.get('https://www.runoob.com/python3/python3-stdlib.html').content.decode()
# print(html)
mylist=re.findall('',html)