import sys
import numpy

from ImageProcessor import ImageProcessor


class ScrapBooker:
    def crop(self, array, dimensions, position=(0, 0)):
        x = position[0]
        y = position[1]
        dimx = dimensions[0]
        dimy = dimensions[1]
        if dimx > len(array)-x or dimy > len(array[0])-y:
            print("Crop dimensions to high for image")
            return()
        # Delete Axis colonne = 1, ligne = 0
        a_crop = numpy.delete(array, numpy.s_[0:x], 0)
        a_crop = numpy.delete(a_crop, numpy.s_[0:y], 1)
        a_crop = numpy.delete(a_crop, numpy.s_[dimx:len(a_crop)], 0)
        a_crop = numpy.delete(a_crop, numpy.s_[dimy:len(a_crop[0])], 1)
        return a_crop

    def thin(self, array, n, axis):
        if axis == 1:
            a_thin = numpy.delete(array, numpy.s_[n-1:len(array[0])+1:n], 0)
        else:
            a_thin = numpy.delete(array, numpy.s_[n-1:len(array)+1:n], 1)
        return a_thin

    def juxtapose(self, array, n, axis):
        a_juxt = numpy.copy(array)
        while n > 0:
            if axis == 1:
                a_juxt = numpy.concatenate((a_juxt, array), 0)
            else:
                a_juxt = numpy.concatenate((a_juxt, array), 1)
            n -= 1
        return a_juxt

    def mosaic(self, array, dimensions):
        a_juxt = numpy.copy(array)
        x = dimensions[0]
        y = dimensions[1]
        while x > 1:
            a_juxt = numpy.concatenate((a_juxt, array), 0)
            x -= 1
        new_array = numpy.copy(a_juxt)
        while y > 1:
            a_juxt = numpy.concatenate((a_juxt, new_array), 1)
            y -= 1
        return a_juxt


if __name__ == "__main__":
    # img = [	["0A", "B", "0C", "D", "E", "F", "G", "H", "I", "J", "0Q", "L"],
    # 		["1A", "B", "1C", "D", "E", "F", "G", "H", "I", "J", "1Q", "L"],
    # 		["2A", "B", "2C", "D", "E", "F", "G", "H", "I", "J", "2Q", "L"],
    # 		["3A", "B", "3C", "D", "E", "F", "G", "H", "I", "J", "3Q", "L"],
    # 		["4A", "B", "4C", "D", "E", "F", "G", "H", "I", "J", "4Q", "L"],
    # 		["5A", "B", "5C", "D", "E", "F", "G", "H", "I", "J", "5Q", "L"],
    # 		["6A", "B", "6C", "D", "E", "F", "G", "H", "I", "J", "6Q", "L"],
    # 		["7A", "B", "7C", "D", "E", "F", "G", "H", "I", "J", "7Q", "L"],
    # 		["8A", "B", "8C", "D", "E", "F", "G", "H", "I", "J", "8Q", "L"],
    # 		["9A", "B", "9C", "D", "E", "F", "G", "H", "I", "J", "9Q", "L"],
    # 		["10A", "B", "10C", "D", "E", "F", "G", "H", "I", "J", "10Q", "L"],
    # 		]
    # img_array = numpy.array(img)

    imp = ImageProcessor()
    img_array = imp.load("../resources/42AI.png")
    scrap = ScrapBooker()
    # print(img_array, "\n")
    # print(scrap.crop(img_array, (5, 10), (0, 0)), "\n")
    imp.display(scrap.crop(img_array, (200, 200), (0, 0)))
    # print(scrap.thin(img_array, 3, 0), "\n")
    imp.display(scrap.thin(img_array, 3, 0))
    # img = [	["0A", "B"],
    # 		["1A", "B"],
    # 		]
    # img_array = numpy.array(img)
    # print(scrap.juxtapose(img_array, 2, 0), "\n")
    imp.display(scrap.juxtapose(img_array, 2, 0))
    # print(scrap.mosaic(img_array, (2, 2)))
    imp.display(scrap.mosaic(img_array, (2, 2)))
