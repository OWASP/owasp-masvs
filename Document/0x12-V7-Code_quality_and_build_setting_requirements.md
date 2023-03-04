# MASVS-CODE: Code Quality

## Description

Mobile apps have many data entry points, including the UI, IPC, network, and file system, which might receive data that has been inadvertently modified by untrusted actors. By treating this data as untrusted input and properly verifying and sanitizing it before use, developers can prevent classical injection attacks, such as SQL injection, XSS, or insecure deserialization. However, other common coding vulnerabilities, such as memory corruption flaws, are hard to detect in penetration testing but easy to prevent with secure architecture and coding practices. Developers should follow best practices such as the [OWASP Software Assurance Maturity Model (SAMM)](https://owaspsamm.org/model/) and [NIST.SP.800-218 Secure Software Development Framework (SSDF)](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218.pdf) to avoid introducing these flaws in the first place.

This category covers coding vulnerabilities that arise from external sources such as app data entry points, the OS, and third-party software components. Developers should verify and sanitize all incoming data to prevent injection attacks and bypass of security checks. They should also enforce app updates and ensure that the app runs up-to-date platforms to protect users from known vulnerabilities.

## Controls

| ID | Statement |
|----|-----------|
| MASVS-CODE-1 | The app requires an up-to-date platform version. |
| MASVS-CODE-2 | The app has a mechanism for enforcing app updates. |
| MASVS-CODE-3 | The app only uses software components without known vulnerabilities. |
| MASVS-CODE-4 | The app validates and sanitizes all untrusted inputs. |

## References

The OWASP Mobile Application Security Testing Guide provides detailed instructions for verifying the requirements listed above.

- General: Mobile App Code Quality - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x04h-Testing-Code-Quality.md>
- Android: Testing Code Quality and Build Settings - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x05i-Testing-Code-Quality-and-Build-Settings.md>
- iOS: Testing Code Quality and Build Settings - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x06i-Testing-Code-Quality-and-Build-Settings.md>
