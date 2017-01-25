# V5: Network Communication Requirements

## Control Objective

The purpose of this control is to ensure the confidentiality and integrity of information exchanged between the mobile app and remote service endpoints. At the very least, a mobile app must set up a secure, encrypted channel for network communication using regular PKI infrastructure. For level two or higher, additional defense-in-depth measure such as SSL pinning are required.

## Security Verification Requirements

| # | Description | 1 | 2 |
| --- | --- | --- | --- |
| **5.1** | Sensitive data is encrypted on the network using TLS. The secure channel is used consistently throughout the app. | ✓ | ✓ |
| **5.2** | The app verifies the X.509 certificate of the remote endpoint when the secure channel is established. Only certificates signed by a valid CA are accepted. | ✓ | ✓ |
| **5.3** | The app either uses its own certificate store, or pins the endpoint certificate or public key, and subsequently does not establish connections with endpoints that offer a different certificate or key, even if signed by a trusted CA. |   | ✓ |
| **5.4** | The cipher suite used to encrypt network data enables perfect forward secrecy. |   | ✓ |
| **5.5** | The app doesn't rely on a single insecure communication channel (email or SMS) for critical operations, such as enrollments and account recovery. |  | ✓ |

## References

For more information, see also:

- OWASP Mobile Top 10:  M3 - Insecure Communication
- CWE: https://cwe.mitre.org/data/definitions/319.html
- CWE: https://cwe.mitre.org/data/definitions/295.html
