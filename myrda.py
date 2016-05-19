#coding=utf-8
import urllib2
import urllib
import re
import cookielib
class Myrda():
    def __init__(self):
        self.data={
            '__EVENTTARGET':'',
            '__EVENTARGUMENT':'',
            '__VIEWSTATE':'',
            '__VIEWSTATEGENERATOR':'',
            '__EVENTVALIDATION':'',
            'txtUserName':'pengwang01',
            'txtUserPwd':'Wp123456',
            'butLogin.x':'34',
            'butLogin.y':'16'
        }
        self.url="http://crm.rdamicro.com/RDAWebApp/login.aspx"
        self.headers={ 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' }




    def GetData(self):
        req=urllib2.Request(self.url,headers=self.headers)
        res=urllib2.urlopen(req)
        mypage=res.read()
        item=re.findall('id="__VIEWSTATE" value="(.*?)" />',mypage,re.S)
        self.data['__VIEWSTATE']=item[0]
        item=re.findall('id="__VIEWSTATEGENERATOR" value="(.*?)" />',mypage,re.S)
        self.data['__VIEWSTATEGENERATOR']=item[0]
        item=re.findall('id="__EVENTVALIDATION" value="(.*?)" />',mypage,re.S)
        self.data['__EVENTVALIDATION']=item[0]
        return
    def LoginAndSave(self):
        postdata=urllib.urlencode(self.data)
        req=urllib2.Request(self.url,postdata,headers=self.headers)
        cookie=cookielib.CookieJar()
        opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        opener.open(req)
        req=urllib2.Request('http://crm.rdamicro.com/RDAWebApp/AttendanceMoniter.aspx',postdata,headers=self.headers)
        mypage=opener.open(req).read().decode("utf-8")
        info=re.findall('fullname=\'(\w*?) (.*?)\'(.*?)In: </span>(\S*?) (.*?)Out: </span>(.*?)</',mypage,re.S)
        for item in info:
            print item[0],item[1],item[3],item[5]


    def Start(self):
        self.GetData()
        self.LoginAndSave()


rda=Myrda()
rda.Start()
