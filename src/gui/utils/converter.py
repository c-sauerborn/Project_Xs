import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

try:
    import cv2
    from PIL import Image, ImageTk
    import os.path
except ImportError as import_fail:
    raise \
    Exception("Could not import the required modules, " \
              "make sure you are running with the correct python version, " \
              "and that packages are installed correctly.") \
    from import_fail

def convertImageToImageTk(inputImage) -> ImageTk.PhotoImage: 
    split = cv2.split(inputImage)
    if len(split) == 3:
        blue,green,red = split
        inputImage = cv2.merge((red,green,blue))
    result = Image.fromarray(inputImage)
    convertedImage = ImageTk.PhotoImage(image = result)
    return convertedImage


if __name__ == "__main__":
    convertImageToImageTk()
