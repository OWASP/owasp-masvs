# V1：架构，设计和威胁建模要求

## 控制目标

在一个理想的环境中，整个开发流程都要考虑到安全需求。然而实际上，安全需求通常只是SDLC后期的考虑因素。除了技术上的控制，MASVS要求开发流程在规划程序架构设计时就明确考虑安全需求，并且清楚所有组件的功能性与安全性。大多数的移动应用程序都是作为远程应用的客户端，因此远端应用的安全性也必须被充分纳入考量。所以，不仅仅只局限测试于移动应用，完整的移动安全测试需要包含测设远端应用的安全性。

“V1”这个类别罗列了应用程序的架构和设计相关的需求。这是唯一没有对应到OWASP移动测试指南（MSTG）的技术测试类别。为了涵盖威胁建模，安全SDLC，秘钥管理等相关主题，建议读者参考其他相对应的OWASP项目与其他标准（下文将会列出链接）。

## 安全验证要求

下面列出了 `MASVS-L` 和 `MASVS-L2` 的要求。

| # | MSTG-ID | 描叙 | L1 | L2 |
| -- | -------- | ---------------------- | - | - |
| **1.1** | MSTG-ARCH-1 | 所有应用程序组件都须标注出来，并且确定它们全部是必需的。 | ✓ | ✓ |
| **1.2** | MSTG-ARCH-2 | 所有安全控制都必须在客户端与各个远程端点被强制执行。 | ✓ | ✓ |
| **1.3** | MSTG-ARCH-3 | 该移动应用程序的高级架构与所有的远程服务都应该被定义，并且该设计解决了所有安全的相关问题。 | ✓ | ✓ |
| **1.4** | MSTG-ARCH-4 | 在移动应用程序环境下敏感的数据应该被清楚的标识出来。 | ✓ | ✓ |
| **1.5** | MSTG-ARCH-5 | 所有应用程序组件都是根据它们提供的业务功能和/或安全功能来进行定义的。 | | ✓ |
| **1.6** | MSTG-ARCH-6 | 已经制定了此 移动应用程序 和 相关的远程服务 的威胁模型，以识别潜在的威胁以及制定应对措施。 | | ✓ |
| **1.7** | MSTG-ARCH-7 | 所有的安全控制都必须被集中管理。 | | ✓ |
| **1.8** | MSTG-ARCH-8 | 如果移动应用程序用到加密密钥，就必须对密钥管理有明确的规定，并且强制推行密钥生命周期。理想情况下，应遵循 NIST SP 800-57密钥管理标准。 | | ✓ |
| **1.9** | MSTG-ARCH-9 | 该移动应用程序存在强制更新的机制。 | | ✓ |
| **1.10** | MSTG-ARCH-10 | 安全性在软件开发生命周期的所有阶段中都仔细纳入考量。 | | ✓ |
| **1.11** | MSTG-ARCH-11 | 漏洞提交方案存在并且可用。 | | ✓ |
| **1.12** | MSTG-ARCH-12 | 该应用程序必须遵守相关隐私法律法规。 | ✓ | ✓ |

## 参考文献

更多信息，另请参见：

- OWASP Mobile Top 10: M10 (外部功能) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m10-extraneous-functionality>
- OWASP 威胁建模 - <https://owasp.org/www-community/Application_Threat_Modeling>
- OWASP 安全SDLC速查表 - <https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets_excluded/Secure_SDLC_Cheat_Sheet.md>
- Microsoft SDL - <https://www.microsoft.com/en-us/sdl/>
- NIST SP 800-57 - <http://csrc.nist.gov/publications/nistpubs/800-57/sp800-57-Part1-revised2_Mar08-2007.pdf>
- security.txt - <https://securitytxt.org/>
