# V3: Cryptography Requirements

## Control Objective

Cryptography is an essential ingredient when it comes to protecting data stored on a mobile device. It is also a category where things can go horribly wrong, especially when standard conventions are not followed. The purpose of the controls in this chapter is to ensure that the verified application uses cryptography according to industry best practices, including:

- Use of proven cryptographic libraries;
- Proper choice and configuration of cryptographic primitives;
- Handling of errors, so that cryptographic modules fail in a secure manner;
- Suitable random number generator wherever randomness is required;
- Access management for cryptographic keys.

## Security Verification Requirements

| # | Description | L1 | L2 |
| --- | --- | --- | --- |
| **3.1** | The app does not rely on symmetric cryptography with hardcoded keys as a sole method of encryption.| ✓ | ✓ |
| **3.2** | The app uses proven implementations of cryptographic primitives. | ✓ | ✓ |
| **3.3** | The app does not use cryptographic protocols or algorithms that are widely considered depreciated. | ✓ | ✓|
| **3.4** | Cryptographic modules use parameters that adhere to current industry best practices. This includes key length and modes of operation. | ✓ | ✓|
| **3.5** | The app doesn't re-use the same cryptographic key for multiple purposes. | ✓ | ✓ |
| **3.6** | All random values are generated using a sufficiently secure random number generator. | ✓ | ✓ |
| **3.7** | All cryptographic keys are changeable, and are generated or replaced at installation time. |   | ✓ |

## References

For more information, see also:

- OWASP Mobile Top 10: M5 - Insufficient Cryptography
- CWE: https://cwe.mitre.org/data/definitions/310.html
