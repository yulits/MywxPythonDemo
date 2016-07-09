import wx
class BitmapButtonFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Bitmap Button Example',
                size=(500, 400))
        panel = wx.Panel(self, -1)
        bmp = wx.Bitmap("bird.png", wx.BITMAP_TYPE_PNG)#.ConvertToBitmap()
        bmpSize = bmp.GetSize()
        self.button = wx.BitmapButton(panel, -1, bmp, pos=(10, 20), size=bmpSize)
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        self.button.SetDefault()
        bmp = wx.Bitmap("mam.png", wx.BITMAP_TYPE_PNG)
        self.button2 = wx.BitmapButton(panel, -1, bmp, pos=(150, 20),
            style=0)
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button2)
    def OnClick(self, event):
        self.Destroy()
if __name__ == '__main__':
    app = wx.App()
    frame = BitmapButtonFrame()
    frame.Show()
    app.MainLoop()