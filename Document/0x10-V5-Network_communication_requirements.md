# Network Communication (MASVS-NETWORK)

## Description

The purpose of the controls listed in this category is to ensure the confidentiality and integrity of information exchanged between the mobile app and remote service endpoints. At the very least, a mobile app must set up a secure, encrypted channel for network communication.

## Controls

| ID | Statement |
|----|-----------|
| MASVS-NETWORK-1 | The app secures all network traffic according to the current best practices. |
| MASVS-NETWORK-2 | The app performs identity pinning for all remote endpoints under the developer's control. |

## References

The OWASP Mobile Application Security Testing Guide provides detailed instructions for verifying the requirements listed in this section.

- General: Testing Network Communication - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x04f-Testing-Network-Communication.md>
- Android: Testing Network Communication - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x05g-Testing-Network-Communication.md>
- iOS: Testing Network Communication - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x06g-Testing-Network-Communication.md>
