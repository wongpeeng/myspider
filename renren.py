#coding=utf-8
import urllib2
import urllib
import cookielib
data={"email":"635711867@qq.com","password":"wp19890818"}#你的用户名密码
post_data=urllib.urlencode(data )#对data进行url编码
cj=cookielib.CookieJar()#创建cookie对象
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))#创建cookie处理程序、创建opener
req=urllib2.Request("http://www.renren.com/PLogin.do",post_data)#发送请求
content=opener.open(req)
f=open('renren.html','w+')
#print content.read().decode('utf-8')#打印网页
f.write(content.read())
f.close
