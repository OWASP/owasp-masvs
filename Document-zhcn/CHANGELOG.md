# 更新日志

## V1.3 - 11 May 2021

We are proud to announce the introduction of a new document build pipeline, which is major milestone for our project. The build pipeline is based on [Pandocker](https://github.com/dalibo/pandocker) and [Github Actions](https://github.com/OWASP/owasp-masvs/tree/master/.github/workflows). This significantly reduces the time spent on creating new releases. We would like to thank:

- Jeroen Willemsen for kick-starting this initiative last year!
- Damien Clochard and Dalibo for supporting and professionalizing the build pipeline.

The build pipeline will also be the foundation for the OWASP MSTG and will be made available for the OWASP ASVS project.

The following changes are part of release 1.3:

- 4 more translations are available, which are Hindi, Farsi, Portuguese and Brazilian Portuguese
- Added requirement MSTG-PLATFORM-11

## V1.2 - 2020年3月7日 - 国际发行

以下是版本1.2的更改：

- 提供MASVS的简体中文翻译。
- 更改MASVS封面的标题。
- 从MSTG中删除Mobile Top 10与CWE，并与MASVS中的现有引用进行合并。

## V1.2-RC - 2019年10月5号 - 预发行版 (仅限英语)

以下为1.2-RC版本所包含的更新内容：

晋升为同类安全指南最成功的作品。

- 更改要求 MSTG-STORAGE-1 "需要被使用"（need to be used）。
- 增加侧重于数据保护的要求 MSTG-STORAGE-13， MSTG-STORAGE-14， 和 MSTG-STORAGE-15。
- 更新要求MSTG-AUTH-11，以保护上下文信息（contextual information）。
- 更新要求MSTG-CODE-4，以涵盖更多信息而不仅仅是排错调试（debugging）。
- 添加要求MSTG-PLATFORM-10，以进一步安全的使用WebViews。
- 添加要求MSTG-AUTH-12，以提醒开发人员部署授权，特别是在多用户应用程序（multi-user apps）的情况下。
- 在怎样使用MASVS进行风险评估中添加了一点描述。
- 在付费内容（paid content）中添加了一点描述。
- 增加要求MSTG-ARCH-11，以包含针对L2应用程序的 责任披露政策（Responsible Disclosure policy）。
- 增加要求MSTG-ARCH-12，以向应用程序开发人员展示他们应遵守的相关的国际隐私法律。
- 为英文版的引用（references）创建了一个固定的格式。
- 添加要求MSTG-PLATFORM-11，以反击通过第三方键盘进行的间谍活动（spying）。
- 添加要求MSTG-MSTG-RESILIENCE-13，以阻止在应用程序中的窃听。

## V1.1.4 - 2019年7月4号 - 峰会版

以下为1.1.4版本所包含的更新内容：

- 修复所有轻量级标记语言（markdown）问题。
- 更新法文和西班牙文翻译。
- 完成更新日志的繁体中文和日文翻译。
- 自动验证 轻量级标记语言 的语法以及网址是否可以访问。
- 新增标记代码到各个要求，以便于未来在MSTG中可以快速以及方便的找到相关建议和测试方案。
- 缩减仓库大小，新增Generated到.gitignore文件中。
- 新增行为守则以及撰稿准则（Contributing guidelines）。
- 新增拉取要求（Pull-Request）模版。
- 更新与Gitbook网页仓库同步的功能。
- 更新所有翻译版本用来产生XML/JSON/CSV 的脚本。
- 完成繁体中文版《前言》的翻译。

## V1.1.3 - 2019年1月9号 - 小幅度修正

以下为1.1.3版本所包含的更新内容：

- 修正要求7.1内西班牙文翻译问题。
- 在致谢区重新安排翻译者名字。

## V1.1.2 - 2019年1月3号 - 赞助者与国际翻译版

以下为1.1.2版本所包含的更新内容：

- 新增感谢信，这封感谢信给予那些购买了电子版的人。
- 在V4中添加了丢失身份验证链接和更新损坏的身份验证。
- 修正英文版中的4.7和4.8互换。
- 首次国际翻译版本！
  - 修正了西班牙文翻译。翻译目前已与英文版同步（1.1.2）。
  - 修正了俄罗斯文翻译。翻译目前已与英文版同步（1.1.2）。
  - 新增繁体中文，法文，德文和日文的第一版翻译。
- 简化文件格式以方便后续翻译工作。
- 新增自动化发布方式。

## V1.1.0 - 2018年7月14号

以下为1.1版本所包含的更新内容：

- 删除要求2.6"在可能包含敏感信息的文字栏上停止使用剪贴板"。
- 增加要求2.2"任何敏感资料不可以被存储在应用程序容器之外或者系统凭据存储设施中（System credential storage facilities）"。
- 更新要求2.1的用词，改为 "系统凭据存储设施可以适当的用于存储敏感信息，例如：个人资料，使用者凭据或者加密密钥"。

## V1.0 - 2018年1月12号

以下为1.0版本所包含的更新内容：

- 因为要求8.9和要求8.12 相同，因此删除要求8.9。
- 使得要求4.6更加通用。
- 一些小幅度修改（错别字或者错误的语法等）。
