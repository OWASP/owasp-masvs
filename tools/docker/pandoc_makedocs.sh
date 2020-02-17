#!/bin/bash
set -euo pipefail

FOLDER=$1
VERSION=$2

. $FOLDER/LANGUAGE-METADATA

OUTPUT_BASE_NAME=OWASP_MASVS-SNAPSHOT

CHAPTERS="${FOLDER}/0x*.md ${FOLDER}/CHANGELOG.md"

sed -e "s/{{MASVS-VERSION}}/$VERSION/g" first_page.tex > tmp_first_page.tex
sed -e "s/{{MASVS-VERSION}}/$VERSION/g" -e "s/{{MASVS-LANGUAGE}}/$LANGUAGETEXT/g" cover.tex > tmp_cover.tex

# JP,SC,TC,KR

if [ $LANGUAGE == "ja" ]; then
  sed -e "s/%%{{CJK}}//g" -e "s/{{CJK-LANG}}/JP/g" latex-header.tex > tmp_latex-header.tex
elif [ $LANGUAGE == "ko" ]; then
  sed -e "s/%%{{CJK}}//g" -e "s/{{CJK-LANG}}/KR/g" latex-header.tex > tmp_latex-header.tex
elif [ $LANGUAGE == "zhcn" ]; then
  sed -e "s/%%{{CJK}}//g" -e "s/{{CJK-LANG}}/SC/g" latex-header.tex > tmp_latex-header.tex
elif [ $LANGUAGE == "zhtw" ]; then
  sed -e "s/%%{{CJK}}//g" -e "s/{{CJK-LANG}}/TC/g" latex-header.tex > tmp_latex-header.tex
else
  cp latex-header.tex tmp_latex-header.tex
fi

pandoc --resource-path=.:${FOLDER} \
    --pdf-engine=xelatex --template=eisvogel \
    --toc -V toc-title:"${TOC_TITLE}" --toc-depth=1 \
    -H tmp_latex-header.tex -V linkcolor:blue --include-before-body tmp_cover.tex --include-before-body tmp_first_page.tex \
    -o ${OUTPUT_BASE_NAME}-${LANGUAGE}.pdf $CHAPTERS

rm tmp_first_page.tex
rm tmp_cover.tex
rm tmp_latex-header.tex
