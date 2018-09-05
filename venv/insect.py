import urllib2
import urllib
import re
import time

# def getHTML(url):
#     print url
#
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.connect((url, 80))
#     # s.send('''GET https://'''+url+'''/ HTTP/1.1
#     s.send('''GET http://www.pixabay.com/ HTTP/1.1
#     Host: www.baidu.com
#     Connection: keep-alive
#     Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
#     Upgrade-Insecure-Requests: 1
#     User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36
#     Accept-Language: zh-CN,zh;q=0.8
#
#     ''')
#
#     buf = s.recv(1024)
#     if len(buf):
#         print buf
#     # while len(buf):
#     #     print buf
#     #     buf += s.recv(1024)
#     buf1 = s.recv(1024)
#     if len(buf1):
#         print buf1
#     return 0

def getHtml(url):
    request = urllib2.Request(url)

    request.add_header('User-Agent',
                       'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 46.0.2490.76 Mobile Safari / 537.36')

    response = urllib2.urlopen(request)
    html=response.read()
    return html

def getImage(html):
    imglist = re.findall(r'data-original="(.*?.(jpg|jpeg))"', html)
    print(len(imglist))
    # print (imglist)
    path =""
    x = 0
    for img in imglist:
        print (img[0])
        urllib.urlretrieve(img[0],"E:/pyimg/"+str(x) +"."+img[1])
        x += 1
        print (x)
        time.sleep(1)

url = 'https://www.douyu.com/directory/game/yz'
# url = 'https://pixabay.com'
html = getHtml(url)
getImage(html)