# V3：密码学要求

## 控制目标

当涉及保护存储在移动设备上的数据时，密码学是必不可少的要素。 这也是一类可能导致严重错误的类别，尤其是在未遵循标准约定的情况下。 本章中控件的目的是确保经过验证的应用程序根据行业最佳实践使用加密，包括：

- 使用经过验证的密码库；
- 正确选择和配置密码原语；
- 在需要随机性的任何地方，都有合适的随机数生成器。

## 安全验证要求

| # | MSTG-ID | 描述 | L1 | L2 |
| --- | --- | --- | --- | --- |
| **3.1** | MSTG‑CRYPTO‑1 | 该应用程序不依赖具有硬编码密钥的对称加密作为唯一的加密方法。 ✓| ✓|
| **3.2** | MSTG‑CRYPTO‑2 | 该应用程序使用了经过验证的加密原语实现。 | ✓| ✓|
| **3.3** | MSTG‑CRYPTO‑3 | 该应用程序使用适合特定用例的加密原语，并配置了符合行业最佳实践的参数。 | ✓| ✓|
| **3.4** | MSTG‑CRYPTO‑4 | 该应用程序未使用出于安全目的而被广泛认为不赞成使用的加密协议或算法。 | ✓| ✓|
| **3.5** | MSTG‑CRYPTO‑5 | 该应用不会将相同的加密密钥用于多种用途。 | ✓| ✓|
| **3.6** | MSTG‑CRYPTO‑6 | 使用足够安全的随机数生成器生成所有随机值。 | ✓| ✓|

## 参考文献

OWASP 移动安全测试指南提供了验证本节中列出的要求的详细说明。.

- Android: 测试密码学 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05e-Testing-Cryptography.md>
- iOS: 测试密码学 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06e-Testing-Cryptography.md>

测试密码学:

- OWASP 移动版前10名: M5 (加密不足) - <https://www.owasp.org/index.php/Mobile_Top_10_2016-M5-Insufficient_Cryptography>
- CWE 310 (加密问题) - <https://cwe.mitre.org/data/definitions/310.html>
