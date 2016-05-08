import urllib2
#coding=utf-8
def tieba(myurl,sp,ep):
    f=open('tvd.html','w+')
    for i in range(sp,ep+1):
        request=urllib2.Request(myurl+str(i)+'.html')
        content=urllib2.urlopen(request)
        f.write(content.read())
    f.close 
url_p1='http://tieba.baidu.com/f?kw=%E5%90%B8%E8%A1%80%E9%AC%BC%E6%97%A5%E8%AE%B0&ie=utf-8&pn='
sp=1
ep=10

tieba(url_p1,sp,ep)    
