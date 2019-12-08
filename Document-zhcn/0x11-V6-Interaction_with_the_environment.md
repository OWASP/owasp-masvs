# V6：平台互动要求

## 控制目标

该组中的控件可确保该应用以安全的方式使用平台API和标准组件。 此外，控件涵盖了应用程序之间的通信（IPC）。

## 安全验证要求

| # | MSTG-ID |描述L1 | L2 |
| --- | --- | --- | --- | --- |
| **6.1** | MSTG‑PLATFORM‑1 |该应用仅请求必要的最小权限集。 | ✓| ✓|
| **6.2** | MSTG‑PLATFORM‑2 |来自外部资源和用户的所有输入均经过验证，如有必要，还应进行消毒。这包括通过UI，IPC机制（如意图，自定义URL和网络源）接收的数据。 ✓| ✓|
| **6.3** | MSTG‑PLATFORM‑3 |该应用程序不会通过自定义URL方案导出敏感功能，除非这些机制得到了适当的保护。 | ✓| ✓|
| **6.4** | MSTG‑PLATFORM‑4 |该应用程序不会通过IPC设施导出敏感功能，除非这些机制得到了适当的保护。 | ✓| ✓|
| **6.5** | MSTG‑PLATFORM‑5 |除非明确要求，否则在WebView中禁用JavaScript。 | ✓| ✓|
| **6.6** | MSTG‑PLATFORM‑6 | WebView配置为仅允许所需的最少协议处理程序集（理想情况下，仅支持https）。禁用了潜在的危险处理程序，例如文件，电话和应用程序ID。 | ✓| ✓|
| **6.7** | MSTG‑PLATFORM‑7 |如果将应用程序的本机方法公开给WebView，请验证WebView仅呈现应用程序包中包含的JavaScript。 | ✓| ✓|
| **6.8** | MSTG‑PLATFORM‑8 |对象反序列化（如果有）是使用安全的序列化API实现的。 | ✓| ✓|
| **6.9** | MSTG‑PLATFORM‑9 |该应用程序可以保护自己免受屏幕覆盖攻击。 （仅适用于Android）| | ✓|
| **6.10** | MSTG‑PLATFORM‑10 |在销毁WebView之前，应清除WebView的缓存，存储和加载的资源（JavaScript等）。 | | ✓|
| **6.11** | MSTG‑PLATFORM‑11 |每次输入敏感数据时，验证应用是否阻止使用自定义第三方键盘。 | | ✓|

<div style="page-break-after: always;">
</div>

## 参考文献

OWASP 移动安全测试指南提供了验证本节中列出的要求的详细说明。

- Android: 测试平台互动 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05h-Testing-Platform-Interaction.md>
- iOS: 测试平台互动 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06h-Testing-Platform-Interaction.md>

有关更多信息，另请参见:

- OWASP Mobile Top 10: M1 (平台使用不当) - <https://www.owasp.org/index.php/Mobile_Top_10_2016-M1-Improper_Platform_Usage>
- CWE 20 (输入验证不正确) - <https://cwe.mitre.org/data/definitions/20.html>
- CWE 749 (暴露的危险方法或功能) - <https://cwe.mitre.org/data/definitions/749.html>
