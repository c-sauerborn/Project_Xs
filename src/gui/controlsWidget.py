from tkinter import *
from tkinter import ttk


class ControlsWidget(Frame):
    def __init__(self, parent=None):
        ttk.Labelframe.__init__(self, parent, text="Controls")
        self.grid(in_=parent, padx=5, pady=5)
        self.init_variables()
        self.init_widgets()

    def init_widgets(self):
        # Widgets
        monitor_blinks_btn = ttk.Button(
            self, text="Monitor Blinks")  # command=self.monitor_blinks
        reident_btn = ttk.Button(
            self, text="Reidentify")  # command=self.reidentify
        preview_btn = ttk.Button(
            self, text="Preview")  # command=self.preview
        stop_tracking_btn = ttk.Button(
            self, text="Stop Tracking")  # command=self.stop_tracking
        timeline_btn = ttk.Button(
            self, text="Timeline")  # command=self.timeline
        tid_sid_btn = ttk.Button(self, text="TID/SID")  # command=self.tidsid
        reident_noisy_cbox = ttk.Checkbutton(self, text="Reident 1 PK NPC",
                                                   variable=self.var_reident_noisy_check)
        reident_min_lb = ttk.Label(self,text="Reident Min:")
        self.reident_min_sbox = Spinbox(self, from_= 0, to = 9999999999)
        reident_max_lb = ttk.Label(self,text="Reident Max:")
        self.reident_max_sbox = Spinbox(self, from_= 0, to = 9999999999, textvariable=self.var_reident_max)

        # Column 0
        monitor_blinks_btn.grid(column=0, row=0, columnspan=2, padx=5, pady=5)
        reident_btn.grid(column=0, row=1, columnspan=2, padx=5, pady=5)
        preview_btn.grid(column=0, row=2, columnspan=2, padx=5, pady=5)
        stop_tracking_btn.grid(column=0, row=3, columnspan=2, padx=5, pady=5)
        timeline_btn.grid(column=0, row=4, columnspan=2, padx=5, pady=5)
        tid_sid_btn.grid(column=0, row=5, columnspan=2, padx=5, pady=5)
        reident_noisy_cbox.grid(column=0, row=6, columnspan=2, padx=5, pady=5)
        reident_min_lb.grid(column=0, row=7, padx=5, pady=5)
        reident_max_lb.grid(column=0, row=8, padx=5, pady=5)

        # Column 1
        self.reident_min_sbox.grid(column=1, row=7, padx=5, pady=5)
        self.reident_max_sbox.grid(column=1, row=8, padx=5, pady=5)

    def init_variables(self):
        self.var_reident_noisy_check = BooleanVar(value=FALSE)
        self.var_reident_min = IntVar(value = 0)
        self.var_reident_max = IntVar(value = 9999999999)

    def update_widgets_with_variables(self):
        self.reident_min_sbox.delete(0, END)
        self.reident_max_sbox.delete(0, END)

        self.reident_min_sbox.insert(0, self.var_reident_min.get())
        self.reident_max_sbox.insert(0, self.var_reident_max.get())


    def on_config_select(self, reident_min: int, reident_max: int):
        self.var_reident_min.set(reident_min)
        self.var_reident_max.set(reident_max)
        # update config


if __name__ == "__main__":
    ControlsWidget()
