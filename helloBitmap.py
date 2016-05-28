#! /usr/bin/env python

"""hello.py shows a picture in a frame."""

import wx 
import os.path

imgDir=os.path.dirname(__file__) + '\\img'
preDir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'img'))

print(imgDir, preDir)

class Frame(wx.Frame):
    """Frame class that displays an image"""
    
    def __init__(self, parent=None, id=-1, pos=wx.DefaultPosition, size = wx.DefaultSize, title="Hello, wxPython!"):
        """Create a Frame instance and display image"""
        img = wx.Bitmap(imgDir+'\\th.jpg', wx.BITMAP_TYPE_JPEG)#.ConvertToBitmap()
        #temp = wx.Bitmap(img)
        #temp = img.ConvertToBitmap()
        size = img.GetWidth(), img.GetHeight()    
        wx.Frame.__init__(self, parent, id, title, pos, size)
        self.panel  = wx.Panel(self)
        self.bmp = wx.StaticBitmap(self.panel, label=img)

class App(wx.App):
    """Application class"""
    def OnInit(self):
        self.frame = Frame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True
    
def main():
    app = App() 
    app.MainLoop()
    
if __name__ == '__main__':
    main()
