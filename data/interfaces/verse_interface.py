from abc import ABC, abstractmethod

from data.models.verse import Verse

# TODO Specify return types of getters
class VerseInterface(ABC):
    """A bible verse interface. It defines how the data of the verse is obtained and grants access to the verse"""

    def __init__(self, book: str, chapter: int, verse: int):
        self.verse = Verse(book=book, chapter=chapter, verse=verse)

    @abstractmethod
    def loadData() -> None:
        """Load the verse itself from the datasource. It uses the chapter, verse and book property of the class
        itself to search for the verse. Attention: It only gets the verse itself, for the metadata see at the
        function getMetaData.
        """
        pass

    @abstractmethod
    def loadMetaData() -> None:
        """Load the metadata of the verse from the datasource"""
        pass

    def getContent(self):
        """Returns the verse itself

        Returns:
            pandas.StringDtype: The verse itslef
        """
        return self.verse.data

    def getVerse(self):
        """Returns the verse number of the verse

        Returns:
            int:
                number of verse
        """
        return self.verse.metadata["verse"]

    def getChapter(self):
        """Returns the corresponding chapter of the verse

        Returns:
            int:
                number of chapter
        """
        return self.verse.metadata["chapter"]

    def getAuthor(self):
        """Returns the corresponding author of the verse

        Returns:
            _type_:
                Name of author
        """
        return self.verse.metaData["author"]

    def getBook(self):
        """Returns the corresponding book of the verse

        Returns:
            _type_:
                Name of book
        """
        return self.verse.metaData["book"]
