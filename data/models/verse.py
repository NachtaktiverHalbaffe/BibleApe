from dataclasses import dataclass, field


@dataclass(slots=True)
class Verse:
    """Models a Bible verse. The verse itself is divided into the verse itself and the metadata. Because
    the verse can be a too fine-granular unit or can be redundant with the chapter meta-data, the meta
    data itself is optional, but if you want to load the verse the book, chapter and verse properties are
    mandatory. To minimize data size, you can set the metaData to None after you loaded the verse itself
    """

    book: str = ""
    """Name of the book where the verse belongs to"""
    chapter: int = 0
    """Number of chapter where the verse belongs to"""
    verse: int = 0
    """Number of the verse itself"""
    wordCnt: int = 0
    """Number of verses in the chapter"""
    author: str = ""
    """Author of the book where the verse belongs to"""
    tags: list[str] = field(default_factory=list)
    """Tags of the verse. Tags are buzzwords that can categorize a chapter i.e. tags can give some further information 
    about the verse e.g. a tag \"Popular\" if its a popular verse like Joh 3,16d. To be efficiently analyzed a tag from a 
    constant tag pool should be used"""
    data: str = ""
    """Verse itself """
