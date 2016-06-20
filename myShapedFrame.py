#! /usr/bin/env python

"""Create shaped frame"""

import wx

class MyFrame(wx.Frame):
    
    def __init__(self, parent, id=-1, title='', pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.CAPTION | wx.CLOSE_BOX | wx.FRAME_EX_CONTEXTHELP, name='MyFrame'):
        wx.Frame.__init__(self, parent, id, title, pos, size, style, name)
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('TURQUOISE')
        
class ShapedFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Shaped Window",
                style = wx.FRAME_SHAPED | wx.SIMPLE_BORDER)  #| wx.FRAME_NO_TASKBAR)
        self.hasShape = False     
        #self.delta = wx.Point(0,0)                   
        self.bmp = wx.Bitmap(r'C:\PROJECTS\PythonProjects\MywxPythonDemo\img\but.png')                #(1) Получение изображения
        self.bmp.SetMask(wx.Mask(self.bmp, wx.BLACK)) 
        self.SetClientSize((self.bmp.GetWidth(), self.bmp.GetHeight()))
        dc = wx.ClientDC(self)                             #(2) Рисование изображения
        dc.DrawBitmap(self.bmp, 0,0, True)
        self.SetWindowShape()
        self.Bind(wx.EVT_LEFT_DCLICK, self.OnDoubleClick)
        self.Bind(wx.EVT_RIGHT_UP, self.OnExit)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_WINDOW_CREATE, self.SetWindowShape)#(3) Подключение события создания окна
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        self.Bind(wx.EVT_MOTION, self.OnMouseMove)
                                                         
    def SetWindowShape(self, evt=None):                  
        r = wx.Region(self.bmp)                
        self.hasShape = self.SetShape(r)                    #(4) Установка формы
                                                  
    def OnDoubleClick(self, evt):
        if self.hasShape:    
            self.SetShape(wx.Region())                      #(5) Переключение формы                         
            self.hasShape = False
        else:
            self.SetWindowShape()
            
    def OnPaint(self, evt):
        dc = wx.PaintDC(self)
        dc.DrawBitmap(self.bmp, 0,0, True)
        
    def OnExit(self, evt):
        self.Close()

    def OnLeftDown(self, evt):
        self.CaptureMouse()
        pos = self.ClientToScreen(evt.GetPosition())
        origin = self.GetPosition()
        self.delta = wx.Point(pos.x - origin.x, pos.y - origin.y)

    def OnMouseMove(self, evt):
        if evt.Dragging() and evt.LeftIsDown():
            pos = self.ClientToScreen(evt.GetPosition())
            newPos = (pos.x - self.delta.x, pos.y - self.delta.y)
            self.Move(newPos)

    def OnLeftUp(self, evt):
        if self.HasCapture():
            self.ReleaseMouse()
            
class MyApp(wx.App):
    
    def OnInit(self):
        self.frame = ShapedFrame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True
    
if __name__ == '__main__':
    app = wx.App() 
    ShapedFrame().Show()
    app.MainLoop()
    
