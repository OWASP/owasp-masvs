# V2：数据存储和隐私要求

## 控制目标

保护敏感数据（例如用户登录信息和私人信息）是移动安全的重点。首先，不正确地使用操作系统机制（如IPC）将会使敏感资料以外地泄露给同一台设备上的其他应用程序。此外，数据也可能会意外泄漏到云存储，备份或键盘缓存中。与其他类型的设备相比，移动设备更容易丢失或被盗。因此，攻击者得以更容易地窃取敏感信息。所以，在移动应用程序中，对敏感信息的保护机制尤为重要。

注意：由于MASVS是以应用程序开发为中心的，因此它並不包括设备级的解决方案（诸如移动设备管理（Mobile Device Management - MDM ））。然而，我们还是建议您在企业环境中使用相关的设备级的解决方案来进一步提升数据的安全性。

### 敏感数据的定义

MASVS规范中涉及的敏感信息指的是用户登录信息和在实际应用情況中的任何敏感信息，例如：

- 可能被犯罪分子滥用的个人身份识别信息（PII），如身份证号码，信用卡号码，银行账号，个人健康信息，电话号码，家庭住址；
- 一旦泄露，将会引起企业财产和声誉损失的高度敏感的数据，如合同信息，保密协议涵盖的信息，管理层人员信息；
- 任何被法律或出于合规原因必须受到保护的数据。

<!-- \pagebreak -->

## 安全验证要求

通过遵循基本的规则，大多数的数据泄露问题是可以避免的。本章节列出的大多数验证都是必需要遵守的。

| # | MSTG-ID |描述 | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **2.1** | MSTG-STORAGE-1 | 如必须存储敏感信息（诸如PII，用户登录数据，加密密钥等），必须使用操作系统所提供的安全存储机制。| x | x |
| **2.2** | MSTG-STORAGE-2 | 敏感数据不应存储在应用程序容器或者系统凭据存储功能以外的地方。 | x | x |
| **2.3** | MSTG-STORAGE-3 | 敏感数据不应被写入应用程序日志。 | x | x |
| **2.4** | MSTG-STORAGE-4 | 如非绝对必要，敏感数据不能与第三方共享。 | x | x |
| **2.5** | MSTG-STORAGE-5 | 键盘缓存应当在处理敏感数据的文本输入上被禁用。 | x | x |
| **2.6** | MSTG-STORAGE-6 | 该应用程序使用的IPC机制不应泄露任何敏感数据。 | x | x |
| **2.7** | MSTG-STORAGE-7 | 该应用程序用户界面不应泄露任何敏感数据，如密码或密码。 | x | x |
| **2.8** | MSTG-STORAGE-8 | 移动操作系统生成的备份中不应包含敏感数据。 | | x |
| **2.9** | MSTG-STORAGE-9 | 当应用程序被移至后台时，存在当前视图中的敏感数据应当被删除。 | | x |
| **2.10** | MSTG-STORAGE-10 | 该应用程序不会在内存中保存超过必要时效的敏感数据，并且在使用后会彻底清除内存中的敏感数据。 | | x |
| **2.11** | MSTG-STORAGE-11 | 该应用程序采用了最低设备访问安全策略，强制要求用户设置设备密码。 | | x |
| **2.12** | MSTG-STORAGE-12 | 该应用程序主动告知用户其处理的用户个人身份信息的类型，并且主动告知用户使用该应用程序时应遵循的最佳安全做法。 | x | x |
| **2.13** | MSTG-STORAGE-13 | 不应将任何敏感数据存储在本地移动设备上。应用程序应在需要时从远程端点获取数据，并仅将其保存在内存作为临时使用中。 | | x |
| **2.14** | MSTG-STORAGE-14 | 如果需要在本地存储敏感数据，则应该使用需要身份验证的硬件级别加密的存储密钥对其进行加密。 | | x |
| **2.15** | MSTG-STORAGE-15 | 在多次用户尝试登陆应用失败后，应用程序将清除本地应用存储。 | | x |

## 参考文献

OWASP移动安全测试指南对本章节中列出的验证要求都提供了的详细说明。

- Android：测试数据存储 - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x05d-Testing-Data-Storage.md>
- iOS：测试数据存储 - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x06d-Testing-Data-Storage.md>

更多信息，另请参见:

- OWASP Mobile Top 10: M1 (Improper Platform Usage) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m1-improper-platform-usage>
- OWASP Mobile Top 10: M2 (Insecure Data Storage) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m2-insecure-data-storage>
- CWE 117 (Improper Output Neutralization for Logs) - <https://cwe.mitre.org/data/definitions/117.html>
- CWE 200 (Information Exposure) - <https://cwe.mitre.org/data/definitions/200.html>
- CWE 276 (Incorrect Default Permissions) - <https://cwe.mitre.org/data/definitions/276.html>
- CWE 311 (Missing Encryption of Sensitive Data) - <https://cwe.mitre.org/data/definitions/311.html>
- CWE 312 (Cleartext Storage of Sensitive Information) - <https://cwe.mitre.org/data/definitions/312.html>
- CWE 316 (Cleartext Storage of Sensitive Information in Memory) - <https://cwe.mitre.org/data/definitions/316.html>
- CWE 359 (Exposure of Private Information ('Privacy Violation')) - <https://cwe.mitre.org/data/definitions/359.html>
- CWE 522 (Insufficiently Protected Credentials) - <https://cwe.mitre.org/data/definitions/522.html>
- CWE 524 (Information Exposure Through Caching) - <https://cwe.mitre.org/data/definitions/524.html>
- CWE 530 (Exposure of Backup File to an Unauthorized Control Sphere) - <https://cwe.mitre.org/data/definitions/530.html>
- CWE 532 (Information Exposure Through Log Files) - <https://cwe.mitre.org/data/definitions/532.html>
- CWE 534 (Information Exposure Through Debug Log Files) - <https://cwe.mitre.org/data/definitions/534.html>
- CWE 634 (Weaknesses that Affect System Processes) - <https://cwe.mitre.org/data/definitions/634.html>
- CWE 798 (Use of Hard-coded Credentials) - <https://cwe.mitre.org/data/definitions/798.html>
- CWE 921 (Storage of Sensitive Data in a Mechanism without Access Control) - <https://cwe.mitre.org/data/definitions/921.html>
- CWE 922 (Insecure Storage of Sensitive Information) - <https://cwe.mitre.org/data/definitions/922.html>
