#!/bin/bash
set -euo pipefail

FOLDER=$1
VERSION=$2

. $FOLDER/LANGUAGE-METADATA

OUTPUT_BASE_NAME=OWASP_MASVS-SNAPSHOT

CHAPTERS="${FOLDER}/0x*.md ${FOLDER}/CHANGELOG.md"

sed -e "s/{{MASVS-VERSION}}/$VERSION/g" first_page.tex > tmp_first_page-$LANGUAGE.tex
sed -e "s/{{MASVS-VERSION}}/$VERSION/g" -e "s/{{MASVS-LANGUAGE}}/$LANGUAGETEXT/g" cover.tex > tmp_cover-$LANGUAGE.tex

# JP,SC,TC,KR

if [ $LANGUAGE == "ja" ]; then
  sed -e "s/%%{{CJK}}//g" -e "s/{{CJK-LANG}}/JP/g" latex-header.tex > tmp_latex-header-$LANGUAGE.tex
elif [ $LANGUAGE == "ko" ]; then
  sed -e "s/%%{{CJK}}//g" -e "s/{{CJK-LANG}}/KR/g" latex-header.tex > tmp_latex-header-$LANGUAGE.tex
elif [ $LANGUAGE == "zhcn" ]; then
  sed -e "s/%%{{CJK}}//g" -e "s/{{CJK-LANG}}/SC/g" latex-header.tex > tmp_latex-header-$LANGUAGE.tex
elif [ $LANGUAGE == "zhtw" ]; then
  sed -e "s/%%{{CJK}}//g" -e "s/{{CJK-LANG}}/TC/g" latex-header.tex > tmp_latex-header-$LANGUAGE.tex
else
  cp latex-header.tex tmp_latex-header-$LANGUAGE.tex
fi

pandoc --resource-path=.:${FOLDER} \
    --pdf-engine=xelatex --template=eisvogel \
    --toc -V toc-title:"${TOC_TITLE}" --toc-depth=1 \
    -H tmp_latex-header-$LANGUAGE.tex -V linkcolor:blue --include-before-body tmp_cover-$LANGUAGE.tex --include-before-body tmp_first_page-$LANGUAGE.tex \
    -o ${OUTPUT_BASE_NAME}-${LANGUAGE}.pdf $CHAPTERS

rm tmp_first_page-$LANGUAGE.tex
rm tmp_cover-$LANGUAGE.tex
rm tmp_latex-header-$LANGUAGE.tex
