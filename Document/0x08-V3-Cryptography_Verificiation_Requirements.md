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
| **3.2** | Verify that the cryptographic primitives used adhere to industry standards. Algorithms that are widely considered weak should not be used.| ✓ | ✓ | ✓ | ✓ |
| **3.3** | Verify that cryptographic modules operate using parameters that are considered secure (e.g. mode, key length). | ✓ | ✓| ✓ | ✓ |
| **3.4** | If proprietary cryptographic algorithms are used, verify the security of these algorithms. Note that proven standard algorithms are recommended over self-written ones, except when concealing the algorithm is a design goal. | ✓ | ✓ | ✓ | ✓ |
| **3.5** | Verify that the application doesn't re-use the same cryptographical key for multiple purposes. | ✓ | ✓ | ✓ | ✓ |
| **3.6** | Verify that all random numbers, random file names, random GUIDs, and random strings are generated using a secure random number generator. |   | ✓ | ✓ | ✓ |
| **3.7** | Verify that all keys and passwords are changeable, and are generated or replaced at installation time. |   | ✓ | ✓ | ✓ |
| **3.8** | Verify that there is an explicit policy for how cryptographic keys are managed (e.g. generated, distributed, revoked, and expired). Verify that this key lifecycle is properly enforced. |   | ✓ | ✓ | ✓ |
| **3.9** | Verify that random numbers are created with proper entropy during the application lifecycle. |   |   | ✓ | ✓ |
| **3.10** | Verify that cryptographic controls do not keep any reference to a key in memory (e.g. bouncy castle's working key). |   |   | ✓ | ✓ |
| **3.11** | Verify that consumers of cryptographic services do not have direct access to key material. Isolate cryptographic processes, including master secrets through the use of strong software protections or a hardware key vault (HSM). |   |   |   | ✓ |

## References

For more information, please see:

(Link to appropriate chapter in the OMTG and other resources).
