from textnode import TextNode, TextType
from htmlnode import HTMLnode, LeafNode, ParentNode

def main():

    #first_node = TextNode("Some weird stuff here", TextType.BOLD)

    # using the __repr__ method -> when you print an object you get that result not just an object id with no description!
    #print(first_node)

    #another_node = HTMLnode("a", None, None, {"href": "https://www.google.com", "target": "_blank"})

    #print(another_node.props_to_html())
    #print(another_node)
    """
    leaf_node_1 = LeafNode("p", "This is a paragraph of text.")
    leaf_node_2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(leaf_node_1.to_html())
    print(leaf_node_2.to_html())
    """

    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
        None
    )

    print(node.to_html())
    

main()