# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview
from distutils.log import INFO
#import wx.Control

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Processes Caputurer   by Mr.accuracy----- v1.0", pos = wx.DefaultPosition, size = wx.Size( 1257,778 ), style = wx.DEFAULT_FRAME_STYLE, name = u"jin" )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetExtraStyle( wx.WS_EX_BLOCK_EVENTS|wx.WS_EX_PROCESS_IDLE|wx.WS_EX_PROCESS_UI_UPDATES|wx.WS_EX_TRANSIENT|wx.WS_EX_VALIDATE_RECURSIVELY )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
        
        self.m_menubar1 = wx.MenuBar( 0 )
        self.m_menu1 = wx.Menu()
        self.m_menu11 = wx.Menu()
        self.m_menuItem1 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"打开", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu11.AppendItem( self.m_menuItem1 )
        
        self.m_menuItem2 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"保存", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu11.AppendItem( self.m_menuItem2 )
        
        self.m_menuItem3 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"关闭", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu11.AppendItem( self.m_menuItem3 )
        
        self.m_menuItem4 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"最近文件", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu11.AppendItem( self.m_menuItem4 )
        
        self.m_menu1.AppendSubMenu( self.m_menu11, u"打开" )
        
        self.m_menubar1.Append( self.m_menu1, u"文件" ) 
        
        self.m_menu8 = wx.Menu()
        self.m_menubar1.Append( self.m_menu8, u"MyMenu" ) 
        
        self.m_menu2 = wx.Menu()
        self.m_menu21 = wx.Menu()
        self.m_menuItem5 = wx.MenuItem( self.m_menu21, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu21.AppendItem( self.m_menuItem5 )
        
        self.m_menuItem6 = wx.MenuItem( self.m_menu21, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu21.AppendItem( self.m_menuItem6 )
        
        self.m_menu2.AppendSubMenu( self.m_menu21, u"模式" )
        
        self.m_menubar1.Append( self.m_menu2, u"视图" ) 
        
        self.m_menu3 = wx.Menu()
        self.m_menu31 = wx.Menu()
        self.m_menuItem7 = wx.MenuItem( self.m_menu31, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu31.AppendItem( self.m_menuItem7 )
        
        self.m_menuItem8 = wx.MenuItem( self.m_menu31, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu31.AppendItem( self.m_menuItem8 )
        
        self.m_menuItem9 = wx.MenuItem( self.m_menu31, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu31.AppendItem( self.m_menuItem9 )
        
        self.m_menuItem10 = wx.MenuItem( self.m_menu31, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu31.AppendItem( self.m_menuItem10 )
        
        self.m_menu3.AppendSubMenu( self.m_menu31, u"MyMenu" )
        
        self.m_menubar1.Append( self.m_menu3, u"网卡选择" ) 
        
        self.m_menu4 = wx.Menu()
        self.m_menuItem11 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu4.AppendItem( self.m_menuItem11 )
        
        self.m_menubar1.Append( self.m_menu4, u"编辑" ) 
        
        self.m_menu5 = wx.Menu()
        self.m_menu51 = wx.Menu()
        self.m_menu5.AppendSubMenu( self.m_menu51, u"MyMenu" )
        
        self.m_menubar1.Append( self.m_menu5, u"设置" ) 
        
        self.m_menu6 = wx.Menu()
        self.m_menuItem12 = wx.MenuItem( self.m_menu6, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu6.AppendItem( self.m_menuItem12 )
        
        self.m_menubar1.Append( self.m_menu6, u"帮助" ) 
        
        self.m_menu7 = wx.Menu()
        self.m_menuItem13 = wx.MenuItem( self.m_menu7, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu7.AppendItem( self.m_menuItem13 )
        
        self.m_menubar1.Append( self.m_menu7, u"关于" ) 
        
        self.SetMenuBar( self.m_menubar1 )
        
        self.m_menu9 = wx.Menu()
        self.Bind( wx.EVT_RIGHT_DOWN, self.MainFrameOnContextMenu ) 
        
        self.m_statusBar2 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
        bSizer20 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_panel14 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer23 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_dataViewListCtrl32 = wx.dataview.DataViewListCtrl( self.m_panel14, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_dataViewListCtrl32.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
        
        self.m_dataViewListColumn19 = self.m_dataViewListCtrl32.AppendTextColumn( u"Pid" ) 
        self.m_dataViewListColumn18 = self.m_dataViewListCtrl32.AppendTextColumn( u"Process" ) 
        self.m_dataViewListColumn17 = self.m_dataViewListCtrl32.AppendTextColumn( u"CreateTime" ) 
        bSizer23.Add( self.m_dataViewListCtrl32, 1, wx.EXPAND|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
        
        
        self.m_dataViewListCtrl30 = wx.ListCtrl( self.m_panel14, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,wx.LC_REPORT|wx.LC_VRULES|wx.LC_HRULES)
        #self.m_dataViewListCtrl30.SetExtraStyle(LVS_EX_GRIDLINES)
        self.m_dataViewListCtrl30.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 72, 90, 92, False, "@Gulim" ) )
        self.m_dataViewListCtrl30.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )
        self.m_dataViewListCtrl30.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
        self.m_dataViewListCtrl30.SetToolTipString( u"这是一个listcrtl对象，不是dataviewlistctrl" )
            
        self.m_dataViewListColumn8 = self.m_dataViewListCtrl30.InsertColumn(1,'sip')
        self.item1=wx.ListItem()
        self.item1.SetData(1)
        self.m_dataViewListColumn8 = self.m_dataViewListCtrl30.SetColumn(6,self.item1)
        self.m_dataViewListColumn8 = self.m_dataViewListCtrl30.InsertColumn(4,'dip')
        self.m_dataViewListColumn8 = self.m_dataViewListCtrl30.InsertColumn(3,'sssip')
        
       # self.m_dataViewListColumn15 = self.m_dataViewListCtrl30.Append( u"Sport" ) 
       # self.m_dataViewListColumn9 = self.m_dataViewListCtrl30.Append( u"Dip" ) 
       # self.m_dataViewListColumn10 = self.m_dataViewListCtrl30.Append( u"Dport" ) 
       ## self.m_dataViewListColumn12 = self.m_dataViewListCtrl30.Append( u"Rcev" ) 
       # self.m_dataViewListColumn14 = self.m_da30taViewListCtrl30.Append( u"Cat." ) 
        bSizer23.Add( self.m_dataViewListCtrl30, 3, wx.ALIGN_BOTTOM|wx.BOTTOM|wx.EXPAND|wx.RIGHT|wx.TOP, 5 )
        
        
        self.m_panel14.SetSizer( bSizer23 )
        self.m_panel14.Layout()
        bSizer23.Fit( self.m_panel14 )
        bSizer20.Add( self.m_panel14, 3, wx.ALL|wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer20 )
        self.Layout()
        self.m_toolBar2 = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY ) 
        self.m_tool7 = self.m_toolBar2.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"./session2.bmp", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_RADIO, wx.EmptyString, u"232", None ) 
        
        self.m_toolBar2.Realize() 
        
        
        self.Centre( wx.VERTICAL )
        
        # Connect Events
        self.Bind( wx.dataview.EVT_DATAVIEW_COLUMN_HEADER_CLICK, self.m_dataViewListCtrl30OnDataViewListCtrlColumnHeaderClick, id = wx.ID_ANY )
        self.Bind( wx.dataview.EVT_DATAVIEW_COLUMN_HEADER_RIGHT_CLICK, self.m_dataViewListCtrl30OnDataViewListCtrlColumnHeaderRightClick, id = wx.ID_ANY )
        self.Bind( wx.dataview.EVT_DATAVIEW_COLUMN_REORDERED, self.m_dataViewListCtrl30OnDataViewListCtrlColumnReordered, id = wx.ID_ANY )
        self.Bind( wx.dataview.EVT_DATAVIEW_COLUMN_SORTED, self.m_dataViewListCtrl30OnDataViewListCtrlColumnSorted, id = wx.ID_ANY )
        self.Bind( wx.dataview.EVT_DATAVIEW_ITEM_BEGIN_DRAG, self.m_dataViewListCtrl30OnDataViewListCtrlItemBeginDrag, id = wx.ID_ANY )
        self.Bind( wx.dataview.EVT_DATAVIEW_ITEM_COLLAPSED, self.m_dataViewListCtrl30OnDataViewListCtrlItemCollapsed, id = wx.ID_ANY )
        self.Bind( wx.dataview.EVT_DATAVIEW_ITEM_CONTEXT_MENU, self.m_dataViewListCtrl30OnDataViewListCtrlItemContextMenu, id = wx.ID_ANY )
        self.Bind( wx.dataview.EVT_DATAVIEW_ITEM_EDITING_STARTED, self.m_dataViewListCtrl30OnDataViewListCtrlItemEditingStarted, id = wx.ID_ANY )
        self.Bind( wx.dataview.EVT_DATAVIEW_ITEM_START_EDITING, self.m_dataViewListCtrl30OnDataViewListCtrlItemStartEditing, id = wx.ID_ANY )
        self.Bind( wx.dataview.EVT_DATAVIEW_ITEM_VALUE_CHANGED, self.m_dataViewListCtrl30OnDataViewListCtrlItemValueChanged, id = wx.ID_ANY )
        self.Bind( wx.dataview.EVT_DATAVIEW_SELECTION_CHANGED, self.m_dataViewListCtrl30OnDataViewListCtrlSelectionChanged, id = wx.ID_ANY )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def m_dataViewListCtrl30OnDataViewListCtrlColumnHeaderClick( self, event ):
        event.Skip()
    
    def m_dataViewListCtrl30OnDataViewListCtrlColumnHeaderRightClick( self, event ):
        event.Skip()
    
    def m_dataViewListCtrl30OnDataViewListCtrlColumnReordered( self, event ):
        event.Skip()
    
    def m_dataViewListCtrl30OnDataViewListCtrlColumnSorted( self, event ):
        event.Skip()
    
    def m_dataViewListCtrl30OnDataViewListCtrlItemBeginDrag( self, event ):
        event.Skip()
    
    def m_dataViewListCtrl30OnDataViewListCtrlItemCollapsed( self, event ):
        event.Skip()
    
    def m_dataViewListCtrl30OnDataViewListCtrlItemContextMenu( self, event ):
        event.Skip()
    
    def m_dataViewListCtrl30OnDataViewListCtrlItemEditingStarted( self, event ):
        event.Skip()
    
    def m_dataViewListCtrl30OnDataViewListCtrlItemStartEditing( self, event ):
        event.Skip()
    
    def m_dataViewListCtrl30OnDataViewListCtrlItemValueChanged( self, event ):
        event.Skip()
    
    def m_dataViewListCtrl30OnDataViewListCtrlSelectionChanged( self, event ):
        event.Skip()
    
    def MainFrameOnContextMenu( self, event ):
        self.PopupMenu( self.m_menu9, event.GetPosition() )
        


if __name__ == '__main__': 
    app = wx.PySimpleApp() 
    frame = MainFrame(None) 
    frame.Show(True) 
    app.MainLoop()  