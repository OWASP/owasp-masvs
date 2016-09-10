# V3: Cryptography Verification Requirements

## Control objective

{General description)

Ensure that a verified application uses cryptography according to industry best practices.

- Sessions are unique to each individual and cannot be guessed or shared
- Sessions are invalidated when no longer required and timed out during periods of inactivity.

## Requirements

| # | Description | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| **3.1** | Verify that that the app does not use symmetric cryptography with hardcoded secret keys. | ✓ | ✓ | ✓ | ✓ |
| **3.2** | Verify that the cryptographic primitives used adhere to industry standards. | ✓ | ✓ | ✓ | ✓ |
| **3.3** | Verify that the application doesn't contain self-written cryptographical functions and algorithms . This could introduction of cryptographical vulnerabilities | ✓ | ✓ | ✓ | ✓ |


## References

For more information, please see:

- OWASP Mobile Testing Guide 1.0: Testing for Weak Implementations of Cryptography
(Link)

