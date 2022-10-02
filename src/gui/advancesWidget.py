from tkinter import *
from tkinter import ttk 

class AdvancesWidget(Frame):
    def __init__(self, parent=None):
        ttk.Labelframe.__init__(self, parent, text="Advances")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.initVariables()
        self.initWidgets()

    def initWidgets(self):
        # Widgets
        advancesLabel = ttk.Label(self,text="Advances:")
        numberOfAdvancesLabel = ttk.Label(self,text=self.advances)
        timerLabel = ttk.Label(self,text="Timer:")
        timerCountLabel = ttk.Label(self,text=self.count_down)
        xToAdvanceLabel = ttk.Label(self,text="X to advance:")        
        self.advanceSpinBox = Spinbox(self, from_ = 0, to = 999999)
        advanceButton = ttk.Button(self, text="Advance")
        keyPressAdvanceLabel = ttk.Label(self,text="Keypress Advance:")
        self.keypressAdvanceSpinBox = self.keypress_advance = Spinbox(self, from_ = 0, to = 999999)


        # Column 0
        advancesLabel.grid(column=0, row=0, sticky = W,padx=5, pady=5)
        timerLabel.grid(column=0, row=1, sticky = W,padx=5, pady=5)
        xToAdvanceLabel.grid(column=0, row=2, sticky = W,padx=5, pady=5)
        keyPressAdvanceLabel.grid(column=0,row=3, sticky = W, padx=5, pady=5)

        #Column 1
        numberOfAdvancesLabel.grid(column=1, row=0, padx=5, pady=5)
        timerCountLabel.grid(column=1, row=1, padx=5, pady=5)
        self.advanceSpinBox.grid(column=1, row=2, padx=5, pady=5)
        advanceButton.grid(column=1, row=3, padx=5, pady=5)
        self.keypressAdvanceSpinBox.grid(column=1,row=14, padx=5, pady=5)


    def initVariables(self):
        self.advances = 0
        self.count_down = 0

    def insertValues(self):
        self.advanceSpinBox.insert("1.0", 0)
        self.keypressAdvanceSpinBox.insert("1.0", 0)

    def get(self):
        return self.entry.get()

if __name__ == "__main__":
    AdvancesWidget()
