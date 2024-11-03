import unittest

from htmlnode import HTMLnode, LeafNode, ParentNode

# I should also deal with invalid input somehow

class TestHTMLnode(unittest.TestCase):
    def test_props_only_1(self):
        node = HTMLnode("a", None, None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
    
    def test_props_only_2(self):
        node = HTMLnode("img", None, None, {"src": "https://docs.python.org/3/library/stdtypes.html#dict.items"})
        self.assertEqual(node.props_to_html(), ' src="https://docs.python.org/3/library/stdtypes.html#dict.items"')

    def test_props_only_3(self):
        node = HTMLnode("iframe", None, None, None)
        self.assertEqual(node.props_to_html(), '') # gotta check for None here, empty dictionary is not an option here

    def test_leaf_1(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_leaf_2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_3(self):
        node = LeafNode(None, "Plain nonsense right here!", None)
        self.assertEqual(node.to_html(), "Plain nonsense right here!")
    
    def test_leaf4(self):
        node = LeafNode(None, None, None)
        # self.assertRaises(ValueError, node.to_html) 
        # you can't use node.to_html() because the function is called by assertRaises -> by using the () you're calling the func

        # when using a context manager (a with statement) you can also test for other parts of the exception like its message
        with self.assertRaises(ValueError, msg="No value for HTML node!") as raises_excp:
            node.to_html()
        #exception = raises_excp.exception
        #self.assertEqual(exception.args,"No value for HTML node!") # not sure how this works but you can test much more stuff on the exception

    def test_parent1(self):
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

        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_parent2(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text")
            ],
            None
        )

        self.assertEqual(node.to_html(), "<p><b>Bold text</b></p>")

    def test_parent3(self):
        node = ParentNode(
            "a",
            [
                LeafNode("b", "Bold text")
            ],
            {"href": "https://www.google.com"}
        )

        self.assertEqual(node.to_html(), '<a href="https://www.google.com"><b>Bold text</b></a>')

    def test_parent4(self):
        node = ParentNode(
            None,
            [
                LeafNode("b", "Bold text")
            ],
            {"href": "https://www.google.com"}
        )

        with self.assertRaises(ValueError) as raises_excp:
            node.to_html()

# Not sure when None would be in the Children list but anyway it's good to test for that possibility -> handled by a ValueError
    def test_parent5(self):
        node = ParentNode(
            "a",
            [
                None
            ],
            {"href": "https://www.google.com"}
        )

        with self.assertRaises(ValueError) as raises_excp:
            node.to_html()

    def test_parent6(self):
        node = ParentNode(
            "a",
            None,
            {"href": "https://www.google.com"}
        )

        with self.assertRaises(ValueError) as raises_excp:
            node.to_html()

    def test_parent7(self):
        node = ParentNode(
            "a",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
            ],
            {"href": "https://www.google.com"}
        )
    
        self.assertEqual(node.to_html(), '<a href="https://www.google.com"><b>Bold text</b>Normal text<i>italic text</i></a>')

    def test_parent8(self):
        node = ParentNode(
            "a",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
            ],
            {"href": "https://www.google.com", "style": "color: blue"}
        )
    
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" style="color: blue"><b>Bold text</b>Normal text<i>italic text</i></a>')

    def test_parent9(self):
        node = ParentNode(
            "a",
            [
                LeafNode("b", "Bold text")
            ],
            {"href": "https://www.google.com", "style": "color: blue"}
        )
    
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" style="color: blue"><b>Bold text</b></a>')


if __name__ == "__main__":
    unittest.main()