import wx
import string

about_txt = """\
Валидатор, используемый в данном примере проверяет "на лету" ввод данных
пользователем и не ждёт нажатия кнопки "ок". Первое поле не допускает
ввода цифр, во второе поле можно ввести всё, что угодно, а в третье - 
всё, кроме букв.
"""

class CharValidator(wx.Validator):
    def __init__(self, flag):
        wx.Validator.__init__(self)
        self.flag = flag
        # связываем функцию с событием ввода символа
        self.Bind(wx.EVT_CHAR, self.OnChar)

    def Clone(self):
        """
        Будьте внимательны: каждый валидатор должен реализовать метод Clone()
        """
        return CharValidator(self.flag)

    def Validate(self, win):
        return True

    def TransferToWindow(self):
        return True

    def TransferFromWindow(self):
        return True

    # обработчик ввода данных в виджет
    def OnChar(self, evt):
        key = chr(evt.GetKeyCode())
        if self.flag == "no-alpha" and key.isalpha():
            return
        if self.flag == "no-digit" and key.isdigit():
            return
        evt.Skip()

class MyDialog(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, "Validators: behavior modification")

        # Создаём поля для ввода текста
        about = wx.StaticText(self, -1, about_txt)
        name_l = wx.StaticText(self, -1, "Name:")
        email_l = wx.StaticText(self, -1, "Email:")
        phone_l = wx.StaticText(self, -1, "Phone:")

        # добавляем валидатор
        name_t = wx.TextCtrl(self, validator=CharValidator("no-digit"))
        email_t = wx.TextCtrl(self, validator=CharValidator("any"))
        phone_t = wx.TextCtrl(self, validator=CharValidator("no-alpha"))
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

dlg = MyDialog()
dlg.ShowModal()
dlg.Destroy()

app.MainLoop()