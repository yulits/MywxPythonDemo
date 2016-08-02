import wx
import pickle
import os
import wx.lib.buttons as buttons
import wx.html, wx.adv#, wx.AppConsole 
from example1 import SketchWindow

class SketchFrame(wx.Frame):
    def __init__(self, parent):
        self.title = "Sketch Frame"
        wx.Frame.__init__(self, parent, -1, self.title, size=(800,600))
        self.filename = ""
        self.sketch = SketchWindow(self, -1)
        self.sketch.Bind(wx.EVT_MOTION, self.OnSketchMotion)
        self.initStatusBar()                                              # (1) Небольшой рефакторинг                                                
        self.createMenuBar()
        self.createToolBar()
        self.createPanel()                                                                    
    
    
    def initStatusBar(self):
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-1, -2, -3])
        
    def OnSketchMotion(self, event):
        self.statusbar.SetStatusText("Pos: %s" %
                str(event.GetPosition()), 0)
        self.statusbar.SetStatusText("Current Pts: %s" %
                len(self.sketch.curLine), 1)
        self.statusbar.SetStatusText("Line Count: %s" %
                len(self.sketch.lines), 2)
        event.Skip()

    def menuData(self):
        return [("&File", (
                ("&New", "New Sketch file", self.OnNew),
                ("&Open", "Open sketch file", self.OnOpen),
                ("&Save", "Save sketch file", self.OnSave),
                ("", "", ""),
                ("&Color", (
                    ("&Black", "", self.OnColor,
                             wx.ITEM_RADIO),
                    ("&Red", "", self.OnColor,
                             wx.ITEM_RADIO),
                    ("&Green", "", self.OnColor,
                             wx.ITEM_RADIO),
                    ("&Blue", "", self.OnColor,
                             wx.ITEM_RADIO),
                    ("&Other...", "", self.OnOtherColor,
                             wx.ITEM_RADIO))),
                ("", "", ""),
                ("&Quit", "Quit", self.OnCloseWindow))),
                ("&About", (
                ("&Info", "About app", self.OnAbout),
                #("Splash", "Splash window", self.OnSplash)
                ))
                ]
    
    def createMenuBar(self):
        menuBar = wx.MenuBar()
        for eachMenuData in self.menuData():
            menuLabel = eachMenuData[0]
            menuItems = eachMenuData[1]
            menuBar.Append(self.createMenu(menuItems), menuLabel)
        self.SetMenuBar(menuBar)
        
    def createMenu(self, menuData):
        menu = wx.Menu()                                                                        
        for eachItem in menuData:                                                               
            if len(eachItem) == 2:                                        # (3) Создание подменю
                label = eachItem[0]
                subMenu = self.createMenu(eachItem[1])
                menu.Append(wx.NewId(), label, subMenu)
            else:
                self.createMenuItem(menu, *eachItem)
        return menu
    
    def createMenuItem(self, menu, label, status, handler, kind=wx.ITEM_NORMAL):
        if not label:
            menu.AppendSeparator()
            return
        menuItem = menu.Append(-1, label, status, kind)                     # (4) Создание элементов меню с типом
        self.Bind(wx.EVT_MENU, handler, menuItem)
        
    def OnNew(self, event): 
        self.sketch.Clear()                                                                
     
    def OnCloseWindow(self, event):
        self.Destroy()
    
    def createToolBar(self):                                  # (1) Создание панели инструментов
        toolbar = self.CreateToolBar()
        for each in self.toolbarData():
            self.createSimpleTool(toolbar, *each)
        toolbar.AddSeparator()
        for each in self.toolbarColorData():
            self.createColorTool(toolbar, each)
        toolbar.Realize()
        
    def createSimpleTool(self, toolbar, label, filename, helpStr, handler):    # (3) Создание простых инструментов 
        if not label:
            toolbar.AddSeparator()                                        
            return
                                                             
        bmp = wx.Bitmap(filename, wx.BITMAP_TYPE_PNG)
        toolbar.SetToolBitmapSize((16,15))
        tool = toolbar.AddTool(-1,  label, bmp, helpStr)
        self.Bind(wx.EVT_MENU, handler, tool)
    
    def toolbarData(self):
        return (("New", "new.png", "Create new sketch",
                     self.OnNew),
                ("", "", "", ""),
                ("Open", "open.png", "Open existing sketch",
                     self.OnOpen),
                ("Save", "save.png", "Save existing sketch",
                     self.OnSave))
                                                  
                                                  
    def createColorTool(self, toolbar, color):                # (4) Создание инструментов выбора цвета
        bmp = self.MakeBitmap(color)
        #newId = wx.NewId()
        tool = toolbar.AddRadioTool(-1, '', bmp, shortHelp=color)
        self.Bind(wx.EVT_MENU, self.OnColor, tool)
        
    def MakeBitmap(self, color):                              # (5) Создание сплошного битового изображения
        bmp = wx.Bitmap(50, 50)
        dc = wx.MemoryDC()          
        dc.SelectObject(bmp)        
        dc.SetBackground(wx.Brush(color))
        dc.Clear()
        dc.SelectObject(wx.NullBitmap)
        return bmp
    
    def toolbarColorData(self):
        return ("Black", "Red", "Green", "Blue")
    
    def OnColor(self, event):
        menubar = self.GetMenuBar()
        itemId = event.GetId()
        item = menubar.FindItemById(itemId)
        if not item:                                           # (6) Изменение цвета при щелчке на панели инструментов
            toolbar = self.GetToolBar()
            item = toolbar.FindById(itemId)
            color = item.GetShortHelp()
        else:
            color = item.GetLabel()
        self.sketch.SetColor(color)
    
    def OnOtherColor(self, event):     
        dlg = wx.ColourDialog(self)
        dlg.GetColourData().SetChooseFull(True) # Создание объекта цветовых данных
        if dlg.ShowModal() == wx.ID_OK:
            self.sketch.SetColor(dlg.GetColourData().GetColour()) # Установка введенного пользователем цвета
        dlg.Destroy()
        
    def SaveFile(self):                                       #(1) Сохранение файла
        if self.filename:           
            data = self.sketch.GetLinesData()                               
            f = open(self.filename, 'wb')
            pickle.dump(data, f)
            f.close()
    
    def ReadFile(self):                                      #(2) Чтение файла
        if self.filename:
            try:
                f = open(self.filename, 'rb')
                data = pickle.load(f)
                f.close()
                self.sketch.SetLinesData(data)
            except pickle.UnpicklingError:
                wx.MessageBox("%s is not a sketch file."
                         % self.filename, "oops!",
                         style=wx.OK|wx.ICON_EXCLAMATION)
    wildcard = "Sketch files (*.sketch)|*.sketch|All files (*.*)|*.*"
    
    def OnOpen(self, event):                                #(3) Вывод диалога открытия
        dlg = wx.FileDialog(self, "Open sketch file...",                     
                 os.getcwd(), style=wx.FD_OPEN,
                 wildcard=self.wildcard)                
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetPath()
            self.ReadFile()
            self.SetTitle(self.title + ' -- ' + self.filename)
        dlg.Destroy()
    
    def OnSave(self, event):                                #(4) Сохранение файла
        if not self.filename:
            self.OnSaveAs(event)
        else:
            self.SaveFile()
            
    def OnSaveAs(self, event):
        dlg = wx.FileDialog(self, "Save sketch as...",     #(5) Вывод диалога сохранения
                os.getcwd(),
                style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT,
                wildcard=self.wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetPath()
            if not os.path.splitext(filename)[1]:          #(6) Поддержка расширения файла
                filename = filename + '.sketch'
            self.filename = filename
            self.SaveFile()
            self.SetTitle(self.title + ' -- ' +
                    self.filename)
        dlg.Destroy()
        
    def OnAbout(self, event):
        dlg = SketchAbout(self)
        dlg.ShowModal()
        dlg.Destroy()
        
#     def OnSplash(self, event):
#         bitmap = wx.Bitmap('cat.png', wx.BITMAP_TYPE_PNG)
#         wx.adv.SplashScreen(bitmap, wx.adv.SPLASH_CENTRE_ON_PARENT|wx.adv.SPLASH_TIMEOUT, 6000, self, -1, style=wx.NO_BORDER)
        
    def createPanel(self):
        controlPanel = ControlPanel(self, -1, self.sketch)
        box = wx.BoxSizer(wx.HORIZONTAL)
        box.Add(controlPanel, 0, wx.EXPAND)
        box.Add(self.sketch, 1, wx.EXPAND)
        self.SetSizer(box)
        
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
    
    def __init__(self, parent, ID, sketch):
        wx.Panel.__init__(self, parent, ID, style=wx.RAISED_BORDER)
        self.sketch = sketch
        buttonSize = (self.BMP_SIZE + 2 * self.BMP_BORDER,
                      self.BMP_SIZE + 2 * self.BMP_BORDER)
        colorGrid = self.createColorGrid(parent, buttonSize)
        thicknessGrid = self.createThicknessGrid(buttonSize)
        self.layout(colorGrid, thicknessGrid)
                                                             
    def createColorGrid(self, parent, buttonSize):            # (1) Создание сетки цветов 
        self.colorMap = {}
        self.colorButtons = {}
        colorGrid = wx.GridSizer(cols=self.NUM_COLS, hgap=2, vgap=2)
        for eachColor in self.colorList:
            bmp = parent.MakeBitmap(eachColor)
            b = buttons.GenBitmapToggleButton(self, -1, bmp,
                  size=buttonSize)
            b.SetBezelWidth(1)
            b.SetUseFocusIndicator(False)
            self.Bind(wx.EVT_BUTTON, self.OnSetColour, b)
            colorGrid.Add(b, 0)
            self.colorMap[b.GetId()] = eachColor
            self.colorButtons[eachColor] = b
        self.colorButtons[self.colorList[0]].SetToggle(True)
        return colorGrid
                                                         
    def createThicknessGrid(self, buttonSize):               # (2) Создание сетки размеров толщины
        self.thicknessIdMap = {}
        self.thicknessButtons = {}
        thicknessGrid = wx.GridSizer(cols=self.NUM_COLS, hgap=2,
            vgap=2)
        for x in range(1, self.maxThickness + 1):
            b = buttons.GenToggleButton(self, -1, str(x), size=buttonSize)
            b.SetBezelWidth(1)
            b.SetUseFocusIndicator(False)
            self.Bind(wx.EVT_BUTTON, self.OnSetThickness, b)
            thicknessGrid.Add(b, 0)
            self.thicknessIdMap[b.GetId()] = x
            self.thicknessButtons[x] = b
        self.thicknessButtons[1].SetToggle(True)
        return thicknessGrid
                                                             
    def layout(self, colorGrid, thicknessGrid):             # (3) Группировка сеток
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(colorGrid, 0, wx.ALL, self.SPACING)
        box.Add(thicknessGrid, 0, wx.ALL, self.SPACING)
        self.SetSizer(box)
        box.Fit(self)
    
    def OnSetColour(self, event):
        color = self.colorMap[event.GetId()]
        if color != self.sketch.color:
            self.colorButtons[self.sketch.color].SetToggle(False)
        self.sketch.SetColor(color)
        
    def OnSetThickness(self, event):
        thickness = self.thicknessIdMap[event.GetId()]
        if thickness != self.sketch.thickness:
            self.thicknessButtons[self.sketch.thickness].SetToggle(False)
        self.sketch.SetThickness(thickness)
        
class SketchAbout(wx.Dialog):
    text = '''
        <html>
        <body bgcolor="#ACAA60">
        <center><table bgcolor="#455481" width="100%" cellspacing="0"
        cellpadding="0" border="1">
        <tr>
             <td align="center"><h1>Sketch!</h1></td>
        </tr>
        </table>
        </center>
        <p><b>Sketch</b> is a demonstration program for
        <b>wxPython In Action</b>
        Chapter 6. It is based on the SuperDoodle demo included
        with wxPython, available at http://www.wxpython.org/
        </p>
        <p><b>SuperDoodle</b> and <b>wxPython</b> are brought to you by
        <b>Robin Dunn</b> and <b>Total Control Software</b>, Copyright
        &copy; 1997-2006.</p>
        </body>
        </html>
        '''
    
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, -1, 'About Sketch', size=(440, 400) )
        html = wx.html.HtmlWindow(self)
        html.SetPage(self.text)
        button = wx.Button(self, wx.ID_OK, "Okay")
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(html, 1, wx.EXPAND|wx.ALL, 5)
        sizer.Add(button, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        self.SetSizer(sizer)
        self.Layout()
    
class SketchApp(wx.App):
    def OnInit(self):
        bmp = wx.Bitmap("cat.png", wx.BITMAP_TYPE_PNG)
        wx.adv.SplashScreen(bmp, wx.adv.SPLASH_CENTRE_ON_SCREEN | wx.adv.SPLASH_TIMEOUT, 5000, None, -1, 
                            style=wx.NO_BORDER|wx.STAY_ON_TOP)

        wx.Yield()
        frame = SketchFrame(None)
        frame.Show(True)
        self.SetTopWindow(frame)
        return True
            
if __name__ == '__main__':
    app = SketchApp()
    app.MainLoop()