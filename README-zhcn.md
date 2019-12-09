<a href="https://github.com/OWASP/owasp-masvs/releases/download/1.1/OWASP_Mobile_AppSec_Verification_Standard_v1.1.pdf"><img width="25%" align="right" style="float: right;" src="Document/images/masvs-mini-cover.png"></a>

# OWASP 移动应用安全验证标准 [![Twitter Follow](https://img.shields.io/twitter/follow/OWASP_MSTG.svg?style=social&label=Follow)](https://twitter.com/OWASP_MSTG)

[![Creative Commons License](https://licensebuttons.net/l/by-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-sa/4.0/ "CC BY-SA 4.0")
[![OWASP Flagship](https://img.shields.io/badge/owasp-flagship%20project-48A646.svg)](https://www.owasp.org/index.php/Category:OWASP_Project#tab=Project_Inventory)
[![Build Status](https://travis-ci.com/OWASP/owasp-masvs.svg?branch=master)](https://travis-ci.com/OWASP/owasp-masvs)

这是OWASP移动应用程序安全验证标准（MASVS）的官方Github存储库。 MASVS为移动应用程序确定了基线安全要求，这些要求在许多情况下都非常有用，包括：

- 在SDLC中-建立解决方案架构师和开发人员应遵循的安全要求；
- 在移动应用渗透测试中-确保移动应用渗透测试的完整性和一致性；
- 在采购中-作为移动应用安全性的量度指标，例如 以供应商问卷的形式；
- Et cetera

MASVS是[OWASP移动安全测试指南]的姊妹项目。(https://github.com/OWASP/owasp-mstg "OWASP Mobile Security Testing Guide").

# 获取MASVS

PDF/Mobi/Epub/Docx 下载可在[发布页面]（https://github.com/OWASP/owasp-masvs/releases“发布”）上获得。 [MASVS的当前版本是1.1.4版]（https://github.com/OWASP/owasp-masvs/releases/tag/1.1.4“ MASVS 1.1.4版”）。 MASVS还提供不同语言的版本：

- [西班牙语](https://github.com/OWASP/owasp-masvs/tree/master/Document-es "Spanish")  
- [俄语](https://github.com/OWASP/owasp-masvs/tree/master/Document-ru "Russian")
- [德语](https://github.com/OWASP/owasp-masvs/tree/master/Document-de "German")
- [法语](https://github.com/OWASP/owasp-masvs/tree/master/Document-fr "French")
- [日语](https://github.com/OWASP/owasp-masvs/tree/master/Document-ja "Japanese")
- [中文 - ZHTW](https://github.com/OWASP/owasp-masvs/tree/master/Document-zhtw "Traditional Chinese (ZHTW)")
- [中文 - ZHCN](https://github.com/OWASP/owasp-masvs/tree/master/Document-zhcn "Simplified Chinese (ZHCN)")

## Gitbook

在 [Gitbook](https://mobile-security.gitbook.io/masvs/ "GitBook Mobile AppSec Verification Standard")上阅读它。 这本书会自动与主仓库同步

## 创建新的PDF，Epub或Mobi

您可以在发布页面中找到文档。 如果要自己生成文档，请执行以下步骤。 克隆存储库并运行gitbook生成器。 这将在“ Generated”子目录中生成PDF，Epub和Mobi文件。

```shell
$ git clone https://github.com/OWASP/owasp-masvs/
$ cd owasp-masvs/tools/
$ ./gitbookepubandpdf.sh LATEST
```

## 创建 Word 文档

克隆存储库并运行文档生成器（需要[pandoc]（http://pandoc.org/ "Pandoc"））。 这将在"Generated"子目录中生成docx和HTML文件。

```shell
$ git clone https://github.com/OWASP/owasp-masvs/
$ cd owasp-mstg/tools/
$ ./generate_document.sh
```

## 导出为JSON，XML和CSV

该存储库包含一个Python工具，用于将需求转换为各种格式。 克隆仓库并从tools文件夹运行 `export.py`。

```shell
export.py [-h] [--format {json,xml,csv}] [--lang {es/ru/en/fr/de/zhtw/ja}]
```

## 建议和反馈

要报告和错误或提出改进建议，请创建一个 [issue](https://github.com/OWASP/owasp-masvs/issues "Github issues") 或创建一个请求请求。

# 如何贡献

MASVS是一项开源工作，我们欢迎您提供意见和反馈。如果您想贡献其他内容或改善现有内容，建议您首先通过OWASP MSTG Slack渠道与我们联系：

<https://owasp.slack.com/messages/project-mobile_omtg/details/>

您可以在这里注册：

[https://owaspslack.com/](https://join.slack.com/t/owasp/shared_invite/enQtNjExMTc3MTg0MzU4LTViMDg1MmJiMzMwZGUxZjgxZWQ1MTE0NTBlOTBhNjhhZDIzZTZiNmEwOTJlYjdkMzAxMGVhNDkwNDNiNjZiOWQ)

在您开始贡献之前，请查看我们的[贡献指南](https://github.com/OWASP/owasp-masvs/blob/master/CONTRIBUTING.md "Contribution Guide") 它可以帮助您入门。

# 在此处阅读 MASVS 的各个部分

- [标题](Document-zhcn/0x00-Header.md)
- [序言](Document-zhcn/Foreword.md)
- [标题页](Document-zhcn/0x02-Frontispiece.md)
- [移动应用安全验证标准](Document-zhcn/0x03-Using_the_MASVS.md)
- [评估与验证](Document-zhcn/0x04-Assessment_and_Certification.md)
- [V1: 架构，设计和威胁建模要求](Document-zhcn/0x06-V1-Architecture_design_and_threat_modelling_requireme.md)
- [V2: 数据存储和隐私要求](Document-zhcn/0x07-V2-Data_Storage_and_Privacy_requirements.md)
- [V3: 密码学要求](Document-zhcn/0x08-V3-Cryptography_Verification_Requirements.md)
- [V4: 身份验证和会话管理要求](Document-zhcn/0x09-V4-Authentication_and_Session_Management_Requirements.md)
- [V5: 网络通信要求](Document-zhcn/0x10-V5-Network_communication_requirements.md)
- [V6: 环境互动要求](Document-zhcn/0x11-V6-Interaction_with_the_environment.md)
- [V7: 代码质量和构建设置要求](Document-zhcn/0x12-V7-Code_quality_and_build_setting_requirements.md)
- [V8: 针对逆向工程要求的弹性](Document-zhcn/0x15-V8-Resiliency_Against_Reverse_Engineering_Requirements.md)
- [附录A：词汇表](Document-zhcn/0x90-Appendix-A_Glossary.md)
- [附录B：参考](Document-zhcn/0x91-Appendix-B_References.md)
