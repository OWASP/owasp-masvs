# V2: Data Storage and Privacy Requirements

## Control Objective

The protection of sensitive data, such as user credentials and private information, is a key focus in mobile security. Firstly, sensitive data can be unintentionally exposed to other apps running on the same device if operating system mechanisms like IPC are used improperly. Data may also unintentionally leak to cloud storage, backups, or the keyboard cache. Additionally, mobile devices can be lost or stolen more easily compared to other types of devices, so an adversary gaining physical access is a more likely scenario. In that case, additional protections can be implemented to make retrieving the sensitive data more difficult.

## Security Verification Requirements

Fortunately, the vast majority of data disclosure issues can be prevented by following simple rules. Most of the controls listed in this chapter are mandatory for all verification levels.

| # | Description | L1 | L2 |
| --- | --- | --- | --- |
| **2.1** | System credential storage facilities are used appropriately to store sensitive data, such as user credentials or cryptographic keys. | ✓ | ✓ |
| **2.2** | No sensitive data is written to application logs. | ✓ | ✓ |
| **2.3** | No sensitive data is synced with cloud storage. | ✓ | ✓ |
| **2.4** | No sensitive data is sent to third parties. | ✓ | ✓ |
| **2.5** | The keyboard cache is disabled on text inputs that process sensitive data. | ✓ | ✓ |
| **2.6** | The clipboard is deactivated on text fields that may contain sensitive data. | ✓ | ✓ |
| **2.7** | No sensitive data is exposed via IPC mechanisms. | ✓ | ✓ |
| **2.8** | No sensitive data, such as passwords and credit card numbers, is exposed through the user interface or leaks to screenshots. | ✓ | ✓ |
| **2.9** | No sensitive data is included in backups. |   | ✓ |
| **2.10** | The app removes sensitive data from views when backgrounded. |  | ✓ |
| **2.11** | The app does not hold sensitive data in memory longer than necessary, and memory is cleared explicitly after use. |  | ✓ |
| **2.12** | The app enforces a minimum device-access-security policy, such as requiring the user to set a device passcode. |  | ✓ |

## References

For more information, see also:

- OWASP Mobile Top 10: M2  - Insecure Data Storage
- CWE: https://cwe.mitre.org/data/definitions/922.html
