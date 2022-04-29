from abc import ABC, abstractmethod

from data.models.verse import Verse


class VerseInterface(ABC):
    """A bible verse interface. It defines how the data of the verse is collected"""

    @abstractmethod
    async def collectVerse(book: str, chapter: int, verse: int) -> Verse:
        """Collect the verse itself from the datasource. 

        Args:
            book (str): Name of the correpsonding book. Defaults to "".
            chapter (int): Number of the correpsonding chapter. Defaults to 0.
            verse (int): Verse number to load. Defaults to 0.
        """
        pass

    @abstractmethod
    async def collectMetaData(verse: Verse) -> Verse:
        """Collect the metadata of the verse from the datasource"""
        pass
