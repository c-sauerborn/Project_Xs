from tkinter import *
from tkinter import ttk 

class CameraWidget(Frame):
    def __init__(self, parent=None):
        ttk.Labelframe.__init__(self, parent, text="Camera")
        self.grid(in_=parent, padx=5, pady=5)
        self.initVariables()
        self.initWidgets()

    def initWidgets(self):
        # Widgets
        windowPrefixLabel = ttk.Label(self, text="Capture Window Prefix: ")
        windowPrefixInput = ttk.Entry(self, textvariable=self.windowPrefix)
        cameraLabel = ttk.Label(self,text="Camera:")
        cameraIndexSpinBox = Spinbox(self, from_= 0, to = 99, width = 5, textvariable=self.cameraIndex)
        monitorWindowCbox = ttk.Checkbutton(self,text="Monitor Window", variable=self.shouldMonitorWindow)
        displayPercentLabel = ttk.Label(self,text="Display Percent")
        displayPercentSpinBox = Spinbox(self, from_ = 0, to = 500, textvariable=self.displayPercentage)

        # Column 0
        windowPrefixLabel.grid(column=0, row=0, sticky = W, padx=5, pady=5)
        displayPercentLabel.grid(column=0, row=1, sticky = W, padx=5, pady=5)

        # Column 1
        # eyeDisplay spans in row 1 here
        windowPrefixInput.grid(column=1,row=0, padx=5, pady=5)
        displayPercentSpinBox.grid(column=1,row=1, padx=5, pady=5)

        # Column 2
        monitorWindowCbox.grid(column=2,row=0, columnspan=2, sticky = W, padx=5, pady=5)
        cameraLabel.grid(column=2, row=1, sticky = W, padx=5, pady=5)

        # Column 3
        # addConfigButtons spans here in row 0
        # monitorWindowCbox spans here in row 1
        cameraIndexSpinBox.grid(column=3,row=2, padx=5, pady=5)

    def initVariables(self):
        self.shouldMonitorWindow = BooleanVar(value = FALSE)
        self.cameraIndex = StringVar(value = "0")
        self.windowPrefix = StringVar(value = "Add window prefix")
        self.displayPercentage = IntVar(value = 100)

    def onConfigUpdate(self, config):
        self.shouldMonitorWindow = config.shouldMonitorWindow
        self.cameraIndex = config.cameraIndex
        self.windowPrefix = config.windowPrefix
        self.displayPercentage = config.displayPercentage

if __name__ == "__main__":
    CameraWidget()
