import wx
import wx.lib.buttons as buttons
class GenericButtonFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Generic Button Example',
                size=(500, 350))
        panel = wx.Panel(self, -1)
        sizer = wx.FlexGridSizer(4, 3, 20, 20)
        b = wx.Button(panel, -1, "A wx.Button")
        b.SetDefault()
        sizer.Add(b)
        b = wx.Button(panel, -1, "non-default wx.Button")
        sizer.Add(b)
        sizer.Add((10,10))
                                                      
        b = buttons.GenButton(panel, -1, 'Generic Button')            # Базовая типовая кнопка
        sizer.Add(b)
        b = buttons.GenButton(panel, -1, 'disabled Generic')          # Блокированная типовая кнопка
        b.Enable(False)                    
        sizer.Add(b)                       
        b = buttons.GenButton(panel, -1, 'bigger')                    # Кнопка с заданным пользователем размером и цветом
        b.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.BOLD, False))
        b.SetBezelWidth(5)
        b.SetBackgroundColour("Navy")
        b.SetForegroundColour("white")
        b.SetToolTip("This is a BIG button...")
        sizer.Add(b)
                                                  
        bmp = wx.Image("bird.png",              
            wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        b = buttons.GenBitmapButton(panel, -1, bmp)                   # Типовая кнопка с битовым изображением
        sizer.Add(b)
        b = buttons.GenBitmapToggleButton(panel, -1, bmp)
        sizer.Add(b)     # Типовая кнопка-переключатель с битовым изображением
        b = buttons.GenBitmapTextButton(panel, -1, bmp,
            "Bitmapped Text", size=(175, 75))                         # Кнопка с битовым изображением и текстом
        b.SetUseFocusIndicator(False)                  
        sizer.Add(b)
        b = buttons.GenToggleButton(panel, -1, "Toggle Button")       # Типовая кнопка-переключатель
        sizer.Add(b)                              
        panel.SetSizer(sizer)
if __name__ == '__main__':
    app = wx.App()
    frame = GenericButtonFrame()
    frame.Show()
    app.MainLoop()