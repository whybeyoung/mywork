# -*- coding: cp936 -*-
import wx
app=wx.App()
basicframe = wx.Frame(None,title="Xx的记事本")
panel = wx.Panel(basicframe)
openbutton = wx.Button(basicframe,label='打开记事本')
savebutton = wx.Button(basicframe,label='保存记事本')
selectfile = wx.TextCtrl(basicframe)
inputframe = wx.TextCtrl(basicframe,style=wx.TE_MULTILINE|wx.HSCROLL)
topbox = wx.BoxSizer()
topbox.Add(selectfile,proportion=1,flag=wx.EXPAND)
topbox.Add(openbutton,proportion=0,flag=wx.LEFT,border=5)
topbox.Add(savebutton,proportion=0,flag=wx.LEFT,border=5)

bottombox =wx.BoxSizer(wx.VERTICAL)#第二个box上下结构布局，是整体的一个大Box
bottombox.Add(topbox,proportion=0,flag=wx.EXPAND|wx.ALL,border=5)
bottombox.Add(inputframe,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT,border=5)

panel.SetSizer(bottombox)

basicframe.Show()
app.MainLoop()