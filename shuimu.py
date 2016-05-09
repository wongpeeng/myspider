#coding=utf-8
import urllib  
import urllib2
import cookielib

#初始化一个CookieJar来处理Cookie的信息#
cookie = cookielib.CookieJar()

#创建一个新的opener来使用我们的CookieJar#
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

#需要POST的数据#
postdata=urllib.urlencode({
    'id':'wongpeeng',  
    'passwd':'wp19890818'
})

user_agent='Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:46.0) Gecko/20100101 Firefox/46.0'


headers={ 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','X-Requested-With':'XMLHttpRequest','User-Agent' : user_agent }
#自定义一个请求#
req = urllib2.Request(  
    url = 'http://www.newsmth.net/nForum/user/ajax_login.json',  
    data = postdata,
    headers=headers
)

#访问该链接#
result = opener.open(req)

#打印返回的内容#
print result.content()


#打印cookie的值
#for item in cookie:  
#    print 'Cookie：Name = '+item.name  
#    print 'Cookie：Value = '+item.value

    
#访问该链接#
#result = opener.open('http://jwxt.sdu.edu.cn:7777/pls/wwwbks/bkscjcx.curscopre')

#打印返回的内容#
#print result.read()



