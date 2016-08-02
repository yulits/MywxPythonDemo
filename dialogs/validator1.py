import wx
about_txt = """\
Валидатор, используемый в этом примере проверяет наличие текста в
текстовых полях при нажатии на кнопку "ок" и не даёт Вам закрыть диалог,
если это условие не выполняется."""

# создаём подкласс валидатора
class NotEmptyValidator(wx.Validator):
    def __init__(self):
        wx.Validator.__init__(self)

    def Clone(self):
        """
        Обратите внимание, что каждый валидатор должен реализовать метод Clone().
        """
        return NotEmptyValidator()

    # метод проверки
    def Validate(self, win):
        textCtrl = self.GetWindow()
        text = textCtrl.GetValue()

        if len(text) == 0:
            wx.MessageBox("This field must contain some text!", "Error")
            textCtrl.SetBackgroundColour("pink")
            textCtrl.SetFocus()
            textCtrl.Refresh()
            return False
        else:
            textCtrl.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
            textCtrl.Refresh()
            return True

    def TransferToWindow(self):
        return True

    def TransferFromWindow(self):
        return True

class MyDialog(wx.Dialog):
    def __init__(self):
            wx.Dialog.__init__(self, None, -1, "Validators: validating")
            
            # Создаём поля для ввода текста
            about = wx.StaticText(self, -1, about_txt)
            name_l = wx.StaticText(self, -1, "Name:")
            email_l = wx.StaticText(self, -1, "Email:")
            phone_l = wx.StaticText(self, -1, "Phone:")
            
            # используем валидаторы
            name_t = wx.TextCtrl(self, validator=NotEmptyValidator())
            email_t = wx.TextCtrl(self, validator=NotEmptyValidator())
            phone_t = wx.TextCtrl(self, validator=NotEmptyValidator())

            # Используем стандартные ID кнопок
            okay = wx.Button(self, wx.ID_OK)
            okay.SetDefault()
            cancel = wx.Button(self, wx.ID_CANCEL)

            # размещаем виджеты с помощью координаторов
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

dlg = MyDialog()
dlg.ShowModal()
dlg.Destroy()

app.MainLoop()