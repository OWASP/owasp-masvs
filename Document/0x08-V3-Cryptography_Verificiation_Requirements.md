# V3: Cryptography Verificiation Requirements

## Control objective

One of the core components of any web-based application is the mechanism by which it controls and maintains the state for a user interacting with it. This is referred to this as Session Management and is defined as the set of all controls governing state-full interaction between a user and the web-based application.

Ensure that a verified application satisfies the following high level session management requirements:

- Sessions are unique to each individual and cannot be guessed or shared
- Sessions are invalidated when no longer required and timed out during periods of inactivity.

## Requirements

| # | **Description** | **1** | **2** | **3** | **Since** |
| --- | --- | --- | --- | --- | --- |
| **3.1** | Verify that there is no custom session manager, or that the custom session manager is resistant against all common session management attacks. | ✓ | ✓ | ✓ | 1.0 |
| **3.2** | Verify that sessions are invalidated when the user logs out. | ✓ | ✓ | ✓ | 1.0 |
| **3.3** | Verify that sessions timeout after a specified period of inactivity. | ✓ | ✓ | ✓ | 1.0 |
| **3.4** | Verify that sessions timeout after an administratively-configurable maximum time period regardless of activity (an absolute timeout). |   |   | ✓ | 1.0 |
| **3.5** | Verify that all pages that require authentication have easy and visible access to logout functionality. | ✓ | ✓ | ✓ | 1.0 |

## References

For more information, please see:

- OWASP Testing Guide 4.0: Session Management Testing [https://www.owasp.org/index.php/Testing\_for\_Session\_Management](https://www.owasp.org/index.php/Testing_for_Session_Management)
- OWASP Session Management Cheat Sheet: [https://www.owasp.org/index.php/Session\_Management\_Cheat\_Sheet](https://www.owasp.org/index.php/Session_Management_Cheat_Sheet)
