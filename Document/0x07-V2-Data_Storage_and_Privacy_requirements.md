# V2: Data Storage and Privacy requirements

## Control objective

Handling of sensitive data is a central topic in mobile security. First of all, sensitive data processed by a mobile app can be unintentionally exposed to other apps running on the same device if operating system APIs are used improperly. Sensitive data may leak to cloud storage, backups, or the keyboard cache. Additionally, mobile devices can be lost or stolen more easily compared to other types of devices, such as web servers and desktop PCs, so an adversary gaining physical access to a device is a more likely scenario. In that case, additional protections can be implemented to make retrieving the sensitive data more difficult.

## Requirements

-- TODO --

| # | Description | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| **2.1** | Verify that secure credential storage factilites are used to store sensitive data, such as user credentials or cryptographic keys. | ✓ | ✓ | ✓ | ✓ |
| **2.2** | Verify that no sensitive data is written to log files. | ✓ | ✓ | ✓ | ✓ |
| **2.3** | Verify that no sensitive data is synced to cloud storage in plaintext. | ✓ | ✓ | ✓ | ✓ |
| **2.4** | Verify that no sensitive data is sent to third parties. | ✓ | ✓ | ✓ | ✓ |
| **2.5** | Verify that the app does not hold sensitive data in memory longer than necessary (e.g. during the login process). |   | ✓ | ✓ | ✓ |
| **2.6** | Verify that sensitive data is explicitly cleared from memory after use. |   | ✓ | ✓ | ✓ |
| **2.7** | Verify that the keyboard cache is disabled on text input that process sensitive data. | ✓ | ✓ | ✓ | ✓ |
| **2.8** | Verify that the clipboard is deactivated on text fields that may contain sensitive data. | ✓ | ✓ | ✓ | ✓ |
| **2.9** | Verify that sensitive data is obscured in the user interface | ✓ | ✓ | ✓ | ✓ |
| **2.10** | Verify that no sensitive data is exposed via IPC facilities. | ✓ | ✓ | ✓ | ✓ |
| **2.11** | Verify that sensitive data does not leak via application snapshots (iOS). |  | ✓ | ✓ | ✓ |
| **2.12** | Verify that sensitive data does not leak via the task switcher (Android). | ✓ | ✓ | ✓ | ✓ |
| **2.13** | Verify that data backup via ADB is disabled (Android). | ✓ | ✓ | ✓ | ✓ |
| **2.14** | If a remote locking mechansim exists, ensure that local storage is wiped upon locking. |  | ✓ | ✓ | ✓ |

## References

For more information, please see:

-- TODO --

