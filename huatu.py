#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Function:��ͼ
    Input��NONE
    Output: NONE
    author: socrates
    blog:http://www.cnblogs.com/dyx1024/
    date:2012-07-15
'''  

import wx
import wx.lib.buttons
import cPickle
import os
import wx.g  rid,psutil
class SimpleGid(wx.grid.Grid):
    def __init__(self,parent):
        wx.grid.Grid.__init__(self,parent)
        proclist=psutil.pids()
        listnum=len(proclist)
        self.CreateGrid(listnum,2)
        self.SetColLabelValue( 0, "PROSS NAME" )  
        self.SetColLabelValue( 1, "PROSS " )# 设置列的名称
        self.SetColSize ( 0, 250)
        self.SetColSize ( 1, 250)
        i=0
        j=1
        
        for pid in proclist:
            
            self.SetCellValue(i,0,str(pid))
            i=i+1 
            
            
            
            
           
class ProcessFrame(wx.Frame):
    
    def __init__(self, parent):
        self.title = "Process Frame"
        wx.Frame.__init__(self, parent, -1, self.title, size = (800, 600))
        
        
        #״̬��
        #self.paint.Bind(wx.EVT_MOTION, self.OnPaintMotion)
        self.InitStatusBar()
        
        #�����˵�
        self.CreateMenuBar()
        
        self.filename = ""
        self.Creategrid()
        #����������ʹ�õ����
        #self.CreatePanel()
    def Creategrid(self):
        SimpleGid(self)
        
    def CreatePanel(self):
        controlPanel = ControlPanel(self, -1, self.paint)
        box = wx.BoxSizer(wx.HORIZONTAL) #����ˮƽ��box sizer
        box.Add(controlPanel, 0, wx.EXPAND) #ˮƽ������չʱ���ı�ߴ�
        #box.Add(self.paint, -1, wx.EXPAND)
        self.SetSizer(box)
        

        
    def InitStatusBar(self):
        self.statusbar = self.CreateStatusBar()
        #��״̬���ָ�Ϊ3������,����Ϊ1:2:3
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-1, -2, -3])   
        
    def OnPaintMotion(self, event):
        
        #����״̬��1����
        self.statusbar.SetStatusText(u"���λ�ã�" + str(event.GetPositionTuple()), 0)
        
        #����״̬��2����
        self.statusbar.SetStatusText(u"��ǰ�������ȣ�%s" % len(self.paint.curLine), 1)
        
        #����״̬��3����
        self.statusbar.SetStatusText(u"������Ŀ��%s" % len(self.paint.lines), 2)   
             
        event.Skip()
        
    def MenuData(self):
        '''
                   �˵�����
        '''
        #��ʽ���˵����ݵĸ�ʽ������(��ǩ, (��Ŀ))�����У���Ŀ���Ϊ����ǩ, ��������, ������, ��ѡ��kind
        #��ǩ����Ϊ2����Ŀ�ĳ�����3��4
        return [("&File", (             #һ���˵���
                           ("&New", "New paint file", self.OnNew),             #�����˵���
                           ("&Open", "Open paint file", self.OnOpen),
                           ("&Save", "Save paint file", self.OnSave),
                           ("", "", ""),                                       #�ָ���
                           ("&Color", (
                                       ("&Black", "", self.OnColor, wx.ITEM_RADIO),  #�����˵����ѡ
                                       ("&Red", "", self.OnColor, wx.ITEM_RADIO),
                                       ("&Green", "", self.OnColor, wx.ITEM_RADIO), 
                                       ("&Blue", "", self.OnColor, wx.ITEM_RADIO),
                                       ("&Other", "", self.OnOtherColor, wx.ITEM_RADIO))),
                           ("", "", ""),
                           ("&Quit", "Quit", self.OnCloseWindow)))
               ]  
    def CreateMenuBar(self):
        '''
        �����˵�
        '''
        menuBar = wx.MenuBar()
        for eachMenuData in self.MenuData():
            menuLabel = eachMenuData[0]
            menuItems = eachMenuData[1]
            menuBar.Append(self.CreateMenu(menuItems), menuLabel) 
        self.SetMenuBar(menuBar)
        
    def CreateMenu(self, menuData):
        '''
        ����һ���˵�
        '''
        menu = wx.Menu()
        for eachItem in menuData:
            if len(eachItem) == 2:
                label = eachItem[0]
                subMenu = self.CreateMenu(eachItem[1])
                menu.AppendMenu(wx.NewId(), label, subMenu) #�ݹ鴴���˵���
            else:
                self.CreateMenuItem(menu, *eachItem)
        return menu
    
    def CreateMenuItem(self, menu, label, status, handler, kind = wx.ITEM_NORMAL):
        '''
        �����˵�������
        '''
        if not label:
            menu.AppendSeparator()
            return
        menuItem = menu.Append(-1, label, status, kind)
        self.Bind(wx.EVT_MENU, handler,menuItem)
    
    def OnNew(self, event):
        pass
    
    def OnOpen(self, event):
        '''
        �򿪿��ļ��Ի���
        '''
        file_wildcard = "Paint files(*.paint)|*.paint|All files(*.*)|*.*" 
        dlg = wx.FileDialog(self, "Open paint file...",
                            os.getcwd(), 
                            style = wx.OPEN,
                            wildcard = file_wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetPath()
            self.ReadFile()
            self.SetTitle(self.title + '--' + self.filename)
        dlg.Destroy()
        
        
    
    def OnSave(self, event): 
        '''
        �����ļ�
        '''
        if not self.filename:
            self.OnSaveAs(event)
        else:
            self.SaveFile()
            
    def OnSaveAs(self, event):
        '''
        �����ļ�����Ի���
        '''
        file_wildcard = "Paint files(*.paint)|*.paint|All files(*.*)|*.*" 
        dlg = wx.FileDialog(self, 
                            "Save paint as ...",
                            os.getcwd(),
                            style = wx.SAVE | wx.OVERWRITE_PROMPT,
                            wildcard = file_wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetPath()
            if not os.path.splitext(filename)[1]: #���û���ļ�����׺
                filename = filename + '.paint'
            self.filename = filename
            self.SaveFile()
            self.SetTitle(self.title + '--' + self.filename)
        dlg.Destroy()    
                   
    
    def OnColor(self, event):
        '''
        ���Ļ�������
        '''
        menubar = self.GetMenuBar()
        itemid = event.GetId()
        item = menubar.FindItemById(itemid)
        color = item.GetLabel() #��ȡ�˵�������
        self.paint.SetColor(color)
        
    def OnOtherColor(self, event):
        '''
        ʹ����ɫ�Ի���
        '''
        dlg = wx.ColourDialog(self)
        dlg.GetColourData().SetChooseFull(True)   #������ɫ��������
        if dlg.ShowModal() == wx.ID_OK:
            self.paint.SetColor(dlg.GetColourData().GetColour()) #����ѡ�����û�����ɫ
        dlg.Destroy()
        
    def OnCloseWindow(self, event):
        self.Destroy()
        
    def SaveFile(self):
        '''
        �����ļ�
        '''
        if self.filename:
            data = self.paint.GetLinesData()
            f = open(self.filename, 'w')
            cPickle.dump(data, f)
            f.close()
                     
    def ReadFile(self):
        if self.filename:
            try:
                f = open(self.filename, 'r')
                data = cPickle.load(f)
                f.close()
                self.paint.SetLinesData(data)
            except cPickle.UnpicklingError:
                wx.MessageBox("%s is not a paint file."
                              % self.filename, "error tip",
                              style = wx.OK | wx.ICON_EXCLAMATION)
     
class ControlPanel(wx.Panel):
    BMP_SIZE = 16 
    BMP_BORDER = 3
    NUM_COLS = 4
    SPACING = 4
    
    colorList = ('Black', 'Yellow', 'Red', 'Green', 'Blue', 'Purple',
                 'Brown', 'Aquamarine', 'Forest Green', 'Light Blue',
                 'Goldenrod', 'Cyan', 'Orange', 'Navy', 'Dark Grey',
                 'Light Grey')
    maxThickness = 16
    
    def __init__(self, parent, ID, paint):
        wx.Panel.__init__(self, parent, ID, style = wx.RAISED_BORDER)
        self.paint = paint
        buttonSize = (self.BMP_SIZE + 2 * self.BMP_BORDER,
                      self.BMP_SIZE + 2 * self.BMP_BORDER)
        colorGrid = self.createColorGrid(parent, buttonSize) #������ɫgrid sizer
        thicknessGrid = self.createThicknessGrid(buttonSize) #��������grid sizer
        self.layout(colorGrid, thicknessGrid)
        
    def createColorGrid(self, parent, buttonSize):
        self.colorMap = {}
        self.colorButtons = {}
        colorGrid = wx.GridSizer(cols = self.NUM_COLS, hgap = 2, vgap = 2)
        for eachColor in self.colorList:
            bmp = self.MakeBitmap(eachColor)
            b = wx.lib.buttons.GenBitmapToggleButton(self, -1, bmp, size = buttonSize)
            b.SetBezelWidth(1)
            b.SetUseFocusIndicator(False)
            self.Bind(wx.EVT_BUTTON, self.OnSetColour, b)
            colorGrid.Add(b, 0)
            self.colorMap[b.GetId()] = eachColor
            self.colorButtons[eachColor] = b
        self.colorButtons[self.colorList[0]].SetToggle(True)
        return colorGrid
    
    def createThicknessGrid(self, buttonSize):
        self.thicknessIdMap = {}
        self.thicknessButtons = {}
        thicknessGrid = wx.GridSizer(cols = self.NUM_COLS, hgap = 2, vgap = 2)
        for x in range(1, self.maxThickness + 1):
            b = wx.lib.buttons.GenToggleButton(self, -1, str(x), size = buttonSize)
            b.SetBezelWidth(1)
            b.SetUseFocusIndicator(False)
            self.Bind(wx.EVT_BUTTON, self.OnSetThickness, b)
            thicknessGrid.Add(b, 0)
            self.thicknessIdMap[b.GetId()] = 2
            self.thicknessButtons[x] = b
        self.thicknessButtons[1].SetToggle(True)
        return thicknessGrid
    
    def layout(self, colorGrid, thicknessGrid):
        box = wx.BoxSizer(wx.VERTICAL) #ʹ�ô�ֱ��box szier����grid sizer
        box.Add(colorGrid, 0, wx.ALL, self.SPACING) #����0��ʾ�ڴ�ֱ������չʱ���ı�ߴ�
        box.Add(thicknessGrid, 0, wx.ALL, self.SPACING)
        self.SetSizer(box)
        box.Fit(self)
            
    def OnSetColour(self, event):
        color = self.colorMap[event.GetId()]
        if color != self.paint.color:
            self.colorButtons[self.paint.color].SetToggle(False)
        self.paint.SetColor(color)
        
    def OnSetThickness(self, event):
        thickness = self.thicknessIdMap[event.GetId()]
        if thickness != self.paint.thickness:
            self.thicknessButtons[self.paint.thickness].SetToggle(False)
        self.paint.SetThickness(thickness)

    def MakeBitmap(self, color):
        bmp = wx.EmptyBitmap(16, 15)
        dc = wx.MemoryDC(bmp)
        dc.SetBackground(wx.Brush(color))
        dc.Clear()
        dc.SelectObject(wx.NullBitmap)
        return bmp
        
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = ProcessFrame(None)
    frame.Show(True)
    app.MainLoop()
