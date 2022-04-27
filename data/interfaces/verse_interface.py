from abc import ABC, abstractmethod

from data.models.verse import Verse


class VerseInterface(ABC):
    """A bible verse interface. It defines how the data of the verse is obtained and grants access to the verse"""

    def __init__(self, book="", chapter=0, verse=0):
        self.verse = Verse(book=book, chapter=chapter, verse=verse)

    @abstractmethod
    async def loadData(book="", chapter=0, verse=0) -> None:
        """Load the verse itself from the datasource. It uses the chapter, verse and book property of the class 
        itself to search for the verse. Attention: It only gets the verse itself, for the metadata see at the
        function loadMetaData.

        Args:
            book (str, optional): Name of the correpsonding book. Defaults to "".
            chapter (int, optional): Number of the correpsonding chapter. Defaults to 0.
            verse (int, optional): Verse number to load. Defaults to 0.
        """
        pass

    @abstractmethod
    async def loadMetaData() -> None:
        """Load the metadata of the verse from the datasource"""
        pass

    def getContent(self) -> str:
        """Returns the verse itself

        Returns:
            str: The verse itself
        """
        return self.verse.data

    def getVerse(self) -> int:
        """Returns the verse number of the verse

        Returns:
            int: Number of the verse
        """
        return self.verse.verse

    def getChapter(self) -> int:
        """Returns the corresponding chapter of the verse

        Returns:
            int: Number of chapter where the verse belongs to
        """
        return self.verse.chapter

    def getAuthor(self) -> str:
        """Returns the corresponding author of the verse

        Returns:
            str: Name of author where the verse belongs to
        """
        return self.verse.author

    def getBook(self) -> str:
        """Returns the corresponding book of the verse

        Returns:
            str:  Name of book where the verse belongs to
        """
        return self.verse.book

    def getMetaData(self) -> dict:
        """Returns the meta data as a dictionary which only contains entries which have a explicit entry

        Returns:
            dict: metaData with only the values which contains data
        """

        payload = dict()
        if self.verse.verse != 0:
            payload["verse"] = self.verse.verse
        if self.verse.chapter != 0:
            payload["chapter"] = self.verse.chapter
        if self.verse.book != "":
            payload["book"] = self.verse.book
        if self.verse.author != "":
            payload["author"] = self.verse.author
        if self.verse.wordCnt != 0:
            payload["wordCnt"] = self.verse.wordCnt

        return payload
