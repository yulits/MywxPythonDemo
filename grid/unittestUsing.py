import unittest
import flintstonizeMVC
                                                
import wx
                                                 
class TestExample(unittest.TestCase): # (1) Объявление тест-контейнера
                                   
    def setUp(self):                  # (2) Настройка каждого теста  
        self.app = wx.App()
        self.frame = flintstonizeMVC.ModelExample(parent=None, id=-1)
                                      
    def tearDown(self):               # (3) Завершение каждого теста
        self.frame.Destroy()
                                        
    def testModel(self):              # (4) Объявление теста
        self.frame.OnBarney(None)
        self.assertEqual("Barney", self.frame.model.first,
             msg="First is wrong")    # (5) Контрольная директива, которая может потерпеть неудачу
        self.assertEqual("Rubble", self.frame.model.last)
        
    def testModel2(self):              # (4) Объявление теста
        self.frame.OnFred(None)
        self.assertEqual("Fred", self.frame.model.first,
             msg="First is wrong")    # (5) Контрольная директива, которая может потерпеть неудачу
        self.assertEqual("Flintstone", self.frame.model.last)
        
    def testEvent(self):
        panel = self.frame.GetChildren()[0]
        for each in panel.GetChildren():
            if each.GetLabel() == "Wilmafy":
                wilma = each
                break
        event = wx.CommandEvent(wx.wxEVT_COMMAND_BUTTON_CLICKED, #целочисленная константа типа события
                                wilma.GetId())
        wilma.GetEventHandler().ProcessEvent(event)
        self.assertEqual("Wilma", self.frame.model.first)
        self.assertEqual("Flintstone", self.frame.model.last)
                                                                   
def suite():                          # (6) Создание тест-комплекта                                   
    suite = unittest.makeSuite(TestExample, 'test')               
    return suite                                                  
if __name__ == '__main__':
    unittest.main(defaultTest='suite')# (7) Запуск теста