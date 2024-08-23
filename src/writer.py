"""
The `Writer` class provides functionality for appending data to a text file.
It is used to write information to a file, with specific handling for different data elements.

Attributes:
-----------
- `path`: The file path where data will be written.
- `f`: The file object used for writing data to the file.

Methods:
--------
- `__init__(path)`:
    Initializes the `Writer` instance with the file path where data will be appended.
    Parameters:
        - `path`: The file path to which data will be written.

- `write(data)`:
    Appends the provided data to the file specified by `path`.
    Parameters:
        - `data` (iterable): An iterable containing elements to be written to the file. Each element is written on a new line.
    Notes:
        - If an element in `data` is the second element of the `data` iterable, it will be prefixed with "Page: ".
        - Each element, including the special case, is followed by a newline character.
        - An additional newline character is written at the end of the data.

"""

class Writer:
    def __init__(self, path):
        self.path = path
        self.f = None

    def write(self, data):
        self.f = open(self.path, 'a')
        for element in data:
            if element == data[1]:
                self.f.write(f"Page: {element}")
            else:
                self.f.write(element)
            self.f.write("\n")
        self.f.write("\n")
        self.f.close()



