# V3：加密要求

## 控制目标

在移动设备上，涉及保护存储的数据时，加密是必不可少的因素。 这也是一个可能出现严重错误的地方，尤其是在不遵循标准规则的情况下。本章中的管理目的是：确保经过安全验证的应用程序，使用加密技术，并依照了业界的最佳做法。这里包括:

- 使用经过验证的密码函数库；
- 正确选择和配置加密基元（cryptographic primitives）；
- 在任何需要随机数的地方都使用安全的随机数生成器。

## 安全验证要求

| # | MSTG-ID | 描述 | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **3.1** | MSTG-CRYPTO-1 | 该应用程序不依赖带有硬编码密钥的对称加密方式作为唯一的加密方法。 | x | x |
| **3.2** | MSTG-CRYPTO-2 | 该应用程序使用经过实现验证的密码基元。 | x | x |
| **3.3** | MSTG-CRYPTO-3 | 该应用在特定的案例下使用了合适的加密基元，参数配置符合行业最佳实践。 | x | x |
| **3.4** | MSTG-CRYPTO-4 | 该应用不使用基于安全目的而被广泛认为已经淘汰的加密协议或者算法。  | x | x |
| **3.5** | MSTG-CRYPTO-5 | 该应用不会将相同的秘钥重复用于多种途径。  | x | x |
| **3.6** | MSTG-CRYPTO-6 | 所有的随机数都被一个足够安全的随机数生成器生成。 | x | x |

## 参考文献

OWASP 移动安全测试指南提供了验证本节中列出的要求的详细说明。

- Android: 测试密码学 - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x05e-Testing-Cryptography.md>
- iOS: 测试密码学 - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x06e-Testing-Cryptography.md>

测试密码学:

- OWASP Mobile Top 10: M5 (Insufficient Cryptography) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m5-insufficient-cryptography>
- CWE 310 (Cryptographic Issues) - <https://cwe.mitre.org/data/definitions/310.html>
- CWE 321 (Use of Hard-coded Cryptographic Key) - <https://cwe.mitre.org/data/definitions/321.html>
- CWE 326 (Inadequate Encryption Strength) - <https://cwe.mitre.org/data/definitions/326.html>
- CWE 327 (Use of a Broken or Risky Cryptographic Algorithm) - <https://cwe.mitre.org/data/definitions/327.html>
- CWE 329 (Not Using a Random IV with CBC Mode) - <https://cwe.mitre.org/data/definitions/329.html>
- CWE 330 (Use of Insufficiently Random Values) - <https://cwe.mitre.org/data/definitions/330.html>
- CWE 337 (Predictable Seed in PRNG) - <https://cwe.mitre.org/data/definitions/337.html>
- CWE 338 (Use of Cryptographically Weak Pseudo Random Number Generator (PRNG)) - <https://cwe.mitre.org/data/definitions/338.html>
