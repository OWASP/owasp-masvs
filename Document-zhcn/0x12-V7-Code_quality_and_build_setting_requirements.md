# V7: 代码质量和编译要求

## 控制目标

此控制的目标是确保应用程序开发时遵循基本安全编程实践，并确保应用程序使用编译器所提供的基本安全功能。

## 安全验证要求

| # | MSTG-ID | 描述 | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **7.1** | MSTG-CODE-1 | 该应用程序使用有效的证书进行签名， 且私钥受到足够保护。 | x | x |
| **7.2** | MSTG-CODE-2 | 该应用程序以发布模式进行编译， 并配有适合发布版本的设置（例如不可调试模式）。 | x | x |
| **7.3** | MSTG-CODE-3 | 调试符号已从二进制文件中删除。 | x | x |
| **7.4** | MSTG-CODE-4 | 调试代码以及开发人员协助代码（例如程序后门、 隐藏设置）已被删除。应用程序不应记录详细错误或调试消息。 | x | x |
| **7.5** | MSTG-CODE-5 | 检查所有应用程序使用的第三方组件， 库以及框架，并检查其已知漏洞。| x | x |
| **7.6** | MSTG-CODE-6 | 该应用程序需能捕获并处理程序异常。 | x | x |
| **7.7** | MSTG-CODE-7 | 默认情况下， 安全控制中的错误处理逻辑拒绝访问。 | x | x |
| **7.8** | MSTG-CODE-8 | 对于没有自动进行内存管理的程序语言， 内存的分配，释放及使用需要被妥当地处理。 | x | x |
| **7.9** | MSTG-CODE-9 | 编译器提供的免费内置的二进制安全保护机制，例如代码缩小化， 堆栈保护，PIE支持和自动引用计数，已经开启。 | x | x |

## 参考文献

OWASP 移动安全测试指南提供了验证上述要求的详细说明。

- Android: 测试代码质量和编译设置 - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x05i-Testing-Code-Quality-and-Build-Settings.md>
- iOS: 测试代码质量和编译设置 - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x06i-Testing-Code-Quality-and-Build-Settings.md>

有关详细信息，请参阅：

- OWASP Mobile Top 10: M7 (Poor Code Quality) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m7-client-code-quality>
- CWE 20 (Improper Input Validation) - <https://cwe.mitre.org/data/definitions/20.html>
- CWE 89 (Improper Neutralization of Special Elements used in an SQL Command) - <https://cwe.mitre.org/data/definitions/89.html>
- CWE 95 (Improper Neutralization of Directives in Dynamically Evaluated Code ('Eval Injection')) - <https://cwe.mitre.org/data/definitions/95.html>
- CWE 119 (Improper Restriction of Operations within the Bounds of a Memory Buffer) - <https://cwe.mitre.org/data/definitions/119.html>
- CWE 215 (Information Exposure through Debug Information) - <https://cwe.mitre.org/data/definitions/215.html>
- CWE 388 (7PK - Errors) - <https://cwe.mitre.org/data/definitions/388.html>
- CWE 489 (Leftover Debug Code) - <https://cwe.mitre.org/data/definitions/489.html>
- CWE 502 (Deserialization of Untrusted Data) - <https://cwe.mitre.org/data/definitions/502.html>
- CWE 511 (Logic/Time Bomb) - <https://cwe.mitre.org/data/definitions/511.html>
- CWE 656 (Reliance on Security through Obscurity) - <https://cwe.mitre.org/data/definitions/656.html>
- CWE 676 (Use of Potentially Dangerous Function)  - <https://cwe.mitre.org/data/definitions/676.html>
- CWE 937 (OWASP Top Ten 2013 Category A9 - Using Components with Known Vulnerabilities) - <https://cwe.mitre.org/data/definitions/937.html>
