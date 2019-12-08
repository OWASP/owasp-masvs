# V1：架构，设计和威胁建模要求

## 控制目标

在一个完美的世界中，将在开发的所有阶段都考虑安全性。然而，实际上，安全性通常只是SDLC后期的考虑因素。除了技术控制之外，MASVS还要求制定适当的流程，以确保在计划移动应用程序的体系结构时已明确解决了安全问题，并确保所有组件的功能和安全角色都是已知的。由于大多数移动应用程序充当远程服务的客户端，因此必须确保将适当的安全标准也应用于这些服务-单独测试移动应用程序是不够的。

"V1"类别列出了与应用程序的体系结构和设计有关的要求。因此，这是《 OWASP移动测试指南》中唯一不映射到技术测试用例的类别。为了涵盖诸如威胁建模，安全SDLC，密钥管理之类的主题，MASVS的用户应咨询各自的OWASP项目和/或其他标准，例如下面链接的标准。

<div style="page-break-after: always;">
</div>

## 安全验证要求

下面列出了对 MASVS-L 和 MASVS-L2 的要求。

| # | MSTG-ID | Description | L1 | L2 |
| --- | --- | --- | --- | --- |
| **1.1** | MSTG‑ARCH‑1 |确定了所有应用程序组件，并确定它们是必需的。 | ✓| ✓|
| **1.2** | MSTG‑ARCH‑2 |安全控制永远不会仅在客户端上执行，而只会在相应的远程端点上执行。 | ✓| ✓|
| **1.3** | MSTG‑ARCH‑3 |已经为移动应用程序和所有连接的远程服务定义了高级体系结构，并在该体系结构中解决了安全问题。 | ✓| ✓|
| **1.4** | MSTG‑ARCH‑4 |明确识别了在移动应用程序上下文中被认为敏感的数据。 | ✓| ✓|
| **1.5** | MSTG‑ARCH‑5 |所有应用程序组件均根据其提供的业务功能和/或安全功能进行定义。 | | ✓|
| **1.6** | MSTG‑ARCH‑6 |已经为移动应用程序和相关的远程服务创建了威胁模型，该模型可以识别潜在的威胁和对策。 | | ✓|
| **1.7** | MSTG‑ARCH‑7 |所有安全控制都有集中的实现。 | | ✓|
| **1.8** | MSTG‑ARCH‑8 |对于如何管理加密密钥（如果有）以及实施加密密钥的生命周期，有一个明确的策略。理想情况下，请遵循诸如NIST SP 800-57之类的密钥管理标准。 | | ✓|
| **1.9** | MSTG‑ARCH‑9 |存在强制执行移动应用程序更新的机制。 | | ✓|
| **1.10** | MSTG‑ARCH‑10 |在软件开发生命周期的所有部分中都解决了安全问题。 | | ✓|
| **1.11** | MSTG‑ARCH‑11 |负责任的披露政策已经到位并得到有效实施。 | | ✓|
| **1.12** | MSTG‑ARCH‑12 |该应用程序应符合隐私法律和法规。 | ✓| ✓|

## 参考文献

有关更多信息，另请参见：

- OWASP Mobile Top 10: M10 (外部功能) - <https://www.owasp.org/index.php/Mobile_Top_10_2016-M10-Extraneous_Functionality>
- OWASP 安全体系结构速查表 - <https://www.owasp.org/index.php/Application_Security_Architecture_Cheat_Sheet>
- OWASP 威胁建模 - <https://www.owasp.org/index.php/Application_Threat_Modeling>
- OWASP 安全SDLC备忘单 - <https://www.owasp.org/index.php/Secure_SDLC_Cheat_Sheet>
- Microsoft SDL - <https://www.microsoft.com/en-us/sdl/>
- NIST SP 800-57 - <http://csrc.nist.gov/publications/nistpubs/800-57/sp800-57-Part1-revised2_Mar08-2007.pdf>
- security.txt - <https://securitytxt.org/>
