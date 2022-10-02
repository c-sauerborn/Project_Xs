from tkinter import *
from tkinter import ttk
from turtle import color


class SeedsWidget(Frame):
    def __init__(self, parent=None):
        ttk.Labelframe.__init__(self, parent, text="Seeds")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.init_widgets()
        self.insert_values()

    def init_widgets(self):
        # Widgets
        s_0_3_label = ttk.Label(self, text="S[0-3]:")
        self.s_0_3_text = Text(self, width=10, height=4,
                               state=DISABLED, bg='#D3D3D3', fg="#000000")
        s_0_1_label = ttk.Label(self, text="S[0-1]:")
        self.s_0_1_text = Text(self, width=20, height=2,
                               state=DISABLED, bg='#D3D3D3', fg="#000000")

        # Column 0
        s_0_3_label.grid(column=0, row=0, sticky=W, padx=5, pady=5)
        s_0_1_label.grid(column=0, row=1, sticky=W, padx=5, pady=5)

        # Column 1
        self.s_0_3_text.grid(column=1, row=0, sticky=W, padx=5, pady=5)
        self.s_0_1_text.grid(column=1, row=1, sticky=W, padx=5, pady=5)

    def insert_values(self):
        self.s_0_3_text.configure(state=NORMAL)
        self.s_0_3_text.insert("1.0", "ABCABCBC")
        self.s_0_3_text.configure(state=DISABLED)
        self.s_0_1_text.configure(state=NORMAL)
        self.s_0_1_text.insert("1.0", "")
        self.s_0_1_text.configure(state=DISABLED)

if __name__ == "__main__":
    SeedsWidget()
