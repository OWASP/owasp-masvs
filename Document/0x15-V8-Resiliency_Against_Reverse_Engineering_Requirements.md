# V8: Resilience Requirements

## Control objective

This section covers defense-in-depth measures that are recommended for apps that process, or give access to, sensitive data or functionality. Lack of any of these controls does not cause a vulnerability - instead, they are meant to increase the app's resiliency against reverse engineering and specific client-side attacks.

The controls in this section differ from previous sections in that they do not apply to all mobile apps generically. Rather, the controls described here should be applied as needed, based on a risk assessment as per the unauthorized tampering with the app and/or reverse engineering of the code.

We suggest consulting the OWASP document "Technical Risks of Reverse Engineering and Unauthorized Code Modification Reverse Engineering and Code Modification Prevention" (see references below) for a list business risks as well as dependent technical threats. 

For any of the controls in the list below to be effective, the app must fulfil at least all of MASVS-L1 (i.e., solid security controls must be in place), as well as all lower-numbered requriements in V8. For examples, the obfuscation controls listed in under "impede comprehension" must be combined with "app isolation", "impede dynamic analysis and tampering" and "device binding".

**Note that software protections must never be used as a replacement for security controls. The controls listed in MASVR-R are intended to add threat-specific, additional protective controls to apps that also fulfil the MASVS security requirements.**

The following considerations apply:

1. A threat model must be defined that clearly outlines the attacker's goals. Additionally, a targets must be set that specifies the level of protection the protection scheme is meant to provide (e.g., cause significant manual effort to a skilled reverse engineer using state-of-the-art tools and processes to reach their goal).

2. The threat model must be sensical. For example, hiding a cryptographic key in a white-box implementation is besides the point if the attacker can simply code-lift the white-box as a whole. 

3. The protection scheme should be subjected to manual testing by a subject matter expert (see also the "reverse engineering" and "assessing software protections" chapters in the Mobile Security Testing Guide).

### Impede Dynamic Analysis and Tampering

| # | Description | R |
| --- | --- | --- |
| **8.1** | The app detects, and responds to, the presence of a rooted or jailbroken device either by alerting the user or terminating the app. | ✓ |
| **8.2** | The app implements prevents debugging and/or detects, and responds to, a debugger being attached. All available debugging protocols must be covered (Android: JDWP and ptrace, iOS: Mach IPC and ptrace). | ✓ |
| **8.3** | The app detects, and responds to, tampering with executable files and critical data within its own container. | ✓ |
| **8.4** | The app detects the presence of widely used reverse engineering tools and frameworks that support code injection, hooking, instrumentation and debugging. | ✓ |
| **8.5** | The app detects, and responds to, being run in an emulator.  | ✓ |
| **8.6** | The app continually verifies the integrity of critical code and data structures within its own memory space. | ✓ |
| **8.7** | The app implements multiple mechanisms to fulfil requirements 8.1 to 8.6. Note that resilience scales with the amount, diversity of the originality of the mechanisms used. | ✓ |
| **8.8** | The detection mechanisms trigger different responses, including stealthy ones that don't simply terminate the app. | ✓ |
| **8.9** |All executable files and libraries belonging to the app are either encrypted on the file level and/or important code and data segments inside the executables are encrypted or packed. Trivial static analysis does not reveal important code or data. | ✓ |
| **8.10** | Obfuscating transformations and functional defenses are interdependent and well-integrated throughout the app. | ✓ |

### Device Binding

| # | Description | R |
| --- | --- | --- |
| **8.11**| The app implements a 'device binding' functionality using a device fingerprint derived from multiple properties unique to the device. | ✓ |

### Impede Comprehension

| # | Description | R |
| --- | --- | --- |
| **8.12** | If the architecture requires sensitive computations be performed on the client-side, these computations are isolated from the operating system by using a hardware-based SE or TEE. Alternatively, the computations are protected using obfuscation. Considering current published research, the obfuscation type and parameters are sufficient to cause significant manual effort to reverse engineers seeking to comprehend the sensitive portions of the code and/or data. | ✓ |

## References

The OWASP Mobile Security Testing Guide provides detailed instructions for verifying the requirements listed in this section.

- Android - https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05j-Testing-Resiliency-Against-Reverse-Engineering.md
- iOS - https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06j-Testing-Resiliency-Against-Reverse-Engineering.md

For more information, see also:

- OWASP Mobile Top 10: M8 - Code Tampering, M9 - Reverse Engineering
- WASP Reverse Engineering Threats -https://www.owasp.org/index.php/Technical_Risks_of_Reverse_Engineering_and_Unauthorized_Code_Modification
- OWASP Reverse Engineering and Code Modification Prevention - https://www.owasp.org/index.php/OWASP_Reverse_Engineering_and_Code_Modification_Prevention_Project
