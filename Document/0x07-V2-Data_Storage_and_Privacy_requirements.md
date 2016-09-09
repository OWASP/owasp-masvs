# V2: Data Storage and Privacy requirements

## Control objective

Authentication is the act of establishing, or confirming, something (or someone) as authentic, that is, that claims made by or about the thing are true. Ensure that a verified application satisfies the following high level requirements:

- Verifies the digital identity of the sender of a communication.
- Ensures that only those authorised are able to authenticate and credentials are transported in a secure manner.

## Requirements

-- TODO --

| # | Description | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| **2.1** | Verify that appropriate APIs are used to store credentials. | ✓ | ✓ | ✓ | ✓ |
| **2.2** | Verify that log files do not contain sensitive data. | ✓ | ✓ | ✓ | ✓|
| **2.3** | Verify that no sensitive data is synced to cloud storage. | ✓ | ✓ | ✓ | ✓ |
| **2.4** | Verify that no sensitive data is disclosed in local files or databases. | ✓ | ✓ | ✓ | ✓ |
| **2.5** | Verify that no sensitive data is sent to third parties. | ✓ | ✓ | ✓ | ✓ |
| **2.6** | Verify that sensitive data is encrypted in memory. |  | ✓ | ✓ | ✓ |
| **2.7** | Verify that no sensitive data leaks via the keyboard cache. | ✓ | ✓ | ✓ | ✓ |
| **2.8** | Verify that the clipboard is deactivated on sensitive input fields | ✓ | ✓ | ✓ | ✓ |
| **2.9** | Verify that sensitive data is obscured in the user interface | ✓ | ✓ | ✓ | ✓ |
| **2.10** | Verify that sensitive data does not leak via application snapshots (iOS) |  | ✓ | ✓ | ✓ |
| **2.11** | Verify that sensitive data does not leak via the task switcher (Android) | ✓ | ✓ | ✓ | ✓ |
| **2.12** | Verify that sensitive data does not leak via IPC facilities | ✓ | ✓ | ✓ | ✓ |
| **2.13** | Verify that data backup via ADB is disabled (Android) | ✓ | ✓ | ✓ | ✓ |

## References

For more information, please see:

-- TODO --

