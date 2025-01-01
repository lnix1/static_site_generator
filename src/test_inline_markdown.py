import unittest
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links
from textnode import TextType, TextNode

class TestSplitNodes(unittest.TestCase):
    def test_eq(self):
        node_list = [TextNode("This is a node with `code` example.", TextType.TEXT)]
        node2 = split_nodes_delimiter(node_list, "`", TextType.CODE)
        node3 = TextNode("This is a node with ", TextType.TEXT)
        node4 = TextNode("code", TextType.CODE)
        node5 = TextNode(" example.", TextType.TEXT)
        self.assertEqual(node2, [node3, node4, node5])

class TestExctractions(unittest.TestCase):
    def test_image_extraction(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        images = extract_markdown_images(text)
        self.assertEqual(images[0], ('rick roll', 'https://i.imgur.com/aKaOqIh.gif'))
        self.assertEqual(images[1], ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg'))
    
    def test_link_extraction(self):
        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        images = extract_markdown_links(text)
        self.assertEqual(images[0], ('rick roll', 'https://i.imgur.com/aKaOqIh.gif'))
        self.assertEqual(images[1], ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg'))

if __name__ == "__main__":
    unittest.main()
