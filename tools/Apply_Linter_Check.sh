#!/bin/bash
# Script taken from https://github.com/OWASP/CheatSheetSeries/blob/master/scripts/Apply_Linter_Check.sh and adapted for multi-langual processing
# Script in charge of auditing the released MD files with the linter policy defined at project level

cd ..

newline_at_eof()
{
    if [ -z "$(tail -c 1 "$1")" ]
    then
        echo "all good"
    else
        echo "No newline at end of file!"
        sed -i '' -e '$a\' $1
    fi
}

apply_lint_check_en(){
    rm linter-result.out
    markdownlint -c .markdownlint.json -o linter-result.out Document
    errors=`wc -m linter-result.out | cut -d' ' -f1`
    content=`cat linter-result.out`
    if [[ $errors != "0" ]]
    then
        echo "[!] $errors Error(s) found by the Linter for language en: $content"
        newline_at_eof linter-result.out
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
        echo "[!] $errors Error(s) found by the Linter for language $1: $content"
        newline_at_eof linter-result-$1.out
    else
        echo "[+] No error found by the Linter for language $1."
        rm linter-result-$1.out
    fi
}

finalize() {
    #getlint-result-total
    if test -f "lint-check-result-all-lang.out"; then
            rm lint-check-result-all-lang.out
    fi
    cat linter-result.out linter-result-de.out linter-result-es.out linter-result-fa.out linter-result-fr.out linter-result-ja.out linter-result-ru.out linter-result-zhtw.out > lint-check-result-all-lang.out
    errors_total=$(wc -l lint-check-result-all-lang.out)
    errors_total_number=$(echo $errors_total| cut -d' ' -f 1)
    echo "Errors total: $errors_total_number"
    if [[ $errors_total_number != "0" ]] 
    then
        exit $(($errors_total_number))
    fi
}

npm install -g markdownlint
apply_lint_check_en
apply_lint_check_lang de
apply_lint_check_lang es
apply_lint_check_lang fa
apply_lint_check_lang fr
apply_lint_check_lang ja
apply_lint_check_lang ko
apply_lint_check_lang ru
apply_lint_check_lang zhtw
apply_lint_check_lang zhcn
finalize
