# -*- coding: utf-8 -*-
import wx
import wx.xrc
import time

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 605,457 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
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
        self.m_dataViewListCtrl1 = wx.ListCtrl( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.LC_HRULES|wx.LC_VRULES)
        self.m_dataViewListCtrl1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 72, 90, 92, False, "@Gulim" ) )
        self.m_dataViewListCtrl1.SetForegroundColour( 'Blue')
        self.m_dataViewListCtrl1.SetBackgroundColour( "Gray" )
        self.m_dataViewListCtrl1.SetToolTipString( u"这是一个listcrtl " )
        self.m_dataViewListColumn1 = self.m_dataViewListCtrl1.InsertColumn(1, u"Sip" )#�����1��ʾ����1�к���
        self.m_dataViewListColumn2 = self.m_dataViewListCtrl1.InsertColumn( 2,u"Sport" )
        bSizer2.Add( self.m_dataViewListCtrl1, 1, wx.EXPAND |wx.ALL, 5 )
        self.timeshuaxin()
    def OnGetItemText(self, item, col):
        return "Item %d, column %d" % (item, col)    
    def __del__( self ):
        pass
    
    def timeshuaxin(self):
        self.listitem2 = wx.ListItem()
        self.listitem1 = wx.ListItem()
        #self.m_dataViewListCtrl1.Append('2')
        self.listitem2.SetColumn(0)
        self.listitem2.SetText('1')
        time.sleep(2)
        self.listitem2.SetText('2')
        self.listitem2.SetId(0)
        self.listitem2.SetData(2222)
        
       # self.listitem2.SetColumn(1)
       # self.listitem2.SetText("12")
        #self.listitem2.SetId(1)
        #self.m_dataViewListCtrl1.SetItemCount(30)
        #self.m_dataViewListCtrl1.SetItem(self.listitem2)
        self.m_dataViewListCtrl1.InsertItem(self.listitem2)
       # self.m_dataViewListCtrl1.InsertItem(self.listitem1)
        #self.m_dataViewListCtrl1.Append(self.listitem2)
if __name__ == '__main__': 
    app = wx.PySimpleApp() 
    frame = MyFrame1 (None)

   # thread1 = ThreadGet(frame.m_dataViewListCtrl32)
 
    frame.Show(True) 
    app.MainLoop()   
        