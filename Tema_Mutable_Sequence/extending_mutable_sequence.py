from collections.abc import MutableSequence


class CrayonsBox(MutableSequence):
    def __init__(self, iterable):
        self._crayons = list(iterable)

    def __len__(self):
        print('Getting the len of the crayon box: {}'.format(len(self._crayons)))
        return len(self._crayons)

    def __getitem__(self, index):
        print('getting item with index {}; that is {}'.format(index, self._crayons[index]))
        return self._crayons[index]

    def __delitem__(self, index):
        print(f"Deleting the {self._crayons[index]} crayon with the specified index {index}")
        del self._crayons[index]
        return self._crayons

    def __setitem__(self, index, value):
        print(f"Setting the ")
        self._crayons[index] = value
        return self._crayons


    def insert(self, index: int, value):
        self._crayons.insert(index, value)
        return self._crayons



crayons = 'White Yellow Blue Red Green Black Brown'.split()
crayons_box = CrayonsBox(crayons)
