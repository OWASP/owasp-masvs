#!/bin/bash
set -ev

if [ -z "$TRAVIS_TAG" ]; then 
exit 0; 
fi
#additional before install steps that are only required when we are TAGGING/releasing:
brew install pandoc
brew cask install calibre
brew install epubcheck
brew install gnu-sed