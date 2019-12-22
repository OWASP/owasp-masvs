#!/bin/bash
set -ev

if [ -z "$TRAVIS_TAG" ]; then 
exit 0; 
fi
#additional before install steps that are only required when we are TAGGING/releasing:
brew install pandoc
# https://qiita.com/diggy-mo/items/eef12b3f854e88a2b07e, therefore do not install calibre latest:
brew cask install https://raw.githubusercontent.com/Homebrew/homebrew-cask/0609402ee984aa887752a205b3086191aed1385e/Casks/calibre.rb 
brew install epubcheck
brew install gnu-sed