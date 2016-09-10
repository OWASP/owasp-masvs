# V5: Network communication requirements

## Control objective

{overview)

Ensure that a verified application satisfies the following high level requirements:

(list)

## Requirements

| # | Description | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| **5.1** | Verify that sensitive data is encrypted on the network using secure communication protocols. This guarantees integrity of the data as well as authenticity. For the HTTP protocol, this means that only HTTPS should be used. Reference "Cryptography Verificiation Requirements" to ensure HTTPS is properly configured and implemented| ✓ | ✓ | ✓ | ✓ |
| **5.2** | Verify integrity of this secure channel in a systematic way, for each request being send (and received in case of client authenication).|  |  | ✓ | ✓ |
| **5.3** | Verify the authenticity of the rest/web backend before any acton or data is send to it.| ✓ | ✓ | ✓ | ✓ |
| **5.4** | Verify that the rest/Web server authenticates the application before any data is send back to it. Parameters collected during the device binding process should be used to identify the device itself. In the best case, this process is part of mutual authentication using e.g. PKI. |   |   | ✓ | ✓ |
| **5.5** | Verify that the the application implements an addition layer of security on top of the secure channel, when sending and receiving data. In the case that the secure channel is compromised (e.g. hartbleed, Drown, Poodle), the application still has a way to ensure integrity and confidentiality is preserved. This layer has to be implemented using proven and appropriate cryptograhic algorithms and methods (e.g. HMAC).|   |   |   | ✓ |
| **5.6** | Verify that the Application doesn't rely on external (to the application) unsecure communication (e.g email, SMS, etc.) for critical operations (enrollment, device binding, One time passwords, etc.). Unsecure communication channels could be used as an attack vector to circumvent application security mechanisms. |   |   |   | ✓ | 


## References

For more information, please see:

TODO
