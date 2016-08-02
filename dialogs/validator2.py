import wx
import pprint

about_txt = """\
В данном примере валидатор используется для демонстрации
возможности автоматической передачи данных в и из текстового поля
при открытии и закрытии диалога."""

# объявляем валидатор
class DataXferValidator(wx.Validator):
    def __init__(self, data, key):
        wx.Validator.__init__(self)
        self.data = data
        self.key = key

    def Clone(self):
        """
        Будьте внимательны: каждый валидатор должен реализовать метод Clone()
        """
        return DataXferValidator(self.data, self.key)
    
    # не проверяем данные
    def Validate(self, win):
        return True
    
    # вызывается при открытии диалога
    def TransferToWindow(self):
        textCtrl = self.GetWindow()
        textCtrl.SetValue(self.data.get(self.key, ""))
        return True
    
    # вызывается при закрытии диалога
    def TransferFromWindow(self):
        textCtrl = self.GetWindow()
        self.data[self.key] = textCtrl.GetValue()
        return True

class MyDialog(wx.Dialog):
    def __init__(self, data):
        wx.Dialog.__init__(self, None, -1, "Validators: data transfer")

        about = wx.StaticText(self, -1, about_txt)
        name_l = wx.StaticText(self, -1, "Name:")
        email_l = wx.StaticText(self, -1, "Email:")
        phone_l = wx.StaticText(self, -1, "Phone:")

        name_t = wx.TextCtrl(self, validator=DataXferValidator(data, "name"))
        email_t = wx.TextCtrl(self, validator=DataXferValidator(data, "email"))
        phone_t = wx.TextCtrl(self, validator=DataXferValidator(data, "phone"))

        okay = wx.Button(self, wx.ID_OK)
        okay.SetDefault()
        cancel = wx.Button(self, wx.ID_CANCEL)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(about, 0, wx.ALL, 5)
        sizer.Add(wx.StaticLine(self), 0, wx.EXPAND|wx.ALL, 5)

        fgs = wx.FlexGridSizer(3, 2, 5, 5)
        fgs.Add(name_l, 0, wx.ALIGN_RIGHT)
        fgs.Add(name_t, 0, wx.EXPAND)
        fgs.Add(email_l, 0, wx.ALIGN_RIGHT)
        fgs.Add(email_t, 0, wx.EXPAND)
        fgs.Add(phone_l, 0, wx.ALIGN_RIGHT)
        fgs.Add(phone_t, 0, wx.EXPAND)
        fgs.AddGrowableCol(1)
        sizer.Add(fgs, 0, wx.EXPAND|wx.ALL, 5)

        btns = wx.StdDialogButtonSizer()
        btns.AddButton(okay)
        btns.AddButton(cancel)
        btns.Realize()
        sizer.Add(btns, 0, wx.EXPAND|wx.ALL, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)

app = wx.App()

data = { "name" : "Jordyn Dunn" }
dlg = MyDialog(data)
dlg.ShowModal()
dlg.Destroy()
wx.MessageBox("You entered these values:\n\n" + pprint.pformat(data))
app.MainLoop()