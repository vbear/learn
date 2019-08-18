#coding=utf8

import httplib2
import urllib2
client=httplib2.Http()
url="http://www.baidu.com"
#数据包头部
headers={
    'Host':'www.baidu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Connection':'Keep-alive'
}
#获取头信息
header,content = client.request(url,"Get")
for field,value in header.items():
    print field + ": " + value

print "------------1---------------"
#获取网页
req=urllib2.Request(url,headers=headers)
response=urllib2.urlopen(req)
response_header = response.info()
print response_header
print "------------2---------------"
#处理cookie
import cookielib
filename='Mycookie.txt'
FileCookieJar=cookielib.MozillaCookieJar(filename)
FileCookieJar.save()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(FileCookieJar))
opener.open(url)
FileCookieJar.save()
print open(filename).read()


