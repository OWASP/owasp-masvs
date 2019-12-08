# V5：网络通信要求

## 控制目标

本节中列出的控件的目的是确保移动应用程序与远程服务端点之间交换的信息的机密性和完整性。 至少，移动应用必须使用TLS协议和适当的设置来建立安全的加密通道以进行网络通信。 级别2列出了其他深度防御措施，例如SSL固定。

## 安全验证要求

| # | MSTG-ID |描述L1 | L2 |
| --- | --- | --- | --- | --- |
| **5.1** | MSTG‑NETWORK‑1 |数据使用TLS在网络上加密。在整个应用程序中始终使用安全通道。 | ✓| ✓|
| **5.2** | MSTG‑NETWORK‑2 | TLS设置符合当前的最佳做法，如果移动操作系统不支持建议的标准，则设置应尽可能接近。 | ✓| ✓|
| **5.3** | MSTG‑NETWORK‑3 |建立安全通道后，应用程序将验证远程端点的X.509证书。仅接受由受信任的CA签名的证书。 | ✓| ✓|
| **5.4** | MSTG‑NETWORK‑4 |该应用程序要么使用自己的证书存储，要么固定端点证书或公共密钥，并且随后即使与受信任的CA签署，也不会与提供不同证书或密钥的端点建立连接。 | | ✓|
| **5.5** | MSTG‑NETWORK‑5 |该应用程序不依赖单个不安全的通信渠道（电子邮件或SMS）进行关键操作，例如注册和帐户恢复。 | | ✓|
| **5.6** | MSTG‑NETWORK‑6 |该应用程序仅依赖于最新的连接性和安全性库。 | | ✓|

## 参考文献

OWASP移动安全测试指南提供了验证本节中列出的要求的详细说明。

- 常规：测试网络通信 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04f-Testing-Network-Communication.md>
- Android: 测试网络通信 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05g-Testing-Network-Communication.md>
- iOS: 测试网络通信 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06g-Testing-Network-Communication.md>

有关更多信息，另请参见：

- OWASP Mobile Top 10: M3 (不安全通信) - <https://www.owasp.org/index.php/Mobile_Top_10_2016-M3-Insecure_Communication>
- CWE 319 (敏感信息的明文传输) - <https://cwe.mitre.org/data/definitions/319.html>
- CWE 295 (不正确的证书验证) - <https://cwe.mitre.org/data/definitions/295.html>
