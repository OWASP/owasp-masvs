# V3: Cryptography Verification Requirements

## Control objective

Cryptography is an essential ingredient when it comes to protecting data stored on a mobile device. It is also a category where things can go horribly wrong, especially when standard conventions are not followed. The purpose of the controls in this chapter is to ensure that the verified application uses cryptography according to industry best practices, including:

- Use of proven cryptographic libraries;
- Proper choice and configuration of cryptographic primitives;
- Handling of errors, so that cryptographic modules fail in a secure manner;
- Suitable random number generator wherever randomness is required;
- Access management for cryptographic keys.

## Requirements

| # | Description | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| **3.1** | Verify that that the application does not rely on symmetric cryptography with hardcoded keys as a sole method of encryption.| ✓ | ✓ | ✓ | ✓ |
| **3.2** | Verify that the app uses proven implementations of cryptographic functions. | ✓ | ✓ | ✓ | ✓ |
| **3.3** | Verify that the app does not use cryptograpic protocols or algorithms are used that are widely considered depreciated. | ✓ | ✓| ✓ | ✓ |
| **3.3** | Verify that cryptographic modules use parameters that adhere to current industry best practices. This includes key length and modes of operation. | ✓ | ✓| ✓ | ✓ |
| **3.4** | Verify that the application doesn't re-use the same cryptographic key for multiple purposes. | ✓ | ✓ | ✓ | ✓ |
| **3.5** | Verify that all random numbers, random file names, random GUIDs, and random strings are generated using a secure random number generator. | ✓ | ✓ | ✓ | ✓ |
| **3.6** | Verify that all keys and passwords are changeable, and are generated or replaced at installation time. |   | ✓ | ✓ | ✓ |
| **3.7** | Verify that random numbers are created with proper entropy during the application lifecycle. |   |   | ✓ | ✓ |
| **3.8** | Verify that cryptographic controls explicitly clear memory containing (working-)keys after they have been used. |   |   | ✓ | ✓ |
| **3.9** | Verify that consumers of cryptographic services do not have direct access to key material if the keying material is locally generated. Isolate cryptographic processes, including master secrets through the use of strong software protections (MASVS L4) or a hardware key vault (HSM). |   |   |   | ✓ |

## References

For more information, see also:

- OWASP Mobile Top 10: M5 - Insufficient Cryptography
- CWE: https://cwe.mitre.org/data/definitions/310.html
