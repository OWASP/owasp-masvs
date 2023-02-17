# Authentication and Authorization (MASVS-AUTH)

## Description

In most cases, users logging into a remote service is an integral part of the overall mobile app architecture. Even though most of the logic happens at the endpoint, MASVS defines some basic requirements that should also be considered from the client-side as well as other local authentication mechanisms such as biometrics.

## Controls

| ID | Statement |
|----|-----------|
| MASVS-AUTH-1 | The app uses secure authentication and authorization protocols and follows the relevant best practices. |
| MASVS-AUTH-2 | The app performs local authentication securely according to the platform best practices. |
| MASVS-AUTH-3 | The app secures sensitive operations with additional authentication. |

## References

The OWASP Mobile Application Security Testing Guide provides detailed instructions for verifying the requirements listed above.

- General: Authentication and Session Management - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x04e-Testing-Authentication-and-Session-Management.md>
- Android: Testing Local Authentication - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x05f-Testing-Local-Authentication.md>
- iOS: Testing Local Authentication - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x06f-Testing-Local-Authentication.md>
