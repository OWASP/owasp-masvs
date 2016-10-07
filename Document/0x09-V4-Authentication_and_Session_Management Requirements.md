# V4: Authentication and Session Management Requirements

## Control objective

In most cases, user login to a remote service is an integral part of the overall mobile app architecture. Even though most of the logic happens at the endpoint, MASVS defines some basic requirements regarding how user accounts and sessions are managed. The requirements can be easily verified without access to the source code of the service endpoint.

## Requirements

| # | Description | 1 | 2 | 3 | 4 | 
| --- | --- | --- | --- | --- | --- |
| **4.1** | If the app requires access to a remote service, verify that an acceptable form of authentication such as username/password authentication is performed at service endpoints. | ✓ | ✓ | ✓ | ✓ |
| **4.2** | Verify that a password policy exists and is enforced at the remote endpoint. | ✓ | ✓ | ✓ | ✓ |
| **4.3** | Verify that the remote service terminates an existing session when the user logs out. | ✓ | ✓ | ✓ | ✓ |
| **4.4** | Verify that sessions are terminated at the remote end after a predefined period of inactivity. | ✓ | ✓ | ✓ | ✓ |
| **4.5** | Verify that the remote service blocks login attempts in response to an excessive number of unsuccessful attempts. | ✓ | ✓ | ✓ | ✓ |
| **4.6** | Verify that a second factor of authentication exists at the remote endpoint, and that the 2FA requirement is enforced at the remote end.  |   | ✓ | ✓ | ✓ |
| **4.7** | Verify that the remote service generate short-lived access token to authenticate client requests without sending the user's credentials.  |   | ✓ | ✓ | ✓ |

## References

For more information, please see:

- OWASP Mobile Top 10: M4 - Insecure Authentication, M6 - Insecure Authorization
- CWE:  https://cwe.mitre.org/data/definitions/287.html


