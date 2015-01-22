# -*- coding: utf-8 -*-
import wx
import wx.xrc
import psutil
import threading
import time
from time import ctime,sleep
###########################################################################

## Class MyFrame1
columns = ["Request ID", "Summary", "Date", "Submitted By"]

rows1 = [
    ("987441", "additions to RTTI?", "2004-07-08 10:22", "g00fy"),
    ("846368", "wxTextCtrl - disable auto-scrolling", "2003-11-20 21:25", "ryannpcs"),
    ("846367", "Less flicker when resizing a window", "2003-11-20 21:24", "ryannpcs"),
    ("846366", "Wishlist - wxDbGetConnection return value", "2003-11-20 21:23", "ryannpcs"),
    ("846364", "wxPostscriptDC with floating point coordinates", "2003-11-20 21:22", "ryannpcs"),
    ("846363", "Wishlist - Better wxString Formatting", "2003-11-20 21:22", "ryannpcs"),
    ("846362", "Wishlist - Crossplatform wxRichText Widget", "2003-11-20 21:20", "ryannpcs"),
    ("953341", "Support for paper trays when printing", "2004-05-13 08:01", "tonye"),
    ("952466", "mac menu - Window menu", "2004-05-12 03:19", "pimbuur"),
    ("928899", "FloatCanvas demo should work with numarray", "2004-04-03 08:30", "glchapman"),
    ("912714", "wxGrid: Support for Search / Replace", "2004-03-09 05:46", "rclund"),
    ("901061", "wxComboBox - add small icons as in MSW CComboBoxEx ", "2004-02-20 04:04", "tomash"),
    ("900768", "Please add more codepages support to your source built", "2004-02-19 15:49", "jsat66"),
    ("894921", "trigger on event-system creation", "2004-02-11 08:10", "g00fy"),
    ("869808", "HitTest in wxCheckListBox", "2004-01-03 01:22", "dickkniep"),
    ("863306", "wxGrid - Thaw/Freeze column/row", "2003-12-19 17:54", "zinit"),
    ("975435", "wxMenu anchor right position in wxMenuBar", "2004-06-18 08:44", "jmt2715"),
    ("969811", "wxColourEnumerator", "2004-06-09 11:41", "wyo"),
    ("959849", "wx.Grid gridlines past max row/col", "2004-05-24 19:39", "dodywijaya"),
    ("959158", "wxGrid: Arbitrary controls in the grid", "2004-05-23 16:56", "somecoder"),
    ("953824", "mac menu - Window menu", "2004-05-14 02:06", "pimbuur"),
    ("863301", "wxTextCtrl - edit mode", "2003-12-19 17:48", "zinit"),
    ("855902", "virtual window classes", "2003-12-07 12:39", "cursorstar"),
    ("852379", "wxGrid row/col size limits", "2003-12-01 15:47", "jbrouwers"),
    ("846375", "wxGraphicsPath", "2003-11-20 21:30", "ryannpcs"),
    ("846374", "wxToolBar - return tool at position", "2003-11-20 21:29", "ryannpcs"),
    ("846373", "Scrolling improvements", "2003-11-20 21:28", "ryannpcs"),
    ("846372", "Hooks for standard remote events", "2003-11-20 21:27", "ryannpcs"),
    ("846370", "wxDial - dial widget", "2003-11-20 21:27", "ryannpcs"),
    ("846369", "wxGird - auto-scrolling", "2003-11-20 21:26", "ryannpcs"),
    ("846361", "Wishlist - wxStaticText that takes fonts, colors, etc.", "2003-11-20 21:19", "ryannpcs"),
    ("819559", "wxListCtrl column widths in wxLC_ICON mode ", "2003-10-07 13:34", "nwmoriarty"),
    ("817429", "OS X wheel mouse", "2003-10-03 14:05", "mdcowles"),
]

###########################################################################



