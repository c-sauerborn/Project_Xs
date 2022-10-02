from tkinter import *
from tkinter import ttk


class SceneSettingsWidget(Frame):
    def __init__(self, parent=None):
        ttk.Labelframe.__init__(self, parent, text="Controls")
        self.grid(in_=parent, padx=5, pady=5)
        self.init_variables()
        self.init_widgets()
        self.update_widgets_with_variables()

    def init_widgets(self):
        # Widgets
        menu_check_cbox = ttk.Checkbutton(self, text="+1 on menu close",
            variable=self.var_menu_check)
        time_delay_lb = ttk.Label(self,text="Time Delay")
        self.time_delay_spbox = Spinbox(self, from_= 0, to = 999, width = 5, increment=0.1)
        advance_delay_lb = ttk.Label(self,text="Advance Delay")
        self.advance_delay_spbox = Spinbox(self, from_= 0, to = 999, width = 5, increment=1)
        advance_delay_2_lb = ttk.Label(self,text="Advance Delay 2")
        self.advance_delay_2_spbox = Spinbox(self, from_= 0, to = 999, width = 5, increment=1)
        npcs_lb = ttk.Label(self,text="NPCs")
        self.npcs_spbox = Spinbox(self, from_= 0, to = 999, width = 5, increment=1)
        npcs_during_timeline_lb = ttk.Label(self,text="NPCs during Timeline")
        self.npcs_during_timeline_spbox = Spinbox(self, from_= -1, to = 999, width = 5, increment=1)
        pkm_npcs_lb = ttk.Label(self,text="Pokemon NPCs")
        self.pkm_npcs_spbox = Spinbox(self, from_= 0, to = 999, width = 5, increment=1)
        
        # Column 0
        menu_check_cbox.grid(column=0, row=0, columnspan = 2, sticky = W, padx = 5, pady =5)
        time_delay_lb.grid(column=0, row=1, sticky = W, padx = 5, pady =5)
        advance_delay_lb.grid(column=0, row=2, sticky = W, padx = 5, pady =5)
        advance_delay_2_lb.grid(column=0, row=3, sticky = W, padx = 5, pady =5)
        npcs_lb.grid(column=0, row=4, sticky = W, padx = 5, pady =5)
        npcs_during_timeline_lb.grid(column=0, row=5, sticky = W, padx = 5, pady =5)
        pkm_npcs_lb.grid(column=0, row=6, sticky = W, padx = 5, pady =5)

        # Column 1
        # menu_check_cbox takes row 1
        self.time_delay_spbox.grid(column=1, row=1, sticky = W, padx=5, pady=5)
        self.advance_delay_spbox.grid(column=1, row=2, sticky = W, padx=5, pady=5)
        self.advance_delay_2_spbox.grid(column=1, row=3, sticky = W, padx=5, pady=5)
        self.npcs_spbox.grid(column=1, row=4, sticky = W, padx=5, pady=5)
        self.npcs_during_timeline_spbox.grid(column=1, row=5, sticky = W, padx=5, pady=5)
        self.pkm_npcs_spbox.grid(column=1, row=6, sticky = W, padx=5, pady=5)

    def init_variables(self):
        self.var_menu_check = BooleanVar(value = TRUE)
        self.var_time_delay = IntVar(value = 0)
        self.var_advance_delay = IntVar(value = 0)
        self.var_advance_delay_2 = IntVar(value= 0)
        self.var_npcs = IntVar(value = 0)
        self.var_npcs_during_timeline = IntVar(value = 0)
        self.var_pkm_npcs = IntVar(value = 0)

    def update_widgets_with_variables(self):
        self.time_delay_spbox.delete(0, END)
        self.advance_delay_spbox.delete(0, END)
        self.advance_delay_2_spbox.delete(0, END)
        self.npcs_spbox.delete(0, END)
        self.npcs_during_timeline_spbox.delete(0, END)
        self.pkm_npcs_spbox.delete(0, END)

        self.time_delay_spbox.insert(0, self.var_time_delay.get())
        self.advance_delay_spbox.insert(0, self.var_advance_delay.get())
        self.advance_delay_2_spbox.insert(0, self.var_advance_delay_2.get())
        self.npcs_spbox.insert(0, self.var_npcs.get())
        self.npcs_during_timeline_spbox.insert(0, self.var_npcs_during_timeline.get())
        self.pkm_npcs_spbox.insert(0, self.var_pkm_npcs.get())

    def on_config_select(self, menu_check: bool, time_delay: int, advance_delay: int, advance_delay_2: int, npcs: int, npcs_during_timeline: int, pkm_npcs: int):
        self.var_menu_check.set(menu_check)
        self.var_time_delay.set(time_delay)
        self.var_advance_delay.set(advance_delay)
        self.var_advance_delay_2.set(advance_delay_2)
        self.var_npcs.set(npcs)
        self.var_npcs_during_timeline(npcs_during_timeline)
        self.var_pkm_npcs(pkm_npcs)
        self.update_widgets_with_variables()


if __name__ == "__main__":
    SceneSettingsWidget()
