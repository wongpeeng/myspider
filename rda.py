#coding=utf-8 
import urllib2
from bs4 import BeautifulSoup 
import urllib 
import cookielib 
import re 
import httplib 
import time 
loginUrl="http://crm.rdamicro.com/RDAWebApp/login.aspx"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36"} 
studentCookie = cookielib.CookieJar()  
pageOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(studentCookie)) 
loginPageRequest = urllib2.Request(loginUrl)  
loginPageHTML = pageOpener.open(loginPageRequest).read() 
#print loginPageHTML 
soup=BeautifulSoup(loginPageHTML) 
  
__VIEWSTATE=soup.find(id="__VIEWSTATE")['value']
__VIEWSTATEGENERATOR=soup.find(id="__VIEWSTATEGENERATOR")['value']
__EVENTVALIDATION=soup.find(id="__EVENTVALIDATION")['value']  
print __VIEWSTATEGENERATOR
print __VIEWSTATE
print __EVENTVALIDATION
login_data={ 
   ' __EVENTTARGET':'', '__EVENTARGUMENT':'', '__VIEWSTATE':__VIEWSTATE, '__VIEWSTATEGENERATOR':__VIEWSTATEGENERATOR,'__EVENTVALIDATION':__EVENTVALIDATION, 'txtUserName':'pengwang01','txtUserPwd':'Wp123456', 'butLogin.x':'34', 'butLogin.y':'16'
   } 
loginData=urllib.urlencode(login_data) 
loginRequest = urllib2.Request(loginUrl , loginData , headers) 
loginResponse = pageOpener.open(loginRequest) 
#print loginResponse.read()
