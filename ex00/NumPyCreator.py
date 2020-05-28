import sys
import numpy


class NumPyCreator:
    def from_list(self, lst, dtype=None):
        return (numpy.array(lst, dtype))

    def from_tuple(self, tpl, dtype=None):
        return (numpy.array(tpl, dtype))

    def from_iterable(self, itr, dtype=None):
        return (numpy.fromiter(itr, dtype))

    def from_shape(self, shape, value=0, dtype=None):
        return (numpy.full(shape, value, dtype))

    def random(self, shape):
        return(numpy.random.rand(*shape))

    def identity(self, n, dtype=None):
        return (numpy.identity(n, dtype))


if __name__ == "__main__":
    npc = NumPyCreator()

    print(npc.from_list([[1, 2, 3], [6, 3, 4]]))

    print(npc.from_tuple(("a", "b", "c")))

    print(npc.from_iterable(range(5)))

    shape = (3, 5)
    print(npc.from_shape(shape))

    print(npc.random(shape))

    print(npc.identity(4))
