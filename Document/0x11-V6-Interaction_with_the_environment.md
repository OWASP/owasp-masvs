# MASVS-PLATFORM: Platform Interaction

## Description

The security of mobile apps heavily depends on their interaction with the mobile platform, which often involves exposing data or functionality intentionally through the use of platform-provided inter-process communication (IPC) mechanisms and WebViews to enhance the user experience. However, these mechanisms can also be exploited by attackers or co-installed apps, potentially compromising the app's security.

Furthermore, sensitive data, such as passwords, credit card details, and one-time passwords in notifications, is often displayed in the app's user interface. It is essential to ensure that this data is not unintentionally leaked through platform mechanisms such as auto-generated screenshots or accidental disclosure through shoulder surfing or device sharing.

This category comprises controls that ensure the app's interactions with the mobile platform occur securely. These controls cover the secure use of platform-provided IPC mechanisms, WebView configuration to prevent sensitive data leakage and functionality exposure, and secure display of sensitive data in the app's user interface. By implementing these controls, mobile app developers can safeguard sensitive user information and prevent unauthorized access by attackers.

## Controls

| ID | Statement |
|----|-----------|
| MASVS-PLATFORM-1 | The app uses IPC mechanisms securely. |
| MASVS-PLATFORM-2 | The app uses WebViews securely. |
| MASVS-PLATFORM-3 | The app uses the user interface securely. |

## References

The OWASP Mobile Application Security Testing Guide provides detailed instructions for verifying the requirements listed in this section.

- Android: Testing Platform Interaction - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x05h-Testing-Platform-Interaction.md>
- iOS: Testing Platform Interaction - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x06h-Testing-Platform-Interaction.md>
