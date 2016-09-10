# V7: Secure coding requirements

## Control objective

Ensure that a verified application satisfies the following high level requirements:

- That all cryptographic modules fail in a secure manner and that errors are handled correctly.
- That a suitable random number generator is used when randomness is required.
- That access to keys is managed in a secure way.

## Requirements

| # | Description | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| **7.2** | Verify that all cryptographic modules fail securely, and errors are handled in a way that does not enable oracle padding. | ✓ | ✓ | ✓ |  ✓ |
| **7.6** | Verify that all random numbers, random file names, random GUIDs, and random strings are generated using the cryptographic module's approved random number generator when these random values are intended to be not guessable by an attacker. |   | ✓ | ✓ | ✓ |
| **7.7** | Verify that cryptographic algorithms used by the application have been validated against FIPS 140-2 or an equivalent standard. | ✓ | ✓ | ✓ | ✓ |
| **7.8** | Verify that cryptographic modules operate in their approved mode according to their published security policies. |   |   | ✓ | ✓ |
| **7.9** | Verify that there is an explicit policy for how cryptographic keys are managed (e.g., generated, distributed, revoked, and expired). Verify that this key lifecycle is properly enforced. |   | ✓ | ✓ | ✓ |
| **7.11** | Verify that all consumers of cryptographic services do not have direct access to key material. Isolate cryptographic processes, including master secrets and consider the use of a hardware key vault (HSM). |   |   | ✓ | ✓ |
| **7.12** | _Personally Identifiable Information_ should be stored encrypted at rest and ensure that communication goes via protected channels. |   | ✓ | ✓ | ✓ |
| **7.13** | Verify that where possible, keys and secrets are zeroed when destroyed. |   | ✓ | ✓ | ✓ |
| **7.14** | Verify that all keys and passwords are replaceable, and are generated or replaced at installation time. |   | ✓ | ✓ | ✓ |
| **7.15** | Verify that random numbers are created with proper entropy even when the application is under heavy load, or that the application degrades gracefully in such circumstances. |   |   | ✓ | ✓ |



| **X** | Verify that no confidential data is stored in the application code. Examples of this kind of data are credentials, keys, etc. Reverse engineering techniques allow extraction of this data. | ✓ | ✓ | ✓ | ✓ |

| **X** | Verify that no confidential data is cached on the client device. Examples of this kind of data are credentials, keys, etc. Examples of caching vectors are keyboard key-presses, network requests, cookies, etc. Reverse engineering techniques allow extraction of this cached data. |   | ✓ | ✓ | ✓ |



## References

TODO

