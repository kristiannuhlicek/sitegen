import unittest

from htmlnode import HTMLnode

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

if __name__ == "__main__":
    unittest.main()