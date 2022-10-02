from tkinter import *
from tkinter import ttk 
from advancesWidget import AdvancesWidget
from cameraWidget import CameraWidget
from configWidget import ConfigWidget
from seedsWidget import SeedsWidget
from eyesWidget import EyesWidget
from controlsWidget import ControlsWidget
from sceneSettingsWidgets import SceneSettingsWidget

class Application(Frame):
    def __init__(self, master:Tk = None):
        super().__init__(master)
        self.master = master
        self.initWindow(master)
        self.initWidgets()
    
    def initWindow(self, master:Tk = None):
        self.master.title('Project XS')

    def initWidgets(self):
        self.grid(column=0, row=0, sticky=(N,W,E,S))
        self.grid_columnconfigure(index = 0, weight= 1, minsize = 200)
        self.grid_rowconfigure(index = 0, weight= 1)
        self.grid_columnconfigure(index = 1, weight= 0)
        self.grid_rowconfigure(index = 1, weight= 0)
        AdvancesWidget(self.master).grid(column=0, row=0, sticky = NW)
        CameraWidget(self.master).grid(column=1, row=0, sticky = NW)
        ConfigWidget(self.master).grid(column=3, row=0, sticky = NW)
        SeedsWidget(self.master).grid(column=4, row=0, sticky = NW)
        EyesWidget(self.master).grid(column=0, row=1, sticky = NW)
        ControlsWidget(self.master).grid(column=1, row=1, sticky = NW)
        SceneSettingsWidget(self.master).grid(column=2, row=1, sticky = NW)


root = Tk()
app = Application(master = root)
root.mainloop()
