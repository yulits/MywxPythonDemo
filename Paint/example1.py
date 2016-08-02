import wx
class SketchWindow(wx.Window):
    def __init__(self, parent, ID):
        wx.Window.__init__(self, parent, ID)
        self.SetBackgroundColour("White")
        self.color = "Black"                                               
        self.thickness = 1
        self.pen = wx.Pen(self.color, self.thickness, wx.SOLID) # (1) Создание объекта wx.Pen
        self.lines = []
        self.curLine = []
        self.pos = (0, 0)                                  
        self.InitBuffer()                                   
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)            # (2) Присоединение событий
        self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        self.Bind(wx.EVT_MOTION, self.OnMotion)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_IDLE, self.OnIdle)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
                                     
    def InitBuffer(self):                                       # (3) Создание контекста устройства с буферизацией 
        size = self.GetClientSize()
        self.buffer = wx.Bitmap(size.width, size.height)
        dc = wx.BufferedDC(None, self.buffer)
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))  # (4) Использование контекста устройства
        dc.Clear()
        self.DrawLines(dc)
        self.reInitBuffer = False  
    
    def Clear(self):
        dc = wx.BufferedDC(None, self.buffer)
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))  # (4) Использование контекста устройства
        dc.Clear()
        self.Refresh()
                                        
    def GetLinesData(self):
        return self.lines[:]
    
    def SetLinesData(self, lines):
        self.lines = lines[:]
        self.InitBuffer()
        self.Refresh()
        
    def OnLeftDown(self, event):
        self.curLine = []
        self.pos = event.GetPosition()                     # (5) Получение позиции мыши
        self.CaptureMouse()        
                                                            # (6) Захват мыши
    def OnLeftUp(self, event):
        if self.HasCapture():
            self.lines.append((self.color,
                self.thickness,
                self.curLine))
            self.curLine = []
            self.ReleaseMouse()                                 # (7) Освобождение мыши
                                                            
    def OnMotion(self, event):
        if event.Dragging() and event.LeftIsDown():             # (8) Определение продолжения операции перетаскивания
            dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)  # (9) Создание другого контекста с буферизацией
            self.drawMotion(dc, event)
        event.Skip()                                   
                                                      
    def drawMotion(self, dc, event):                            # (10) Рисование в контексте устройства 
        dc.SetPen(self.pen)
        newPos = event.GetPosition()  
        coords = self.pos + newPos              
        self.curLine.append(coords)                
        dc.DrawLine(self.pos, newPos)
        self.pos = newPos

    def OnSize(self, event):                                   # (11) Обработка события изменения размера
        self.reInitBuffer = True
 
    def OnIdle(self, event):                                   # (12) Обработка простоя
        if self.reInitBuffer:
            self.InitBuffer()
            self.Refresh(False)

    def OnPaint(self, event):                                  # (13) Обработка запроса на прорисовку
        dc = wx.BufferedPaintDC(self, self.buffer)

    def DrawLines(self, dc):                                   # (14) Рисование всех линий
        for colour, thickness, line in self.lines:
            pen = wx.Pen(colour, thickness, wx.SOLID)
            dc.SetPen(pen)           
            for i in range(len(line)-1):
                dc.DrawLine(line[i], line[i+1])

    def SetColor(self, color):
        self.color = color
        self.pen = wx.Pen(self.color, self.thickness, wx.SOLID)

    def SetThickness(self, num):
        self.thickness = num
        self.pen = wx.Pen(self.color, self.thickness, wx.SOLID)

class SketchFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "Sketch Frame", size=(800,600))
        self.sketch = SketchWindow(self, -1)

if __name__ == '__main__':
    app = wx.App()
    frame = SketchFrame(None)
    frame.Show(True)
    app.MainLoop()