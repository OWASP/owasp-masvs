# V3: Cryptography Requirements

## Control Objective

Cryptography is an essential ingredient when it comes to protecting data stored on a mobile device. It is also a category where things can go horribly wrong, especially when standard conventions are not followed. The purpose of the controls in this chapter is to ensure that the verified application uses cryptography according to industry best practices, including:

- Use of proven cryptographic libraries;
- Proper choice and configuration of cryptographic primitives;
- A suitable random number generator wherever randomness is required.

## Security Verification Requirements

| # | MSTG-ID | Description | L1 | L2 |
| --- | --- | --- | --- | --- |
| **3.1** | MSTG‑CRYPTO‑1 | The app does not rely on symmetric cryptography with hardcoded keys as a sole method of encryption.| ✓ | ✓ |
| **3.2** | MSTG‑CRYPTO‑2 | The app uses proven implementations of cryptographic primitives. | ✓ | ✓ |
| **3.3** | MSTG‑CRYPTO‑3 | The app uses cryptographic primitives that are appropriate for the particular use-case, configured with parameters that adhere to industry best practices. | ✓ | ✓|
| **3.4** | MSTG‑CRYPTO‑4 | The app does not use cryptographic protocols or algorithms that are widely considered depreciated for security purposes. | ✓ | ✓|
| **3.5** | MSTG‑CRYPTO‑5 | The app doesn't re-use the same cryptographic key for multiple purposes. | ✓ | ✓ |
| **3.6** | MSTG‑CRYPTO‑6 | All random values are generated using a sufficiently secure random number generator. | ✓ | ✓ |

<div style="page-break-after: always;"></div>

## References

The OWASP Mobile Security Testing Guide provides detailed instructions for verifying the requirements listed in this section.

- Android - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05e-Testing-Cryptography.md>
- iOS - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06e-Testing-Cryptography.md>

For more information, see also:

- OWASP Mobile Top 10: M5 - Insufficient Cryptography: <https://www.owasp.org/index.php/Mobile_Top_10_2016-M5-Insufficient_Cryptography>
- CWE: <https://cwe.mitre.org/data/definitions/310.html>
