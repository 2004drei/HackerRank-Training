import xml.etree.ElementTree as ET

root = ET.Element("root")
child1 = ET.SubElement(root, "child1")
# child2 = et.SubElement(root, "child2")
ET.SubElement(child1, "name").text = "Jaime"
child1.set("id", "001")

tree = ET.ElementTree(root)
tree.write("file.xml", encoding="utf-8", xml_declaration=True)
print("file.xml created successfully!")