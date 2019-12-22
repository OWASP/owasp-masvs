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
mkdir -p ../Generated
rm ../Generated/*.*
echo "cleanup completed"
sh ./gitbookepubandpdf.sh $1
sh ./generate_document.sh $1
sh ./generate_document_de.sh $1
sh ./generate_document_es.sh $1
sh ./generate_document_fr.sh $1
sh ./generate_document_ja.sh $1
sh ./generate_document_ko.sh $1
sh ./generate_document_ru.sh $1
sh ./generate_document_zhtw.sh $1

echo "Checking epub validity"
sh epubcheck ../Generated/OWASP_Mobile_AppSec_Verification_Standard_$1_Document.epub
sh epubcheck ../Generated/OWASP_Mobile_AppSec_Verification_Standard_$1_Document-de.epub
sh epubcheck ../Generated/OWASP_Mobile_AppSec_Verification_Standard_$1_Document-fr.epub
sh epubcheck ../Generated/OWASP_Mobile_AppSec_Verification_Standard_$1_Document-es.epub
sh epubcheck ../Generated/OWASP_Mobile_AppSec_Verification_Standard_$1_Document-ja.epub
sh epubcheck ../Generated/OWASP_Mobile_AppSec_Verification_Standard_$1_Document-ko.epub
sh epubcheck ../Generated/OWASP_Mobile_AppSec_Verification_Standard_$1_Document-ru.epub
sh epubcheck ../Generated/OWASP_Mobile_AppSec_Verification_Standard_$1_Document-zhtw.epub