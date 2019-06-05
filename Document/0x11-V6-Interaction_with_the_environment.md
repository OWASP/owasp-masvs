# V6: Platform Interaction Requirements

## Control Objective

The controls in this group ensure that the app uses platform APIs and standard components in a secure manner. Additionally, the controls cover communication between apps (IPC).

## Security Verification Requirements

| # | MSTG-ID | Description | L1 | L2 |
| --- | --- | --- | --- | --- |
| **6.1** | MSTG‑PLATFORM‑1 | The app only requests the minimum set of permissions necessary. | ✓ | ✓ |
| **6.2** | MSTG‑PLATFORM‑2 | All inputs from external sources and the user are validated and if necessary sanitized. This includes data received via the UI, IPC mechanisms such as intents, custom URLs, and network sources.| ✓ | ✓ |
| **6.3** | MSTG‑PLATFORM‑3 | The app does not export sensitive functionality via custom URL schemes, unless these mechanisms are properly protected. | ✓ | ✓ |
| **6.4** | MSTG‑PLATFORM‑4 | The app does not export sensitive functionality through IPC facilities, unless these mechanisms are properly protected. | ✓ | ✓ |
| **6.5** | MSTG‑PLATFORM‑5 | JavaScript is disabled in WebViews unless explicitly required. | ✓ | ✓ |
| **6.6** | MSTG‑PLATFORM‑6 | WebViews are configured to allow only the minimum set of protocol handlers required (ideally, only https is supported). Potentially dangerous handlers, such as file, tel and app-id, are disabled. | ✓ | ✓ |
| **6.7** | MSTG‑PLATFORM‑7 | If native methods of the app are exposed to a WebView, verify that the WebView only renders JavaScript contained within the app package. | ✓ | ✓ |
| **6.8** | MSTG‑PLATFORM‑8 | Object deserialization, if any, is implemented using safe serialization APIs. | ✓ | ✓ |

<div style="page-break-after: always;"></div>

## References

The OWASP Mobile Security Testing Guide provides detailed instructions for verifying the requirements listed in this section.

- Android - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05h-Testing-Platform-Interaction.md>
- iOS - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06h-Testing-Platform-Interaction.md>

For more information, see also:

- OWASP Mobile Top 10: M1 - Improper Platform Usage: <https://www.owasp.org/index.php/Mobile_Top_10_2016-M1-Improper_Platform_Usage>
- CWE: <https://cwe.mitre.org/data/definitions/20.html>
- CWE: <https://cwe.mitre.org/data/definitions/749.html>
