# V3：密码学要求

## 控制目标

当涉及保护存储在移动设备上的数据时，密码学是必不可少的要素。 这也是一个可能出现严重错误的类别，尤其是在不遵循标准惯例的情况下。本章管制的目的，是确保已核实的应用程式根据业界的最佳做法使用密码技术，包括:

- 使用经过验证的密码库；
- 密码基元的正确选择和配置
- 任何需要随机性的地方都有一个适当的随机数生成器。

## 安全验证要求

| # | MSTG-ID | 描述 | L1 | L2 |
| --- | --- | --- | --- | --- |
| **3.1** | MSTG‑CRYPTO‑1 | 该应用程序不依赖带有硬编码密钥的对称加密作为唯一的加密方法。 ✓| ✓|
| **3.2** | MSTG‑CRYPTO‑2 | 该应用程序使用了经过验证的加密基元来实现。 | ✓| ✓|
| **3.3** | MSTG‑CRYPTO‑3 | 应用程序使用适合于特定用例的密码原语，并使用符合行业最佳实践的参数进行配置。 | ✓| ✓|
| **3.4** | MSTG‑CRYPTO‑4 | 该应用程序没有使用淘汰的加密协议或算法，这些协议或算法被广泛废弃基于安全目的。 | ✓| ✓|
| **3.5** | MSTG‑CRYPTO‑5 | 该应用不会将相同的加密密钥用于多种用途。 | ✓| ✓|
| **3.6** | MSTG‑CRYPTO‑6 | 所有随机数字都是使用一个足够安全的随机数生成器生成的。 | ✓| ✓|

## 参考文献

OWASP 移动安全测试指南提供了验证本节中列出的要求的详细说明。.

- Android: 测试密码学 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05e-Testing-Cryptography.md>
- iOS: 测试密码学 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06e-Testing-Cryptography.md>

测试密码学:

- OWASP 移动版前10名: M5 (加密不足) - <https://www.owasp.org/index.php/Mobile_Top_10_2016-M5-Insufficient_Cryptography>
- CWE 310 (加密问题) - <https://cwe.mitre.org/data/definitions/310.html>
