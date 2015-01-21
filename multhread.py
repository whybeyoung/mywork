#coding=utf-8
#!/usr/bin/python
#coding=utf-8
import wx,mainframe
import threading
import time
from time import ctime,sleep
import psutil,mainframe,xianshishuju
class timeGetproc(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
                
       # print type(self.name)
       # self.interval = interval
        
    def run(self):
      #  print "Starting " + self.name
       # 获得锁，成功获得锁定后返回True
       # 可选的timeout参数不填时将一直阻塞直到获得锁定
       # 否则超时后将返回False
        self.threadLock.acquire()
        while True:
            #time.sleep(1)
            appenddata(frame.m_dataViewListCtrl32)
            #frame.m_panel14.Refresh() 
           
        # 释放锁
        self.threadLock.release()
    threadLock = threading.Lock()
    threads = []
def getpidintime():
    #proc = xianshishuju.GetProc()
    
    proc=xianshishuju.GetProc()
    print len(proc.getpid())
    return proc.getpidname()
        
def appenddata(control): 
    #print type(control)
    control.DeleteAllItems()
    for data in getpidintime():
        control.Append(data)
        frame.m_panel14.Refresh() 
   
if __name__ == '__main__': 
    app = wx.PySimpleApp() 
    frame = mainframe.MainFrame(None)
    thread1 = timeGetproc()
    thread1.start()
    frame.Show(True) 
    app.MainLoop()     
# 创建新线程
#thread1 = myThread(1, "Thread-1", 1)
#thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
#thread1.start()
#thread2.start()

# 添加线程到线程列表
#threads.append(thread1)
#threads.append(thread2)

# 等待所有线程完成
#for t in threads:
#    t.join()
#print "Exiting Main Thread"