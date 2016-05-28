#! /usr/bin/env python

"""spare.py is a starting point for a wxPython program."""

import wx, os

class MyFrame(wx.Frame):
    
    def __init__(self, parent, id=-1, title='', pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE, name='MyFrame'):
        wx.Frame.__init__(self, parent, id, title, pos, size, style, name)
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('TURQUOISE')
        
        dlg = wx.MessageDialog(None, 'Did he bump her for that awesome girl?', 'New Message', wx.YES_NO | wx.ICON_QUESTION)
        res = dlg.ShowModal()
        dlg.Destroy()
        print("You pressed", res)
        
        dlg = wx.TextEntryDialog(None, "What's your name", 'Enter name', 'None')
        if dlg.ShowModal() == wx.ID_OK:
            print("Your name is ", dlg.GetValue())
            
        dlg = wx.SingleChoiceDialog(None, 'Choose your age?', 'Single choice', ['31','32','33','34'])
        if dlg.ShowModal() == wx.ID_OK:
            print('Your age:', dlg.GetStringSelection())

class MyApp(wx.App):
    
    def OnInit(self):
        self.frame = MyFrame(parent = None)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True
    
if __name__ == '__main__':
    app = MyApp() 
    app.MainLoop()
    
