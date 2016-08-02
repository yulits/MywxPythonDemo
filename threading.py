import time
import wx
 
from threading import Thread
from wx.lib.pubsub import Publisher
 
########################################################################
class TestThread(Thread):
    """Test Worker Thread Class."""
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.start()    # запустить новый поток
 
    #----------------------------------------------------------------------
    def run(self):
        """Run Worker Thread."""
        # этот код выполняется в новом потоке
        for i in range(6):
            time.sleep(10)
            wx.CallAfter(self.postTime, i)
        time.sleep(5)
        wx.CallAfter(Publisher().sendMessage, "update", "Thread finished!")
 
    #----------------------------------------------------------------------
    def postTime(self, amt):
        """
        Посылаем время в GUI
        """
        amtOfTime = (amt + 1) * 10
        Publisher().sendMessage("update", amtOfTime)
 
########################################################################
class MyForm(wx.Frame):
 
    #----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Tutorial")
 
        # добавляем панель, чтобы это правильно выглядело на разных платформах
        panel = wx.Panel(self, wx.ID_ANY)
        self.displayLbl = wx.StaticText(panel, label="Amount of time since thread started goes here")
        self.btn = btn = wx.Button(panel, label="Start Thread")
 
        btn.Bind(wx.EVT_BUTTON, self.onButton)
 
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.displayLbl, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(btn, 0, wx.ALL|wx.CENTER, 5)
        panel.SetSizer(sizer)
 
        # создаём получателя pubsub
        Publisher().subscribe(self.updateDisplay, "update")
 
    #----------------------------------------------------------------------
    def onButton(self, event):
        """
        Запустить поток
        """
        TestThread()
        self.displayLbl.SetLabel("Thread started!")
        btn = event.GetEventObject()
        btn.Disable()
 
    #----------------------------------------------------------------------
    def updateDisplay(self, msg):
        """
        Получаем данные от потока и обновляем приложение
        """
        t = msg.data
        if isinstance(t, int):
            self.displayLbl.SetLabel("Time since thread started: %s seconds" % t)
        else:
            self.displayLbl.SetLabel("%s" % t)
            self.btn.Enable()
 
#----------------------------------------------------------------------
# Запускаем программу
if __name__ == "__main__":
    app = wx.App()
    frame = MyForm().Show()
    app.MainLoop()