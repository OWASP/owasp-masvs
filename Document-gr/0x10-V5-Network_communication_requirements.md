# V5: Απαιτήσεις Επικοινωνίας Δικτύου

## Στόχος Ελέγχου

Ο σκοπός των στοιχείων ελέγχου που παρατίθενται σε αυτήν την ενότητα είναι να διασφαλίσουν την εμπιστευτικότητα και την ακεραιότητα των πληροφοριών που ανταλλάσσονται μεταξύ της mobile εφαρμογής και των τελικών απομακρυσμένων endpoints. Τουλάχιστον, μια mobile εφαρμογή πρέπει να δημιουργήσει ένα ασφαλές, κρυπτογραφημένο κανάλι για επικοινωνία δικτύου χρησιμοποιώντας το πρωτόκολλο TLS με τις κατάλληλες ρυθμίσεις. Το επίπεδο 2 παραθέτει πρόσθετο μέτρο άμυνας σε βάθος, όπως το SSL pinning.

## Απαιτήσεις Επαλήθευσης Ασφάλειας

| # | MSTG-ID | Description | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **5.1** | MSTG-NETWORK-1 | Τα δεδομένα κρυπτογραφούνται στο δίκτυο χρησιμοποιώντας TLS. Το ασφαλές κανάλι χρησιμοποιείται με συνέπεια σε όλη την εφαρμογή. | x | x |
| **5.2** | MSTG-NETWORK-2 | Οι ρυθμίσεις TLS είναι σύμφωνες με τις τρέχουσες βέλτιστες πρακτικές ή όσο το δυνατόν πλησιέστερα εάν το mobile λειτουργικό σύστημα δεν υποστηρίζει τα προτεινόμενα πρότυπα. | x | x |
| **5.3** | MSTG-NETWORK-3 | Η εφαρμογή επαληθεύει το πιστοποιητικό X.509 του απομακρυσμένου endpoint όταν δημιουργηθεί το ασφαλές κανάλι. Γίνονται αποδεκτά μόνο πιστοποιητικά υπογεγραμμένα από αξιόπιστη Aρχή έκδοσης πιστοποιητικών (CA). | x | x |
| **5.4** | MSTG-NETWORK-4 | Η εφαρμογή είτε χρησιμοποιεί το δικό της χώρο αποθήκευσης πιστοποιητικών, είτε κάνει pin το πιστοποιητικό του endpoint ή το δημόσιο κλειδί και στη συνέχεια, δεν δημιουργεί συνδέσεις με endpoints που προσφέρουν διαφορετικό πιστοποιητικό ή κλειδί, ακόμη και αν είναι υπογεγραμμένα από αξιόπιστη αρχή έκδοσης πιστοποιητικών. |   | x |
| **5.5** | MSTG-NETWORK-5 | Η εφαρμογή δεν βασίζεται σε ένα ανασφαλές κανάλι επικοινωνίας (email ή SMS) για κρίσιμες λειτουργίες, όπως εγγραφές και ανάκτηση λογαριασμού. |  | x |
| **5.6** | MSTG-NETWORK-6 | Η εφαρμογή εξαρτάται μόνο από ενημερωμένες βιβλιοθήκες συνδεσιμότητας και ασφάλειας. |  | x |

## Αναφορές

Tο OWASP Mobile Security Testing Guide παρέχει λεπτομερείς οδηγίες για την επαλήθευση των απαιτήσεων που αναφέρονται σε αυτήν την ενότητα.

- General: Testing Network Communication - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04f-Testing-Network-Communication.md>
- Android: Testing Network Communication - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05g-Testing-Network-Communication.md>
- iOS: Testing Network Communication - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06g-Testing-Network-Communication.md>

Για περισσότερες πληροφορίες, δείτε επίσης:

- OWASP Mobile Top 10: M3 (Insecure Communication) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m3-insecure-communication>
- CWE 295 (Improper Certificate Validation) - <https://cwe.mitre.org/data/definitions/295.html>
- CWE 296 (Improper Following of a Certificate's Chain of Trust) - <https://cwe.mitre.org/data/definitions/296.html>
- CWE 297 (Improper Validation of Certificate with Host Mismatch) - <https://cwe.mitre.org/data/definitions/297.html>
- CWE 298 (Improper Validation of Certificate Expiration) - <https://cwe.mitre.org/data/definitions/298.html>
- CWE 308 (Use of Single-factor Authentication) - <https://cwe.mitre.org/data/definitions/308.html>
- CWE 319 (Cleartext Transmission of Sensitive Information) - <https://cwe.mitre.org/data/definitions/319.html>
- CWE 326 (Inadequate Encryption Strength) - <https://cwe.mitre.org/data/definitions/326.html>
- CWE 327 (Use of a Broken or Risky Cryptographic Algorithm) - <https://cwe.mitre.org/data/definitions/327.html>
- CWE 780 (Use of RSA Algorithm without OAEP) - <https://cwe.mitre.org/data/definitions/780.html>
- CWE 940 (Improper Verification of Source of a Communication Channel) - <https://cwe.mitre.org/data/definitions/940.html>
- CWE 941 (Incorrectly Specified Destination in a Communication Channel) - <https://cwe.mitre.org/data/definitions/941.html>
