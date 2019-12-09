# V1：架构，设计和威胁建模要求

## 控制目标

在一个完美的世界中，安全需要在开发的整个阶段被考虑。然而，实际上，安全性通常只是SDLC后期的考虑因素。除了技术控制之外，MASVS要求适当的流程，以确保在规划移动应用程序的架构时明确地解决了安全性问题，并且知道所有组件的功能和安全性角色。由于大多数移动应用程序充当远程服务的客户端，因此必须确保这些服务也运用适当的安全标准 - 单独测试移动应用程序是不够的。

类别“V1”列出了与应用程序的架构和设计相关的需求。因此，这是OWASP移动测试指南中唯一没有映射到技术测试用例的类别。为了涵盖诸如威胁建模、安全SDLC、密钥管理等主题，MASVS的用户应该参考各自的OWASP项目和/或其他标准(如下面链接的标准)。

<div style="page-break-after: always;">
</div>

## 安全验证要求

下面列出了对 `MASVS-L` 和 `MASVS-L2` 的要求。

| # | MSTG-ID | 描叙 | L1 | L2 |
| --- | --- | --- | --- | --- |
| **1.1** | MSTG‑ARCH‑1 |所有的应用程序组件都被标识出来，并被认为是需要的。 | ✓| ✓|
| **1.2** | MSTG‑ARCH‑2 |安全控制不仅仅在客户端强制执行，而是在各个远程端点强制执行。 | ✓| ✓|
| **1.3** | MSTG‑ARCH‑3 |安全已经被强调在移动应用和所有连接的远程服务的高级架构图中。 | ✓| ✓|
| **1.4** | MSTG‑ARCH‑4 |数据在移动应用内容中被定义为敏感的已经被清楚的识别出来。 | ✓| ✓|
| **1.5** | MSTG‑ARCH‑5 |所有应用程序组件都是根据它们提供的业务功能和/或安全功能来定义的。 | | ✓|
| **1.6** | MSTG‑ARCH‑6 |已经为移动应用程序和相关的远程服务生成了一个威胁模型，用于识别潜在的威胁和应对措施。 | | ✓|
| **1.7** | MSTG‑ARCH‑7 |所有的安全控制实现了集中的管控。 | | ✓|
| **1.8** | MSTG‑ARCH‑8 |必须有一个明确的策略，对于如何管理加密密钥(如果有的话)，强制执行加密密钥的生命周期。理想情况下，应遵循NIST SP 800-57密钥管理标准。 | | ✓|
| **1.9** | MSTG‑ARCH‑9 |存在强制更新移动应用程序的机制。 | | ✓|
| **1.10** | MSTG‑ARCH‑10 |安全性在软件开发生命周期的所有部分中都得到了解决。 | | ✓|
| **1.11** | MSTG‑ARCH‑11 |一个负责任漏洞披露政策已经存在并且得到了有效的应用。 | | ✓|
| **1.12** | MSTG‑ARCH‑12 |该应用程序应遵守隐私法律和法规。 | ✓| ✓|

## 参考文献

有关更多信息，另请参见：

- OWASP 移动安全前10: M10 (外部功能) - <https://www.owasp.org/index.php/Mobile_Top_10_2016-M10-Extraneous_Functionality>
- OWASP 安全体系结构速查表 - <https://www.owasp.org/index.php/Application_Security_Architecture_Cheat_Sheet>
- OWASP 威胁建模 - <https://www.owasp.org/index.php/Application_Threat_Modeling>
- OWASP 安全SDLC备忘单 - <https://www.owasp.org/index.php/Secure_SDLC_Cheat_Sheet>
- Microsoft SDL - <https://www.microsoft.com/en-us/sdl/>
- NIST SP 800-57 - <http://csrc.nist.gov/publications/nistpubs/800-57/sp800-57-Part1-revised2_Mar08-2007.pdf>
- security.txt - <https://securitytxt.org/>