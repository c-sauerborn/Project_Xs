import os
from utils.converter import convertImageToImageTk
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

try:
    import cv2
    from tkinter import *
    from tkinter import ttk
    from PIL import ImageTk
    import os.path
    import tkinter.filedialog as fd
except ImportError as import_fail:
    raise \
    Exception("Could not import the required modules, " \
              "make sure you are running with the correct python version, " \
              "and that packages are installed correctly.") \
    from import_fail


class EyesWidget(Frame):
    def __init__(self, parent=None):
        ttk.Labelframe.__init__(self, parent, text="Eyes")
        self.init_variables()
        self.init_widgets()

    def init_widgets(self):
        # Widgets
        self.eye_display = ttk.Label(self, text="(Select an eye image)")
        x_lb = ttk.Label(self,text="X")
        x_spbox= Spinbox(self, from_= 0, to = 99999, width = 5, textvariable=self.var_pos_x)
        y_lb = ttk.Label(self,text="Y")
        y_spbox = Spinbox(self, from_= 0, to = 99999, width = 5, textvariable=self.var_pos_y)
        w_lb = ttk.Label(self,text="W")
        w_spbox = Spinbox(self, from_= 0, to = 99999, width = 5, textvariable=self.var_width)
        h_lb = ttk.Label(self,text="H")
        h_spbox = Spinbox(self, from_= 0, to = 99999, width = 5, textvariable=self.var_heigth)
        threshold_lb = ttk.Label(self,text="Threshold")
        threshold_spbox = Spinbox(self, from_= 0, to = 1, width = 5, increment=0.1, textvariable=self.var_threshold)
        new_eye_btn = ttk.Button(self, text="Select Eye", command=self.on_new_eye_click) #command=self.new_eye

        # Column 0
        x_lb.grid(column=0, row=0,  sticky = W, padx=5, pady=5)
        y_lb.grid(column=0, row=1,  sticky = W, padx=5, pady=5)
        w_lb.grid(column=0, row=2,  sticky = W, padx=5, pady=5)
        h_lb.grid(column=0, row=3,  sticky = W, padx=5, pady=5)
        threshold_lb.grid(column=0, row=4,  sticky = W, padx=5, pady=5)
        self.eye_display.grid(column=0, row=5, columnspan=2, padx=5, pady=5)
        new_eye_btn.grid(column=0, row=6, columnspan=2, padx=5, pady=5)
        
        # Column 0
        x_spbox.grid(column=1, row=0,  sticky = W, padx=5, pady=5)
        y_spbox.grid(column=1, row=1,  sticky = W, padx=5, pady=5)
        w_spbox.grid(column=1, row=2,  sticky = W, padx=5, pady=5)
        h_spbox.grid(column=1, row=3,  sticky = W, padx=5, pady=5)
        threshold_spbox.grid(column=1, row=4,  sticky = W, padx=5, pady=5)
        # eyeDisplay spans in row 5
        # newEyeButton spans in row 6

    def init_variables(self):
        self.var_pos_x = IntVar(value = 0)
        self.var_pos_y = IntVar(value = 0)
        self.var_width = IntVar(value = 0)
        self.var_heigth = IntVar(value = 0)
        self.var_threshold = DoubleVar(value = 0.0)
        self.eye_image = None

    """Convert a cv2 image for use in tkinter"""
    def update_eye_image(self, path = ""):
        print("Load image from path " + path)
        image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        self.eye_image = convertImageToImageTk(image)
        # TODO Set size and ratio
        self.eye_display['image'] = self.eye_image
        self.eye_display.configure(image=self.eye_image)
        self.eye_display.update()

    """Select a new eye image"""
    def on_new_eye_click(self):
        path = "./" + \
            os.path.relpath(fd.askopenfilename(initialdir="./images/", \
            filetypes=[("Image", ".png")])).replace("\\","/")
        self.update_eye_image(path = path)

    def on_config_select(self, x_pos: int, y_pos: int, width: int, height: int, threshold: int, eye_image_path: str):
        print("Config selected for EyesWidget.")
        self.var_pos_x = IntVar(value = x_pos)
        self.var_pos_y = IntVar(value = y_pos)
        self.var_width = IntVar(value = width)
        self.var_heigth = IntVar(value = height)
        self.var_threshold = DoubleVar(value = threshold)
        self.update_eye_image(path = eye_image_path)

if __name__ == "__main__":
    EyesWidget()
