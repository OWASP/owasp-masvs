# Resilience Against Reverse Engineering and Tampering (MASVS-RESILIENCE)

## Description

This category covers defense-in-depth measures recommended for apps that process, or give access to, sensitive data or functionality. Lack of any of these controls does not cause a vulnerability - instead, they are meant to increase the app's resilience against reverse engineering and specific client-side attacks. These controls add threat-specific, additional protective controls to apps which must also fulfil the rest of the MASVS security controls according to their specific threat models.

## Controls

| ID | Statement |
|----|-----------|
| MASVS-RESILIENCE-1 | The app validates the integrity of the platform. |
| MASVS-RESILIENCE-2 | The app implements anti-tampering mechanisms. |
| MASVS-RESILIENCE-3 | The app implements anti-static analysis mechanisms. |
| MASVS-RESILIENCE-4 | The app implements anti-dynamic analysis techniques. |

## References

The OWASP Mobile Application Security Testing Guide provides detailed instructions for verifying the requirements listed in this section.

- Android: Testing Resiliency Against Reverse Engineering - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x05j-Testing-Resiliency-Against-Reverse-Engineering.md>
- iOS: Testing Resiliency Against Reverse Engineering - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x06j-Testing-Resiliency-Against-Reverse-Engineering.md>
