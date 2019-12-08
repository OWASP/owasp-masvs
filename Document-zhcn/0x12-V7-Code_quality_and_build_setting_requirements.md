# V7：代码质量和构建设置要求

## 控制目标

此控件的目标是确保在开发应用程序时遵循基本的安全编码惯例，并激活由编译器提供的“免费”安全功能。

## 安全验证要求

| # | MSTG-ID | 描述 | L1 | L2 |
| --- | --- | --- | --- | --- |
| **7.1** | MSTG‑CODE‑1 |该应用程序已签名并提供了有效证书，且该证书的私钥已得到适当保护。 | ✓| ✓|
| **7.2** | MSTG‑CODE‑2 |该应用已在发布模式下构建，并具有适合发布版本的设置（例如不可调试）。 | ✓| ✓|
| **7.3** | MSTG‑CODE‑3 |调试符号已从本机二进制文件中删除。 | ✓| ✓|
| **7.4** | MSTG‑CODE‑4 |调试代码和开发者帮助代码（例如测试代码，后门，隐藏设置）已删除。该应用程序不会记录详细错误或调试消息。 | ✓| ✓|
| **7.5** | MSTG‑CODE‑5 |识别并检查移动应用程序使用的所有第三方组件，例如库和框架，并检查是否存在已知漏洞。 | ✓| ✓|
| **7.6** | MSTG‑CODE‑6 |该应用程序捕获并处理可能的异常。 ✓| ✓|
| **7.7** | MSTG‑CODE‑7 |安全控件中的错误处理逻辑默认情况下拒绝访问。 | ✓| ✓|
| **7.8** | MSTG‑CODE‑8 |在非托管代码中，安全地分配，释放和使用内存。 | ✓| ✓|
| **7.9** | MSTG‑CODE‑9 |工具链提供的免费安全功能被激活，例如字节码最小化，堆栈保护，PIE支持和自动引用计数。 | ✓| ✓|

## 参考文献

OWASP 移动安全性测试指南提供了验证上面列出的要求的详细说明.

- Android: 测试代码质量和构建设置 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05i-Testing-Code-Quality-and-Build-Settings.md>
- iOS: 测试代码质量和构建设置 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06i-Testing-Code-Quality-and-Build-Settings.md>

有关更多信息，另请参见:

- OWASP Mobile 前10名: M7 (代码质量不佳) - <https://www.owasp.org/index.php/Mobile_Top_10_2016-M7-Poor_Code_Quality>
- CWE 119 (内存缓冲区范围内的操作限制不当) - <https://cwe.mitre.org/data/definitions/119.html>
- CWE 89 (SQL命令中使用的特殊元素的不适当中和) - <https://cwe.mitre.org/data/definitions/89.html>
- CWE 388 (7PK - 错误) - <https://cwe.mitre.org/data/definitions/388.html>
- CWE 489 (遗留调试代码) - <https://cwe.mitre.org/data/definitions/489.html>
