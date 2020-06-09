#这段代码成功的从www.xicidaili.com中获取了代理服务器IP，然后发送请求到测试网站www.fuxianhu.com。如代理服务器不可用，显示连接失败。
import requests
import lxml.html
url='https://www.xicidaili.com/nn'
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/7"}
r=requests.get(url,headers=headers).content.decode()
#print(r)
sel=lxml.html.fromstring(r)
list_selector=sel.xpath("//tr[@class='odd']")
for each_url in list_selector:
    ip=each_url.xpath('td[2]/text()')[0]
    port=each_url.xpath('td[3]/text()')[0]
    http_str=each_url.xpath('td[6]/text()')[0]
    if http_str=='http':
        http1='http'
        myurl = "{}://{}:{}".format(http1, ip, port)
        proxis = {'http': myurl}
    else:
        http2='https'
        myurl="{}://{}:{}".format(http2, ip, port)
        proxis = {'https': myurl}
    print(myurl)
    try:
        data=requests.get('https://www.fuxianhu.com/',proxies=proxis).content.decode()
        print(data)
    except:
        print('连接失败')



