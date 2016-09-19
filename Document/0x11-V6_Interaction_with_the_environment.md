# V6: Interaction with the environment

## Control objective

The controls in group this ensure that the app uses operation system APIs and standard components in a secure manner. Additionally, the controls cover communication between apps (IPC).

## Requirements

| # | Description | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| **3.1** | Verify that that the app does not request any unnecessary permissions. | ✓ | ✓ | ✓ | ✓ |
| **3.2** | Verify that all inputs from external sources is validated. This includes data reveived via the GUI, IPC mechanisms such as intents, custom URLs, and network communication.| ✓ | ✓ | ✓ | ✓ |
| **3.3** | Verify that the app does not export sensitive functionality via custom URL schemes. | ✓ | ✓ | ✓ | ✓ |
| **3.4** | Verify that the app does not export sensitive activities through intent filters (Android). | ✓ | ✓ | ✓ | ✓ |
| **3.5** | Verify that Javascript is disabled in all WebViews unless explicitly required. | ✓ | ✓ | ✓ | ✓ |
| **3.6** | Verify that file access is disabled in all WebViews unless explicitly required. | ✓ | ✓ | ✓ | ✓ |
| **3.7** | If Javascript is required in a WebView, ensure that the WebView is restricted to a specific URL, and that no unfiltered user input is rendered in the WebView. | ✓ | ✓ | ✓ | ✓ |
| **3.8** | Verify that JavaScriptInterface is not used, unless explicitly required (Android). | ✓ | ✓ | ✓ | ✓ |
| **3.9** | Verify that the app updates the Security Provider if needed (Android)|   | ✓ | ✓ | ✓ |
| **3.10** | Verify that the app provides a custom keyboard whenever sensitive data is entered. |   |   | ✓ | ✓ |


## References

https://developer.android.com/training/articles/security-tips.html#IPC
https://developer.apple.com/library/content/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Inter-AppCommunication/Inter-AppCommunication.html
JavaScriptInterface (Android): https://developer.android.com/reference/android/webkit/JavascriptInterface.html

For more information, please see:

(...) TODO - Link to MSTG (...)
