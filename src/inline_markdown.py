from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            split = node.text.split(delimiter)
            for i in range(0, len(split)):
                if (i % 2) == 0:
                    new_nodes.append(TextNode(split[i], TextType.TEXT))
                else:
                    new_nodes.append(TextNode(split[i], text_type))
        else:
            new_nodes.append(nodes)
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

