# V4: Authentication and Session Management Requirements

## Control Objective

In most cases, user login to a remote service is an integral part of the overall mobile app architecture. Even though most of the logic happens at the endpoint, MASVS defines some basic requirements regarding how user accounts and sessions are managed. The requirements can be easily verified without access to the source code of the service endpoint.

## Security Verification Requirements

| # | Description | L1 | L2 |
| --- | --- | --- | --- |
| **4.1** | If the app provides users with access to a remote service, an acceptable form of authentication such as username/password authentication is performed at the remote endpoint. | ✓ | ✓ |
| **4.2** | The remote endpoint uses randomly generated session identifiers, if classical server side session management is used, to authenticate client requests without sending the user's credentials.  | ✓ | ✓ |
| **4.3** | The remote endpoint uses server side signed tokens, if stateless authentication is used, to authenticate client requests without sending the user's credentials.  | ✓ | ✓ |
| **4.4** | The remote endpoint terminates the existing session when the user logs out. | ✓ | ✓ |
| **4.5** | A password policy exists and is enforced at the remote endpoint. | ✓ | ✓ |
| **4.6** | The remote endpoint implements an exponential back-off, or temporarily locks the user account, when incorrect authentication credentials are submitted an excessive number of times . | ✓ | ✓ |
| **4.7** | Biometric authentication, if any, is not event-bound (i.e. using an API that simply returns "true" or "false"). Instead, it is based on unlocking the keychain/keystore. |   | ✓ |
| **4.8** | Sessions are terminated at the remote endpoint after a predefined period of inactivity. |   | ✓ |
| **4.9** | A second factor of authentication exists at the remote endpoint and the 2FA requirement is consistently enforced.  |   | ✓ |
| **4.10** | Step-up authentication is required to enable actions that deal with sensitive data or transactions.  |   | ✓ |
| **4.11** |  The app informs the user of all login activities with his or her account. Users are able view a list of devices used to access the account, and to block specific devices. |  | ✓ |

## References

The OWASP Mobile Security Testing Guide provides detailed instructions for verifying the requirements listed in this section.

- Fopr Android - https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05f-Testing-Authentication.md
- For iOS - https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06f-Testing-Authentication-and-Session-Management.md

For more information, see also:

- OWASP Mobile Top 10: M4 - Insecure Authentication, M6 - Insecure Authorization
- CWE:  https://cwe.mitre.org/data/definitions/287.html
