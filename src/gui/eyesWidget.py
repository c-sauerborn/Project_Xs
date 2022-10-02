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
        self.initVariables()
        self.initWidgets()

    def initWidgets(self):
        # Widgets
        self.eyeDisplay = ttk.Label(self, text="(Select an eye image)")
        xLabel = ttk.Label(self,text="X")
        posXSpinBox= Spinbox(self, from_= 0, to = 99999, width = 5, textvariable=self.posX)
        yLabel = ttk.Label(self,text="Y")
        posYSpinBox = Spinbox(self, from_= 0, to = 99999, width = 5, textvariable=self.posY)
        wLabel = ttk.Label(self,text="W")
        widthSpinBox = Spinbox(self, from_= 0, to = 99999, width = 5, textvariable=self.width)
        hLabel = ttk.Label(self,text="H")
        heigthSpinBox = Spinbox(self, from_= 0, to = 99999, width = 5, textvariable=self.heigth)
        thresholdLabel = ttk.Label(self,text="Threshold")
        thresholdSpinBox = Spinbox(self, from_= 0, to = 1, width = 5, increment=0.1, textvariable=self.threshold)
        newEyeButton = ttk.Button(self, text="Select Eye", command=self.onNewEyeClick) #command=self.new_eye

        # Column 0
        xLabel.grid(column=0, row=0,  sticky = W, padx=5, pady=5)
        yLabel.grid(column=0, row=1,  sticky = W, padx=5, pady=5)
        wLabel.grid(column=0, row=2,  sticky = W, padx=5, pady=5)
        hLabel.grid(column=0, row=3,  sticky = W, padx=5, pady=5)
        thresholdLabel.grid(column=0, row=4,  sticky = W, padx=5, pady=5)
        self.eyeDisplay.grid(column=0, row=5, columnspan=2, padx=5, pady=5)
        newEyeButton.grid(column=0, row=6, columnspan=2, padx=5, pady=5)
        
        # Column 0
        posXSpinBox.grid(column=1, row=0,  sticky = W, padx=5, pady=5)
        posYSpinBox.grid(column=1, row=1,  sticky = W, padx=5, pady=5)
        widthSpinBox.grid(column=1, row=2,  sticky = W, padx=5, pady=5)
        heigthSpinBox.grid(column=1, row=3,  sticky = W, padx=5, pady=5)
        thresholdSpinBox.grid(column=1, row=4,  sticky = W, padx=5, pady=5)
        # eyeDisplay spans in row 5
        # newEyeButton spans in row 6

    def initVariables(self):
        self.posX = IntVar(value = 0)
        self.posY = IntVar(value = 0)
        self.width = IntVar(value = 0)
        self.heigth = IntVar(value = 0)
        self.threshold = DoubleVar(value = 0.0)

    """Convert a cv2 image for use in tkinter"""
    def readImage(self, path = ""):
        print("Load image from path " + path)
        image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        self.eyeImage = convertImageToImageTk(image)
        # TODO Set size and ratio
    
    def setCurrentImage(self):
        self.eyeDisplay['image'] = self.eyeImage
        self.eyeDisplay.configure(image=self.eyeImage)
        self.eyeDisplay.update()

    """Select a new eye image"""
    def onNewEyeClick(self):
        path = "./" + \
            os.path.relpath(fd.askopenfilename(initialdir="./images/", \
            filetypes=[("Image", ".png")])).replace("\\","/")
        self.readImage(path = path)
        self.setCurrentImage()

if __name__ == "__main__":
    EyesWidget()
