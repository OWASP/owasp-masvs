# V4: Απαιτήσεις Αυθεντικοποίησης και Διαχείρισης Session

## Στόχος Ελέγχου

Στις περισσότερες περιπτώσεις, οι χρήστες που συνδέονται σε μια απομακρυσμένη υπηρεσία αποτελούν αναπόσπαστο μέρος της συνολικής αρχιτεκτονικής εφαρμογών για κινητά. Παρόλο που το μεγαλύτερο μέρος της λογικής συμβαίνει στο endpoint, το MASVS ορίζει ορισμένες βασικές απαιτήσεις σχετικά με τον τρόπο διαχείρισης των λογαριασμών χρηστών και των περιόδων σύνδεσης.

## Απαιτήσεις Επαλήθευσης Ασφάλειας

| # | MSTG-ID | Description | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **4.1** | MSTG-AUTH-1 | Εάν η εφαρμογή παρέχει στους χρήστες πρόσβαση σε μια απομακρυσμένη υπηρεσία, κάποια μορφή ελέγχου ταυτότητας, όπως ο έλεγχος ταυτότητας username/κωδικού πρόσβασης, εκτελείται στο απομακρυσμένο endpoint. | x | x |
| **4.2** | MSTG-AUTH-2 | Εάν χρησιμοποιείται stateful session management, το απομακρυσμένο endpoint χρησιμοποιεί session IDs που δημιουργούνται τυχαία για τον έλεγχο ταυτότητας των requests του client χωρίς αποστολή των διαπιστευτηρίων του χρήστη. | x | x |
| **4.3** | MSTG-AUTH-3 | Εάν χρησιμοποιείται stateless αυθεντικόποιηση με βάση κάποιον token, ο server παρέχει ένα token που έχει υπογραφεί χρησιμοποιώντας έναν ασφαλή αλγόριθμο. | x | x |
| **4.4** | MSTG-AUTH-4 | Το απομακρυσμένο endpoint τερματίζει την υπάρχουσα περίοδο λειτουργίας όταν ο χρήστης αποσυνδεθεί. | x | x |
| **4.5** | MSTG-AUTH-5 | Υπάρχει μια πολιτική κωδικού πρόσβασης και επιβάλλεται στο απομακρυσμένο endpoint. | x | x |
| **4.6** | MSTG-AUTH-6 | Το απομακρυσμένο endpoint εφαρμόζει έναν μηχανισμό για προστασία από την πολλάπλή υποβολή διαπιστευτηρίων. | x | x |
| **4.7** | MSTG-AUTH-7 | Οι περίοδοι λειτουργίας ακυρώνονται στο απομακρυσμένο endpoint μετά από μια προκαθορισμένη περίοδο αδράνειας και τα session tokens λήγουν. | x | x |
| **4.8** | MSTG-AUTH-8 | Ο βιομετρικός έλεγχος ταυτότητας (εάν υπάρχει), δεν δεσμεύεται από events (δηλαδή, χρησιμοποιώντας ένα API που απλώς επιστρέφει "true" ή "false"). Αντίθετα, βασίζεται στο ξεκλείδωμα του keychain/keystore. | | x |
| **4.9** | MSTG-AUTH-9 | Ένας δεύτερος παράγοντας ελέγχου ταυτότητας υπάρχει στο απομακρυσμένο endpoint και η απαίτηση 2FA επιβάλλεται με συνέπεια. | | x |
| **4.10** | MSTG-AUTH-10 | Οι ευαίσθητες συναλλαγές απαιτούν διπλό έλεγχο ταυτότητας (step-up authentication). | | x |
| **4.11** | MSTG-AUTH-11 | Η εφαρμογή ενημερώνει τον χρήστη για όλες τις ευαίσθητες δραστηριότητες με τον λογαριασμό του. Οι χρήστες μπορούν να προβάλουν μια λίστα συσκευών, να προβάλουν πληροφορίες με βάση στοιχεία (διεύθυνση IP, τοποθεσία κλπ.) και να αποκλείσουν συγκεκριμένες συσκευές. | | x |
| **4.12** | MSTG-AUTH-12 | Τα μοντέλα εξουσιοδότησης θα πρέπει να ορίζονται και να επιβάλλονται στο απομακρυσμένο endpoint. | x | x |

## Αναφορές

To OWASP Mobile Security Testing Guide παρέχει λεπτομερείς οδηγίες για την επαλήθευση των απαιτήσεων που αναφέρονται παραπάνω.

- General: Authentication and Session Management - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04e-Testing-Authentication-and-Session-Management.md>
- Android: Testing Local Authentication - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05f-Testing-Local-Authentication.md>
- iOS: Testing Local Authentication - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06f-Testing-Local-Authentication.md>

Για περισσότερες πληροφορίες, δείτε επίσης:

- OWASP Mobile Top 10: M4 (Insecure Authentication) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m4-insecure-authentication>
- OWASP Mobile Top 10: M6 (Insecure Authorization) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m6-insecure-authorization>
- CWE 287 (Improper Authentication) - <https://cwe.mitre.org/data/definitions/287.html>
- CWE 307 (Improper Restriction of Excessive Authentication Attempts) - <https://cwe.mitre.org/data/definitions/307.html>
- CWE 308 (Use of Single-factor Authentication) - <https://cwe.mitre.org/data/definitions/308.html>
- CWE 521 (Weak Password Requirements) - <https://cwe.mitre.org/data/definitions/521.html>
- CWE 604 (Use of Client-Side Authentication) - <https://cwe.mitre.org/data/definitions/604.html>
- CWE 613 (Insufficient Session Expiration) - <https://cwe.mitre.org/data/definitions/613.html>
