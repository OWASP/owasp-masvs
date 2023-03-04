# MASVS-RESILIENCE: Resilience Against Reverse Engineering and Tampering

## Description

Defense-in-depth measures such as code obfuscation, anti-debugging, anti-tampering, etc. are important to increase app resilience against reverse engineering and specific client-side attacks. They add multiple layers of security controls to the app, making it more difficult for attackers to successfully reverse engineer and extract valuable intellectual property or sensitive data from it, which could result in:

- The theft or compromise of valuable business assets such as proprietary algorithms, trade secrets, or customer data
- Significant financial losses due to loss of revenue or legal action
- Legal and reputational damage due to breach of contracts or regulations
- Damage to brand reputation due to negative publicity or customer dissatisfaction

The controls in this category aim to ensure that the app is running on a trusted platform, prevent tampering at runtime and ensure the integrity of the app's intended functionality. Additionally, the controls impede comprehension by making it difficult to figure out how the app works using static analysis and prevent dynamic analysis and instrumentation that could allow an attacker to modify the code at runtime.

However, note that the lack of any of these measures does not necessarily cause vulnerabilities - instead, they add threat-specific additional protection to apps which must also fulfil the rest of the OWASP MASVS security requirements according to their specific threat models.

## Controls

| ID | Statement |
|----|-----------|
| MASVS-RESILIENCE-1 | The app validates the integrity of the platform. |
| MASVS-RESILIENCE-2 | The app implements anti-tampering mechanisms. |
| MASVS-RESILIENCE-3 | The app implements anti-static analysis mechanisms. |
| MASVS-RESILIENCE-4 | The app implements anti-dynamic analysis techniques. |

## References

The OWASP Mobile Application Security Testing Guide provides detailed instructions for verifying the requirements listed in this section.

- General: Mobile App Tampering and Reverse Engineering - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x04c-Tampering-and-Reverse-Engineering.md>
- Android: Testing Resiliency Against Reverse Engineering - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x05j-Testing-Resiliency-Against-Reverse-Engineering.md>
- iOS: Testing Resiliency Against Reverse Engineering - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x06j-Testing-Resiliency-Against-Reverse-Engineering.md>
