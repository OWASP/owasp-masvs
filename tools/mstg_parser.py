# coding: utf-8

""" 
    This script must be run using Python 3.7+ and from its containing folder, i.e. "python3 mstg_parser.py"
    It required the MSTG (owasp-mstg) to be in a folder next to the MASVS (owasp-masvs).

    1. generates a MASVS dict containing GitHub links to MSTG markdown sections containing MSTG IDs.
    2. optionally checks the availability of those links.
    3. parses the MSTG-IDs from the current MASVS and calculates coverage: prints all MSTG-IDs not yet covered in the MSTG.

    Example:

    ## MASVS Dict ##
    {
        "MSTG-NETWORK-3": [
            "https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05g-Testing-Network-Communication.md#testing-endpoint-identify-verification-mstg-network-3",
            "https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06g-Testing-Network-Communication.md#testing-custom-certificate-stores-and-certificate-pinning-mstg-network-3-and-mstg-network-4"
        ],
        "MSTG-NETWORK-4": [
            ...
    ## COVERAGE ##
    MSTG-RESILIENCE-4 not covered
    MSTG-RESILIENCE-5 not covered
    MSTG-RESILIENCE-6 not covered
    ...

    By Carlos Holguera

    Copyright (c) 2020 OWASP Foundation

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

"""

import subprocess
import re
import json
from typing import Dict, List

# import requests # TODO for beta live check (not yet working on remote)

MSTG_PATH = "../../owasp-mstg/Document"
MASVS_PATH = "../Document"

# DO_URL_LIVE_CHECK = False # If set to True, it will take considerable time

def get_masvs_dict() -> Dict[str, List[str]]:

    # TODO update container to have at least Python 3.7. The next line does not work on the remote container.
    # parsed = subprocess.run(["egrep", "-r", r"^### (.*\(MSTG-.*-.*\)$)", MSTG_PATH], capture_output=True)
    parsed = subprocess.check_output(["egrep", "-r", r"^### (.*\(MSTG-.*-.*\)$)", MSTG_PATH])
    # parsed = parsed.stdout

    masvs_dict = {}

    # TODO update container to have at least Python 3.7. The next line does not work on the remote container.
    # for line in parsed.stdout.split(b"\n"):
    for line in parsed.split(b"\n"):
        line = str(line)
        regex = re.compile(r".*/(.*\.md):### (.*) \((MSTG-.*-.*)\)")
        match = re.search(regex, line)

        if match:
            file_name = match.group(1)
            anchor = match.group(2).replace(" ", "-").lower()
            mstg_ids_list = [element for element in match.group(3).split() if element.startswith("MSTG")]
            mstg_ids = match.group(3).replace(" ", "-").lower()
            # TODO update container to have at least Python 3.7. The next line does not work on the remote container.
            # url = f"https://github.com/OWASP/owasp-mstg/blob/master/Document/{file_name}#{anchor}-{mstg_ids}"
            url = "https://github.com/OWASP/owasp-mstg/blob/master/Document/" + file_name + "#" + anchor + "-" + mstg_ids

            for x in mstg_ids_list:
                if x.endswith(','):
                    x = x[:-1]
                if masvs_dict.get(x) is None:
                    masvs_dict[x] = []
                masvs_dict[x].append(url) 

                # if DO_URL_LIVE_CHECK:
                #     beta_live_check(url)

    return masvs_dict

# def beta_live_check(url):

#     ret = requests.get(url)
#     if ret.status_code == 200:
#         print("Exists")
#     else:
#         print("Failed")

def get_mstg_ids_from_masvs() -> List[str]:

    mstg_id_regex = r"\*\*\d\.\d+\*\*\s\|\s{0,1}(.*?)\s{0,1}\|"

    parsed_lines = subprocess.run(["egrep", "-r", mstg_id_regex, MASVS_PATH], capture_output=True)

    mstg_ids = []

    for line in parsed_lines.stdout.split(b"\n"):
        # The MSTG-IDs in the MASVS does not contain regular "-" signs, instead they contain a special character coded as "\xe2\x80\x91"
        line = str(line.replace(b"\xe2\x80\x91", b"-"))
        regex = re.compile(mstg_id_regex)
        match = re.search(regex, line)

        if match:
            mstg_ids.append(match.group(1))
    return mstg_ids

def masvs_coverage(masvs_dict, mstg_ids):

    for mstg_id in mstg_ids:
        if mstg_id not in masvs_dict:
            # TODO replace the following lines once the remote container has Python +3.7
            # print(f"{mstg_id} not covered")
            message = mstg_id + " not covered"
            print(message)

if __name__ == "__main__":
    print("## MASVS Dict ##\n")
    masvs_dict = get_masvs_dict()
    print(json.dumps(masvs_dict, indent=4))

    print("\n\n## COVERAGE ##\n")
    mstg_ids = get_mstg_ids_from_masvs()
    masvs_coverage(masvs_dict, mstg_ids)
