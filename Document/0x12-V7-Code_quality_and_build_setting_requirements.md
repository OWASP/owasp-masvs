# V7: Code Quality and Build Setting Requirements

## Control Objective

The goal of this control is to ensure that basic security coding practices are followed in developing the app, and that "free" security features offered by the compiler are activated.

## Security Verification Requirements

| # | MSTG-ID | Description | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **7.1** | MSTG-CODE-1 | The app is signed and provisioned with a valid certificate, of which the private key is properly protected. | x | x |
| **7.2** | MSTG-CODE-2 | The app has been built in release mode, with settings appropriate for a release build (e.g. non-debuggable). | x | x |
| **7.3** | MSTG-CODE-3 | Debugging symbols have been removed from native binaries. | x | x |
| **7.4** | MSTG-CODE-4 | Debugging code and developer assistance code (e.g. test code, backdoors, hidden settings) have been removed. The app does not log verbose errors or debugging messages. | x | x |
| **7.5** | MSTG-CODE-5 | All third party components used by the mobile app, such as libraries and frameworks, are identified, and checked for known vulnerabilities. | x | x |
| **7.6** | MSTG-CODE-6 | The app catches and handles possible exceptions.| x | x |
| **7.7** | MSTG-CODE-7 | Error handling logic in security controls denies access by default. | x | x |
| **7.8** | MSTG-CODE-8 | In unmanaged code, memory is allocated, freed and used securely.  | x | x |
| **7.9** | MSTG-CODE-9 | Free security features offered by the toolchain, such as byte-code minification, stack protection, PIE support and automatic reference counting, are activated. | x | x |

## References

The OWASP Mobile Application Security Testing Guide provides detailed instructions for verifying the requirements listed above.

- Android: Testing Code Quality and Build Settings - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x05i-Testing-Code-Quality-and-Build-Settings.md>
- iOS: Testing Code Quality and Build Settings - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x06i-Testing-Code-Quality-and-Build-Settings.md>

For more information, see also:

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
