class HTMLnode:
    def __init__(self, tag = None, value = None, children = None, props = None): # the thing here to remember is that Python is checking only if the required parameters are passed, the order is maintained => to make this work in real world you need to make sure None is passed if there is no value
        self.__tag = tag
        self.__value = value
        self.__children = children
        self.__props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html = ""
        if self.__props != None:
            for key, value in self.__props.items():
                html += (f' {key}="{value}"') # when dealing with double quotes inside your string you need to use single quotes and vice versa
        return html
    
    def __repr__(self) -> str:
        return f"HTMLnode({self.__tag}, {self.__value}, {self.__children}, {self.__props})"

"""
tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
children - A list of HTMLNode objects representing the children of this node
props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
"""

"""
An HTMLNode without a tag will just render as raw text
An HTMLNode without a value will be assumed to have children
An HTMLNode without children will be assumed to have a value
An HTMLNode without props simply won't have any attributes
"""