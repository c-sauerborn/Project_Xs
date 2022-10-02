from tkinter import *
from tkinter import ttk 

class ConfigWidget(Frame):
    def __init__(self, parent=None):
        ttk.Labelframe.__init__(self, parent, text = "Config")
        self.grid(in_=parent, padx=5, pady=5)
        self.init_variables()
        self.init_widgets()

    def init_widgets(self):
        # Widgets
        config_lb = ttk.Label(self, text="Configuration: ")
        config_cbox = ttk.Combobox(self, state="readonly", textvariable=self.var_selected_config, values=[])
        config_cbox.bind("<<ComboboxSelected>>", self.on_config_select) 
        # configCombobox.bind("<Button-1>", self.update_configs)
        add_config_btn = ttk.Button(self,text="Add Config", width=18) #command=self.new_config
        save_config_btn = ttk.Button(self, text="Save Config", width=18) #command=self.save_config

        # Column 0
        config_lb.grid(column=0, row=0, sticky = W,padx=5, pady=5)

        # Column 1
        config_cbox.grid(column=1,row=0, padx=5, pady=5)

        # Column 2
        add_config_btn.grid(column=2, row=0, columnspan=2, sticky = W, padx=5, pady=5)
        save_config_btn.grid(column=2, row=1, columnspan=2, sticky = W, padx=5, pady=5)

    def init_variables(self):
        self.var_selected_config = StringVar(value="")
        #self.update_configs()

    def on_config_select(self):
        print(f"Config selected to {self.var_selected_config}")
        # update config

if __name__ == "__main__":
    ConfigWidget()
