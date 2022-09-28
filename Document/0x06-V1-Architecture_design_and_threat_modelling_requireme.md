# V1: Architecture, Design and Threat Modeling Requirements

## Control Objective

In a perfect world, security would be considered throughout all phases of development. In reality however, security is often only a consideration at a late stage in the SDLC. Besides the technical controls, the MASVS requires processes to be in place that ensure that the security has been explicitly addressed when planning the architecture of the mobile app, and that the functional and security roles of all components are known. Since most mobile applications act as clients to remote services, it must be ensured that appropriate security standards are also applied to those services - testing the mobile app in isolation is not sufficient.

**The category “V1” lists requirements pertaining to architecture and design of the app. As such, this is the only category that does not map to technical test cases in the OWASP Mobile Application Security Testing Guide. To cover topics such as threat modelling, secure SDLC or key management, users of the MASVS should consult the respective OWASP projects and/or other standards such as the ones linked below.**

## Security Verification Requirements

The requirements for MASVS-L1 and MASVS-L2 are listed below.

| # | MSTG-ID | Description | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **1.1** | MSTG-ARCH-1 | All app components are identified and known to be needed. | x | x |
| **1.2** | MSTG-ARCH-2 | Security controls are never enforced only on the client side, but on the respective remote endpoints. | x | x |
| **1.3** | MSTG-ARCH-3 | A high-level architecture for the mobile app and all connected remote services has been defined and security has been addressed in that architecture. | x | x |
| **1.4** | MSTG-ARCH-4 | Data considered sensitive in the context of the mobile app is clearly identified. | x | x |
| **1.5** | MSTG-ARCH-5 | All app components are defined in terms of the business functions and/or security functions they provide. |  | x |
| **1.6** | MSTG-ARCH-6 | A threat model for the mobile app and the associated remote services has been produced that identifies potential threats and countermeasures. |  | x |
| **1.7** | MSTG-ARCH-7 | All security controls have a centralized implementation. |  | x |
| **1.8** | MSTG-ARCH-8 | There is an explicit policy for how cryptographic keys (if any) are managed, and the lifecycle of cryptographic keys is enforced. Ideally, follow a key management standard such as NIST SP 800-57. |  | x |
| **1.9** | MSTG-ARCH-9 | A mechanism for enforcing updates of the mobile app exists. |  | x |
| **1.10** | MSTG-ARCH-10 | Security is addressed within all parts of the software development lifecycle. |  | x |
| **1.11** | MSTG-ARCH-11 | A responsible disclosure policy is in place and effectively applied. |  | x |
| **1.12** | MSTG-ARCH-12 | The app should comply with privacy laws and regulations. | x | x |

<!-- \pagebreak -->
## References

For more information, see also:

- OWASP Mobile Top 10: M10 (Extraneous Functionality) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m10-extraneous-functionality>
- OWASP Threat modelling - <https://owasp.org/www-community/Application_Threat_Modeling>
- OWASP Secure SDLC Cheat Sheet - <https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets_excluded/Secure_SDLC_Cheat_Sheet.md>
- Microsoft SDL - <https://www.microsoft.com/en-us/securityengineering/sdl/>
- NIST SP 800-57 - <https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final>
- security.txt - <https://securitytxt.org/>
