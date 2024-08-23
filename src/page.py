"""
This module provides classes for processing and extracting information from PDF pages.
It defines three classes: `PageRef`, `IntroPageRef`, and `AbstractPageRef`.

Classes:
--------

1. `PageRef`:
    Base class for handling PDF page references.
    Attributes:
        - `logger`: Logger instance for logging messages.
        - `page`: The page object from which text is extracted.
        - `number`: The page number.
    Methods:
        - `_loop_spans()`: Generator method to iterate over text spans in the page.

2. `IntroPageRef` (inherits from `PageRef`):
    Extracts and merges bold text spans from the page to form a header.
    Attributes:
        - `_header`: The merged header text.
        - `bold_spans`: List of tuples containing bold text spans, each with its text, font size, and font.
    Methods:
        - `merge_bold()`: Merges consecutive bold text spans with the same font and size into a single header string.
        - `get_header()`: Returns the merged header text.
        - `extract_bold()`: Extracts bold text spans from the page and stores them in `bold_spans`.

3. `AbstractPageRef` (inherits from `PageRef`):
    Extracts abstract text from the page based on specific keywords.
    Attributes:
        - `keywords`: List of keywords to identify the start of an abstract section.
        - `_keyword`: The keyword that triggered the abstract extraction.
        - `_abstract`: The extracted abstract text.
    Methods:
        - `_check_for_keywords(text)`: Checks if the given text contains any of the keywords.
        - `_loop_spans()`: Generator method to iterate over lines of text blocks, logging each block.
        - `extract_abstract()`: Extracts the abstract text based on the identified keyword and consistent text formatting.
        - `get_abstract()`: Returns the extracted abstract text.
        - `get_keyword()`: Returns the keyword that was found and used for extracting the abstract.

"""
import logging


class PageRef:
    def __init__(self, page, number):
        self.logger = logging.getLogger(__name__)
        self.page = page
        self.number = number

    def _loop_spans(self):
        for text_block in self.page.get_text("dict")["blocks"]:
            for line in text_block["lines"]:
                for span in line["spans"]:
                    yield span


class IntroPageRef(PageRef):
    def __init__(self, page, number):
        super().__init__(page, number)
        self._header = ""
        self.bold_spans = []

    def merge_bold(self):
        if not self.bold_spans:
            return
        merged = [self.bold_spans[0][0]]
        i = 1
        while i < len(self.bold_spans):
            if self.bold_spans[i - 1][1:] == self.bold_spans[i][1:]:
                merged.append(self.bold_spans[i][0])
                i += 1
            i += 1
        self.logger.info(merged)
        self._header = " ".join(merged)

    def get_header(self):
        return self._header

    def extract_bold(self):
        for span in self._loop_spans():
            if "bold" in span["font"].lower():
                text = span["text"].strip()
                if text:
                    font_size = round(span["size"], 3)
                    self.bold_spans.append((text, font_size, span["font"]))


class AbstractPageRef(PageRef):
    def __init__(self, page, number):
        super().__init__(page, number)
        self.keywords = ["abstract", "summary"]
        self._keyword = None
        self._abstract = ""

    def _check_for_keywords(self, text):
        lower = text.lower()
        for keyword in self.keywords:
            if keyword in lower:
                self._keyword = keyword
                return True
        return False

    def _loop_spans(self):
        for text_block in self.page.get_text("dict")["blocks"]:
            self.logger.info(text_block)
            lines = text_block.get("lines")
            if lines:  # Check if 'lines' is present and not None
                for line in lines:
                    yield line

    def extract_abstract(self):
        abstract_text = []
        start_extracting = False
        prev = {
            "size": None,
            "font": None,
            "color": None
        }

        for line in self._loop_spans():
            line_contains_keyword = False
            for span in line["spans"]:
                text = span["text"].strip().lower()
                if start_extracting:
                    prev.update({key: span[key] for key in prev.keys() if prev[key] is None})
                    if all(prev[key] == span[key] for key in prev.keys()) and text:
                        abstract_text.append(span["text"].strip())
                elif self._check_for_keywords(text):
                    start_extracting = True
                    break
            if line_contains_keyword:
                continue

        self._abstract = " ".join(abstract_text)

    def get_abstract(self):
        return self._abstract

    def get_keyword(self):
        return self._keyword
