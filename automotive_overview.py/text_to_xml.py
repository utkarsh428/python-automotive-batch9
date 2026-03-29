import xml.etree.ElementTree as ET

data = {}

with open("/Users/utkarshmishra/Documents/python-automotive-batch9/automotive_overview.py/data.txt", "r") as file:
    for line in file:
        key, value = line.strip().split("=")
        data[key] = value

root = ET.Element("VehicleDetails")

for key, value in data.items():
    element = ET.SubElement(root, key)
    element.text = value

tree = ET.ElementTree(root)
tree.write("vehicle_data.xml")

print("Data successfully written to XML file.")