#!/usr/bin/env python

''' MASVS document parser and converter class.

    By Bernhard Mueller, updated by Jeroen Beckers and Carlos Holguera

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

    '''

import os
import re
import json
from xml.sax.saxutils import escape
import csv

import mstg_parser

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


class MASVS:
    ''' Creates requirements list out of markdown files. '''
    requirements = []

    def __init__(self, lang, includeCategoriesHeader):

        if lang == "en":
            target = "../Document"
        else:
            target = "../Document-{}".format(lang)


        for file in sorted(os.listdir(target)):

            if re.match("0x\d{2}-V", file):
                cat = {}
                catRequirements = []
                for line in open(os.path.join(target, file)):

                    if includeCategoriesHeader == "with":
                        regex = re.compile(r'#\sV(\d):\s(.*)')
                        if lang == "fa":
                            line = line.decode('utf-8')
                        m = re.search(regex, line)

                        if m:
                            cat['id'] = m.group(1).strip()
                            cat['text'] = m.group(2).strip()


                    regex = re.compile(r'\*\*(\d\.\d+)\*\*\s\|\s{0,1}(.*?)\s{0,1}\|\s{0,1}(.*?)\s{0,1}\|\s{0,1}(.*?)\s{0,1}\|(\s{0,1}(.*?)\s{0,1}\|)?')
                    if lang=="fa" :
                        line=line.decode('utf-8')
                    m = re.search(regex, line)

                    if m:
                        req = {}

                        req['id'] = m.group(1).strip()
                        req['text'] = m.group(3).strip()
                        req['category'] = m.group(2).replace(u"\u2011", "-")
                        if m.group(5):
                            req['L1'] = len(m.group(4).strip()) > 0
                            req['L2'] = len(m.group(5).strip()) > 0
                            req['R'] = False
                        else:
                            req['R'] = True
                            req['L1'] = False
                            req['L2'] = False

                        if includeCategoriesHeader == "with":
                            catRequirements.append(req)
                        else:
                            self.requirements.append(req)

                if includeCategoriesHeader == "with":
                    cat['requirements'] = catRequirements
                    self.requirements.append(cat)

        masvs_dict = mstg_parser.get_masvs_dict()

        if includeCategoriesHeader == "with":
            for cat in self.requirements:
                for r in cat['requirements']:
                    self.add_mstg_info(r, masvs_dict)
        else:
            for r in self.requirements:
                self.add_mstg_info(r, masvs_dict)



    def add_mstg_info(self, r, masvs_dict):
        if r.get('category') in masvs_dict:
            r['covered'] = True
            r['links'] = masvs_dict[r.get('category')]
        else:
            r['covered'] = False

        # TODO Description will contain the first paragraph from each MSTG section related to MASVS reqs.
        # TODO Solution will contain another paragraph from each MSTG section related to MASVS reqs.
        # This will be added as part of a new PR. The MSTG has to be enhanced to have those "first paragraphs" everywhere.
        r['description'] = ""
        r['solution'] = ""

    def to_json(self):
        ''' Returns a JSON-formatted string '''
        return json.dumps(self.requirements)


    def to_xml(self):
        ''' Returns XML '''
        xml = '<requirements>'

        # TODO add categorie tag
        for r in self.requirements:
            xml += "<requirement id='{}' category='{}' L1='{}' L2='{}' R='{}'>{}</requirement>\n".format(r['id'], r['category'], int(r['L1']), int(r['L2']), int(r['R']), escape(r['text']))
        
        xml += '</requirements>'
        return xml


    def to_csv(self):
        ''' Returns CSV '''
        si = StringIO()

        # TODO add categorie tag ?
        writer = csv.DictWriter(si, ['id', 'text', 'category', 'L1', 'L2', 'R'], extrasaction='ignore')
        writer.writeheader()
        writer.writerows(self.requirements)

        return si.getvalue()
