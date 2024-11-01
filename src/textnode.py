from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMG = "image"

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.__text = text
        self.__text_type = text_type.value
        self.__url = url
    
    def __eq__(self, other):
        if self.__text == other.__text and self.__text_type == other.__text_type and self.__url == other.__url:
            return True
        return False

    def __repr__(self):
        return f"TextNode({self.__text}, {self.__text_type}, {self.__url})"