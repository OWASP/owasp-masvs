# V2: Data Storage and Privacy requirements

## Control objective

The protection of sensitive data, such as user credentials and private informaion, is a key focus in mobile security. Firstly, sensitive data can be unintentionally exposed to other apps running on the same device if operating system mechanisms like IPC are used improperly. Data may also unintentionally leak to cloud storage, backups, or the keyboard cache. Additionally, mobile devices can be lost or stolen more easily compared to other types of devices, so an adversary gaining physical access is a more likely scenario. In that case, additional protections can be implemented to make retrieving the sensitive data more difficult.

## Requirements

Fortunately, the vast majority of data disclosure issues can be prevented by following simple rules. Most of the controls listed in this chapter are mandatory for all verification levels.

| # | Description | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| **2.1** | Verify that system credential storage facilities are used appropriately to store sensitive data, such as user credentials or cryptographic keys. | ✓ | ✓ | ✓ | ✓ |
| **2.2** | Verify that no sensitive data is written to log files. | ✓ | ✓ | ✓ | ✓ |
| **2.3** | Verify that no sensitive data leaks to cloud storage. | ✓ | ✓ | ✓ | ✓ |
| **2.4** | Verify that no sensitive data is sent to third parties. | ✓ | ✓ | ✓ | ✓ |
| **2.5** | Verify that the keyboard cache is disabled on text inputs that process sensitive data. | ✓ | ✓ | ✓ | ✓ |
| **2.6** | Verify that the clipboard is deactivated on text fields that may contain sensitive data. | ✓ | ✓ | ✓ | ✓ |
| **2.7** | Verify that no sensitive data is exposed via IPC mechanisms. | ✓ | ✓ | ✓ | ✓ |
| **2.8** | Verify that sensitive data, such as passwords and credit card numbers, is not exposed through the user interface, and does not leak to screenshots. | ✓ | ✓ | ✓ | ✓ |
| **2.9** | Verify that sensitive data does not leak to backups. | ✓ | ✓ | ✓ | ✓ |
| **2.10** | Verify that the app removes sensitive data from views when backgrounded. |  | ✓ | ✓ | ✓ |
| **2.11** | Verify that the app does not hold sensitive data in memory longer than necessary, and that the memory is cleared explicitly after use. |  | ✓ | ✓ | ✓ |
| **2.12** | Verify that the app only runs on operating system versions that offer a hardware-backed keystore, and that the device supports the hardware-backed keystore. Alternatively, verify that encryption has been implemented according to the controls in MASVS V3. |  |  | ✓ | ✓ |
| **2.13** | If a remote locking mechansim exists, ensure that local storage is wiped upon locking. |  |  | ✓ | ✓ |

## References

For more information, please see:

-- TODO --
