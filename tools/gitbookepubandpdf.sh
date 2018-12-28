#!/bin/bash
echo "Usage: ./gitbookepubandpdf VERSIONTAG"
echo "Do not forget to install npm, gitbookcli (https://www.npmjs.com/package/gitbook-cli), calibre (brew cask install calibre on Mac OS X)"
if [[ $# -eq 0 ]] ; then
    echo 'Please give a VERSIONTAG (default/1.1.1)'
    exit 0
fi
echo 'Versiontag is' $1
echo 'setting up book.json for en/de/es/fr/ja/ru/zhtw'
cp book.json ../book.json
sed -i.bak "s/\[\]/$1/g" ../book.json
rm ../book.json.bak
echo 'setting up new GLOSSARY.MD per language'

cp ../Document/0x90-Appendix-A_Glossary.md ../Document/GLOSSARY.md
sed -i.bak "s/\- \*\*/## /g" ../Document/GLOSSARY.md
sed -i.bak "s/\*\* \– /\\`echo -e '\n\r'`/g" ../Document/GLOSSARY.md
cp ../CHANGELOG.md ../Document/CHANGELOG.md

update_glossary_and_changelog() {
  cp ../CHANGELOG.md ../Document-$2/CHANGELOG.md
  cp ../Document-$2/0x90-Appendix-A_Glossary.md ../Document-$2/GLOSSARY.md
  sed -i.bak "s/\- \*\*/## /g" ../Document-$2/GLOSSARY.md
  sed -i.bak "s/\*\* \– /\\`echo -e '\n\r'`/g" ../Document-$2/GLOSSARY.md
  rm ../Document-$2/GLOSSARY.md.bak
}

update_glossary_and_changelog $1 de
update_glossary_and_changelog $1 es
update_glossary_and_changelog $1 fr
update_glossary_and_changelog $1 ja
update_glossary_and_changelog $1 ru
update_glossary_and_changelog $1 zhtw


gitbook install ../

gitbook pdf ../ ../Generated/OWASP_Mobile_AppSec_Verification_Standard_$1.pdf
gitbook epub ../ ../Generated/OWASP_Mobile_AppSec_Verification_Standard_$1.epub
gitbook mobi ../ ../Generated/OWASP_Mobile_AppSec_Verification_Standard_$1.mobi

echo "We are done: please do not forget to update the leanpub publication!"
