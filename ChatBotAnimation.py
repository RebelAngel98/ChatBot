import wx
from wx.adv import Animation, AnimationCtrl


class Main_Panel(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, title='Quit Now & Cake Will Be Served Immediately')
        sizer = wx.BoxSizer(wx.VERTICAL)
        my_animation_asset = Animation('Glados.gif')
        my_animation_control = AnimationCtrl(self, -1, my_animation_asset)
        my_animation_control.Play()
        sizer.Add(my_animation_control)
        self.SetSizerAndFit(sizer)
        self.Show()
        my_animation_control


if __name__ == '__main__':
    app = wx.App()
    Main_Panel(None)

    app.MainLoop()