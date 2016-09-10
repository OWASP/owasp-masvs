# V3: Cryptography Verification Requirements

## Control objective

Ensure that a verified application uses cryptography according to industry best practices.

- Sessions are unique to each individual and cannot be guessed or shared
- Sessions are invalidated when no longer required and timed out during periods of inactivity.
- All cryptographic modules fail in a secure manner and errors are handled correctly.
- A suitable random number generator is used when randomness is required.
- Access to keys is managed in a secure way.

## Requirements

| # | Description | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| **3.1** | Verify that that the application does not hardcode any private cryptographic key. The application instead uses the mobile API to securely store it, in case keys are functionally required to be stored.| ✓ | ✓ | ✓ | ✓ |
| **3.2** | Verify that the cryptographic primitives used adhere to industry standards. (e.g. Block size, digest size, key length, etc. )| ✓ | ✓ | ✓ | ✓ |
| **3.3** | Verify that the application doesn't contain self-written cryptographical functions and algorithms . This could introduction of cryptographical vulnerabilities | ✓ | ✓ | ✓ | ✓ |
| **3.4** | Verify that the application doesn't re-use the same cryptograhical key for multiple purposes. Each purpose should have a different key. | ✓ | ✓ | ✓ | ✓ |
| **3.5** | Verify that all cryptographic modules fail securely, and errors are handled in a way that does not enable oracle padding. | ✓ | ✓ | ✓ |  ✓ |
| **3.6** | Verify that all random numbers, random file names, random GUIDs, and random strings are generated using the cryptographic module's approved random number generator when these random values are intended to be not guessable by an attacker. |   | ✓ | ✓ | ✓ |
| **3.7** | Verify that cryptographic modules operate in their approved mode according to their published security policies. |   |   | ✓ | ✓ |
| **3.8** | Verify that there is an explicit policy for how cryptographic keys are managed (e.g., generated, distributed, revoked, and expired). Verify that this key lifecycle is properly enforced. |   | ✓ | ✓ | ✓ |
| **3.9** | Verify that all consumers of cryptographic services do not have direct access to key material. Isolate cryptographic processes, including master secrets and consider the use of a hardware key vault (HSM). |   |   | ✓ | ✓ |
| **3.10** | Personally Identifiable Information should be stored encrypted at rest and ensure that communication goes via protected channels. |   | ✓ | ✓ | ✓ |
| **3.11** | Verify that where possible, keys and secrets are zeroed when destroyed. |   | ✓ | ✓ | ✓ |
| **3.12** | Verify that all keys and passwords are replaceable, and are generated or replaced at installation time. |   | ✓ | ✓ | ✓ |
| **3.13** | Verify that random numbers are created with proper entropy even when the application is under heavy load, or that the application degrades gracefully in such circumstances. |   |   | ✓ | ✓ |
| **3.14** | Verify that random numbers are created with proper entropy even when the application is under heavy load, or that the application degrades gracefully in such circumstances. |   |   | ✓ | ✓ |


## Certificate specific things, not sure yet were to put it. Belongs close to :use HTTPS (network) and close to :do SSL pining (defense in depth.. Needs to be discussed
* Verify that the certificates private keys are build using strong encryption algorithms.

* Verify that the certificates used by an application are not revoked. This could be done by implementing and checking a CRL (Certificate Revocation List).

* Verify that the certificates are not expired and that their chain is validated using the trusted root certificate store present on the mobile device. Verify that the application doesn't use self-signed certificates. 

## References

For more information, please see:

- OWASP Mobile Testing Guide 1.0: Testing for Weak Implementations of Cryptography
(Link)

