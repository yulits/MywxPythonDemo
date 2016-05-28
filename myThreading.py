
#! /usr/bin/env python

"""spare.py is a starting point for a wxPython program."""

import wx
import threading, sys

class MyThread(threading.Thread):
    cancelFlag = False
    def __init__(self):
        threading.Thread.__init__(self)
        
        
    def run(self):
        self.summ = 0
        tot = 100000000
        for i in range(tot):
            if  i % 10000000 == 0: print('i = ', i, ' cancelFlag = ', MyThread.cancelFlag)
            if MyThread.cancelFlag: 
                print('Shut down of ', tot, 'on', i)
                sys.exit(0)
            self.summ += i
        print('Sum of ', tot, ':', self.summ)

class MyFrame(wx.Frame):
    
    def __init__(self, parent, id=-1, title='', pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE, name='MyFrame'):
        wx.Frame.__init__(self, parent, id, title, pos, size, style, name)
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('TURQUOISE')
        self.newBtn = wx.Button(self.panel, label='New')
        self.Bind(wx.EVT_BUTTON, self.onClick, self.newBtn)
        
        self.cancelBtn = wx.Button(self.panel, label='Cancel', pos=(100,-1))
        self.Bind(wx.EVT_BUTTON, self.onCancel, self.cancelBtn)
    
    def onClick(self, event):
        th = MyThread()
        th.start()
        th2 = MyThread()
        th2.start()
    
    def onCancel(self, event):
        MyThread.cancelFlag = True

class MyApp(wx.App):
    
    def OnInit(self):
        self.frame = MyFrame(parent = None)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True
    
if __name__ == '__main__':
    app = MyApp() 
    app.MainLoop()
    
