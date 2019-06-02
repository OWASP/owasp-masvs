#!/bin/bash
# Script taken from https://github.com/OWASP/CheatSheetSeries/blob/master/scripts/Apply_Linter_Check.sh
# Script in charge of auditing the released MD files with the linter policy defined at project level

#todo: make it multilanguage!
cd ..

apply_lint_check_en(){
    rm linter-result.out
    markdownlint -c .markdownlint.json -o linter-result.out Document
    errors=`wc -m linter-result.out | cut -d' ' -f1`
    content=`cat linter-result.out`
    if [[ $errors != "0" ]]
    then
        echo "[!] Error(s) found by the Linter for language en: $content"
        echo "Only warning for now..."
        #exit $errors
    else
        echo "[+] No error found by the Linter for language en."
        rm linter-result.out
    fi
}

apply_lint_check_lang(){
    rm linter-result-$1.out
    markdownlint -c .markdownlint.json -o linter-result-$1.out Document-$1
    errors=`wc -m linter-result-$1.out | cut -d' ' -f1`
    content=`cat linter-result-$1.out`
    if [[ $errors != "0" ]]
    then
        echo "[!] Error(s) found by the Linter for language $1: $content"
        echo "Only warning for now..."
        #exit $errors
    else
        echo "[+] No error found by the Linter for language $1."
        rm linter-result-$1.out
    fi
}

apply_lint_check_en
apply_lint_check_lang de
apply_lint_check_lang es
apply_lint_check_lang fr
apply_lint_check_lang ja
apply_lint_check_lang ru
apply_lint_check_lang zhtw