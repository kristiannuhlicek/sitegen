from textnode import TextNode, TextType
from htmlnode import HTMLnode

def main():

    #first_node = TextNode("Some weird stuff here", TextType.BOLD)

    # using the __repr__ method -> when you print an object you get that result not just an object id with no description!
    #print(first_node)

    another_node = HTMLnode("a", None, None, {"href": "https://www.google.com", "target": "_blank"})

    print(another_node.props_to_html())
    print(another_node)

main()