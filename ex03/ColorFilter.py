import sys
import numpy
from ImageProcessor import ImageProcessor


class ColorFilter:
    def invert(self, array):
        a_inv = 1-array
        return a_inv

    def to_blue(self, array):
        a_blue = numpy.zeros(array.shape)
        a_blue[:, :, 2] = array[:, :, 2]
        return a_blue

    def to_green(self, array):
        a_green = array * 0
        a_green[:, :, 1] = array[:, :, 1]
        return a_green

    def to_red(self, array):
        a_red = array - self.to_green(array)
        a_red = a_red - self.to_blue(array)
        return a_red

    def celluloid(self, array, treshold=4):
        img1 = numpy.copy(array)
        if treshold < 1:
            print("Please use a treshold equals or higher ", end='')
            print("than 2 (Using default 4 for the current image)")
            treshold = 4
        tresh = numpy.linspace(0, 1, treshold+1)
        n = 0
        img1[(img1 >= tresh[n]) & (img1 <= tresh[n+1])] = n/(treshold-1)
        n = 1
        while n < treshold:
            img1[(img1 > tresh[n]) & (img1 <= tresh[n+1])] = n/(treshold-1)
            n += 1
        return img1

    def to_grayscale(self, array, filter='weighted'):
        def by_mean(array):
            a_mgray = array / 1
            r = array[:, :, 0]
            g = array[:, :, 1]
            b = array[:, :, 2]
            m = (r+g+b)/3
            for i in (0, 1, 2):
                a_mgray[:, :, i] = m
            return(a_mgray)

        def by_weight(array):
            a_wgray = array * 0
            r = array[:, :, 0] * 0.299
            g = array[:, :, 1] * 0.587
            b = array[:, :, 2] * 0.114
            m = (r+g+b)
            for i in (0, 1, 2):
                a_wgray[:, :, i] = m
            return a_wgray

        if filter == "mean" or filter == "m":
            return by_mean(array)
        if filter == "weighted" or filter == "w":
            return by_weight(array)


if __name__ == "__main__":
    imp = ImageProcessor()
    img_array = imp.load("../resources/42AI.png")
    print(img_array)
    cfilter = ColorFilter()
    imp.display(cfilter.invert(img_array))
    imp.display(img_array)
    imp.display(cfilter.to_blue(img_array))
    imp.display(img_array)
    imp.display(cfilter.to_green(img_array))
    imp.display(img_array)
    imp.display(cfilter.to_red(img_array))
    imp.display(img_array)
    imp.display(cfilter.celluloid(img_array, 4))
    imp.display(img_array)
    imp.display(cfilter.to_grayscale(img_array, 'm'))
    imp.display(cfilter.to_grayscale(img_array, 'w'))
    imp.display(img_array)
