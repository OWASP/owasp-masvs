# V8：弹性要求

## 控制目标

本节介绍了针对处理或允许访问敏感数据或功能的应用程序建议的纵深防御措施。缺少这些控件不会导致漏洞-相反，它们旨在提高应用程序抵抗逆向工程和特定客户端攻击的弹性。

应根据对未经授权篡改应用程序和/或代码的反向工程所造成的风险的评估，根据需要应用本节中的控件。我们建议参考OWASP文档“逆向工程和未经授权的代码修改的技术风险逆向工程和代码修改的预防”（请参阅​​下面的参考资料），以列出商业风险以及相关的技术威胁。

为了使以下列表中的任何控件有效，该应用程序必须至少满足所有MASVS-L1（即必须具备可靠的安全控件）以及V8中所有较低编号的要求。例如，“阻碍理解”下列出的混淆控制必须与“阻碍动态分析和篡改”以及“设备绑定”结合使用。

**请注意，绝对不能将软件保护用作安全控制的替代品。 MASVR-R中列出的控件旨在向还满足MASVS安全要求的应用添加特定于威胁的附加保护控件。**

适用以下注意事项：

1. 必须定义一个威胁模型，清楚地概述要防御的客户端威胁。 此外，必须指定计划要提供的保护等级。 例如，一个既定的目标可能是迫使目标恶意软件的作者寻求对应用进行检测，以投入大量的人工反向工程工作。

2. 威胁模型必须明智。 例如，如果攻击者可以简单地将白盒作为一个整体进行代码提升，那么在白盒实现中隐藏加密密钥就不那么重要了。

3. 保护的有效性应始终由具有测试所用特定类型的防篡改和混淆经验的人类专家进行验证(另请参见《移动安全测试指南》中的"逆向工程"和"评估软件保护"两章))。

<div style="page-break-after: always;">
</div>

### 阻碍动态分析和篡改

| # | MSTG-ID |描述R |
| --- | --- | --- | -|
| **8.1** | MSTG‑RESILIENCE‑1 |该应用程序通过提醒用户或终止该应用程序来检测并响应有根或越狱的设备的存在。 | ✓|
| **8.2** | MSTG‑RESILIENCE‑2 |该应用程序可防止调试和/或检测并响应已附加的调试器。必须涵盖所有可用的调试协议。 | ✓|
| **8.3** | MSTG‑RESILIENCE‑3 |该应用程序会检测并响应其自身沙箱中的可执行文件和关键数据的篡改。 | ✓|
| **8.4** | MSTG‑RESILIENCE‑4 |该应用程序可检测并响应设备上广泛使用的逆向工程工具和框架。 ✓|
| **8.5** | MSTG‑RESILIENCE‑5 |该应用程序检测并响应在模拟器中运行的情况。 | ✓|
| **8.6** | MSTG‑RESILIENCE‑6 |该应用程序检测并响应篡改其自身存储空间中的代码和数据。 | ✓|
| **8.7** | MSTG‑RESILIENCE‑7 |该应用程序在每个防御类别（8.1至8.6）中实现多种机制。请注意，弹性随使用的机制的新颖性的数量和多样性而定。 | ✓|
| **8.8** | MSTG‑RESILIENCE‑8 |检测机制触发不同类型的响应，包括延迟响应和隐身响应。 | ✓|
| **8.9** | MSTG‑RESILIENCE‑9 |模糊处理应用于程序防御，这又通过动态分析阻止了模糊处理。 | ✓|

### 设备绑定

| # | MSTG-ID |描述R |
| --- | --- | --- | -|
| **8.10** | MSTG‑RESILIENCE‑10 |该应用程序使用从设备唯一的多个属性派生的设备指纹来实现“设备绑定”功能。 | ✓|

### 阻碍理解

| # | MSTG-ID |描述R |
| --- | --- | --- | -|
| **8.11** | MSTG‑RESILIENCE‑11 |属于该应用程序的所有可执行文件和库都在文件级别进行了加密，并且/或者对可执行文件中的重要代码和数据段进行了加密或打包。简单的静态分析不会显示重要的代码或数据。 | ✓|
| **8.12** | MSTG‑RESILIENCE‑12 |如果混淆的目的是保护敏感的计算，则考虑当前已发表的研究，使用既适合于特定任务又针对手动和自动去混淆方法具有鲁棒性的混淆方案。混淆方案的有效性必须通过手动测试进行验证。请注意，只要有可能，首选基于硬件的隔离功能胜于混淆。 | ✓|

### 阻止窃听

| # | MSTG-ID |描述R |
| --- | --- | --- | -|
| **8.13** | MSTG‑RESILIENCE‑13 |作为深度防御，除了对通信方进行全面加固之外，还可以应用应用程序级别有效负载加密来进一步阻止窃听。 | ✓|

<div style="page-break-after: always;">
</div>

## 参考

OWASP 移动安全测试指南提供了验证本节中列出的要求的详细说明。

- Android: 针对逆向工程测试弹性 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05j-Testing-Resiliency-Against-Reverse-Engineering.md>
- iOS: 针对逆向工程测试弹性 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06j-Testing-Resiliency-Against-Reverse-Engineering.md>

有关更多信息，另请参见：

- OWASP Mobile Top 10: M8 (代码篡改) - <https://www.owasp.org/index.php/Mobile_Top_10_2016-M8-Code_Tampering>
- OWASP Mobile Top 10: M9 (逆向工程) - <https://www.owasp.org/index.php/Mobile_Top_10_2016-M9-Reverse_Engineering>
- OWASP 逆向工程威胁 - <https://www.owasp.org/index.php/Technical_Risks_of_Reverse_Engineering_and_Unauthorized_Code_Modification>
- OWASP 逆向工程和代码修改预防 - <https://www.owasp.org/index.php/OWASP_Reverse_Engineering_and_Code_Modification_Prevention_Project>
