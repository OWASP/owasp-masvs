# V7: Code Quality and Build Setting Requirements

## Control Objective

The goal of this control is to ensure that basic security coding practices are followed in developing the app, and that "free" security features offered by the compiler are activated.

## Security Verification Requirements

| # | MSTG-ID | Description | L1 | L2 |
| --- | --- | --- | --- | --- |
| **7.1** | MSTG‑CODE‑1 | The app is signed and provisioned with a valid certificate, of which the private key is properly protected. | ✓ | ✓ |
| **7.2** | MSTG‑CODE‑2 | The app has been built in release mode, with settings appropriate for a release build (e.g. non-debuggable). | ✓ | ✓ |
| **7.3** | MSTG‑CODE‑3 | Debugging symbols have been removed from native binaries. | ✓ | ✓ |
| **7.4** | MSTG‑CODE‑4 | Debugging code has been removed, and the app does not log verbose errors or debugging messages. | ✓ | ✓ |
| **7.5** | MSTG‑CODE‑5 | All third party components used by the mobile app, such as libraries and frameworks, are identified, and checked for known vulnerabilities. | ✓ | ✓ |
| **7.6** | MSTG‑CODE‑6 | The app catches and handles possible exceptions.| ✓ | ✓ |
| **7.7** | MSTG‑CODE‑7 | Error handling logic in security controls denies access by default. | ✓ | ✓ |
| **7.8** | MSTG‑CODE‑8 | In unmanaged code, memory is allocated, freed and used securely.  | ✓ | ✓ |
| **7.9** | MSTG‑CODE‑9 | Free security features offered by the toolchain, such as byte-code minification, stack protection, PIE support and automatic reference counting, are activated. | ✓ | ✓ |

<div style="page-break-after: always;"></div>

## References

The OWASP Mobile Security Testing Guide provides detailed instructions for verifying the requirements listed above.

- Android - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05i-Testing-Code-Quality-and-Build-Settings.md>
- iOS - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06i-Testing-Code-Quality-and-Build-Settings.md>

For more information, see also:

- OWASP Mobile Top 10: M7 - Poor Code Quality: <https://www.owasp.org/index.php/Mobile_Top_10_2016-M7-Poor_Code_Quality>
- CWE: <https://cwe.mitre.org/data/definitions/119.html>
- CWE: <https://cwe.mitre.org/data/definitions/89.html>
- CWE: <https://cwe.mitre.org/data/definitions/388.html>
- CWE: <https://cwe.mitre.org/data/definitions/489.html>
