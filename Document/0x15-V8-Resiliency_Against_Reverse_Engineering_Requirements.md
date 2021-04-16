# V8: Resilience Requirements

## Control Objective

This section covers defense-in-depth measures recommended for apps that process, or give access to, sensitive data or functionality. Lack of any of these controls does not cause a vulnerability - instead, they are meant to increase the app's resilience against reverse engineering and specific client-side attacks.

The controls in this section should be applied as needed, based on an assessment of the risks caused by unauthorized tampering with the app and/or reverse engineering of the code. We suggest consulting the OWASP document "Technical Risks of Reverse Engineering and Unauthorized Code Modification Reverse Engineering and Code Modification Prevention" (see references below) for a list of business risks as well as associated technical threats.

For any of the controls in the list below to be effective, the app must fulfil at least all of MASVS-L1 (i.e., solid security controls must be in place), as well as all lower-numbered requirements in V8. For examples, the obfuscation controls listed in under "impede comprehension" must be combined with "impede dynamic analysis and tampering" and "device binding".

**Note that software protections must never be used as a replacement for security controls. The controls listed in MASVR-R are intended to add threat-specific, additional protective controls to apps that also fulfil the MASVS security requirements.**

The following considerations apply:

1. A threat model must be defined that clearly outlines the client-side threats that are to be defended. Additionally, the grade of protection the scheme is meant to provide must be specified. For example, a stated goal could be to force authors of targeted malware seeking to instrument the app to invest significant manual reverse engineering effort.

2. The threat model must be credible and relevant. For example, hiding a cryptographic key in a white-box implementation might prove redundant if an attacker can simply code-lift the white-box as a whole.

3. The effectiveness of the protection should always be verified by a human expert with experience in testing the particular types of anti-tampering and obfuscation used (see also the "reverse engineering" and "assessing software protections" chapters in the Mobile Security Testing Guide).

<!-- \pagebreak -->

### Impede Dynamic Analysis and Tampering

| # | MSTG-ID | Description | R |
| -- | ----------- | ---------------------- | - |
| **8.1** | MSTG-RESILIENCE-1 | The app detects, and responds to, the presence of a rooted or jailbroken device either by alerting the user or terminating the app. | ✓ |
| **8.2** | MSTG-RESILIENCE-2 | The app prevents debugging and/or detects, and responds to, a debugger being attached. All available debugging protocols must be covered. | ✓ |
| **8.3** | MSTG-RESILIENCE-3 | The app detects, and responds to, tampering with executable files and critical data within its own sandbox. | ✓ |
| **8.4** | MSTG-RESILIENCE-4 | The app detects, and responds to, the presence of widely used reverse engineering tools and frameworks on the device.| ✓ |
| **8.5** | MSTG-RESILIENCE-5 | The app detects, and responds to, being run in an emulator.  | ✓ |
| **8.6** | MSTG-RESILIENCE-6 | The app detects, and responds to, tampering the code and data in its own memory space. | ✓ |
| **8.7** | MSTG-RESILIENCE-7 | The app implements multiple mechanisms in each defense category (8.1 to 8.6). Note that resiliency scales with the amount, diversity of the originality of the mechanisms used. | ✓ |
| **8.8** | MSTG-RESILIENCE-8 | The detection mechanisms trigger responses of different types, including delayed and stealthy responses. | ✓ |
| **8.9** | MSTG-RESILIENCE-9 | Obfuscation is applied to programmatic defenses, which in turn impede de-obfuscation via dynamic analysis.  | ✓ |

### Device Binding

| # | MSTG-ID | Description | R |
| -- | ----------- | ---------------------- | - |
| **8.10** | MSTG-RESILIENCE-10 | The app implements a 'device binding' functionality using a device fingerprint derived from multiple properties unique to the device. | ✓ |

<!-- \pagebreak -->

### Impede Comprehension

| # | MSTG-ID | Description | R |
| -- | ----------- | ---------------------- | - |
| **8.11** | MSTG-RESILIENCE-11 |All executable files and libraries belonging to the app are either encrypted on the file level and/or important code and data segments inside the executables are encrypted or packed. Trivial static analysis does not reveal important code or data. | ✓ |
| **8.12** | MSTG-RESILIENCE-12 | If the goal of obfuscation is to protect sensitive computations, an obfuscation scheme is used that is both appropriate for the particular task and robust against manual and automated de-obfuscation methods, considering currently published research. The effectiveness of the obfuscation scheme must be verified through manual testing. Note that hardware-based isolation features are preferred over obfuscation whenever possible. | ✓ |

### Impede Eavesdropping

| # | MSTG-ID | Description | R |
| -- | ----------- | ---------------------- | - |
| **8.13** | MSTG-RESILIENCE-13 | As a defense in depth, next to having solid hardening of the communicating parties, application level payload encryption can be applied to further impede eavesdropping. | ✓ |

<!-- \pagebreak -->

## References

The OWASP Mobile Security Testing Guide provides detailed instructions for verifying the requirements listed in this section.

- Android: Testing Resiliency Against Reverse Engineering - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05j-Testing-Resiliency-Against-Reverse-Engineering.md>
- iOS: Testing Resiliency Against Reverse Engineering - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06j-Testing-Resiliency-Against-Reverse-Engineering.md>

For more information, see also:

- OWASP Mobile Top 10: M8 (Code Tampering) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m8-code-tampering>
- OWASP Mobile Top 10: M9 (Reverse Engineering) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m9-reverse-engineering>
- OWASP Reverse Engineering Threats - <https://wiki.owasp.org/index.php/Technical_Risks_of_Reverse_Engineering_and_Unauthorized_Code_Modification>
- OWASP Reverse Engineering and Code Modification Prevention - <https://wiki.owasp.org/index.php/OWASP_Reverse_Engineering_and_Code_Modification_Prevention_Project>
