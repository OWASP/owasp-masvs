# MASVS-STORAGE: Data Storage

## Description

Mobile applications handle a wide variety of sensitive data, such as personally identifiable information (PII), cryptographic material, memorized secrets, and API keys, that often need to be stored locally. This sensitive data may be stored in private locations, such as the app's internal storage, or in public folders that are accessible by the user or other apps installed on the device. However, sensitive data can also be unintentionally stored or exposed to publicly accessible locations, typically as a side-effect of using certain APIs or system capabilities such as backups or logs.

This category is designed to help developers ensure that any sensitive data intentionally stored by the app is properly protected, regardless of the target location. It also covers unintentional leaks that can occur due to improper use of APIs or system capabilities. By following the recommendations and best practices outlined in this category, developers can minimize the risk of sensitive data exposure and ensure the security of their users' data.

## Controls

| ID | Statement |
|----|-----------|
| MASVS-STORAGE-1 | The app securely stores sensitive data. |
| MASVS-STORAGE-2 | The app prevents leakage of sensitive data. |

## References

The OWASP Mobile Application Security Testing Guide provides detailed instructions for verifying the requirements listed in this section.

- Android: Testing Data Storage - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x05d-Testing-Data-Storage.md>
- iOS: Testing Data Storage - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x06d-Testing-Data-Storage.md>
