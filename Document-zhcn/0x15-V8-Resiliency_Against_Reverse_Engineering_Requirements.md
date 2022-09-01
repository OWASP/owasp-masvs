# V8: 韧性要求

## 控制目标

本节涵盖的是对于应用程序中敏感数据（或功能）的处理以及访问的纵深防御措施。缺少这些防御措施并不会导致漏洞的产生，但是会降低应用程序对于逆向工程和某些客户端攻击的抵御能力。

相关人员应根据实际需求，基于应用程序可能面对的篡改或逆向工程进行风险评估从而实施本章节中的提到防御。我们建议查阅OWASP文档中的"逆向工程和未经授权的代码篡改的技术风险"章节（请参阅下面的参考资料）来了解相关的技术和业务风险。

**请注意，本章节列出的软件保护措施不能作为安全控制的替代品。MASVR-R中列出的防御措施旨在同时满足MASVS的安全要求的前提下，对于特定威胁的提供额外的保护。**

此外，还有以下几点注意事项：

1. 必须定义威胁模型且明确描述应用程序客户端所面临的威胁。此外，必须制定方案所提供的保护等级。例如，防御的既定目标可以是保护应用程序以迫使恶意软件作者必须投入大量精力来进行手动逆向分析。

2. 威胁模型必须敏感。例如，如果攻击者只需将白盒作为一个整体进行代码提升，那么在白盒实现中隐藏加密密钥就无从下手了。

3. 为了验证防御措施的有效性，必须通过具有相关经验（防篡改，防代码混淆）的从业人员进行手动测试（另见OWASP移动安全测试指南中的“逆向工程”和“评估软件保护”章节）。

### 阻碍动态分析与篡改

| # | MSTG-ID | 描述 | R |
| -- | ----------- | ---------------------- | - |
| **8.1** | MSTG-RESILIENCE-1 | 该应用程序具有检测移动设备越狱（iOS）或rooted（安卓）的功能。在检测到时，必须提醒用户或终止应用程序。 | x |
| **8.2** | MSTG-RESILIENCE-2 | 该应用程序具有检测和防御调试器的功能。必须涵盖所有相关的调试协议。 | x |
| **8.3** | MSTG-RESILIENCE-3 | 该应用程序具有检测和防御对于其可执行文件和对于其沙盒中关键数据篡改的机制。 | x |
| **8.4** | MSTG-RESILIENCE-4 | 该应用程序具有检测和防御逆向工程工具与框架的机制。 | x |
| **8.5** | MSTG-RESILIENCE-5 | 该应用程序具有检测和防御模拟器的使用。 | x |
| **8.6** | MSTG-RESILIENCE-6 | 该应用程序具有检测和防御对于其内存空间中代码和数据篡改的机制。 | x |
| **8.7** | MSTG-RESILIENCE-7 | 该应用程序在每个防御类别中实现多个机制（8.1~8.6）。请注意，应用程序的韧性会随所用机制的原创性和多样性而增强。 | x |
| **8.8** | MSTG-RESILIENCE-8 | 检测机制应触发不同类型的（例如延迟的或隐避的）响应和防御机制。 | x |
| **8.9** | MSTG-RESILIENCE-9 | 代码混淆须应用于程序性的防御，这反过来又阻碍了通过动态分析攻击。 | x |

### 设备绑定

| # | MSTG-ID | 描述 | R |
| -- | ----------- | ---------------------- | - |
| **8.10** | MSTG-RESILIENCE-10 | 该应用程序使用从多个设备特 有的属性中派生的设备指纹实现设备绑定功能。 | x |

### 阻碍理解

| # | MSTG-ID | 描述 | R |
| -- | ----------- | ---------------------- | - |
| **8.11** | MSTG-RESILIENCE-11 | 应用程序须对所有可执行文件和库进行文件级加密。必须对其中重要代码和数据段进行加密或加壳。普通的静态分析不应获取重要的代码或数据。 | x |
| **8.12** | MSTG-RESILIENCE-12 | 如果应用程序使用代码混淆来保护敏感的数据运算，则代码混淆须使用最新的方法及研究成果，以防御自动与手动反混淆。 如有可能，相对于硬件级别，尽可能使用硬件级别的代码隔离。 | x |

### 阻碍窃听

| # | MSTG-ID | 描述 | R |
| -- | ----------- | ---------------------- | - |
| **8.13** | MSTG-RESILIENCE-13 | 作为深度防御的一项措施，除了对网络通信， 对于应用程序级的通信加密可进一步阻止窃听。 | x |

## 参考文献

OWASP 移动安全测试指南提供了验证本节中列出的要求的详细说明。

- Android: 测试对于逆向工程的韧性 - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x05j-Testing-Resiliency-Against-Reverse-Engineering.md>
- iOS: 测试对于逆向工程的韧性 - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x06j-Testing-Resiliency-Against-Reverse-Engineering.md>

有关详细信息，请参阅：

- OWASP Mobile Top 10: M8 - <https://owasp.org/www-project-mobile-top-10/2016-risks/m8-code-tampering>
- OWASP Mobile Top 10: M9 - <https://owasp.org/www-project-mobile-top-10/2016-risks/m9-reverse-engineering>
- OWASP Reverse Engineering Threats - <https://wiki.owasp.org/index.php/Technical_Risks_of_Reverse_Engineering_and_Unauthorized_Code_Modification>
- OWASP Reverse Engineering and Code Modification Prevention - <https://wiki.owasp.org/index.php/OWASP_Reverse_Engineering_and_Code_Modification_Prevention_Project>
