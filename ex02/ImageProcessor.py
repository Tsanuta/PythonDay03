import sys
import matplotlib.image as mplimg
import matplotlib.pyplot as mplplt


class ImageProcessor:
    def load(self, path):
        img = mplimg.imread(path)
        width = len(img)
        height = len(img[0])
        print("Loading image of dimensions", str(width), "x", str(height))
        return (img)

    def display(self, array):
        mplplt.imshow(array)
        mplplt.show()


if __name__ == "__main__":
    imp = ImageProcessor()
    arr = imp.load("../resources/42AI.png")
    print(arr)
    imp.display(arr)
