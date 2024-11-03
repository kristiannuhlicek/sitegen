from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMG = "image"
    TEST = "test"

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.__text = text
        self.__text_type = text_type.value
        self.__url = url

    def get_text(self):
        return self.__text
    
    def get_text_type(self):
        return self.__text_type
    
    def get_url(self):
        return self.__url
    
    def __eq__(self, other):
        if self.__text == other.__text and self.__text_type == other.__text_type and self.__url == other.__url:
            return True
        return False

    def __repr__(self):
        return f"TextNode({self.__text}, {self.__text_type}, {self.__url})"
    
def text_node_to_html_node(text_node):
    if not isinstance(text_node, TextNode):
        raise ValueError("Input must be a TextNode - 'cause otherwise it ain't make no sense")
    match text_node.get_text_type():
        case "normal":
            new_node = LeafNode(None, text_node.get_text(), None)
        case "bold":
            new_node = LeafNode("b", text_node.get_text(), None)
        case "italic":
            new_node = LeafNode("i", text_node.get_text(), None)
        case "code":
            new_node = LeafNode("code", text_node.get_text(), None)
        case "link":
            new_node = LeafNode("a", text_node.get_text(), {"href": text_node.get_url()})
        case "image":
            new_node = LeafNode("img", "", {"src": text_node.get_url(), "alt": text_node.get_text()})
        case _:
            raise ValueError(f"Undefined TextType {text_node.get_text_type()}")
    return new_node