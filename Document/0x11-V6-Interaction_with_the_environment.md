# V6: Platform Interaction Requirements

## Control Objective

The controls in this group ensure that the app uses platform APIs and standard components in a secure manner. Additionally, the controls cover communication between apps (IPC).

## Security Verification Requirements

| # | MSTG-ID | Description | L1 | L2 |
| -- | -------- | ---------------------- | - | - |
| **6.1** | MSTG-PLATFORM-1 | The app only requests the minimum set of permissions necessary. | ✓ | ✓ |
| **6.2** | MSTG-PLATFORM-2 | All inputs from external sources and the user are validated and if necessary sanitized. This includes data received via the UI, IPC mechanisms such as intents, custom URLs, and network sources.| ✓ | ✓ |
| **6.3** | MSTG-PLATFORM-3 | The app does not export sensitive functionality via custom URL schemes, unless these mechanisms are properly protected. | ✓ | ✓ |
| **6.4** | MSTG-PLATFORM-4 | The app does not export sensitive functionality through IPC facilities, unless these mechanisms are properly protected. | ✓ | ✓ |
| **6.5** | MSTG-PLATFORM-5 | JavaScript is disabled in WebViews unless explicitly required. | ✓ | ✓ |
| **6.6** | MSTG-PLATFORM-6 | WebViews are configured to allow only the minimum set of protocol handlers required (ideally, only https is supported). Potentially dangerous handlers, such as file, tel and app-id, are disabled. | ✓ | ✓ |
| **6.7** | MSTG-PLATFORM-7 | If native methods of the app are exposed to a WebView, verify that the WebView only renders JavaScript contained within the app package. | ✓ | ✓ |
| **6.8** | MSTG-PLATFORM-8 | Object deserialization, if any, is implemented using safe serialization APIs. | ✓ | ✓ |
| **6.9** | MSTG-PLATFORM-9 | The app protects itself against screen overlay attacks. (Android only) |  | ✓ |
| **6.10** | MSTG-PLATFORM-10 | A WebView's cache, storage, and loaded resources (JavaScript, etc.) should be cleared before the WebView is destroyed. |  | ✓ |
| **6.11** | MSTG-PLATFORM-11 | Verify that the app prevents usage of custom third-party keyboards whenever sensitive data is entered (iOS only). | | ✓ |

## References

The OWASP Mobile Security Testing Guide provides detailed instructions for verifying the requirements listed in this section.

- Android: Testing Platform Interaction - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05h-Testing-Platform-Interaction.md>
- iOS: Testing Platform Interaction - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06h-Testing-Platform-Interaction.md>

For more information, see also:

- OWASP Mobile Top 10: M1 (Improper Platform Usage) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m1-improper-platform-usage>
- OWASP Mobile Top 10: M7 (Poor Code Quality) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m7-client-code-quality>
- CWE 20 (Improper Input Validation) - <https://cwe.mitre.org/data/definitions/20.html>
- CWE 79 (Improper Neutralization of Input During Web Page Generation) - <https://cwe.mitre.org/data/definitions/79.html>
- CWE 200 (Information Leak / Disclosure) - <https://cwe.mitre.org/data/definitions/200.html>
- CWE 250 (Execution with Unnecessary Privileges) - <https://cwe.mitre.org/data/definitions/250.html>
- CWE 672 (Operation on a Resource after Expiration or Release) - <https://cwe.mitre.org/data/definitions/672.html>
- CWE 749 (Exposed Dangerous Method or Function) - <https://cwe.mitre.org/data/definitions/749.html>
- CWE 772 (Missing Release of Resource after Effective Lifetime) - <https://cwe.mitre.org/data/definitions/772.html>
- CWE 920 (Improper Restriction of Power Consumption) - <https://cwe.mitre.org/data/definitions/920.html>
- CWE 925 (Improper Verification of Intent by Broadcast Receiver) - <https://cwe.mitre.org/data/definitions/925.html>
- CWE 926 (Improper Export of Android Application Components) - <https://cwe.mitre.org/data/definitions/926.html>
- CWE 927 (Use of Implicit Intent for Sensitive Communication) - <https://cwe.mitre.org/data/definitions/927.html>
- CWE 939 (Improper Authorization in Handler for Custom URL Scheme) - <https://cwe.mitre.org/data/definitions/939.html>
