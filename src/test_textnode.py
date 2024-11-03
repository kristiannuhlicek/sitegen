import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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
    
    def test_html_conversion_Normal(self):
        node = TextNode("This is some normal text", TextType.NORMAL, None)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.get_value(), "This is some normal text")
        self.assertEqual(html_node.get_tag(), None)
        self.assertEqual(html_node.get_props(), None)

    def test_html_conversion_Bold(self):
        node = TextNode("This is pretty bold of you, mister", TextType.BOLD, None)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.get_value(), "This is pretty bold of you, mister")
        self.assertEqual(html_node.get_tag(), "b")
        self.assertEqual(html_node.get_props(), None)

    def test_html_conversion_Italic(self):
        node = TextNode("Don't get all italic on me, missy", TextType.ITALIC, None)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.get_value(), "Don't get all italic on me, missy")
        self.assertEqual(html_node.get_tag(), "i")
        self.assertEqual(html_node.get_props(), None)

    def test_html_conversion_Code(self):
        node = TextNode("Had quite enough code already, wouldn't you say, m'lord?", TextType.CODE, None)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.get_value(), "Had quite enough code already, wouldn't you say, m'lord?")
        self.assertEqual(html_node.get_tag(), "code")
        self.assertEqual(html_node.get_props(), None)

    def test_html_conversion_Link(self):
        node = TextNode("Linkin'n through the park, eh?", TextType.LINK, "https://developer.mozilla.org/en-US/docs/Glossary/Block-level_content")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.get_value(), "Linkin'n through the park, eh?")
        self.assertEqual(html_node.get_tag(), "a")
        self.assertEqual(html_node.get_props(), {"href": node.get_url()})

    def test_html_conversion_Image(self):
        node = TextNode("Never too late for a good picture", TextType.IMG, "https://developer.mozilla.org/en-US/docs/Glossary/Block-level_content")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.get_value(), "")
        self.assertEqual(html_node.get_tag(), "img")
        self.assertEqual(html_node.get_props(), {"src": node.get_url(), "alt": node.get_text()})

    def test_html_conversion_Undefined(self):
        node = TextNode("Never too late for a good picture", TextType.TEST, "https://developer.mozilla.org/en-US/docs/Glossary/Block-level_content")

        with self.assertRaises(ValueError) as raises_excp:
            text_node_to_html_node(node)
    
    def test_html_conversion_WrongObject(self):
        node = TextType.BOLD

        with self.assertRaises(ValueError) as raises_excp:
            text_node_to_html_node(node)

if __name__ == "__main__":
    unittest.main()