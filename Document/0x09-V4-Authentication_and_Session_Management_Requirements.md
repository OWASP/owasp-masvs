# V4: Authentication and Session Management Requirements

## Control Objective

In most cases, users logging into a remote service is an integral part of the overall mobile app architecture. Even though most of the logic happens at the endpoint, MASVS defines some basic requirements regarding how user accounts and sessions are to be managed.

## Security Verification Requirements

| # | MSTG-ID | Description | L1 | L2 |
| -- | -------- | ---------------------- | - | - |
| **4.1** | MSTG-AUTH-1 | If the app provides users access to a remote service, some form of authentication, such as username/password authentication, is performed at the remote endpoint. | ✓ | ✓ |
| **4.2** | MSTG-AUTH-2 | If stateful session management is used, the remote endpoint uses randomly generated session identifiers to authenticate client requests without sending the user's credentials. | ✓ | ✓ |
| **4.3** | MSTG-AUTH-3 | If stateless token-based authentication is used, the server provides a token that has been signed using a secure algorithm. | ✓ | ✓ |
| **4.4** | MSTG-AUTH-4 | The remote endpoint terminates the existing session when the user logs out. | ✓ | ✓ |
| **4.5** | MSTG-AUTH-5 | A password policy exists and is enforced at the remote endpoint. | ✓ | ✓ |
| **4.6** | MSTG-AUTH-6 | The remote endpoint implements a mechanism to protect against the submission of credentials an excessive number of times. | ✓ | ✓ |
| **4.7** | MSTG-AUTH-7 | Sessions are invalidated at the remote endpoint after a predefined period of inactivity and access tokens expire. | ✓ | ✓ |
| **4.8** | MSTG-AUTH-8 | Biometric authentication, if any, is not event-bound (i.e. using an API that simply returns "true" or "false"). Instead, it is based on unlocking the keychain/keystore. | | ✓ |
| **4.9** | MSTG-AUTH-9 | A second factor of authentication exists at the remote endpoint and the 2FA requirement is consistently enforced.  | | ✓ |
| **4.10** | MSTG-AUTH-10 | Sensitive transactions require step-up authentication. | | ✓ |
| **4.11** | MSTG-AUTH-11 | The app informs the user of all sensitive activities with their account. Users are able to view a list of devices, view contextual information (IP address, location, etc.), and to block specific devices. | | ✓ |
| **4.12** | MSTG-AUTH-12 | Authorization models should be defined and enforced at the remote endpoint. | ✓ | ✓ |

## References

The OWASP Mobile Security Testing Guide provides detailed instructions for verifying the requirements listed above.

- General: Authentication and Session Management - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04e-Testing-Authentication-and-Session-Management.md>
- Android: Testing Local Authentication - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05f-Testing-Local-Authentication.md>
- iOS: Testing Local Authentication - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06f-Testing-Local-Authentication.md>

For more information, see also:

- OWASP Mobile Top 10: M4 (Insecure Authentication) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m4-insecure-authentication>
- OWASP Mobile Top 10: M6 (Insecure Authorization) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m6-insecure-authorization>
- CWE 287 (Improper Authentication) - <https://cwe.mitre.org/data/definitions/287.html>
- CWE 307 (Improper Restriction of Excessive Authentication Attempts) - <https://cwe.mitre.org/data/definitions/307.html>
- CWE 308 (Use of Single-factor Authentication) - <https://cwe.mitre.org/data/definitions/308.html>
- CWE 521 (Weak Password Requirements) - <https://cwe.mitre.org/data/definitions/521.html>
- CWE 604 (Use of Client-Side Authentication) - <https://cwe.mitre.org/data/definitions/604.html>
- CWE 613 (Insufficient Session Expiration) - <https://cwe.mitre.org/data/definitions/613.html>
