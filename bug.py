#coding=utf-8
import urllib2
import urllib
import re
import thread 
import time

class Spider():
    def __init__(self):
        self.page=1
        self.pages=[]
        self.enable=False

    def GetPage(self,page):
        myurl="http://www.qiushibaike.com/hot/page/"+page+"/?s=4875338"
        user_agent= 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers={ 'User-Agent' : user_agent }
        req=urllib2.Request(myurl,headers=headers)
        myres=urllib2.urlopen(req)
        mypage=myres.read()
        codepage=mypage.decode("utf-8")
        pageitem=re.findall('<div.*?class="content".*?>(.*?)</div>',codepage,re.S)
        items=[]
        for item in pageitem:
            items.append(item.replace("\n",""))
        return items
    



    def LoadPage(self):
        while self.enable:
            if len(self.pages)<2:
                try:
                    mypage=self.GetPage(str(self.page))
                    self.page+=1
                    self.pages.append(mypage)
                except:
                    print 'can nont connect to the website'
            else:
                time.sleep(1)


    def ShowPage(self,nowpage):
        for item in nowpage:
            print '############################'
            print item
            myinput=raw_input()
            if myinput=="quit":
                self.enable=False
                break
    def Start(self):
        self.enable=True
        page=self.page
        thread.start_new_thread(self.LoadPage,())
        while self.enable:
            if self.pages:
                nowpage=self.pages[0]
                del self.pages[0]
                self.ShowPage(nowpage)
                page+=1



# new a spider class
mymodel=Spider()
mymodel.Start()
