
import json

from utils.translator import Translator


class ConstantLoader:
    def __init__(self):
        # Open JSON file in correct language where translation are stored
        try:
            jsonFile = open('.\constants.json')
        except:
            raise FileNotFoundError(
                "File is not located under /utils/constants.json")
        self.constFile = json.load(jsonFile)
        # Close file after translation is loaded
        jsonFile.close()

    def getConstants(self, key: str, locale="en_EN") -> list[str]:
        """Returns a list of translated constants corresponding to the key

        Args:
            key (str): key of desired constant
            locale(str, opt): language in which the string should be returned. Defaults to "en_EN"
        Raises:
            KeyError: If key has incorrect format

        Returns:
            str: translated list of constants
        """

        if key.lower() in self.constFile.keys():
            trList = self.constFile[key.lower()]
            for i in range(len(trList)):
                trList[i] = Translator(locale).getText(f'{key}.{trList[i]}')
            return trList
        else:
            raise KeyError(
                f"Key \"{key}\" does not belong to a constant or pool of constant. Check if the key is formatted right and contained in the right translation file")

    def getConstant(self, key: str, locale="en_EN") -> str:
        """Returns a translated constant corresponding to the key

        Args:
            key (str): key of desired constant
            locale(str, opt): language in which the string should be returned. Defaults to "en_EN"

        Raises:
            KeyError: If key has incorrect format

        Returns:
            str: translated string
        """

        if key.lower() in self.constFile.keys():
            return Translator(locale).getText(self.constFile[key.lower()])
        else:
            raise KeyError(
                f"Key \"{key}\" does not belong to a constant or pool of constant. Check if the key is formatted right and contained in the right translation file")
