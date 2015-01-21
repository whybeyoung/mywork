import psutil
import wx
import random
from mainframe import *

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

        
    

    