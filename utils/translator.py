
import json


class Translator:

    def __init__(self, locale="en_EN"):
        # Open JSON file in correct language where translation are stored
        try:
            jsonFile = open(f'translations\{locale}.json', encoding='utf-8')
        except:
            jsonFile = open(f'translations\en_EN.json')
        self.constFile = json.load(jsonFile)
        #  Close file after translation is loaded
        jsonFile.close()

    def getText(self, key: str) -> str:
        """Returns the translated string of the corresponding key. The translation files are located under utils/translations
        and the notation is <first json object key>.<second json object key>.<...>

        Args:
            key (str): key of desired constant

        Raises:
            KeyError: If key has incorrect format

        Returns:
            str: translated string
        """

        transStr = self.constFile
        for item in key.split("."):
            if item.lower() in transStr.keys():
                transStr = transStr[item.lower()]

        if type(transStr) == str:
            return transStr
        else:
            raise KeyError(
                f"Key \"{key}\" does not belong to a translatable string. Check if the key is formatted right and contained in the right translation file")
