# V3: Cryptography Verification Requirements

## Control objective

Ensure that a verified application uses cryptography according to industry best practices.

- All cryptographic modules fail in a secure manner and errors are handled correctly.
- A suitable random number generator is used when randomness is required.
- Access to keys is managed in a secure way.

## Requirements

| # | Description | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| **3.1** | Verify that that the application does noy use any hardcoded cryptographic keys as a sole method of encryption.| ✓ | ✓ | ✓ | ✓ |
| **3.2** | Verify that the cryptographic primitives used adhere to industry standards. Algorithms that are widely considered weak should not be used.| ✓ | ✓ | ✓ | ✓ |
| **3.3** | Verify that cryptographic modules operate using parameters that are considered secure (e.g. mode, key length). | ✓ | ✓| ✓ | ✓ |
| **3.4** | If proprietary crytopgraphic algorithms are used, verify the security of these algorithms. Note that proven standard algorithms are recommended over self-written ones, except when concealing the algorithm is a design goal. | ✓ | ✓ | ✓ | ✓ |
| **3.5** | Verify that the application doesn't re-use the same cryptograhical key for multiple purposes. | ✓ | ✓ | ✓ | ✓ |
| **3.6** | Verify that all cryptographic modules fail securely, and errors are handled in a way that does not enable oracle padding. | ✓ | ✓ | ✓ | ✓ |
| **3.7** | Verify that all random numbers, random file names, random GUIDs, and random strings are generated using the cryptographic module's secure random number generator. |   | ✓ | ✓ | ✓ |
| **3.0** | Verify that all keys and passwords are changeable, and are generated or replaced at installation time. |   | ✓ | ✓ | ✓ |
| **3.9** | Verify that there is an explicit policy for how cryptographic keys are managed (e.g. generated, distributed, revoked, and expired). Verify that this key lifecycle is properly enforced. |   | ✓ | ✓ | ✓ |
| **3.10** | Verify that random numbers are created with proper entropy even when the application is under heavy load, or that the application degrades gracefully in such circumstances. |   |   | ✓ | ✓ |
| **3.11** | Verify that consumers of cryptographic services do not have direct access to key material. Isolate cryptographic processes, including master secrets through the use of strong software protections or a hardware key vault (HSM). |   |   |   | ✓ |

## References

For more information, please see:

- OWASP Mobile Testing Guide 1.0: Testing for Weak Implementations of Cryptography
(Link)
