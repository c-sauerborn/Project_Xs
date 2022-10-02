
try:
    from tkinter import *
    import cv2
    import tkinter.filedialog as fd
    from tkinter import ttk
except ImportError as import_fail:
    raise \
    Exception("Could not import the required modules, " \
              "make sure you are running with the correct python version, " \
              "and that packages are installed correctly.") \
    from import_fail

class CameraWidget(Frame):
    def __init__(self, parent=None):
        ttk.Labelframe.__init__(self, parent, text="Camera")
        self.grid(in_=parent, padx=5, pady=5)
        self.init_variables()
        self.init_widgets()

    def init_widgets(self):
        # Widgets
        window_prefix_lb = ttk.Label(self, text="Capture Window Prefix: ")
        window_prefix_input = ttk.Entry(
            self, textvariable=self.var_window_prefix)
        camera_lb = ttk.Label(self, text="Camera:")
        camera_index_spbox = Spinbox(
            self, from_=0, to=99, width=5, textvariable=self.var_camera_index)
        monitor_window_cbox = ttk.Checkbutton(
            self, text="Monitor Window", variable=self.var_is_monitoring_window)
        display_percent_lb = ttk.Label(self, text="Display Percent")
        display_percent_spbox = Spinbox(
            self, from_=0, to=500, textvariable=self.var_display_percentage)
        raw_screenshot_btn = ttk.Button(self, text="Raw Screenshot", \
            command=self.save_screenshot)

        # Column 0
        window_prefix_lb.grid(column=0, row=0, sticky=W, padx=5, pady=5)
        display_percent_lb.grid(column=0, row=1, sticky=W, padx=5, pady=5)
        raw_screenshot_btn.grid(column=0, row=2, padx=5, pady=5)

        # Column 1
        # eyeDisplay spans in row 1 here
        window_prefix_input.grid(column=1, row=0, padx=5, pady=5)
        display_percent_spbox.grid(column=1, row=1, padx=5, pady=5)

        # Column 2
        monitor_window_cbox.grid(
            column=2, row=0, columnspan=2, sticky=W, padx=5, pady=5)
        camera_lb.grid(column=2, row=1, sticky=W, padx=5, pady=5)

        # Column 3
        # addConfigButtons spans here in row 0
        # monitorWindowCbox spans here in row 1
        camera_index_spbox.grid(column=3, row=1, sticky=W, padx=5, pady=5)

    def init_variables(self):
        self.var_is_monitoring_window = BooleanVar(value=FALSE)
        self.var_camera_index = StringVar(value="0")
        self.var_window_prefix = StringVar(value="Windowed")
        self.var_display_percentage = IntVar(value=100)
        self.var_raw_screenshot = None # TODO assign frame

    def on_config_update(self, is_monitoring_window: bool, camera_index: int, window_prefix: str, display_percentage: int):
        self.var_is_monitoring_window = is_monitoring_window
        self.var_camera_index = camera_index
        self.var_window_prefix = window_prefix
        self.var_display_percentage = display_percentage

    """Save a raw screenshot of the current output for cropping an eye image"""
    def save_screenshot(self):
        with fd.asksaveasfile(initialdir="./", filetypes=[("PNG", ".png")]) as file:
            cv2.imwrite(file.name,self.var_raw_screenshot)

if __name__ == "__main__":
    CameraWidget()
