import wx
import wx.adv
# создаём простую страницу
class TitledPage(wx.adv.WizardPageSimple):
    def __init__(self, parent, title):
        wx.adv.WizardPageSimple.__init__(self, parent)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.sizer)
        titleText = wx.StaticText(self, -1, title)
        titleText.SetFont(
        wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
        self.sizer.Add(titleText, 0, wx.ALIGN_CENTRE | wx.ALL, 5)
        self.sizer.Add(wx.StaticLine(self, -1), 0, wx.EXPAND | wx.ALL, 5)
if __name__ == "__main__":
    app = wx.App()
    # создаём экземпляр мастера
    wizard = wx.adv.Wizard(None, -1, "Simple Wizard")
    # создаём страницы мастера
    page1 = TitledPage(wizard, "Page 1")
    page2 = TitledPage(wizard, "Page 2")
    page3 = TitledPage(wizard, "Page 3")
    page4 = TitledPage(wizard, "Page 4")
    page1.sizer.Add(wx.StaticText(page1, -1, "Testing the wizard"))
    page4.sizer.Add(wx.StaticText(page4, -1, "This is the last page."))
    # задаём последовательность страниц
    page1.SetNext(page2)
    page2.SetNext(page3)
    page3.SetNext(page4)
    # задаём размер мастера
    wizard.FitToPage(page1)
    # запускаем мастера
    if wizard.RunWizard(page1):
        print("Success")