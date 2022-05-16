# V3: Απαιτήσεις Κρυπτογραφίας

## Στόχος ελέγχου

Η κρυπτογραφία είναι ένα βασικό συστατικό όταν πρόκειται για την προστασία των δεδομένων που είναι αποθηκευμένα σε μια φορητή συσκευή. Είναι επίσης μια κατηγορία όπου τα πράγματα μπορεί να πάνε τρομερά στραβά, ειδικά όταν δεν τηρούνται οι τυπικές συμβάσεις. Ο σκοπός των ελέγχων σε αυτό το κεφάλαιο είναι να διασφαλίσουν ότι η επαληθευμένη εφαρμογή χρησιμοποιεί κρυπτογραφία σύμφωνα με τις βέλτιστες πρακτικές του κλάδου, συμπεριλαμβανομένων:

- Χρήση αποδεδειγμένων βιβλιοθηκών κρυπτογράφησης.
- Σωστή επιλογή και διαμόρφωση κρυπτογραφικών παραμέτρων.
- Μια κατάλληλη γεννήτρια τυχαίων αριθμών όπου απαιτείται τυχαιότητα.

## Απαιτήσεις Ασφάλειας

| # | MSTG-ID | Description | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **3.1** | MSTG-CRYPTO-1 | Η εφαρμογή δεν βασίζεται στη συμμετρική κρυπτογραφία με hardcoded κλειδιά ως μοναδική μέθοδο κρυπτογράφησης.| x | x |
| **3.2** | MSTG-CRYPTO-2 | Η εφαρμογή χρησιμοποιεί αποδεδειγμένες υλοποιήσεις κρυπτογραφικών δυνατοτήτων. | x | x |
| **3.3** | MSTG-CRYPTO-3 | Η εφαρμογή χρησιμοποιεί κρυπτογραφικές υλοποιήσεις που είναι κατάλληλες για τη συγκεκριμένη περίπτωση χρήσης, διαμορφωμένες με παραμέτρους που συμμορφώνονται με τις βέλτιστες πρακτικές του κλάδου. | x | x |
| **3.4** | MSTG-CRYPTO-4 | Η εφαρμογή δεν χρησιμοποιεί κρυπτογραφικά πρωτόκολλα ή αλγόριθμους που θεωρούνται ευρέως καταργημένοι για λόγους ασφαλείας. | x | x |
| **3.5** | MSTG-CRYPTO-5 | Η εφαρμογή δεν επαναχρησιμοποιεί το ίδιο κρυπτογραφικό κλειδί για πολλούς σκοπούς. | x | x |
| **3.6** | MSTG-CRYPTO-6 | Όλες οι τυχαίες τιμές δημιουργούνται χρησιμοποιώντας μια επαρκώς ασφαλή γεννήτρια τυχαίων αριθμών. | x | x |

## References

Το OWASP Mobile Security Testing Guide παρέχει λεπτομερείς οδηγίες για την επαλήθευση των απαιτήσεων που αναφέρονται σε αυτήν την ενότητα.

- Android: Testing Cryptography - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05e-Testing-Cryptography.md>
- iOS: Testing Cryptography - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06e-Testing-Cryptography.md>

Για περισσότερες πληροφορίες δείτε επίσης:

- OWASP Mobile Top 10: M5 (Insufficient Cryptography) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m5-insufficient-cryptography>
- CWE 310 (Cryptographic Issues) - <https://cwe.mitre.org/data/definitions/310.html>
- CWE 321 (Use of Hard-coded Cryptographic Key) - <https://cwe.mitre.org/data/definitions/321.html>
- CWE 326 (Inadequate Encryption Strength) - <https://cwe.mitre.org/data/definitions/326.html>
- CWE 327 (Use of a Broken or Risky Cryptographic Algorithm) - <https://cwe.mitre.org/data/definitions/327.html>
- CWE 329 (Not Using a Random IV with CBC Mode) - <https://cwe.mitre.org/data/definitions/329.html>
- CWE 330 (Use of Insufficiently Random Values) - <https://cwe.mitre.org/data/definitions/330.html>
- CWE 337 (Predictable Seed in PRNG) - <https://cwe.mitre.org/data/definitions/337.html>
- CWE 338 (Use of Cryptographically Weak Pseudo Random Number Generator (PRNG)) - <https://cwe.mitre.org/data/definitions/338.html>
