#! /usr/bin/env python

"""Creating a statusbar, a toolbar and a menubar."""

import wx, os

imgDir = os.path.dirname(__file__) + '\\img'

class MyFrame(wx.Frame):
    
    def __init__(self, parent, id=-1, title='', pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE, name='MyFrame'):
        wx.Frame.__init__(self, parent, id, title, pos, size, style, name)
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('TURQUOISE')
        
        statusBar = self.CreateStatusBar()
        self.createToolBar()
        self.createMenuBar()
        
    def createToolBar(self):
        toolBar = self.CreateToolBar()
        toolBar.SetToolBitmapSize((32,32))
        
        saveIco = wx.ArtProvider.GetBitmap(wx.ART_MINUS, wx.ART_TOOLBAR, (32,32))
        
        saveIco = wx.Bitmap(imgDir+'\\save.png', wx.BITMAP_TYPE_PNG)
        saveTool = toolBar.AddTool(wx.NewId(), "&Save", saveIco,  "Save the Curren Worksheet")
        self.Bind(wx.EVT_TOOL, self.onSave, saveTool)
        
        houseIco = wx.Bitmap(imgDir+'\\house.png', wx.BITMAP_TYPE_PNG)
        houseTool = toolBar.AddTool(wx.NewId(), "&House", houseIco,  "Go home")
        self.Bind(wx.EVT_TOOL, self.onHouse, houseTool)
        
        flashIco = wx.Bitmap(imgDir+'\\flash.png', wx.BITMAP_TYPE_PNG)
        flashTool = toolBar.AddTool(wx.NewId(), "F&lash", flashIco,  "It'smuseful in the dark")
        self.Bind(wx.EVT_TOOL, self.onFlash, flashTool)
        
        toolBar.AddSeparator()
        
        undoIco = wx.Bitmap(imgDir+'\\undo.png', wx.BITMAP_TYPE_PNG)
        undoTool = toolBar.AddTool(wx.ID_UNDO, "&Undo", undoIco,  "Go forward")
        toolBar.EnableTool(wx.ID_UNDO, False)
        self.Bind(wx.EVT_MENU, self.onUndo, undoTool)
        
        redoIco = wx.Bitmap(imgDir+'\\redo.png', wx.BITMAP_TYPE_PNG)
        redoTool = toolBar.AddTool(wx.ID_REDO, "&Redo", redoIco,  "Go backward")
        toolBar.EnableTool(wx.ID_REDO, False)
        self.Bind(wx.EVT_MENU, self.onRedo, redoTool)
        
        toolBar.Realize()
        
    def createMenuBar(self):
        """Creating menubar with accelarators"""
        def doBind(handler, item):
            """Creating menu events."""
            self.Bind(wx.EVT_MENU, handler, item)
        
         
        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        mSave = fileMenu.Append(wx.ID_SAVE, "&Save", "Save worksheet")
        mSave.Enable(False)
        mQuit = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+M')
        doBind(self.onQuit, mQuit)
        mQuit.SetBitmap(wx.Bitmap(imgDir+'\\door.png', wx.BITMAP_TYPE_PNG))
        accel_table = wx.AcceleratorTable([(wx.ACCEL_CTRL, ord('M'), mQuit.GetId())])   
        self.SetAcceleratorTable(accel_table)
        fileMenu.Append(mQuit)
        menuBar.Append(fileMenu, 'File')
        
        editMenu = wx.Menu()
        doBind(self.onCopy, editMenu.Append(wx.ID_COPY, "Copy", "Copy content"))
        doBind(self.onCut, editMenu.Append(wx.ID_CUT, "Cut", ""))
        doBind(self.onPaste, editMenu.Append(wx.ID_PASTE, "Paste", ""))
        editMenu.AppendSeparator()
        importMenu = wx.Menu()
        importMenu.Append(wx.NewId(), 'Import to MPEG', "")
        importMenu.Append(wx.NewId(), 'Import to AVI', "")
        importMenu.Append(wx.NewId(), 'Import to MKV', "")
        editMenu.Append(wx.NewId(), "Import...", importMenu)

        menuBar.Append(editMenu, "&Edit")
        
        self.SetMenuBar(menuBar)

    def onSave(self, e):
        print('Save tool pressed')
        
    def onCopy(self, e):
        print('COPY!')
        
    def onCut(self, e):
        print('CUT!')
    
    def onPaste(self, e):
        print('PASTE!')    
        
    def onHouse(self, e):
        pass
    
    def onFlash(self, e):
        pass
    
    def onCart(self, e):
        pass
    
    def onUndo(self, e):
        pass
    
    def onRedo(self, e):
        pass
    
    def onQuit(self, e):
        self.Close()
        
class MyApp(wx.App):
    
    def OnInit(self):
        self.frame = MyFrame(parent = None)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True
    
if __name__ == '__main__':
    app = MyApp() 
    app.MainLoop()
    
