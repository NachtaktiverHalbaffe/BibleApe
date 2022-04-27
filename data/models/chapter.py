from dataclasses import dataclass, field

from data.models.verse import Verse


@dataclass(slot=True)
class Chapter:
    """Models a Bible verse. The verse itself is divided into the verse itself and the metadata.
    The book and chapter properties are mandatory, the other can be passed via the constructor
    or gained via one of the interfaces 
    """

    book: str = ""
    """ Name of the book where the verse belongs to """
    chapter: int = 0
    """ Number of chapter where the verse belongs to """
    verseCnt: int = 0
    """ Number of verses in the chapter """
    author: str = ""
    """ Author of the book where the verse belongs to """
    topics: list[str] = field(default_factory=list)
    """ Core topics of the chapter """
    figures: list[str] = field(default_factory=list)
    """ Figures that occur in the chapter. Can be a person or a group, role tc. """
    data: list[Verse] = field(default_factory=list)
    """ The chapter itself containing all verses """
