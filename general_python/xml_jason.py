import xml.etree.ElementTree as ET
import json


def jason_parse(json_path):
    with open(json_path, "r") as f:
        content = json.load(f)

    print(content)


def jason_parse_write(json_path):
    write_dict = {"First": "Eyal", "Last": "Hadad", "Phone": ["0547248850", "026428899"]}
    with open(json_path, "w") as f:
        json.dump(write_dict, f)

    with open(json_path, "a") as f:
        f.write("\n")
        json.dump(write_dict, f)


def xml_parse(xml_path):
    root = ET.parse(xml_path)
    for child in root.iter("person"):
        print(child.attrib["id"])

    for child in root.iter("name"):
        print(child.text)
    i = 7


if __name__ == '__main__':
    # jason_parse(r'C:\Users\Eyal-TLV\Desktop\readJson.json')
    # jason_parse_write(r'C:\Users\Eyal-TLV\Desktop\readJsonWrite.json')
    xml_parse(r'C:\Users\Eyal-TLV\Desktop\xml_example.xml')
