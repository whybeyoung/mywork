# -*- coding: utf-8 -*-
import wx,mainframe
import threading
import time
from time import ctime,sleep
import psutil,mainframe
import random
class ThreadGet(threading.Thread):
    #def __init__(self,name):
    def __init__(self):   
        threading.Thread.__init__(self)
        #self.name=name
    def run(self):
        
        self.threadLock.acquire()
        while True:
           time.sleep(1)
           self.nowproc =GetProc()
          # self.nowproc.appenddata(self.name)
           self.nowproc.appenddata(frame.m_dataViewListCtrl32)    
            #frame.m_panel14.Refresh() 
           
        # �ͷ���
        self.threadLock.release()
    threadLock = threading.Lock()
    threads = []
    def getleftstr(self):
        self.left3str =self.nowproc.getpidname()
        return self.left3str

        
                  
class GetProc():
    
    def getpid(self):
        self.proclist=psutil.pids()
        return self.proclist
    def getlistnum(self):
        self.listnum=len(self.proclist)
        return self.listnum
    def getcreatetime(self,pid):
        self.createtime=psutil.Process(pid).create_time()
        return self.createtime
    def getpidname(self):
        self.pidandnameandtime=[]
        for i in self.getpid()[:]:
            try:
                self.pidandnameandtime.append([i,psutil.Process(i).name(),self.getcreatetime(i)])
            except psutil.AccessDenied:
                pass
        return self.pidandnameandtime
    def appenddata(self,control): 
    #print type(control)
        control.DeleteAllItems()
        for data in self.getpidname():
            control.Append(data)
            frame.m_panel14.Refresh() 
 
    def getlistuple(self):
        self.listuple=[]
        try:
            for j in self.getpid():
            
                #print self.getpid()
                p=psutil.Process(j).connections()
                #print p
                count = len(p)
                #print count
                for pcon in range(count):
                    try:    
                    
                        self.listuple.append([p[pcon][3][0],p[pcon][3][1],p[pcon][4][0],p[pcon][4][1],random.randint(10,100),random.randint(10,100),p[pcon][4],p[pcon][0]])
                    except IndexError:
                        pass         
                print self.listuple
        except psutil.AccessDenied:
            pass
        
        return self.listuple  
if __name__ == '__main__': 
    app = wx.PySimpleApp() 
    frame = mainframe.MainFrame(None)
    thread1 = ThreadGet()
   # thread1 = ThreadGet(frame.m_dataViewListCtrl32)
    thread1.start()
    frame.Show(True) 
    app.MainLoop()     
