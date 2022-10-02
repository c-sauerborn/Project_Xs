from tkinter import *
from tkinter import ttk 

class ConfigWidget(Frame):
    def __init__(self, parent=None):
        ttk.Labelframe.__init__(self, parent, text = "Config")
        self.grid(in_=parent, padx=5, pady=5)
        self.initVariables()
        self.initWidgets()

    def initWidgets(self):
        # Widgets
        configLabel = ttk.Label(self, text="Configuration: ")
        configCombobox = ttk.Combobox(self, state="readonly", textvariable=self.selectedConfig, values=[])
        configCombobox.bind("<<ComboboxSelected>>", self.onConfigSelect) 
        # configCombobox.bind("<Button-1>", self.update_configs)
        addConfigButton = ttk.Button(self,text="Add Config", width=18) #command=self.new_config
        saveConfigButton = ttk.Button(self, text="Save Config", width=18) #command=self.save_config

        # Column 0
        configLabel.grid(column=0, row=0, sticky = W,padx=5, pady=5)

        # Column 1
        configCombobox.grid(column=1,row=0, padx=5, pady=5)

        # Column 2
        addConfigButton.grid(column=2, row=0, columnspan=2, sticky = W, padx=5, pady=5)
        saveConfigButton.grid(column=2, row=1, columnspan=2, sticky = W, padx=5, pady=5)

    def initVariables(self):
        self.selectedConfig = StringVar(value="")
        #self.update_configs()

    def onConfigSelect(self):
        print(f"Config selected to {self.selectedConfig}")
        # update config

if __name__ == "__main__":
    ConfigWidget()
