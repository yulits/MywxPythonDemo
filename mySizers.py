#! /usr/bin/env python

"""spare.py is a starting point for a wxPython program."""

import wx
#import wx.lib.platebtn as pbtn

class MyFrame(wx.Frame):
    
    def __init__(self, parent, id=-1, title='Script', pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX , name='MyFrame'):
        wx.Frame.__init__(self, parent, id, title, pos, size, style, name)
        self.panel = wx.Panel(self)
        #self.panel.SetBackgroundColour(wx.Colour(198, 226, 255))
        
        gridLst = "grid1 grid2 grid3".split()
        paramLst = "parap1 param2 param3".split()
        
        self.selGridLbl = wx.StaticText(self.panel, -1, 'Select grid')
        self.selGridLst = wx.Choice(self.panel, -1, size=(200,-1), choices = gridLst)
        
        self.selParamLbl = wx.StaticText(self.panel, -1, "Select parameter")
        self.selParamLst = wx.Choice(self.panel, -1, size=(200,-1), choices = paramLst)
        
        self.paramCodeLbl = wx.StaticText(self.panel, -1, "Parameter code")
        self.paramCodeEdt = wx.TextCtrl(self.panel, -1, "", size = (200, -1))
        
        self.distCellLbl = wx.StaticText(self.panel, -1, "Distance cell")
        self.distCellEdt = wx.TextCtrl(self.panel, -1, "", size = (200, -1))
        
        self.discripLbl = wx.StaticText(self.panel, -1, "Bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla")
        
        self.numProcBtn = wx.Button(self.panel, -1, label="N.Procs")
        self.numProcBtn.Enable(False)
        
        self.createdByLbl = wx.StaticText(self.panel, -1, "created by")
                                        
        self.helpBtn = wx.Button(self.panel, -1, label="Help")
        self.runBtn = wx.Button(self.panel, -1, label="Run")
        self.cancelBtn = wx.Button(self.panel, -1, label="Cancel")
        
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.selSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
        self.selSizer.AddGrowableCol(1)
        self.selSizer.Add(self.selGridLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 10)
        self.selSizer.Add(self.selGridLst, 0, wx.EXPAND)
        self.selSizer.Add(self.selParamLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 10)
        self.selSizer.Add(self.selParamLst, 0, wx.EXPAND)
        self.selSizer.Add(self.paramCodeLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 10)
        self.selSizer.Add(self.paramCodeEdt, 0, wx.EXPAND)
        self.selSizer.Add(self.distCellLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 10)
        self.selSizer.Add(self.distCellEdt, 0, wx.EXPAND)
       
        self.mainSizer.Add(self.selSizer, 0, wx.EXPAND|wx.ALL, 10) 
        self.mainSizer.Add(wx.StaticLine(self.panel), 0, wx.EXPAND|wx.ALL, 5)
        self.mainSizer.Add(self.discripLbl, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 10)
        self.mainSizer.Add((20,20), 1)
        
        self.infoSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.infoSizer.Add(self.numProcBtn)
        self.infoSizer.Add((20,20), 1)
        self.infoSizer.Add(self.createdByLbl)
        self.mainSizer.Add(self.infoSizer, 0, wx.EXPAND|wx.ALL, 10)
         
        self.mainSizer.Add(wx.StaticLine(self.panel), 0, wx.EXPAND|wx.ALL, 5)
        self.runSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.runSizer.Add(self.helpBtn)
        self.runSizer.Add((20,20), 1)
        self.runSizer.Add(self.runBtn)
        self.runSizer.Add((20,20), 1)
        self.runSizer.Add(self.cancelBtn)
        self.mainSizer.Add(self.runSizer, 0, wx.EXPAND|wx.ALL, 10)
        self.panel.SetSizer(self.mainSizer)

        # Fit the frame to the needs of the sizer.  The frame will
        # automatically resize the panel as needed.  Also prevent the
        # frame from getting smaller than this size.
        self.mainSizer.Fit(self)
        self.mainSizer.SetSizeHints(self)
        self.Bind(wx.EVT_CHOICE, self.onGridChoice, self.selGridLst)
        self.Bind(wx.EVT_CHOICE, self.onParamChoice, self.selParamLst)
        
    def onGridChoice(self, event):
        print(event.GetString())
        
    def onParamChoice(self, event):
        print(event.getValue())
        
class MyApp(wx.App):
    
    def OnInit(self):
        self.frame = MyFrame(parent = None)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True
    
if __name__ == '__main__':
    app = MyApp() 
    app.MainLoop()
    
