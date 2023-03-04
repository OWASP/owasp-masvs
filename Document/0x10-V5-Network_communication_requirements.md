# MASVS-NETWORK: Network Communication

## Description

Secure networking is a critical aspect of mobile app security, particularly for apps that communicate over the network. In order to ensure the confidentiality and integrity of data in transit, developers typically rely on encryption and authentication of the remote endpoint, such as through the use of TLS. However, there are numerous ways in which a developer may accidentally disable the platform secure defaults or bypass them entirely by utilizing low-level APIs or third-party libraries.

This category is designed to ensure that the mobile app sets up secure connections under any circumstances. Specifically, it focuses on verifying that the app establishes a secure, encrypted channel for network communication. Additionally, this control covers situations where a developer may choose to trust only specific Certificate Authorities (CAs), which is commonly referred to as certificate pinning or SSL pinning.

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
