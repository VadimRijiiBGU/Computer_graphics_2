from PIL import Image
import glob

metadata = {
    "1": 1, 
    "L": 8, 
    "P": 8, 
    "RGB": 24, 
    "RGBA": 32, 
    "CMYK": 32, 
    "YCbCr": 24, 
    "LAB": 24, 
    "HSV": 24, 
    "I": 32, 
    "F": 32
}

def showImagesInfo():
    for image in map(Image.open, glob.glob('images/*')):
        print("Image", image.filename, " metadata: ")
        print("size:", image.size, "px")
        print("resolution:", image.info.get("dpi"))
        print("color depth:", metadata[image.mode])
        print("compression:", image.info.get('compression'))
        print()

showImagesInfo()
