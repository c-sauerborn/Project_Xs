from tkinter import *
from tkinter import ttk 

class AdvancesWidget(Frame):
    def __init__(self, parent=None):
        ttk.Labelframe.__init__(self, parent, text="Advances")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.init_variables()
        self.init_widgets()
        self.update_widgets_with_variables()

    def init_widgets(self):
        # Widgets
        progress_lb = ttk.Label(self,text="Progress:")
        progress_number_lb = ttk.Label(self,text=f"{self.var_progress.get()}/{self.var_max_progres.get()}")
        advances_lab = ttk.Label(self,text="Advances:")
        advances_number_lb = ttk.Label(self,text=self.var_advances.get())
        timer_lb = ttk.Label(self,text="Timer:")
        timer_number_lb = ttk.Label(self,text=self.count_down.get())
        x_to_advance_lb = ttk.Label(self,text="X to advance:")        
        self.x_to_advance_spbox = Spinbox(self, from_ = 0, to = 999999)
        advance_btn = ttk.Button(self, text="Advance")
        key_press_advance_lb = ttk.Label(self,text="Keypress Advance:")
        self.key_press_advance_spbox = self.keypress_advance = Spinbox(self, from_ = 0, to = 999999)


        # Column 0
        progress_lb.grid(column=0, row=0, sticky=W, padx=5, pady=5)
        advances_lab.grid(column=0, row=1, sticky = W,padx=5, pady=5)
        timer_lb.grid(column=0, row=2, sticky = W,padx=5, pady=5)
        x_to_advance_lb.grid(column=0, row=3, sticky = W,padx=5, pady=5)
        key_press_advance_lb.grid(column=0,row=4, sticky = W, padx=5, pady=5)

        #Column 1
        progress_number_lb.grid(column=1, row=0, padx=5, pady=5)
        advances_number_lb.grid(column=1, row=1, padx=5, pady=5)
        timer_number_lb.grid(column=1, row=2, padx=5, pady=5)
        self.x_to_advance_spbox.grid(column=1, row=3, padx=5, pady=5)
        self.key_press_advance_spbox.grid(column=1,row=4, padx=5, pady=5)
        advance_btn.grid(column=1, row=5, padx=5, pady=5)


    def init_variables(self):
        self.var_x_to_advance = IntVar(value = 0)
        self.var_key_press_advance = IntVar(value = 0)
        self.var_advances = IntVar(value= 0)
        self.count_down = IntVar(value = 0)
        self.var_progress = IntVar(value = 0)
        self.var_max_progres = IntVar(value = 0)

    def update_widgets_with_variables(self):
        self.x_to_advance_spbox.delete(0, END)
        self.key_press_advance_spbox.delete(0, END)

        self.x_to_advance_spbox.insert(0, self.var_x_to_advance.get())
        self.key_press_advance_spbox.insert(0, self.var_key_press_advance.get())

if __name__ == "__main__":
    AdvancesWidget()
