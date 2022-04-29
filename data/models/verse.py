from dataclasses import dataclass, field
import logging
import sys

from utils.constantLoader import ConstantLoader


@dataclass(slots=True)
class Verse:
    """Models a Bible verse. This is the only data model containing real data
    """

    book: str = ""
    """Name of the book where the verse belongs to"""
    chapter: int = 0
    """Number of chapter where the verse belongs to"""
    verse: int = 0
    """Number of the verse itself"""
    wordCnt: int = 0
    """Number of verses in the chapter"""
    content: str = ""
    """Verse itself """

    def __init__(self) -> None:
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[
                logging.FileHandler("/logs/data.log"),
                logging.StreamHandler(sys.stdout)
            ]
        )

    def __post__init__(self) -> None:
        if self.content != "" and self.wordCnt != 0:
            self.wordCnt = len(self.content.split(" "))

    def getMetaData(self) -> dict:
        """Returns the meta data as a dictionary which only contains entries which have a explicit entry

        Returns:
            dict: metaData with only the values which contains data
        """

        payload = dict()
        if self.verse != 0:
            payload["verse"] = self.verse
        if self.chapter != 0:
            payload["chapter"] = self.chapter
        if self.book != "":
            payload["book"] = self.book
        if self.wordCnt != 0:
            payload["wordCnt"] = self.wordCnt
        if self.chapter != "":
            payload["content"] = self.content

        return payload

    def validateData(self) -> bool:
        """Validates the data to avoid having false data

        Returns:
            bool: If data is valid (true) or has fault (false)
        """

        # Book
        if type(self.book) != type(str):
            logging.warning(
                f"Property book has wrong type: {type(self.book)}. Expected type: str")
            return False
        elif not self.book in ConstantLoader().getConstants("books"):
            logging.warning(
                f"{self.book} is not defined as a book in the constant pool ")
            return False

        # Chapter
        if type(self.chapter) != type(int):
            logging.warning(
                f"Property chapter has wrong type: {type(self.chapter)}. Expected type: int")
            return False
        elif self.chapter < 0 or self.chapter > 150:
            logging.warning(
                "Property chapter is either too big or too small. There are only 150 chapters in the biggest book of the bible")
            # Value out o bounds (the biggest book has 150 chapters)
            return False

        # Verse
        if type(self.verse) != type(int):
            logging.warning(
                f"Property verse has wrong type: {type(self.verse)}. Expected type: int")
            return False
        elif self.verse < 0:
            logging.warning("Property verse is either too small or too big")
            return False

        # wordCnt
        if type(self.wordCnt) != type(int):
            logging.warning(
                f"Property wordCnt has wrong type: {type(self.wordCnt)}. Expected type: int")
            return False
        elif self.wordCnt < 0:
            logging.warning("Property wordCnt is negative")
            return False

        # tags
        for tag in self.tags:
            if type(tag) != type(str):
                logging.warning(
                    f"Entry in property tags has wrong type: {type(tag)}. Expected type: str")
                return False
            elif not tag in ConstantLoader().getConstants("tags"):
                logging.warning(
                    f"{tag} is not defined as a tag in the constant pool ")
                return False

        # content
        if type(self.content) != type(str):
            logging.warning(
                f"Property content has wrong type: {type(self.content)}. Expected type: str")
            return False

        return True