class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1024,800 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        
        
        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        self.m_dataViewListCtrl1 = VirtualListCtrl( self.m_panel1,DataSource())
        self.m_dataViewListCtrl1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 72, 90, 92, False, "@Gulim" ) )
        self.m_dataViewListCtrl1.SetForegroundColour( 'Blue')
        self.m_dataViewListCtrl1.SetBackgroundColour( "Gray" )
        self.m_dataViewListCtrl1.SetToolTipString( u"这是一个listcrtl " )
        self.m_dataViewListColumn1 = self.m_dataViewListCtrl1.InsertColumn(1, u"pid",width=100 )#�����1��ʾ����1�к���
        self.m_dataViewListColumn2 = self.m_dataViewListCtrl1.InsertColumn( 2,u"name" ,width=100)
        self.m_dataViewListColumn2 = self.m_dataViewListCtrl1.InsertColumn( 3,u"Creat_time",width=100 )
        self.m_dataViewListColumn2 = self.m_dataViewListCtrl1.InsertColumn( 4,u"running?",width=100 )
        self.m_dataViewListColumn2 = self.m_dataViewListCtrl1.InsertColumn( 5,u"meminfo" ,width=100)
        self.m_dataViewListColumn2 = self.m_dataViewListCtrl1.InsertColumn( 6,u"parent" ,width=100)
        self.m_dataViewListColumn2 = self.m_dataViewListCtrl1.InsertColumn(7,u"Child",width=100 )
        self.m_dataViewListColumn2 = self.m_dataViewListCtrl1.InsertColumn( 8,u"raddrip" ,width=100)
        self.m_dataViewListColumn2 = self.m_dataViewListCtrl1.InsertColumn( 9,u"raddrport" ,width=100)
        #########self.m_dataViewListCtrl1.SetItemCount(100)
       # self.m_dataViewListCtrl1.SetItemCount(dataSource.GetCount())#设置列表的大小
        bSizer2.Add( self.m_dataViewListCtrl1, 1, wx.EXPAND |wx.ALL, 5 )
        #self.timeshuaxin()
    def OnGetItemText(self, item, col):
        return "Item %d, column %d" % (item, col)    
    def __del__( self ):
        pass
class VirtualListCtrl(wx.ListCtrl):#1 声明虚列表
    """
    A generic virtual listctrl that fetches data from a DataSource.
    """
    def __init__(self, parent, dataSource):
        wx.ListCtrl.__init__(self, parent,
            style=wx.LC_REPORT|wx.LC_HRULES|wx.LC_VRULES|wx.LC_VIRTUAL)#使用wx.LC_VIRTUAL标记创建虚列表
        self.dataSource = dataSource
        self.Bind(wx.EVT_LIST_CACHE_HINT, self.DoCacheItems)
        self.SetItemCount(dataSource.GetCount())#设置列表的大小

        #columns = dataSource.GetColumnHeaders()
        #for col, text in enumerate(columns):
          #  self.InsertColumn(col, text)
        

    def DoCacheItems(self, evt):
        self.dataSource.UpdateCache(
            evt.GetCacheFrom(), evt.GetCacheTo())

    def OnGetItemText(self, item, col):#得到需求时的文本
        data = self.dataSource.GetItem(item)
        return data[col]

    def OnGetItemAttr(self, item):  return None
    def OnGetItemImage(self, item): return -1
class DataSource():
    def __init__(self):
        self.GetPidinfo()
    def GetPid(self):
        self.pids=psutil.pids()
        return self.pids
    def GetPidinfo(self):
        self.piddict={}
        self.rows=[]
        for proc in self.GetPid():
             try:
                 if psutil.pid_exists(proc):
                     self.name= psutil.Process(proc).name()
                     self.createtime =  psutil.Process(proc).create_time()
                     self.status =  psutil.Process(proc).is_running()
                     self.meminfo = psutil.Process(proc).memory_info()
                     self.parentproc = psutil.Process(proc).parent()
                     self.child = psutil.Process(proc).children()
                     self.raddrip=''
                     self.raddrport=''
                     try:
                         pconns = psutil.Process(proc).connections('tcp')
                         if len(pconns):
                             for ele in pconns:
                                 self.raddrip = ele[3][0]
                                 self.raddrport = ele[3][1]
                     except IndexError:
                         pass
             except psutil.AccessDenied:
                pass
             self.piddict[proc] =(self.name,self.createtime,self.status,self.meminfo,self.parentproc,self.child,self.raddrip,self.raddrport)
             self.rows.append([proc,self.name,self.createtime,self.status,self.meminfo,self.parentproc,self.child,self.raddrip,self.raddrport])
        
        return self.rows
    def GetColumnHeaders(self):
        return columns

    def GetCount(self):
       # self.GetPidinfo
        return len(self.rows)

    def GetItem(self, index):
        return self.rows[index]

    def UpdateCache(self, start, end):
        pass
    
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
            time.sleep(1)
            a.GetPidinfo()
            print len(a.GetPidinfo())
            #frame.m_dataViewListCtrl1.RefreshItems(0,a.GetCount())
            frame.m_dataViewListCtrl1.RefreshItems(1,1000)
            #frame.m_panel14.Refresh() 
           
        # 释放锁
        self.threadLock.release()
    threadLock = threading.Lock()
    threads = []        #return data.rows[index]
if __name__ == '__main__': 
    a=DataSource()  
    app = wx.PySimpleApp()  
    frame = MyFrame1 (None)
    thread1 = timeGetproc()
    thread1.start()
    
    
   
   # thread1 = ThreadGet(frame.m_dataViewListCtrl32)
 
    frame.Show(True) 
    app.MainLoop()         
        
                
            