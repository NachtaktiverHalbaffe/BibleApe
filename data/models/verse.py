import numpy as np
import pandas as pd

# TODO Document types of properties
class Verse:
    """Models a Bible verse. The verse itself is divided into the verse itself and the metadata.
    The book, chapter and verse properties are mandatory, the other can be passed via the constructor
    or gained via one of the interfaces

    Properties:
    ---------
    metadata: panda.DataFrame
        Metadata of the Bible verse
        Properties:
            book:
                name of the book where the verse belongs to
            chapter:
                number of chapter where the verse belongs to
            verse:
                number of the verse
            author:
                author of the book where the verse belongs to
    data: numpy.char
        The verse itself
    """

    def __init__(self, book: str, chapter: int, verse: int, author="", topics=[""]):
        self.metaData = pd.DataFrame(
            {
                "book": book,
                "chapter": chapter,
                "verse": verse,
                "author": author,
            }
        )
        self.data = np.char
