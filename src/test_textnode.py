import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq_noUrl(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is the stuff", TextType.ITALIC, "https://docs.python.org/3/library/unittest.html")
        node2 = TextNode("This is the stuff", TextType.ITALIC, "https://docs.python.org/3/library/unittest.html")
        self.assertEqual(node, node2)
    
    def test_neq_text(self):
        node = TextNode("This is almost the same ting", TextType.BOLD)
        node2 = TextNode("This is ain't the ting", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_neq_textType(self):
        node = TextNode("This is the same ting", TextType.IMG)
        node2 = TextNode("This is the same ting", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_neq_url(self):
        node = TextNode("This is the feast", TextType.LINK, "https://docs.python.org/3/library/stdtypes.html#tuple")
        node2 = TextNode("This is the feast", TextType.LINK, "https://docs.python.org/3/library/unittest.html")
        self.assertNotEqual(node, node2)
    
    def test_eq_url_None(self):
        node = TextNode("This is the some other stuff", TextType.NORMAL, None)
        node2 = TextNode("This is the some other stuff", TextType.NORMAL, None)
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()