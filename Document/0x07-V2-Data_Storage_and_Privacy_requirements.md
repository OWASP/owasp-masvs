# V2: Data Storage and Privacy requirements

## Control objective

The protection of sensitive data, such as user credentials and private informaion, is a key focus in mobile security. Firstly, sensitive data can be unintentionally exposed to other apps running on the same device if operating system mechanisms like IPC are used improperly. Data may also unintentionally leak to cloud storage, backups, or the keyboard cache. Additionally, mobile devices can be lost or stolen more easily compared to other types of devices, so an adversary gaining physical access is a more likely scenario. In that case, additional protections can be implemented to make retrieving the sensitive data more difficult.

## Requirements

Fortunately, the vast majority of data disclosure issues can be prevented by following simple rules. Most of the controls listed in this chapter are mandatory for all verification levels.

| # | Description | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| **2.1** | Verify that secure credential storage facilities are used to store sensitive data, such as user credentials or cryptographic keys. | ✓ | ✓ | ✓ | ✓ |
| **2.2** | Verify that no sensitive data is written to log files. | ✓ | ✓ | ✓ | ✓ |
| **2.3** | Verify that no sensitive data is synced to cloud storage in plaintext. | ✓ | ✓ | ✓ | ✓ |
| **2.4** | Verify that no sensitive data is sent to third parties. | ✓ | ✓ | ✓ | ✓ |
| **2.5** | Verify that the keyboard cache is disabled on text input that process sensitive data. | ✓ | ✓ | ✓ | ✓ |
| **2.6** | Verify that the clipboard is deactivated on text fields that may contain sensitive data. | ✓ | ✓ | ✓ | ✓ |
| **2.7** | Verify that sensitive data does not leak via application snapshots (iOS). | ✓ | ✓ | ✓ | ✓ |
| **2.8** | Verify that no sensitive data is exposed via intents (Android). | ✓ | ✓ | ✓ | ✓ |
| **2.9** | Verify that sensitive data does not leak via the task switcher (Android). | ✓ | ✓ | ✓ | ✓ |
| **2.10** | Verify that sensitive data, such as passwords and credit card numbers, are masked in the user interface. | ✓ | ✓ | ✓ | ✓ |
| **2.11** | Verify that data backup via ADB is disabled (Android). | ✓ | ✓ | ✓ | ✓ |
| **2.12** | Verify that the app does not hold sensitive data in memory longer than necessary (e.g. during the login process), and that the memory is cleared explicitly after use. |  | ✓ | ✓ | ✓ |
| **2.13** | If a remote locking mechansim exists, ensure that local storage is wiped upon locking. |  |  | ✓ | ✓ |
| **2.14** | If the Android keystore is used in Android 6 or higher, ensure that the Android patch level is properly updated. |  |  | | ✓ |


## References

For more information, please see:

-- TODO --
