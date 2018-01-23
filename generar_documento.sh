#!/bin/bash
type pandoc >/dev/null 2>&1 || { echo >&2 "I require pandoc but it's not installed.  Aborting."; exit 1; }
# Generar Docx
cd Document-es
pandoc -f gfm --columns 10000 -t docx -o ../MASVS.docx *.md
#pandoc -f markdown_github --columns 10000 -t docx -o MASVS.docx Document/*.md
cd ..
# Generar PDF
#cd Document
#pandoc --pdf-engine=xelatex -o ../MASVS.pdf *.md
#cd ..
