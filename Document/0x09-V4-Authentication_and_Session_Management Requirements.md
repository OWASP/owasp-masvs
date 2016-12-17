# V4: Authentication and Session Management Requirements

## Control objective

In most cases, user login to a remote service is an integral part of the overall mobile app architecture. Even though most of the logic happens at the endpoint, MASVS defines some basic requirements regarding how user accounts and sessions are managed. The requirements can be easily verified without access to the source code of the service endpoint.

## Requirements

| # | Description | L1 | L2 | R |
| --- | --- | --- | --- | --- |
| **4.1** | If the app provides users with access to a remote service, an acceptable form of authentication such as username/password authentication is performed at the remote endpoint. | ✓ | ✓ | ✓ |
| **4.2** | The remote endpoint generates short-lived access tokens to authenticate client requests without sending the user's credentials.  | ✓ | ✓ | ✓ |
| **4.3** | A password policy exists and is enforced at the remote endpoint. | ✓ | ✓ | ✓ |
| **4.4** | The remote endpoint terminates the existing session when the user logs out. | ✓ | ✓ | ✓ |
| **4.5** | Sessions are terminated at the remote endpoint after a predefined period of inactivity. | ✓ | ✓ | ✓ |
| **4.6** | The remote endpoint implements an exponential back-off, or temporarily locks the user account, when incorrect authentication credentials are submitted an excessive number of times . | ✓ | ✓ | ✓ |
| **4.7** | Biometric authentication, if any, is not event-bound, but is based on keying material being unlocked by the specific biometric authentication method. | ✓  | ✓ | ✓ |
| **4.8** | A second factor of authentication exists at the remote endpoint and the 2FA requirement is consistently enforced.  |   | ✓ | ✓ |
| **4.9** | Step-up authentication is required to enable actions that deal with sensitive data or transactions.  |   | ✓ | ✓ |
| **4.10** | The remote endpoint prevents session hijacking (e.g. by binding the session to the client IP address, or indirectly by using payload encryption).  |   | ✓ | ✓ |
| **4.11** |  The app informs the user of all login activities with his or her account. Users are able view a list of devices used to access the account, and to block specific devices. |  | ✓ | ✓ |

## References

For more information, see also:

- OWASP Mobile Top 10: M4 - Insecure Authentication, M6 - Insecure Authorization
- CWE:  https://cwe.mitre.org/data/definitions/287.html
