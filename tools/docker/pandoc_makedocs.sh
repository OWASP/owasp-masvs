#!/bin/bash

# NOTE: This script is not meant to be run locally on your machine (e.g. macOS). Docker will run it for you.

set -euo pipefail

FOLDER=$1
VERSION=$2

# Load the language metadata (env. vars)
. $FOLDER/LANGUAGE-METADATA

OUTPUT_BASE_NAME="OWASP_MASVS-SNAPSHOT"

# Put all chapters in order and CHANGELOG at the end
CHAPTERS="${FOLDER}/0x*.md ${FOLDER}/CHANGELOG.md"

# Use per-language tmp files for the cover and the first page
# Replace the placeholder {{MASVS-VERSION}} with the given VERSION and {{MASVS-LANGUAGE}} with the given LANGUAGETEXT
sed -e "s/{{MASVS-VERSION}}/$VERSION/g" -e "s/{{MASVS-LANGUAGE}}/$LANGUAGETEXT/g" ./tools/docker/cover.tex > tmp_cover-$LANGUAGE.tex
sed -e "s/{{MASVS-VERSION}}/$VERSION/g" ./tools/docker/first_page.tex > tmp_first_page-$LANGUAGE.tex

# latex-header.tex contains 2 placeholders for "using CJK fonts" and for the language itself: JP,SC,TC,KR (part of the font name)
# The following does the replacement and writes to a tmp file
if [ $LANGUAGE == "ja" ]; then
  sed -e "s/%%{{CJK}}//g" -e "s/{{CJK-LANG}}/JP/g" ./tools/docker/latex-header.tex > tmp_latex-header-$LANGUAGE.tex
elif [ $LANGUAGE == "ko" ]; then
  sed -e "s/%%{{CJK}}//g" -e "s/{{CJK-LANG}}/KR/g" ./tools/docker/latex-header.tex > tmp_latex-header-$LANGUAGE.tex
elif [ $LANGUAGE == "zhcn" ]; then
  sed -e "s/%%{{CJK}}//g" -e "s/{{CJK-LANG}}/SC/g" ./tools/docker/latex-header.tex > tmp_latex-header-$LANGUAGE.tex
elif [ $LANGUAGE == "zhtw" ]; then
  sed -e "s/%%{{CJK}}//g" -e "s/{{CJK-LANG}}/TC/g" ./tools/docker/latex-header.tex > tmp_latex-header-$LANGUAGE.tex
else
  cp ./tools/docker/latex-header.tex tmp_latex-header-$LANGUAGE.tex
fi

# --columns 60 -> pandoc will attempt to wrap lines to the column width specified by --columns (default 72). We need it because of ZHCN.
# --toc to create a Table of Contents with the title from the loaded env. vars.
# -H to apply our customizations in the .tex header file
# --include-before-body -> to include the auto-generated cover and first page as the very beginning
pandoc --resource-path=.:${FOLDER} \
    --pdf-engine=xelatex --template=eisvogel \
    --columns 60 \
    --toc -V toc-title:"${TOC_TITLE}" --toc-depth=1 \
    -H tmp_latex-header-$LANGUAGE.tex -V linkcolor:blue \
    --include-before-body tmp_cover-$LANGUAGE.tex --include-before-body tmp_first_page-$LANGUAGE.tex \
    -o ${OUTPUT_BASE_NAME}-${LANGUAGE}.pdf $CHAPTERS

rm tmp_first_page-$LANGUAGE.tex
rm tmp_cover-$LANGUAGE.tex
rm tmp_latex-header-$LANGUAGE.tex
