import xml.etree.ElementTree as ET

# Read and parse the XML file
tree = ET.parse(r"/Users/utkarshmishra/Documents/python-automotive-batch9/medical/patient.xml")
root = tree.getroot()

# List to store medical problems
medical_problems = []

# Read each <problem> tag from XML
for problem in root.iter("problem"):
    if problem.text:                      
        medical_problems.append(problem.text.strip())

# Sort the list alphabetically 
medical_problems.sort()

# Print output
print("Medical Problems:")
for problem in medical_problems:
    print(problem)