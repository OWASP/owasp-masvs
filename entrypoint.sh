#!/bin/sh

set -e

FOLDER=$1
VERSION=$2

. $FOLDER/LANGUAGE-METADATA

OUTPUT_BASE_NAME=OWASP_MASVS-SNAPSHOT

CHAPTERS="${FOLDER}/0x*.md ${FOLDER}/CHANGELOG.md"

sed -e "s/{{MASVS-VERSION}}/$VERSION/g" first_page.tex > tmp_first_page.tex
sed -e "s/{{MASVS-VERSION}}/$VERSION/g" -e "s/{{MASVS-LANGUAGE}}/$LANGUAGETEXT/g" cover.tex > tmp_cover.tex

pandoc --resource-path=.:${FOLDER} \
    --pdf-engine=xelatex --template=eisvogel \
    --toc -V toc-title:"${TOC_TITLE}" --toc-depth=1 -H \
    latex-header.tex -V linkcolor:blue --include-before-body tmp_cover.tex --include-before-body tmp_first_page.tex \
    -o ${OUTPUT_BASE_NAME}-${LANGUAGE}.pdf $CHAPTERS

rm tmp_first_page.tex
rm tmp_cover.tex