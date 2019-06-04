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
sh ./gitbookepubandpdf.sh latest
sh ./generate_document.sh latest
sh ./generate_document_de.sh latest
sh ./generate_document_es.sh latest
sh ./generate_document_fr.sh latest
sh ./generate_document_ja.sh latest
sh ./generate_document_ru.sh latest
sh ./generate_document_zhtw.sh latest

echo "Checking epub validity"
sh epubcheck ../Generated/OWASP_Mobile_AppSec_Verification_Standard_latest_Document.epub
sh epubcheck ../Generated/OWASP_Mobile_AppSec_Verification_Standard_latest_Document-de.epub
sh epubcheck ../Generated/OWASP_Mobile_AppSec_Verification_Standard_latest_Document-fr.epub
sh epubcheck ../Generated/OWASP_Mobile_AppSec_Verification_Standard_latest_Document-es.epub
sh epubcheck ../Generated/OWASP_Mobile_AppSec_Verification_Standard_latest_Document-ja.epub
sh epubcheck ../Generated/OWASP_Mobile_AppSec_Verification_Standard_latest_Document-ru.epub
sh epubcheck ../Generated/OWASP_Mobile_AppSec_Verification_Standard_latest_Document-zhtw.epub