#! /usr/bin/env python

"""Output redirection"""

import wx, os

class MyFrame(wx.Frame):
    
    def __init__(self, parent, id=-1, title='', pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE ^ wx.CLOSE_BOX, name='MyFrame'):
        wx.Frame.__init__(self, parent, id, title, pos, size, style, name)
       

class MyApp(wx.App):
    
    def OnInit(self):
        self.frame = MyFrame(parent = None)
        self.frame.Show()
        print('App OnInit') 
        self.SetTopWindow(self.frame)
        return True
    
if __name__ == '__main__':
    app = MyApp(True, r'D:\PythonRMSProjects\roxarAPI\output.txt')
    print('Before MainLoop') 
    app.MainLoop()
    print('After MainLoop') 
