# V8：弹性要求

## 控制目标

本节介绍了为处理或访问敏感数据或功能的应用程序推荐的深度防御措施。缺少这些控制并不会导致漏洞 - 相反，它们是为了提高应用程序对逆向工程和特定客户端攻击的弹性。

根据对未经授权篡改应用程序和/或代码反向工程造成的风险的评估，应根据需要应用本节中的控制。我们建议查阅OWASP文档“逆向工程的技术风险和未经授权的代码修改逆向工程和代码修改预防”(参见下面的参考资料)，以获得业务风险和相关技术威胁的列表。

要使下面列表中的任何管控有效，应用程序必须至少满足所有`MASVS-L1`(即)，以及V8中所有编号较低的需求。例如，“阻止理解”中列出的模糊控制必须与“阻止动态分析和篡改”和“设备绑定”相结合。

**请注意，软件保护永远不能代替安全控制。在MASVR-R中列出的管控宗旨在为应用程序添加特定于威胁的额外保护管控，同时满足MASVS安全要求。**

以下是应注意的事项:

1. 必须定义一个威胁模型，该模型清楚地描述了防御的客户端威胁。此外，必须指定该方案要提供的保护等级。例如，一个明确的目标可能是迫使目标恶意软件的作者利用应用程序进行大量的人工逆向工程。

2. 威胁模型必须是合理的。例如，如果攻击者可以简单地对整个白盒进行编码，那么在白盒实现中隐藏加密密钥就不是重点了。

3. 这种保护的有效性应该总是由一位在测试特定类型的防篡改和模糊处理方面有经验的专家来验证(参见移动安全测试指南中的“反向工程”和“评估软件保护”章节)。

<div style="page-break-after: always;">
</div>

### 妨碍 动态分析 和 篡改

| # | MSTG-ID | 描述 | R |
| --- | --- | --- | - |
| **8.1** | MSTG‑RESILIENCE‑1 | 该应用程序通过警告用户或终止应用程序来检测和响应有ROOT设备或越狱设备的存在。 | ✓|
| **8.2** | MSTG‑RESILIENCE‑2 | 应用程序可以防止调试和/或检测并响应附加的调试器。必须覆盖所有可用的调试协议。 | ✓|
| **8.3** | MSTG‑RESILIENCE‑3 | 该应用程序可在自己的沙箱中检测、响应、任何篡改可执行文件和关键数据。 | ✓|
| **8.4** | MSTG‑RESILIENCE‑4 | 该应用程序检测并响应设备上常见的逆向工程工具和框架。 | ✓|
| **8.5** | MSTG‑RESILIENCE‑5 | 应用程序检测并响应正在模拟器中运行的程序。 | ✓|
| **8.6** | MSTG‑RESILIENCE‑6 | 应用程序在自己的内存空间中检测、响应其篡改代码和数据。 | ✓|
| **8.7** | MSTG‑RESILIENCE‑7 | 该应用程序在每个防御类中实现多个机制(8.1到8.6)。请注意，弹性的规模与数量，多样性的原始使用的机制。 | ✓|
| **8.8** | MSTG‑RESILIENCE‑8 | 检测机制触发不同类型的响应，包括延迟响应和隐形响应。 | ✓|
| **8.9** | MSTG‑RESILIENCE‑9 | 混淆化被应用于程序化的防御，这反过来又通过动态分析阻碍去混淆化。 | ✓|

### 设备绑定

| # | MSTG-ID | 描述 | R |
| --- | --- | --- | -|
| **8.10** | MSTG‑RESILIENCE‑10 | 该应用程序实现了一个“设备绑定”功能，使用一个设备指纹衍生自该设备的多个独特属性。 | ✓|

### 阻碍透析

| # | MSTG-ID | 描述 | R |
| --- | --- | --- | -|
| **8.11** | MSTG‑RESILIENCE‑11 | 应用程序的所有可执行文件和库都在文件级加密，可执行文件中的重要代码和数据段都加密或打包。简单的静态分析并不能揭示重要的代码或数据。 | ✓|
| **8.12** | MSTG‑RESILIENCE‑12 | 如果混淆化的目标是保护敏感的计算结果，那么考虑到目前发表的研究成果，混淆化方案既适用于特定的任务，又对机械化的手动和自动去混淆化方法具有较强的阻碍。混淆化方案的有效性必须通过人工测试来验证。请注意，尽可能使用基于硬件的隔离特性而不是混淆。 | ✓|

### 阻止窃听

| # | MSTG-ID | 描述 | R |
| --- | --- | --- | -|
| **8.13** | MSTG‑RESILIENCE‑13 | 作为一种深度防御，除了对通信方进行可靠的强化之外，还可以对应用程序级有效负载(payload)加密来进一步阻止窃听。 | ✓|

<div style="page-break-after: always;">
</div>

## 参考

OWASP 移动安全测试指南提供了验证本节中列出的要求的详细说明。

- Android: 针对逆向工程测试弹性 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05j-Testing-Resiliency-Against-Reverse-Engineering.md>
- iOS: 针对逆向工程测试弹性 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06j-Testing-Resiliency-Against-Reverse-Engineering.md>

有关更多信息，另请参见：

- OWASP 移动安全前 10: M8 (代码篡改) - <https://www.owasp.org/index.php/Mobile_Top_10_2016-M8-Code_Tampering>
- OWASP 移动安全前 10: M9 (逆向工程) - <https://www.owasp.org/index.php/Mobile_Top_10_2016-M9-Reverse_Engineering>
- OWASP 逆向工程威胁 - <https://www.owasp.org/index.php/Technical_Risks_of_Reverse_Engineering_and_Unauthorized_Code_Modification>
- OWASP 逆向工程和代码修改预防 - <https://www.owasp.org/index.php/OWASP_Reverse_Engineering_and_Code_Modification_Prevention_Project>
