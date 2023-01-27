# V2: Απαιτήσεις Αποθήκευσης Δεδομένων και Ιδιωτικότητας

## Στόχος Ελέγχου

Η προστασία των ευαίσθητων δεδομένων όπως τα διαπιστευτήρια του χρήστη και η ιδιωτική πληροφορία, είναι σημαντικού σκοπού στην ασφάλεια mobile εφαρμογών. Αρχικά, ευαίσθητα δεδομένα μπορεί να εκτεθούν κατα λάθος σε άλλες εφαρμογές που τρέχουν στην ίδια συσκευή αν οι μηχανισμοί του λειτουργικού συστήματος (όπως το IPC) δεν χρησιμοποιούνται κατάλληλα. Δεδομένα μπορεί καταλάθος να διαρεύσουν στο cloud, μέσω μηχανισμών αποθήκευσης, backups ή από την cache του πληκτρολόγιου. Επιπροσθέτως, οι mobile συσκευές, μπορεί να χαθούν ή κλαπούν πιο εύκολα σε σύγκριση με άλλου τύπου συσκευές, με αποτέλεσμα το να αποκτήσει φυσική πρόσβαση ένας επιτιθέμενος να είναι ένα πιο πιθανό σενάριο. Σε αυτή τη περίπτωση, επιπλέον μορφές προστασίας μπορούν να υλοποιηθούν προκειμένου να κάνουν την ανάκτηση ευαίσθητων δεδομένων πιο δύσκολη.

Να σημειωθεί ότι το MASVS είναι προσανατολισμένος γύρω από την εφαρμογή, και δε καλύπτει πολιτικές στο επίπεδο της συσκευής όπως εκείνες που εμπλέκονται με τα λύσεις Διαχείρισης Φορητής Συσκευής (MDM). Ενθαρρύνουμε τη χρήση τέτοιων πολιτικών σε ένα Enterprise περιβάλλον για την επιπλέον ενίσχυση της ασφάλειας των δεδομένων.

### Ορισμός των ευαίσθητων δεδομένων

Τα Ευαίσθητα δεδομένα στο σκοπό του MASVS περιλαμβάνουν και τα διαπιστευτήρια του χρήστη, και κάθε άλλα δεδομένα που θεωρούνται ευαίσθητα στο συγκεκριμένο πλαίσιο όπως:

- Προσωπικά Ταυτοποιήσιμη Πληροφορία (ΡΙΙ) που θα μπορούν να χρησιμοποιηθεί κακόβουλα για κλοπή ταυτότητας. Αριθμοί κοινωνικής ασφάλισης, αριθμοί πιστωτικών καρτών, αριθμοί τραπεζικών λογαριασμών, πληροφορίες υγείας,
- Πολύ ευαίσθητα δεδομένα τα οποία θα οδηγούσαν σε απώλεια φήμης ή/και οικονομικά κόστη σε περίπτωση έκθεσης τους. Πληροφορίες συμβολαίων, πληροφορίες που δε καλύπτονται απο συμφωνο περι μη αποκάλυψης πληροφοριών (non disclosure agreement), πληροφορίες management.
- Οτιδήποτε δεδομένο υποχρεούται να προστατευθεί από το νόμο ή για λόγους συμμόρφωσης.

<!-- \pagebreak -->
## Απαιτήσεις Ασφάλειας

Η συντριπτική πλειοψηφία των προβλημάτων αποκάλυψης δεδομένων μπορεί να αποφευχθεί ακολουθώντας απλούς κανόνες. Οι περισσότεροι από τους μηχανισμούς που περιγράφονται σε αυτό το κεφάλαιο είναι υποχρεωτικοί για όλα τα επίπεδα επαλήθευσης.

