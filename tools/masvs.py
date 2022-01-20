#!/usr/bin/env python

''' MASVS document parser and converter class.

    By Bernhard Mueller, updated by Jeroen Beckers and Carlos Holguera

    Copyright (c) OWASP Foundation

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

    '''

import os
import re
import json
import yaml
from xml.sax.saxutils import escape
import csv
from pathlib import Path

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

def order_filenames(target):
    if Path(target).exists():
        keys = [f"-V{k}-" for k in range(1,9)]
        l = [file.name for file in Path(target).glob("0x*-V*.md")]
        ret_l = []
        for k in keys:
            for name in l:
                if k in name:
                    ret_l.append(name)
        return ret_l
    raise Exception(f"The provided path ({target}) does not exist. Does the corresponding language supported in the MASVS?")

class MASVS:
    ''' Creates requirements list out of markdown files. '''
    requirements = {}

    def __init__(self, lang):

        if lang == "en":
            target = "../Document"
        else:
            target = "../Document-{}".format(lang)

        for file in order_filenames(target):
            for line in open(os.path.join(target, file)):
                regex = re.compile(r'\*\*(\d\.\d+)\*\*\s\|\s{0,1}(.*?)\s{0,1}\|\s{0,1}(.*?)\s{0,1}\|\s{0,1}(.*?)\s{0,1}\|(\s{0,1}(.*?)\s{0,1}\|)?')
                m = re.search(regex, line)

                if m:
                    req = {}
                    num_id = m.group(1).strip()
                    mstg_id = m.group(2).replace(u"\u2011", "-")
                    req['id'] = num_id
                    req['category'] = mstg_id
                    req['text'] = m.group(3).strip()
                    if m.group(5):
                        req['L1'] = len(m.group(4).strip()) > 0
                        req['L2'] = len(m.group(5).strip()) > 0
                        req['R'] = False
                    else:
                        req['R'] = True
                        req['L1'] = False
                        req['L2'] = False

                    self.requirements[mstg_id] = req
                   
    def to_json(self):
        ''' Returns a JSON-formatted string '''
        return json.dumps(self.requirements)

    def to_yaml(self):
        ''' Returns a YAML-formatted string '''
        return yaml.dump(self.requirements, allow_unicode=True, indent=4, default_flow_style=False, sort_keys=False)

    def to_xml(self):
        ''' Returns XML '''
        xml = '<requirements>\n'

        for id, r in self.requirements.items():
            xml += f"\t<requirement id='{r['id']}' category='{r['category']}' L1='{int(r['L1'])}' L2='{int(r['L2'])}' R='{int(r['R'])}'>\n\t\t{escape(r['text'])}\n\t</requirement>\n"
        
        xml += '</requirements>'
        return xml

    def to_csv(self):
        ''' Returns CSV '''
        si = StringIO()

        writer = csv.DictWriter(si, ['id', 'category', 'text', 'L1', 'L2', 'R'], extrasaction='ignore')
        writer.writeheader()
        rows = [r for id, r in self.requirements.items()]
        writer.writerows(rows)

        return si.getvalue()
