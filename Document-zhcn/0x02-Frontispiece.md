# 关于标准

<img src="images/OWASP_logo.png" title="OWASP LOGO" />

欢迎阅读移动应用安全验证标准（MASVS）1.2版. MASVS 是一个社区项目，其宗旨是建立一个安全需求的框架给人们去设计、开发和测试iOS和Android的移动应用程序。

MASVS是社区努力和行业反馈的成果。我们希望该标准会随着时间的推移不断更新，并且非常欢迎来自社区的意见反馈。

与我们取得联系的最佳方式是通过OWASP Mobile Project Slack频道: <https://owasp.slack.com/messages/project-mobile_omtg/details/>

可以通过以下URL创建帐户: [https://owasp.slack.com/join/shared_invite/zt-g398htpy-AZ40HOM1WUOZguJKbblqkw#/](https://owasp.slack.com/join/shared_invite/zt-g398htpy-AZ40HOM1WUOZguJKbblqkw#/)

## 版权和许可

[<img src="images/CC-license.png" title="License" width="200px" height="45px" />](https://creativecommons.org/licenses/by-sa/4.0/)

版权所有©2020 OWASP基金会。本作品是根据[知识共享署名-相同方式共享 4.0 国际许可](https://creativecommons.org/licenses/by-sa/4.0/)。对于任何重复使用或分发，您必须向他人明确此作品的许可条款。

<!-- \pagebreak -->

## 致谢

| 项目负责人 | 主要作者 | 贡献者和审稿人
| ------- | --- | ----------------- |
| Sven Schleier，Jeroen Willemsen和Carlos Holguera | Bernhard Mueller |亚历山大·安图克（Alexander Antukh），梅谢里亚科夫（Meshyayakov Aleksey），巴切夫斯基·阿特姆（Bachevsky Artem），耶隆·贝克斯（Jeroen Beckers），弗拉迪斯拉夫·切尔诺科夫（Fladislav Chelnokov），本·切尼（Ben Cheney），彼得·奇（Lex Chien），史蒂芬·科比奥克斯（Stephen Corbiaux），曼努埃尔·德尔加多（Manuel Delgado），拉切科·丹尼斯（Ratchenko Denis），瑞安·德赫斯特（Ryan Dewhurst），泰瑞辛·德米特里（Tereshin Dmitry），克里斯蒂安·东（Christian Dong），奥普拉·埃戈尔（Bry Gardiner） ，亨利·胡（Henry Hu），舍尔·兰格坎珀（Sjoerd Langkemper），维尼修斯·亨利克·马兰戈尼（ViníciusHenrique Marangoni），马丁·马西卡诺（Roberto Martelloni），加尔·马克西姆（Gall Maxim），冈田里奥塔罗·冈田（Riotaro Okada），阿比纳夫·塞普帕尔（Afhinav Sejpal），史蒂芬·塞伊斯（Stefaan Seys），尤格什·夏尔马（Yogesh Sharma），普拉汉（Prabhant Singh），斯文·史莱尔（Sven Schleier），尼基·索尼（Nanhil Soni），安南·斯里瓦斯塔库（Anant Shrivastava），弗朗切斯科·斯蒂瓦拉托（Francesco Stillavato） Abdessamad Temmar，Koki Takeyama，Celnokov Vladislav，Leo Wang |

<br/>

| 语言 |翻译和审核 |
| --- | ------------------------------ |
| 繁體中文 | Peter Chi, and Lex Chien, Henry Hu, Leo Wang |
| 簡體中文 | Bob Peng, Harold Zang, Jack S |
| 法语 | Romuald Szkudlarek, Christian Dong (审核) |
| 德文 | Rocco Gränitz, Sven Schleier (审核) |
| 印地语 | Mukesh Sharma, Ritesh Kumar, Atul Kunwar, Parag Dave, Devendra Kumar Sinha, Vikrant Shah |
| 西班牙语 | Martin Marsicano, Carlos Holguera |
| 日语 | Koki Takeyama, Riotaro Okada (审核) |
| 俄语 | Gall Maxim, Chelnokov Vladislav (审核), Oprya Egor (审核), Tereshin Dmitry (审核) |
| 韩语 | Youngjae Jeon, Jeongwon Cho, Jiyou Han, Jiyeon Sung |

本文档是由Jim Manico编写的OWASP Application Security Verification Standard的一个分支。

## 赞助商

虽然MASVS和MSTG都是由社区自愿创建和维护的，但是有时候仍然需要一点外部的帮助。因此，我们感谢我们的赞助商提供资金来聘请技术编辑。但是，他们的赞助不会以任何方式影响MASVS或MSTG的内容。赞助方案的具体细节：[OWASP项目Wiki](https://owasp.org/www-project-mobile-security-testing-guide/#div-sponsorship "OWASP Mobile Security Testing Guide Sponsorship Packages").

### 特别致谢

[<img src="images/NowSecure_logo.png" title="NowSecure" width="200px" height="58px" />](https://www.nowsecure.com/ "NowSecure")

### 好心人赞助

[<img src="images/Randorisec_logo.png" title="Randorisec" width="200px" height="58px" />](https://www.randorisec.fr/ "RandoriSec")

接下来，我们要感谢OWASP湾区分会的赞助。最后，我们要感谢每一位从Leanpub购买了这本书并以这种方式赞助我们的人。
