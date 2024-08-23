"""
The `Reader` class provides functionality to read and process PDF documents using the PyMuPDF library.
It extracts information from pages, such as headers and abstracts, by utilizing the `IntroPageRef` and `AbstractPageRef` classes.

Attributes:
-----------
- `doc`: The PyMuPDF document object representing the opened PDF file.
- `page`: The current page object being processed (an instance of `AbstractPageRef`).

Methods:
--------
- `__init__(path)`:
    Initializes the `Reader` instance by opening the PDF document at the specified `path`.
    Parameters:
        - `path`: The file path to the PDF document.

- `loop(start=1, end=None)`:
    Iterates over a range of pages in the PDF document to extract headers and abstracts.
    Parameters:
        - `start` (int): The starting page number (1-based index). Default is 1.
        - `end` (int, optional): The ending page number (1-based index). If not provided or is beyond the number of pages, processing continues to the last page.
    Yields:
        - A tuple containing:
            - `header` (str): The merged header text extracted from the previous page.
            - `page_number` (int): The current page number where the abstract was found.
            - `keyword` (str): The keyword found in the current page that triggered the abstract extraction.
            - `abstract` (str): The extracted abstract text from the current page.
    Raises:
        - `ValueError`: If `start` or `end` page numbers are invalid.
"""
import logging
import pymupdf as pp
from page import IntroPageRef, AbstractPageRef


class Reader:
    def __init__(self,path):
        self.doc = pp.open(path)
        self.page = None
        self.logger = logging.getLogger(__name__)

    def loop(self, start=1, end=None):
        num_pages = len(self.doc)
        if end is None or end > num_pages:
            end = num_pages

        if start < 1 or start >= num_pages or start >= end:
            raise ValueError("Invalid start or end page")

        for i in range(start, end):
            self.page = AbstractPageRef(self.doc.load_page(i), i)
            self.page.extract_abstract()
            if self.page.get_abstract() != "":
                keyword = self.page.get_keyword()
                intro_page = IntroPageRef(self.doc.load_page(i-1), i-1)
                intro_page.extract_bold()
                intro_page.merge_bold()
                header = intro_page.get_header()
                yield header, i, keyword, self.page.get_abstract()


