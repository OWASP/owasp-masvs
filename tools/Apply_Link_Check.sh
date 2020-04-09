#!/bin/bash
# Script taken and adapted from https://github.com/OWASP/CheatSheetSeries/blob/master/scripts/Apply_Link_Check.sh and adapted for multi-lingual processing
# Script in charge of auditing the released MD files in order to detect dead links



apply_link_check_lang() {
    echo "Checking links for language $1"
    if test -f "../link-check-result-$1.out"; then
        rm ../link-check-result-$1.out
    fi
    cd ../Document-$1
    find . -name \*.md -exec markdown-link-check -q -c ../.markdownlinkcheck.json {} \; 1>../link-check-result-$1.out 2>&1

    errors=`grep -c "ERROR:" ../link-check-result-$1.out`
    content=`cat ../link-check-result-$1.out`
    if [[ $errors != "0" ]]
    then
        echo "[!] Error(s) found by the Links validator for $1: $errors pages have dead links! Verbose output in /link-check-result-$1.out"
    else
        echo "[+] No error found by the Links validator for $1."
        rm ../link-check-result-$1.out
    fi
}

apply_link_check_en() {
    echo "Checking links for language EN"
    if test -f "../link-check-result.out"; then
        rm ../link-check-result.out
    fi
    cd ../Document
    find . -name \*.md -exec markdown-link-check -q -c ../.markdownlinkcheck.json {} \; 1>../link-check-result.out 2>&1
    errors=`grep -c "ERROR:" ../link-check-result.out`
    content=`cat ../link-check-result.out`
    if [[ $errors != "0" ]]
    then
        echo "[!] Error(s) found by the Links validator for EN: $errors pages have dead links! Verbose output in /link-check-result.out"
    else
        echo "[+] No error found by the Links validator for EN."
        rm ../link-check-result.out
    fi
}

finalize () {
    #getlink-result-total
    if test -f "../link-check-result-all-lang.out"; then
            rm ../lint-check-result-all-lang.out
        fi
    cd ..
    cat link-check-result.out link-check-result-de.out link-check-result-es.out link-check-result-fr.out link-check-result-ja.out link-check-result-ru.out link-check-result-zhtw.out > link-check-result-all-lang.out
    
    errors_total=`grep -c "ERROR:" link-check-result-all-lang.out`
    echo "Errors total: $errors_total"
    if [[ $errors_total != "0" ]] 
    then
        exit $errors_total
    fi
}

npm install -g markdown-link-check

apply_link_check_en
apply_link_check_lang de
apply_link_check_lang es
apply_link_check_lang fr
apply_link_check_lang hi
apply_link_check_lang ja
apply_link_check_lang ko
apply_link_check_lang ru
apply_link_check_lang zhtw
apply_link_check_lang zhcn
finalize
