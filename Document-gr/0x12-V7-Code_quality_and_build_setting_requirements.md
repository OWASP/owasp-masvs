# V7: Απαιτήσεις Ποιότητας Κώδικα και Ρύθμισης Build

## Στόχος Ελέγχου

Ο στόχος αυτού του ελέγχου είναι να διασφαλίσει ότι ακολουθούνται βασικές πρακτικές ασφαλούς κώδικα κατά την ανάπτυξη της εφαρμογής, και ότι ενεργοποιούνται οι "δωρεάν" δυνατότητες ασφαλείας που προσφέρονται από τον μεταγλωττιστή.

## Απαιτήσεις Επαλήθευσης Ασφάλειας

| # | MSTG-ID | Description | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **7.1** | MSTG-CODE-1 | Η εφαρμογή είναι υπογεγραμμένη και εφοδιασμένη με έγκυρο πιστοποιητικό, του οποίου το ιδιωτικό κλειδί προστατεύεται κατάλληλα. | x | x |
| **7.2** | MSTG-CODE-2 | Η εφαρμογή έχει δημιουργηθεί σε λειτουργία έκδοσης (release mode), με ρυθμίσεις κατάλληλες για ένα release build (π.χ. χωρίς τη δυνατότητα debugging). | x | x |
| **7.3** | MSTG-CODE-3 | Tα debugging symbols έχουν αφαιρεθεί από τα native binaries | x | x |
| **7.4** | MSTG-CODE-4 | Κώδικας Debugging and κώδικας που χρησιμοποιείται για βοήθεια του developer (πχ test code, backdoors, κρυφές ρυθμίσεις) έχουν αφαιρεθεί. Η εφαρμογή δε καταγράφει αναλυτικά (verbose) error ή debugging μηνύματα. | x | x |
| **7.5** | MSTG-CODE-5 | Όλα τα τρίτα στοιχεία/υποσυστήματα που χρησιμοποιούνται από την mobile εφαρμογή, όπως βιβλιοθήκες και frameworks, εντοπίζονται και ελέγχονται για γνωστές ευπάθειες. | x | x |
| **7.6** | MSTG-CODE-6 | Η εφαρμογή εντοπίζει και χειρίζεται πιθανά exceptions. | x | x |
| **7.7** | MSTG-CODE-7 | H λογική διαχείρισης σφαλμάτων (error handling logic) στoυς μηχανισμούς ασφαλείας δεν επιτρέπει τη by default πρόσβαση. | x | x |
| **7.8** | MSTG-CODE-8 | Στον unmanaged κώδικα η μνήμη γίνεται allocate, freed και χρησιμοποιείται με ασφάλεια | x | x |
| **7.9** | MSTG-CODE-9 | Ενεργοποιούνται δωρεάν λειτουργίες ασφαλείας που προσφέρει το toolchain, όπως byte-code minimization , stack protection, PIE support, και reference counting. | x | x |

## Αναφορές

Tο OWASP Mobile Security Testing Guide παρέχει λεπτομερείς οδηγίες για την επαλήθευση των απαιτήσεων που αναφέρονται σε αυτήν την ενότητα.

- Android: Testing Code Quality and Build Settings - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05i-Testing-Code-Quality-and-Build-Settings.md>
- iOS: Testing Code Quality and Build Settings - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06i-Testing-Code-Quality-and-Build-Settings.md>

Για περισσότερες πληροφορίες, δείτε επίσης:

- OWASP Mobile Top 10: M7 (Poor Code Quality) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m7-client-code-quality>
- CWE 20 (Improper Input Validation) - <https://cwe.mitre.org/data/definitions/20.html>
- CWE 89 (Improper Neutralization of Special Elements used in an SQL Command) - <https://cwe.mitre.org/data/definitions/89.html>
- CWE 95 (Improper Neutralization of Directives in Dynamically Evaluated Code ('Eval Injection')) - <https://cwe.mitre.org/data/definitions/95.html>
- CWE 119 (Improper Restriction of Operations within the Bounds of a Memory Buffer) - <https://cwe.mitre.org/data/definitions/119.html>
- CWE 215 (Information Exposure through Debug Information) - <https://cwe.mitre.org/data/definitions/215.html>
- CWE 388 (7PK - Errors) - <https://cwe.mitre.org/data/definitions/388.html>
- CWE 489 (Leftover Debug Code) - <https://cwe.mitre.org/data/definitions/489.html>
- CWE 502 (Deserialization of Untrusted Data) - <https://cwe.mitre.org/data/definitions/502.html>
- CWE 511 (Logic/Time Bomb) - <https://cwe.mitre.org/data/definitions/511.html>
- CWE 656 (Reliance on Security through Obscurity) - <https://cwe.mitre.org/data/definitions/656.html>
- CWE 676 (Use of Potentially Dangerous Function)  - <https://cwe.mitre.org/data/definitions/676.html>
- CWE 937 (OWASP Top Ten 2013 Category A9 - Using Components with Known Vulnerabilities) - <https://cwe.mitre.org/data/definitions/937.html>
