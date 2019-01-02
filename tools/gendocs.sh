#!/bin/sh
cd $TRAVIS_BUILD_DIR/Tools
rm ../generated/*.*
sh ./gitbookepubandpdf.sh $TRAVIS_TAG
sh ./generate_document.sh $TRAVIS_TAG
sh ./generate_document_es.sh $TRAVIS_TAG
sh ./generate_document_fr.sh $TRAVIS_TAG
sh ./generate_document_ja.sh $TRAVIS_TAG
sh ./generate_document_ru.sh $TRAVIS_TAG
sh ./generate_document_zhtw.sh $TRAVIS_TAG
