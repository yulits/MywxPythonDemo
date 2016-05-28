import time
import wx
  

########################################################################
class MyFrame(wx.Frame):
 
    #----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, title="Progress Bar Tutorial")
 
        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)
        self.btn =  wx.Button(panel, label="Start", pos = (10, 10))
        self.btn.Bind(wx.EVT_BUTTON, self.updateProgress)
 
        #sizer = wx.BoxSizer(wx.VERTICAL)
        #sizer.Add(btn, 0, wx.ALL|wx.CENTER, 5)
        #panel.SetSizer(sizer)
        
        self.count = 0
 
        self.progress = wx.Gauge(panel, range=30, pos = (10, 50), size = (300, 25))
 
        #sizer2 = wx.BoxSizer(wx.VERTICAL)
        #sizer2.Add(self.progress, 0, wx.EXPAND)
        #self.SetSizer(sizer2)

        
    def updateProgress(self, event):
        """
        Update the progress bar
        """
        
        for i in range(30):
            time.sleep(0.2)
            self.count += 1
            self.progress.SetValue(self.count)
 
#----------------------------------------------------------------------
# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    frame.Show()
    app.MainLoop()