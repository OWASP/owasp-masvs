# V6: Απαιτήσεις Αλληλεπίδρασης με τη Πλατφόρμα

## Στόχος Ελέγχου

Τα στοιχεία ελέγχου αυτής της ομάδας διασφαλίζουν ότι η εφαρμογή χρησιμοποιεί τα APIs της πλατφόρμας και standard μέρη της με ασφαλή τρόπο. Επιπλέον, τα στοιχεία ελέγχου καλύπτουν την επικοινωνία μεταξύ εφαρμογών (IPC).

## Απαιτήσεις Επαλήθευσης Ασφάλειας

| # | MSTG-ID | Description | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **6.1** | MSTG-PLATFORM-1 | Η εφαρμογή ζητά μόνο το ελάχιστο σύνολο απαραίτητων αδειών. | x | x |
| **6.2** | MSTG-PLATFORM-2 | Όλες τα inputs από εξωτερικές πηγές καθώς και ο χρήστης επικυρώνονται, και εάν χρειάζεται, γίνονται sanitize. Αυτό περιλαμβάνει δεδομένα που λαμβάνονται μέσω της διεπαφής χρήστη (UI), μηχανισμούς IPC, όπως intents, προσαρμοσμένα URLs και πηγές δικτύου. | x | x |
| **6.3** | MSTG-PLATFORM-3 | Η εφαρμογή δεν εξάγει ευαίσθητες λειτουργίες μέσω προσαρμοσμένων URL schemes, εκτός εάν αυτοί οι μηχανισμοί προστατεύονται σωστά. | x | x |
| **6.4** | MSTG-PLATFORM-4 | Η εφαρμογή δεν εξάγει ευαίσθητη λειτουργικότητα μέσω IPC δυνατοτήτων, εκτός εάν αυτοί οι μηχανισμοί προστατεύονται κατάλληλα. | x | x |
| **6.5** | MSTG-PLATFORM-5 | Η JavaScript είναι απενεργοποιημένη στα WebViews, εκτός εάν απαιτείται ρητά. | x | x |
| **6.6** | MSTG-PLATFORM-6 | Τα WebViews έχουν ρυθμιστεί ώστε να επιτρέπουν μόνο το ελάχιστο σύνολο απαιτούμενων protocol handlers (ιδανικά, υποστηρίζεται μόνο το https). Οι δυνητικά επικίνδυνοι handlers, όπως το file, το tel και το app-id, είναι απενεργοποιημένα.| x | x |
| **6.7** | MSTG-PLATFORM-7 | Εάν οι native μέθοδοι της εφαρμογής εκτίθενται σε ένα WebView, βεβαιωθείτε ότι το WebView αποδίδει μόνο JavaScript που περιέχεται στο package της εφαρμογής. | x | x |
| **6.8** | MSTG-PLATFORM-8 | Το object deserialization (εάν υπάρχει), υλοποιείται με χρήση ασφαλών serialization APIs. | x | x |
| **6.9** | MSTG-PLATFORM-9 | Η εφαρμογή προστατεύεται από επιθέσεις επικάλυψης οθόνης (screen overlay attacks, μόνο για Android) |  | x |
| **6.10** | MSTG-PLATFORM-10 | Η cache, το storage και οι φορτωμένοι πόροι (JavaScript, κ.λπ.) ενός WebView θα πρέπει να διαγραφούν πριν καταστραφεί το WebView. |  | x |
| **6.11** | MSTG-PLATFORM-11 | Επαληθεύστε ότι η εφαρμογή αποτρέπει τη χρήση τρίτων (custom) πληκτρολογίων, όποτε εισάγονται ευαίσθητα δεδομένα (μόνο για iOS).| | x |

## Αναφορές

Tο OWASP Mobile Security Testing Guide παρέχει λεπτομερείς οδηγίες για την επαλήθευση των απαιτήσεων που αναφέρονται σε αυτήν την ενότητα.

- Android: Testing Platform Interaction - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05h-Testing-Platform-Interaction.md>
- iOS: Testing Platform Interaction - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06h-Testing-Platform-Interaction.md>

Για περισσότερες πληροφορίες, δείτε επίσης:

- OWASP Mobile Top 10: M1 (Improper Platform Usage) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m1-improper-platform-usage>
- OWASP Mobile Top 10: M7 (Poor Code Quality) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m7-client-code-quality>
- CWE 20 (Improper Input Validation) - <https://cwe.mitre.org/data/definitions/20.html>
- CWE 79 (Improper Neutralization of Input During Web Page Generation) - <https://cwe.mitre.org/data/definitions/79.html>
- CWE 200 (Information Leak / Disclosure) - <https://cwe.mitre.org/data/definitions/200.html>
- CWE 250 (Execution with Unnecessary Privileges) - <https://cwe.mitre.org/data/definitions/250.html>
- CWE 672 (Operation on a Resource after Expiration or Release) - <https://cwe.mitre.org/data/definitions/672.html>
- CWE 749 (Exposed Dangerous Method or Function) - <https://cwe.mitre.org/data/definitions/749.html>
- CWE 772 (Missing Release of Resource after Effective Lifetime) - <https://cwe.mitre.org/data/definitions/772.html>
- CWE 920 (Improper Restriction of Power Consumption) - <https://cwe.mitre.org/data/definitions/920.html>
- CWE 925 (Improper Verification of Intent by Broadcast Receiver) - <https://cwe.mitre.org/data/definitions/925.html>
- CWE 926 (Improper Export of Android Application Components) - <https://cwe.mitre.org/data/definitions/926.html>
- CWE 927 (Use of Implicit Intent for Sensitive Communication) - <https://cwe.mitre.org/data/definitions/927.html>
- CWE 939 (Improper Authorization in Handler for Custom URL Scheme) - <https://cwe.mitre.org/data/definitions/939.html>
