![OWASP LOGO](images/OWASP_logo.png)

# Mobile Application Security Verification Standard

## 本標準について

Mobile Application Security Verification Standard (MASVS) 1.1 へようこそ。MASVS は iOS および Android 上のセキュアなモバイルアプリケーションを設計、開発、テストするときに必要となるセキュリティ要件のフレームワークを確立するためのコミュニティの取組みです。

MASVS はコミュニティにおける取組みと業界からのフィードバックの成果です。私たちは本標準が時間の経過とともに進化することを期待しており、コミュニティからのフィードバックを歓迎します。私たちと連絡を取る最善の方法は OWASP Mobile Project Slack チャンネルを利用することです。

<https://owasp.slack.com/messages/project-mobile_omtg/details/>

アカウントは以下の URL で作成できます。

[https://owasp.slack.com/](https://join.slack.com/t/owasp/shared_invite/enQtNjExMTc3MTg0MzU4LWQ2Nzg3NGJiZGQ2MjRmNzkzN2Q4YzU1MWYyZTdjYjA2ZTA5M2RkNzE2ZjdkNzI5ZThhOWY5MjljYWZmYmY4ZjM)

## 著作権とライセンス

![license](images/CC-license.png)

Copyright © 2019 The OWASP Foundation. 本著作物は [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/) に基づいてライセンスされています。再使用または配布する場合は、他者に対し本著作物のライセンス条項を明らかにする必要があります。

<div style="page-break-after: always;">
</div>

## 謝辞

| プロジェクトリーダー | 主執筆者 | 共同執筆者およびレビュー担当者 |
| --- | --- | --- |
| Sven Schleier, Jeroen Willemsen and Carlos Holguera | Bernhard Mueller | Alexander Antukh, Mesheryakov Aleksey, Bachevsky Artem, Jeroen Beckers, Vladislav Chelnokov, Ben Cheney, Peter Chi, Lex Chien, Stephen Corbiaux, Manuel Delgado, Ratchenko Denis, Ryan Dewhurst, Tereshin Dmitry, Christian Dong, Oprya Egor, Ben Gardiner, Rocco Gränitz, Henry Hu, Sjoerd Langkemper, Vinícius Henrique Marangoni, Martin Marsicano, Roberto Martelloni, Gall Maxim, Eugen Martynov, Riotaro Okada, Abhinav Sejpal, Stefaan Seys, Yogesh Sharma, Prabhant Singh, Sven Schleier, Nikhil Soni, Anant Shrivastava, Francesco Stillavato, Romuald Szkudlarek, Abderrahmane Aftahi, Abdessamad Temmar, Koki Takeyama, Chelnokov Vladislav, Leo Wang |

| 言語 | 翻訳者およびレビュー担当者 |
| --- | --- |
| 中国語 | Peter Chi, and Lex Chien, Henry Hu, Leo Wang |
| フランス語 | Romuald Szkudlarek, Abderrahmane Aftahi, Christian Dong (Review) |
| ドイツ語 | Rocco Gränitz, Sven Schleier (Review) |
| 日本語 | Koki Takeyama, Riotaro Okada (Review) |
| 韓国語 | Youngjae Jeon, Jeongwon Cho, Jiyou Han, Jiyeon Sung |
| ロシア語 | Gall Maxim, Eugen Martynov, Chelnokov Vladislav (Review), Oprya Egor (Review), Tereshin Dmitry (Review) |
| スペイン語 | Martin Marsicano, Carlos Holguera |

本ドキュメントは Jim Manico により執筆された OWASP Web アプリケーションセキュリティ検証標準のフォークとして始まりました。

## スポンサー

MASVS と MSTG のいずれもコミュニティにより無償奉仕で作成および維持されていますが、時にはいくらかの外的支援が必要となることもあります。したがって、テクニカルエディタを雇うことができる資金を提供したスポンサーに感謝します。彼らのスポンサーシップは MASVS や MSTG の内容にいかなる形であれ影響を与えないことに注意します。スポンサーシップパッケージは [OWASP Project Wiki](https://www.owasp.org/index.php/OWASP_Mobile_Security_Testing_Guide#tab=Sponsorship_Packages "OWASP Mobile Security Testing Guide Sponsorship Packages") に記載されています。

### 名誉後援者

[![NowSecure](images/NowSecure_logo.png)](https://www.nowsecure.com/ "NowSecure")

### 慈善後援者

[![RandoriSec](images/Randorisec_logo.png)](https://www.randorisec.fr/ "RandoriSec")

次に、OWASPベイエリア支部の後援に感謝します。 最後に、Leanpubからこの本を購入し私たちを支援してくれた皆様に感謝します。
