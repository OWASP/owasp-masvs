# V4: Authentication and Session Management Requirements

## Control objective

(...) TODO (...)

## Requirements

| # | Description | 1 | 2 | 3 | 4 | 
| --- | --- | --- | --- | --- | --- |
| **4.1** | If the app requires access to a remote service, verify that an acceptable form of authentication such as username/password authentication is performed at service endpoints. | ✓ | ✓ | ✓ | ✓ |
| **4.2** | Verify that a password policy exists and is enforced at the remote endpoint. | ✓ | ✓ | ✓ | ✓ |
| **4.3** | Verify that the remote service terminates an existing session when the user logs out. | ✓ | ✓ | ✓ | ✓ |
| **4.4** | Verify that sessions are terminated at the remote end after a predefined period of inactivity. | ✓ | ✓ | ✓ | ✓ |
| **4.5** | Verify that the remote service blocks login attempts in response to an excessive number of unsuccessful attempts. | ✓ | ✓ | ✓ | ✓ |
| **4.6** | Verify that for all client side controls also server side control are implemented. | ✓ | ✓ | ✓ | ✓ |
| **4.7** | Verify that a second factor of authentication exists at the remote endpoint, and that the 2FA requirement is enforced at the remote end.  |   | ✓ | ✓ | ✓ |
| **4.8** | Verify that local biometric mechanisms, like fingerprint authentication are implemented accordingly to best practices.  |   | ✓ | ✓ | ✓ |
| **4.9** | Verify that local biometric mechanisms are not used as the only authentication control for critical functionalities.  |   | ✓ | ✓ | ✓ |

## References

For more information, please see:

- OWASP Mobile Security Testing Guide 1.0: Authentication and Session Management (link)

