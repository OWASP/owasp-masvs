echo "Applying Linter check"
echo "Counting amount of linter issues:"
lintCommand="sh ./Apply_Linter_Check.sh"
$lintCommand
LINTRESULT=$?
echo "Number of errors with lint-check: $LINTRESULT"

echo "Applying Link check"
linkComamnd="sh ./Apply_Link_Check.sh"
$linkCommand
LINKRESULT=$?
echo "Number of errors with link-check: $LINKRESULT"

echo "Running creaton of pdfs and word documents"
rm ../Generated/*.*
sh ./gitbookepubandpdf.sh $1
sh ./generate_document.sh $1
sh ./generate_document_de.sh $1
sh ./generate_document_es.sh $1
sh ./generate_document_fr.sh $1
sh ./generate_document_ja.sh $1
sh ./generate_document_ru.sh $1
sh ./generate_document_zhtw.sh $1

echo "Checking epub validity"
sh epubcheck ../Generated/OWASP_Mobile_AppSec_Verification_Standard_latest_Document.epub
sh epubcheck ../Generated/OWASP_Mobile_AppSec_Verification_Standard_latest_Document-de.epub
sh epubcheck ../Generated/OWASP_Mobile_AppSec_Verification_Standard_latest_Document-fr.epub
sh epubcheck ../Generated/OWASP_Mobile_AppSec_Verification_Standard_latest_Document-es.epub
sh epubcheck ../Generated/OWASP_Mobile_AppSec_Verification_Standard_latest_Document-ja.epub
sh epubcheck ../Generated/OWASP_Mobile_AppSec_Verification_Standard_latest_Document-ru.epub
sh epubcheck ../Generated/OWASP_Mobile_AppSec_Verification_Standard_latest_Document-zhtw.epub