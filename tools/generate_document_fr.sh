#!/bin/bash
type pandoc >/dev/null 2>&1 || { echo >&2 "I require pandoc but it's not installed.  Aborting."; exit 1; }
# How to generate Docx
cd Document-fr
pandoc -f markdown_github --columns 10000 -t docx -o ../MASVS-fr.docx *.md
#pandoc -f markdown_github --columns 10000 -t docx -o MASVS.docx Document/*.md
cd ..
# how to generate pdf
#cd Document
#pandoc --latex-engine=xelatex -o ../MASVS.pdf *.md
#cd ..
