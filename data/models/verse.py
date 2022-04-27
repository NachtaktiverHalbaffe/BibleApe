from dataclasses import dataclass


@dataclass(slots=True)
class Verse:
    """Models a Bible verse. The verse itself is divided into the verse itself and the metadata. Because
    the verse can be a too fine-granular unit or can be redundant with the chapter meta-data, the meta
    data itself is optional, but if you want to load the verse the book, chapter and verse properties are
    mandatory. To minimize data size, you can set the metaData to None after you loaded the verse itself
    """

    book: str = ""
    """ Name of the book where the verse belongs to """
    chapter: int = 0
    """ Number of chapter where the verse belongs to """
    verse: int = 0
    """ Number of the verse itself """
    wordCnt: int = 0
    """ Number of verses in the chapter """
    author: str = ""
    """ Author of the book where the verse belongs to """
    data: str = ""
    """ Verse itself """
