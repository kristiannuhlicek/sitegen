from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLnode, LeafNode, ParentNode

def main():

    #first_node = TextNode("Some weird stuff here", TextType.BOLD)

    # using the __repr__ method -> when you print an object you get that result not just an object id with no description!
    #print(first_node)

    #another_node = HTMLnode("a", None, None, {"href": "https://www.google.com", "target": "_blank"})

 
        

    node = TextNode("Just testing around", TextType.NORMAL)
    print(text_node_to_html_node(node))

    """
    TextType.TEXT: This should become a LeafNode with no tag, just a raw text value.
    TextType.BOLD: This should become a LeafNode with a "b" tag and the text
    TextType.ITALIC: "i" tag, text
    TextType.CODE: "code" tag, text
    TextType.LINK: "a" tag, anchor text, and "href" prop
    TextType.IMAGE: "img" tag, empty string value, "src" and "alt" props ("src" is the image URL, "alt" is the alt text)
    """


main()