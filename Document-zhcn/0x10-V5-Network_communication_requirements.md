# V5：网络通信要求

## 控制目标

本节中列出的子章节, 目的是确保移动应用程序和远程服务端点之间交换的信息的机密性和完整性。至少，移动应用程序必须使用设置适当的TLS协议为网络通信, 设置一个安全、加密的通道。级别2列出了额外的深度防御措施，如SSL固定。

## 安全验证要求

| # | MSTG-ID | 描述 | L1 | L2 |
| --- | --- | --- | --- | --- |
| **5.1** | MSTG‑NETWORK‑1 | 在网络传输中使用TLS对数据加密. 整个应用程序始终使用安全通道.  | ✓| ✓|
| **5.2** | MSTG‑NETWORK‑2 | 此 TLS 设置符合当前的最佳实践，或者当移动操作系统不支持建议的标准，则设置最接近. | ✓| ✓|
| **5.3** | MSTG‑NETWORK‑3 | 当安全通道被建立后，该应用程序将验证远程端点的X.509证书。 并且仅接受由受信任的CA签名的证书.  | ✓| ✓|
| **5.4** | MSTG‑NETWORK‑4 | 该应用程序要么使用自己的证书存储区，要么固定端点证书或公钥，即便随后提供一个不同的,受信任的CA签署的证书或者秘钥，也不会与端点建立连接. | | ✓|
| **5.5** | MSTG‑NETWORK‑5 | 该应用程序不依赖单一的不安全通信渠道（电子邮件或SMS）进行关键操作(例如, 注册和帐户恢复).  | | ✓|
| **5.6** | MSTG‑NETWORK‑6 | 该应用程序仅依赖于最新的连接 和 安全库. | | ✓|

## 参考文献

OWASP移动安全测试指南提供了验证本节中列出的要求的详细说明。

- 常规：测试网络通信 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04f-Testing-Network-Communication.md>
- Android: 测试网络通信 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05g-Testing-Network-Communication.md>
- iOS: 测试网络通信 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06g-Testing-Network-Communication.md>

有关更多信息，另请参见：

- OWASP Mobile Top 10: M3 (不安全通信) - <https://www.owasp.org/index.php/Mobile_Top_10_2016-M3-Insecure_Communication>
- CWE 319 (敏感信息的明文传输) - <https://cwe.mitre.org/data/definitions/319.html>
- CWE 295 (不正确的证书验证) - <https://cwe.mitre.org/data/definitions/295.html>
