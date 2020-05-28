import sys


class CsvReader():
    def __init__(self, f=None, sep=',',
                 header=False, skip_top=0, skip_bottom=0):
        self.filename = f
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.file = None
        self.content = None
        pass

    def __enter__(self):
        try:
            self.file = open(self.filename, "r")
        except OSError as e:
            print(e.strerror)
            self = None
            return(self)
        lst = []
        lst2 = []
        for line in self.file:
            lst.append(line)
        for x in lst:
            z = x.strip("\n").split(self.sep)
            z = [i.strip(" \"") for i in z]
            lst2.append(z)
        self.content = lst2
        size = len(self.content[0])
        for x in self.content:
            if len(x) != size:
                self = None
                return self
        for x in self.content:
            for y in x:
                if y == '':
                    self = None
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()

    def getdata(self):
        if self.skip_top + self.skip_bottom > len(self.content):
            return self.content
        new_list = self.content.copy()
        if self.header is True:
            new_list.pop(0)
        x = 0
        while x < self.skip_top:
            new_list.pop(0)
            x += 1
        x = 0
        while x < self.skip_bottom:
            new_list.pop(len(self.content) - 1)
            x += 1
        return (new_list)

    def getheader(self):
        if self.header is True:
            return (self.content[0])
        else:
            return None


if __name__ == "__main__":
    with CsvReader('good.csv', header=True) as file:
        data = file.getdata()
        print(str(data))
        header = file.getheader()
        print(str(header))

    with CsvReader('bad.csv') as file:
        if file is None:
            print("File is corrupted")
