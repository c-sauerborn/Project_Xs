from tkinter import *
from tkinter import ttk


class ControlsWidget(Frame):
    def __init__(self, parent=None):
        ttk.Labelframe.__init__(self, parent, text="Controls")
        self.grid(in_=parent, padx=5, pady=5)
        self.initVariables()
        self.initWidgets()

    def initWidgets(self):
        # Widgets
        monitorBlinksButton = ttk.Button(
            self, text="Monitor Blinks")  # command=self.monitor_blinks
        reidentifyButton = ttk.Button(
            self, text="Reidentify")  # command=self.reidentify
        previewButton = ttk.Button(
            self, text="Preview")  # command=self.preview
        stopTrackingButton = ttk.Button(
            self, text="Stop Tracking")  # command=self.stop_tracking
        timelineButton = ttk.Button(
            self, text="Timeline")  # command=self.timeline
        tidSidButton = ttk.Button(self, text="TID/SID")  # command=self.tidsid
        reidentNoisyCheckBox = ttk.Checkbutton(self, text="Reident 1 PK NPC",
                                                   variable=self.reidentNoisyCheck)
        reidentMinLabel = ttk.Label(self,text="Reident Min:")
        reidentMinSpinBox = Spinbox(self, from_= 0, to = 9999999999, textvariable = self.reidentMin)
        reidentMaxLabel = ttk.Label(self,text="Reident Max:")
        reidentMaxSpinBox = Spinbox(self, from_= 0, to = 9999999999, textvariable=self.reidentMax)

        # Column 0
        monitorBlinksButton.grid(column=0, row=0, columnspan=2, padx=5, pady=5)
        reidentifyButton.grid(column=0, row=1, columnspan=2, padx=5, pady=5)
        previewButton.grid(column=0, row=2, columnspan=2, padx=5, pady=5)
        stopTrackingButton.grid(column=0, row=3, columnspan=2, padx=5, pady=5)
        timelineButton.grid(column=0, row=4, columnspan=2, padx=5, pady=5)
        tidSidButton.grid(column=0, row=5, columnspan=2, padx=5, pady=5)
        reidentNoisyCheckBox.grid(column=0, row=6, columnspan=2, padx=5, pady=5)
        reidentMinLabel.grid(column=0, row=7, padx=5, pady=5)
        reidentMaxLabel.grid(column=0, row=8, padx=5, pady=5)

        # Column 1
        reidentMinSpinBox.grid(column=1, row=7, padx=5, pady=5)
        reidentMaxSpinBox.grid(column=1, row=8, padx=5, pady=5)

    def initVariables(self):
        self.reidentNoisyCheck = BooleanVar(value=FALSE)
        self.reidentMin = IntVar(value = 0)
        self.reidentMax = IntVar(value = 0)
        # self.update_configs()

    def onConfigSelect(self):
        print(f"Config selected to {self.selectedConfig}")
        # update config


if __name__ == "__main__":
    ControlsWidget()
