import wx

class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="tree: misc tests", size=(400,500))

        il = wx.ImageList(16,16)

        self.fldridx = il.Add(wx.ArtProvider.GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, (16,16)))
        self.fldropenidx = il.Add(wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN,   wx.ART_OTHER, (16,16)))
        self.fileidx = il.Add(wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, (16,16)))
        
        self.tree = wx.TreeCtrl(self, style=wx.TR_DEFAULT_STYLE | wx.TR_EDIT_LABELS)

        self.tree.AssignImageList(il)

        root = self.tree.AddRoot("wx.Object")
        self.tree.SetItemPyData(root, None)
        self.tree.SetItemImage(root, self.fldridx,wx.TreeItemIcon_Normal)
        self.tree.SetItemImage(root, self.fldropenidx,wx.TreeItemIcon_Expanded)
        
        tree = ["A","B","C","D","E","F","G","H"]

        self.AddTreeNodes(root, tree)

        self.tree.Expand(root)

        menu = wx.Menu()
        mi = menu.Append(-1, "Sort Children")
        self.Bind(wx.EVT_MENU, self.OnSortChildren, mi)
        
        
        mb = wx.MenuBar()
        mb.Append(menu, "Tests")
        self.SetMenuBar(mb)

    def OnSortChildren(self, evt):
        item = self.tree.GetSelection()
        if item:
            self.tree.SortChildren(item)

    def PrintAllItems(self, parent, indent=0):
        text = self.tree.GetItemText(parent)
        print(' '* indent,text)
        indent += 4
        item, cookie = self.tree.GetFirstChild(parent)
        while item:
            if self.tree.ItemHasChildren(item):
                self.PrintAllItems(item, indent)
            else:
                text = self.tree.GetItemText(item)
                print(' ' * indent, text)
            item, cookie = self.tree.GetNextChild(parent, cookie)

    def AddTreeNodes(self, parentItem, items):
        for item in items:
            if type(item) == str:
                newItem = self.tree.AppendItem(parentItem, item)
                self.tree.SetItemPyData(newItem, None)
                self.tree.SetItemImage(newItem, self.fileidx,wx.TreeItemIcon_Normal)
            else:
                newItem = self.tree.AppendItem(parentItem, item[0])
                self.tree.SetItemPyData(newItem, None)
                self.tree.SetItemImage(newItem, self.fldridx,wx.TreeItemIcon_Normal)
                self.tree.SetItemImage(newItem, self.fldropenidx,wx.TreeItemIcon_Expanded)
   
                self.AddTreeNodes(newItem, item[1])

app = wx.App(redirect=True)
frame = TestFrame()
frame.Show()
app.MainLoop()
