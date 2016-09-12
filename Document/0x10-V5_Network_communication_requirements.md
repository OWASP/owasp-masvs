# V5: Network communication requirements

## Control objective

{overview)

Ensure that a verified application satisfies the following high level requirements:

(list)

## Requirements

| # | Description | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| **5.1** | Verify that sensitive data is encrypted on the network using secure communication protocols. Verify that the secure channel is used consistently throughout the app. | ✓ | ✓ | ✓ | ✓ |
| **5.2** | Confirm that the app verifies the identity of the remote endpoint when the secure channel is established. Verify that this is done doing standard methods such as X.509 certificates, and that only certificates signed by a valid CA are accepted. | ✓ | ✓ | ✓ | ✓ |
| **5.3** | Verify that the app ignores uses its own certificate store. Make sure that the CA certificate in the device trust store are ignored. |   |   | ✓ | ✓ |
| **5.4** | Verify that the app pins the endpoint certificate, and subsequently does not establish connections with endpoints that offer a different certificate, even if signed by a trusted CA. |   | ✓ | ✓ | ✓ |
| **5.5** | Confirm that the remote endpoint verifies the identity of the app when secure channel is established (PKI mutual authentication). |   |   | ✓ | ✓ |
| **5.6** | Verify that the app doesn't rely on insecure communication channels (e.g email and SMS) for critical operations, such as enrollments and OTPs. |   |   | ✓| ✓ | 


## References

SSL Pinning  - https://www.owasp.org/index.php/Certificate_and_Public_Key_Pinning

For more information, please see:

TODO
