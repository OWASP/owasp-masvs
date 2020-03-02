# V5：网络通信要求

## 控制目标

本节中列出的控制目标, 目的是确保移动应用程序和远程服务端点之间交换的信息的机密性和完整性。确保移动应用程序必须使用TLS协议作为网络信息传输的安全加密通道。L2列出了额外的深度防御措施，如SSL证书绑定。

## 安全验证要求

| # | MSTG-ID | 描述 | L1 | L2 |
| -- | -------- | ---------------------- | - | - |
| **5.1** | MSTG-NETWORK-1 | 在网络传输中使用TLS对数据加密。整个应用程序始终使用安全加密通道。 | ✓ | ✓ |
| **5.2** | MSTG-NETWORK-2 | 此TLS设置符合当前的最佳实践，当移动操作系统不支持推荐的标准时，则设置为最接近的标准。 | ✓ | ✓ |
| **5.3** | MSTG-NETWORK-3 | 当安全通道被建立后，该应用程序将验证远程端点的X.509证书。 并且仅接受由受信任的CA签名的证书。 | ✓ | ✓ |
| **5.4** | MSTG-NETWORK-4 | 该应用程序要么使用自己的证书存储区，要么固定端点证书或公钥，即便随后提供一个不同的，受信任的CA签署的证书或者秘钥，也不会与端点建立连接。 | | ✓ |
| **5.5** | MSTG-NETWORK-5 | 该应用程序不依赖单一的不安全通信渠道（电子邮件或SMS）进行关键操作（例如：注册和帐户恢复）。  | | ✓ |
| **5.6** | MSTG-NETWORK-6 | 该应用程序仅依赖于最新的连接和安全库。 | | ✓ |

## 参考文献

OWASP移动安全测试指南提供了验证本节中列出的要求的详细说明。

- 常规：测试网络通信 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04f-Testing-Network-Communication.md>
- Android: 测试网络通信 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05g-Testing-Network-Communication.md>
- iOS: 测试网络通信 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06g-Testing-Network-Communication.md>

有关更多信息，另请参见：

- OWASP Mobile Top 10: M3 (Insecure Communication) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m3-insecure-communication>
- CWE 295 (Improper Certificate Validation) - <https://cwe.mitre.org/data/definitions/295.html>
- CWE 296 (Improper Following of a Certificate's Chain of Trust) - <https://cwe.mitre.org/data/definitions/296.html>
- CWE 297 (Improper Validation of Certificate with Host Mismatch) - <https://cwe.mitre.org/data/definitions/297.html>
- CWE 298 (Improper Validation of Certificate Expiration) - <https://cwe.mitre.org/data/definitions/298.html>
- CWE 308 (Use of Single-factor Authentication) - <https://cwe.mitre.org/data/definitions/308.html>
- CWE 319 (Cleartext Transmission of Sensitive Information) - <https://cwe.mitre.org/data/definitions/319.html>
- CWE 326 (Inadequate Encryption Strength) - <https://cwe.mitre.org/data/definitions/326.html>
- CWE 327 (Use of a Broken or Risky Cryptographic Algorithm) - <https://cwe.mitre.org/data/definitions/327.html>
- CWE 780 (Use of RSA Algorithm without OAEP) - <https://cwe.mitre.org/data/definitions/780.html>
- CWE 940 (Improper Verification of Source of a Communication Channel) - <https://cwe.mitre.org/data/definitions/940.html>
- CWE 941 (Incorrectly Specified Destination in a Communication Channel) - <https://cwe.mitre.org/data/definitions/941.html>
