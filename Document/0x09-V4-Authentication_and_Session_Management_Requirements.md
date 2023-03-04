# MASVS-AUTH: Authentication and Authorization

## Description

Authentication and authorization are essential components of most mobile apps, especially those that connect to a remote service. These mechanisms provide an added layer of security and help prevent unauthorized access to sensitive user data. Although the enforcement of these mechanisms must be on the remote endpoint, it is equally important for the app to follow relevant best practices to ensure the secure use of the involved protocols.

Mobile apps often use different forms of authentication, such as biometrics, PIN, or multi-factor authentication code generators, to validate user identity. These mechanisms must be implemented correctly to ensure their effectiveness in preventing unauthorized access. Additionally, some apps may rely solely on local app authentication and may not have a remote endpoint. In such cases, it is critical to ensure that local authentication mechanisms are secure and implemented following industry best practices.

The controls in this category aim to ensure that the verified app implements authentication and authorization mechanisms securely, protecting sensitive user information and preventing unauthorized access. It is important to note that the security of the remote endpoint should also be validated using industry standards such as the [OWASP Application Security Verification Standard (ASVS)](https://owasp.org/www-project-application-security-verification-standard/).

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
