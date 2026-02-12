#!/usr/bin/python3
"""
task_03_xml
Serialize and deserialize a Python dictionary to and from XML
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML and save to the given filename.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # Convert all values to strings

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file into a Python dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        data_dict = {}

        for child in root:
            data_dict[child.tag] = child.text  # Keep as string

        return data_dict

    except (ET.ParseError, FileNotFoundError):
        return None
