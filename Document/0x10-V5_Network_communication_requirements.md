# V5: Network communication requirements

## Control objective

The purpose of this control is to ensure the confidentiality and integrity of intormation exchanged between the mobile app and remote service endpoints. At the very least, a mobile app must set up a secure, encrypted channel for network communcation using regular PKI infrastructure. Starting from level two, additional defense-in-depth measure such as SSL pinning and mutual authentication are required. 

## Requirements

| # | Description | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| **5.1** | Verify that sensitive data is encrypted on the network using secure communication protocols. Verify that the secure channel is used consistently throughout the app. | ✓ | ✓ | ✓ | ✓ |
| **5.2** | Confirm that the app verifies the identity of the remote endpoint when the secure channel is established. Verify that this is done doing standard methods such as X.509 certificates, and that only certificates signed by a valid CA are accepted. | ✓ | ✓ | ✓ | ✓ |
| **5.3** | Verify that the app pins the endpoint certificate, and subsequently does not establish connections with endpoints that offer a different certificate, even if signed by a trusted CA. |   | ✓ | ✓ | ✓ |
| **5.4** | Verify that the app doesn't rely on insecure communication channels (e.g email and SMS) for critical operations, such as enrollments and OTPs. |   | ✓ | ✓ | ✓ | 
| **5.5** | Verify that the app uses its own certificate store. Make sure that the CA certificate in the device trust store are ignored. |   |   | ✓ | ✓ |
| **5.6** | Confirm that the remote endpoint verifies the identity of the app when secure channel is established (PKI mutual authentication). |   |   | ✓ | ✓ |

## References

SSL Pinning  - https://www.owasp.org/index.php/Certificate_and_Public_Key_Pinning

(...) TODO (...)

For more information, please see:

TODO
