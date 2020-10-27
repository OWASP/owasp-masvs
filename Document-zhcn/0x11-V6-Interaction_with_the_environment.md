# V6: 平台交互要求

## 控制目标

此组中的控制应确保应用程序以安全的方式使用平台API和标准组件。
此外，这些控制还须涵盖不同应用之间的IPC通信安全。

## 安全验证要求

| # | MSTG-ID | 描述 | L1 | L2 |
| -- | -------- | ---------------------- | - | - |
| **6.1** | MSTG-PLATFORM-1 | 该应用程序仅仅请求最少且必要的权限。 | ✓ | ✓ |
| **6.2** | MSTG-PLATFORM-2 | 所有外部以及用户输入都需要经过验证，并在必要时进行安全检查和过滤。所有通过用户界面，IPC 机制导入的数据，比如Intent、自定义的URL和来自网络的数据，都在此范畴内。 | ✓ | ✓ |
| **6.3** | MSTG-PLATFORM-3 | 除非这些机制得到正确的保护，否则应用程序不应通过自定义URL导出敏感数据。 | ✓ | ✓ |
| **6.4** | MSTG-PLATFORM-4 | 除非这些机制得到正确的保护，否则应用程序不应通过IPC导出敏感数据。 | ✓ | ✓ |
| **6.5** | MSTG-PLATFORM-5 | 除非明确要求，否则在WebViews中禁用JavaScript。 | ✓ | ✓ |
| **6.6** | MSTG-PLATFORM-6 | 设置WebViews只允许使用所需的最小协议处理程序集（比如，仅支持https）。具有潜在危险的处理程序，如文件存储、电话和应用程序id，应该被禁用。 | ✓ | ✓ |
| **6.7** | MSTG-PLATFORM-7 | 如果WebView可以调用应用程序的native方法，应确保WebView仅执行应用程序中的JavaScript。 | ✓ | ✓ |
| **6.8** | MSTG-PLATFORM-8 | 仅使用安全序列化API实现对象的反序列化。 | ✓ | ✓ |
| **6.9** | MSTG-PLATFORM-9 | 该应用程序具有保护屏幕覆盖攻击的机制。（仅限于Android） |  | ✓ |
| **6.10** | MSTG-PLATFORM-10 | 在销毁WebView之前，应清除WebView 的缓存、保存的文件以及加载的资源（比如JavaScript）。 |  | ✓ |
| **6.11** | MSTG-PLATFORM-11 | 该应用程序在用户输入敏感数据时应禁用第三方键盘程序。 仅限于iOS）| | ✓ |

## 参考文献

OWASP移动安全测试指南提供了验证本节中列出的要求的详细说明。

- Android: 测试平台交互 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05h-Testing-Platform-Interaction.md>
- iOS: 测试平台交互 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06h-Testing-Platform-Interaction.md>

有关详细信息，请参阅：

- OWASP Mobile Top 10: M1 (Improper Platform Usage) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m1-improper-platform-usage>
- OWASP Mobile Top 10: M7 (Poor Code Quality) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m7-client-code-quality>
- CWE 20 (Improper Input Validation) - <https://cwe.mitre.org/data/definitions/20.html>
- CWE 79 (Improper Neutralization of Input During Web Page Generation) - <https://cwe.mitre.org/data/definitions/79.html>
- CWE 200 (Information Leak / Disclosure) - <https://cwe.mitre.org/data/definitions/200.html>
- CWE 250 (Execution with Unnecessary Privileges) - <https://cwe.mitre.org/data/definitions/250.html>
- CWE 672 (Operation on a Resource after Expiration or Release) - <https://cwe.mitre.org/data/definitions/672.html>
- CWE 749 (Exposed Dangerous Method or Function) - <https://cwe.mitre.org/data/definitions/749.html>
- CWE 772 (Missing Release of Resource after Effective Lifetime) - <https://cwe.mitre.org/data/definitions/772.html>
- CWE 920 (Improper Restriction of Power Consumption) - <https://cwe.mitre.org/data/definitions/920.html>
- CWE 925 (Improper Verification of Intent by Broadcast Receiver) - <https://cwe.mitre.org/data/definitions/925.html>
- CWE 926 (Improper Export of Android Application Components) - <https://cwe.mitre.org/data/definitions/926.html>
- CWE 927 (Use of Implicit Intent for Sensitive Communication) - <https://cwe.mitre.org/data/definitions/927.html>
- CWE 939 (Improper Authorization in Handler for Custom URL Scheme) - <https://cwe.mitre.org/data/definitions/939.html>
