# V6：平台交互要求

## 控制目标

该列表中的管控，确保应用程序以安全的方式使用平台api和标准组件。此外，这些控制还包括应用程序之间的通信(IPC)。

## 安全验证要求

| # | MSTG-ID | 描述 | L1 | L2 |
| --- | --- | --- | --- | --- |
| **6.1** | MSTG‑PLATFORM‑1 | 应用程序只请求所需的最小权限集。 | ✓| ✓|
| **6.2** | MSTG‑PLATFORM‑2 | 所有来自外部资源和用户的输入都经过验证，并在必要时进行安全净化。这包括通过UI接收的数据、IPC机制(如intent、自定义url和网络源)。| ✓| ✓|
| **6.3** | MSTG‑PLATFORM‑3 | 应用程序不会通过自定义URL模式导出敏感的功能，除非这些机制得到了适当的保护。| ✓| ✓|
| **6.4** | MSTG‑PLATFORM‑4 | 否则应用程序不会通过IPC工具导出敏感功能，除非这些机制得到适当保护。 | ✓| ✓|
| **6.5** | MSTG‑PLATFORM‑5 | 除非明确要求，否则在webview中禁用JavaScript。 | ✓| ✓|
| **6.6** | MSTG‑PLATFORM‑6 | 将webview配置为只允许所需的最小协议处理程序集(理想情况下，只支持https)。禁用潜在的危险处理程序，如文件、tel和app-id。 | ✓| ✓|
| **6.7** | MSTG‑PLATFORM‑7 | 如果应用程序的原生方法暴露给WebView，请验证WebView只呈现包含在应用程序包中的JavaScript。 | ✓| ✓|
| **6.8** | MSTG‑PLATFORM‑8 | 对象反序列化(如果有)是使用安全的序列化APIs实现的。 | ✓| ✓|
| **6.9** | MSTG‑PLATFORM‑9 | 应用程序保护自己免受屏幕覆盖攻击。(仅适用于Android)| | ✓|
| **6.10** | MSTG‑PLATFORM‑10 | 在销毁WebView之前，应该清除WebView的缓存、存储和加载的资源(JavaScript等). | | ✓|
| **6.11** | MSTG‑PLATFORM‑11 | 验证应用程序在输入敏感数据时防止使用自定义第三方键盘。| | ✓|

<div style="page-break-after: always;">
</div>

## 参考文献

OWASP 移动安全测试指南提供了验证本节中列出的要求的详细说明。

- Android: 测试平台互动 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05h-Testing-Platform-Interaction.md>
- iOS: 测试平台互动 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06h-Testing-Platform-Interaction.md>

有关更多信息，另请参见:

- OWASP 移动安全前 10: M1 (平台使用不当) - <https://www.owasp.org/index.php/Mobile_Top_10_2016-M1-Improper_Platform_Usage>
- CWE 20 (输入验证不正确) - <https://cwe.mitre.org/data/definitions/20.html>
- CWE 749 (暴露的危险方法或功能) - <https://cwe.mitre.org/data/definitions/749.html>
