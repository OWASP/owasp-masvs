#!/bin/bash
echo "Usage: ./gitbookepubandpdf VERSIONTAG LANG"
echo "Do not forget to install npm, gitbookcli (https://www.npmjs.com/package/gitbook-cli), calibre (brew cask install calibre on Mac OS X)"
echo 'Versiontag is' $1
echo 'languagte is' $2
cp book.json ../book.json
sed -i.bak "s/\[\]/$1/g" ../book.json
rm ../book.json.bak
gitbook install ../

gitbook pdf ../ ../Generated/MASVS.pdf
gitbook epub ../ ../Generated/MASVS.epub
gitbook mobi ../ ../Generated/MASVS.mobi

echo "We are done: please do not forget to update the leanpub update!"