| # | MSTG-ID | Περιγραφή | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **2.1** | MSTG-STORAGE-1 | Πρέπει να χρησιμοποιούνται οι παρεχόμενες από το σύστημα δυνατότητας αποθήκευσης διαπιστευτηρίων για να αποθηκεύονται ευαίσθητα δεδομένα όπως PII, διαπιστευτήρια χρηστών ή κλειδιά κρυπτογράφησης. | x | x |
| **2.2** | MSTG-STORAGE-2 | Ευαίσθητα δεδομένα θα πρέπει να μην αποθηκεύονται εκτός του container της εφαρμογής ή των εγκαταστάσεων αποθήκευσης διαπιστευτηρίων του συστήματος. | x | x |
| **2.3** | MSTG-STORAGE-3 | Ευαίσθητα δεδομένα δε θα πρέπει να καταγράφονται σε logs της εφαρμογής. | x | x |
| **2.4** | MSTG-STORAGE-4 | Ευαίσθητα δεδομένα δε θα πρέπει να μοιράζονται με τρίτες οντότητες, εκτός αν είναι ένα απαραίτητο μέρος της Αρχιτεκτόνικης. | x | x |
| **2.5** | MSTG-STORAGE-5 | Η cache του πληκτρολογίου έχει απενεργοποιηθεί στο input του κειμένου που επεξεργάζεται ευαίσθητα δεδομένα. | x | x |
| **2.6** | MSTG-STORAGE-6 | Ευαίσθητα δεδομένα δε θα πρέπει να εκτίθενται μέσω μηχανισμών IPC. | x | x |
| **2.7** | MSTG-STORAGE-7 | Ευαίσθητα δεδομένα όπως κωδικοί ή PINs, δε θα πρέπει να εκτίθεται μέσω της διεπαφής με το χρήστη (user interface) | x | x |
| **2.8** | MSTG-STORAGE-8 | Ευαίσθητα δεδομένα δε θα πρέπει να περιλαμβάνονται σε backups που δημιουργούνται από το λειτουργικό σύστημα.|   | x |
| **2.9** | MSTG-STORAGE-9 | Η εφαρμογή αφαιρεί ευαίσθητα δεδομένα απο τα views όταν η εφαρμογή μετακινείται στο background. |  | x |
| **2.10** | MSTG-STORAGE-10 | Η εφαρμογή δεν κρατάει ευαίσθητα δεδομένα στη μνήμη περισσότερο από το απαραίτητο, και η μνήμη καθαρίζεται μετά τη χρήση αυτή. |  | x |
| **2.11** | MSTG-STORAGE-11 | Η εφαρμογή επιβάλει μια πολιτική ασφάλειας της συσκευής, όπως για παράδειγμα το να απαιτείται από το χρήστη να ορίσει passcode συσκευής. |  | x |
| **2.12** | MSTG-STORAGE-12 | Η εφαρμογή εκπαιδεύει το χρήστη σχετικά με τους τύπους PII που επεξεργάζεται η εφαρμογή, όπως επίσης και για βέλτιστες πρακτικές ασφάλειας που πρέπει να ακολουθεί ο χρήστης κατα τη χρήση της εφαρμογής. | x | x |
| **2.13** | MSTG-STORAGE-13 | Ευαίσθητα δεδομένα δε θα πρέπει να αποθηκεύονται τοπικά στη συσκευή. Αντιθέτως, τα δεδομένα θα πρέπει να ανακτόνται από μια απομακρυσμένη υπηρεσία όταν χρειάζεται, και να αποθηκεύονται μόνο στη μνήμη.|  | x |
| **2.14** | MSTG-STORAGE-14 | Αν απαιτείται τα ευαίσθητα δεδομένα να αποθηκεύονται τοπικά, πρέπει να είναι κρυπτογραφημένα με ένα κλειδί που έχει προκύψει από το hardware-backed storage το οποίο απαιτεί αυθεντικοποίηση. |  | x |
| **2.15** | MSTG-STORAGE-15 | Ο τοπικός αποθηκευτικός χώρος της εφαρμογής θα πρέπει να σβήνεται μετά από έναν υπερβολικό αριθμό από αποτυχημένες προσπάθειες αυθεντικοποίησης. |  | x |

## Αναφορές

Το OWASP Mobile Security Testing Guide παρέχει αναλυτικές οδηγίες για την επαλήθευση οδηγιών των απαιτήσεων που παρουσιάζονται σε αυτό το κεφάλαιο.

- Android: Testing Data Storage - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05d-Testing-Data-Storage.md>
- iOS: Testing Data Storage - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06d-Testing-Data-Storage.md>

For more information, see also:

- OWASP Mobile Top 10: M1 (Improper Platform Usage) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m1-improper-platform-usage>
- OWASP Mobile Top 10: M2 (Insecure Data Storage) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m2-insecure-data-storage>
- CWE 117 (Improper Output Neutralization for Logs) - <https://cwe.mitre.org/data/definitions/117.html>
- CWE 200 (Information Exposure) - <https://cwe.mitre.org/data/definitions/200.html>
- CWE 276 (Incorrect Default Permissions) - <https://cwe.mitre.org/data/definitions/276.html>
- CWE 311 (Missing Encryption of Sensitive Data) - <https://cwe.mitre.org/data/definitions/311.html>
- CWE 312 (Cleartext Storage of Sensitive Information) - <https://cwe.mitre.org/data/definitions/312.html>
- CWE 316 (Cleartext Storage of Sensitive Information in Memory) - <https://cwe.mitre.org/data/definitions/316.html>
- CWE 359 (Exposure of Private Information ('Privacy Violation')) - <https://cwe.mitre.org/data/definitions/359.html>
- CWE 522 (Insufficiently Protected Credentials) - <https://cwe.mitre.org/data/definitions/522.html>
- CWE 524 (Information Exposure Through Caching) - <https://cwe.mitre.org/data/definitions/524.html>
- CWE 530 (Exposure of Backup File to an Unauthorized Control Sphere) - <https://cwe.mitre.org/data/definitions/530.html>
- CWE 532 (Information Exposure Through Log Files) - <https://cwe.mitre.org/data/definitions/532.html>
- CWE 534 (Information Exposure Through Debug Log Files) - <https://cwe.mitre.org/data/definitions/534.html>
- CWE 634 (Weaknesses that Affect System Processes) - <https://cwe.mitre.org/data/definitions/634.html>
- CWE 798 (Use of Hard-coded Credentials) - <https://cwe.mitre.org/data/definitions/798.html>
- CWE 921 (Storage of Sensitive Data in a Mechanism without Access Control) - <https://cwe.mitre.org/data/definitions/921.html>
- CWE 922 (Insecure Storage of Sensitive Information) - <https://cwe.mitre.org/data/definitions/922.html>
