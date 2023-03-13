import os
import yaml
import re

masvs = {
    "metadata": {
        "title": "Mobile Application Security Verification Standard (MASVS)",
        "remarks": "The OWASP MASVS (Mobile Application Security Verification Standard) is the industry standard for mobile app security. It can be used by mobile software architects and developers seeking to develop secure mobile apps, as well as security testers to ensure completeness and consistency of test results."
    },
    "groups": []
}

def read_md_sections(input_text):

    sections_dict = {}

    sections = re.split(r'^##\s(.+)', input_text, flags=re.MULTILINE)
    sections.pop(0)  # Remove the initial empty string
    
    # Loop over the sections and write each one to a separate file
    for i in range(0, len(sections), 2):
        section_title = sections[i].strip()
        section_content = sections[i+1].strip()

        if section_title == "Control":
            sections_dict["statement"] = section_content
        elif section_title == "Description":
            sections_dict["description"] = section_content
    
    return sections_dict

def get_masvs_dict():
    index = 1

    for file in sorted(os.listdir("Document")):
        if "-MASVS-" in file:
            with open(os.path.join("Document", file), "r") as f:
                header = f.readline().replace("# ", "").strip()
                description = f.read()
                category_id = header.split(":")[0].strip()
                title = header.split(":")[1].strip()
                group = {
                    "id": category_id,
                    "index": index,
                    "title": title,
                    "description": description, 
                    "controls": []
                }

                for control_file in os.listdir("controls"):
                    if control_file.startswith(category_id):
                        with open(os.path.join("controls", control_file), "r") as cf:
                            control_id = cf.readline().replace("# ", "").strip()
                            control_content = cf.read()
                            control_sections = read_md_sections(control_content)
                            control = {"id": control_id} | control_sections
                            group["controls"].append(control)

                masvs["groups"].append(group)
            index += 1
    # sort masvs dict by index
    masvs["groups"] = sorted(masvs["groups"], key=lambda k: k["index"])
    
    return masvs

masvs = get_masvs_dict()

with open("masvs.yaml", "w") as f:
    yaml.dump(masvs, f, default_flow_style=False, sort_keys=False, allow_unicode=True, width=float("inf"))
    
