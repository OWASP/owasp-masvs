![OWASP LOGO](Images/OWASP_logo.png)


# Mobile Application Security Verification Standard

## 本標準について

Mobile Application Security Verification Standard (MASVS) 1.1 へようこそ。MASVS は iOS および Android 上のセキュアなモバイルアプリケーションを設計、開発、テストするときに必要となるセキュリティ要件のフレームワークを確立するためのコミュニティの取組みです。

MASVS はコミュニティにおける取組みと業界からのフィードバックの成果です。私たちは本標準が時間の経過とともに進化することを期待しており、コミュニティからのフィードバックを歓迎します。私たちと連絡を取る最善の方法は OWASP Mobile Project Slack チャンネルを利用することです。

https://owasp.slack.com/messages/project-mobile_omtg/details/

アカウントは以下の URL で作成できます。

[http://owasp.herokuapp.com/](https://owasp.slack.com/join/shared_invite/enQtNDI5MzgxMDQ2MTAwLTEyNzIzYWQ2NDZiMGIwNmJhYzYxZDJiNTM0ZmZiZmJlY2EwZmMwYjAyNmJjNzQxNzMyMWY4OTk3ZTQ0MzFhMDY).

## 著作権とライセンス

![license](images/CC-license.png)

Copyright © 2018 The OWASP Foundation. 本著作物は [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/) に基づいてライセンスされています。再使用または配布する場合は、他者に対し本著作物のライセンス条項を明らかにする必要があります。

<div style="page-break-after: always;"></div>

## 謝辞

| プロジェクトリーダー | 主執筆者 | 共同執筆者およびレビュー担当者 |
| --- | --- | --- |
| Sven Schleier & Jeroen Willemsen | Bernhard Mueller | Alexander Antukh, Mesheryakov Aleksey, Bachevsky Artem, Jeroen Beckers, Vladislav Chelnokov, Ben Cheney, Peter Chi, Lex Chien, Stephen Corbiaux, Manuel Delgado, Ratchenko Denis, Ryan Dewhurst, Tereshin Dmitry, Christian Dong, Oprya Egor, Ben Gardiner, Rocco Gränitz, Henry Hu, Sjoerd Langkemper, Vinícius Henrique Marangoni, Martin Marsicano, Roberto Martelloni, Gall Maxim, Rio Okada, Abhinav Sejpal, Stefaan Seys, Yogesh Shamrma, Prabhant Singh, Nikhil Soni, Anant Shrivastava, Francesco Stillavato, Romuald SZKUDLAREK, Abdessamad Temmar, Koki Takeyama, Chelnokov Vladislav, Leo Wang |

本ドキュメントは Jim Manico により執筆された OWASP Web アプリケーションセキュリティ検証標準のフォークとして始まりました。

## スポンサー

MASVS と MSTG のいずれもコミュニティにより無償奉仕で作成および維持されていますが、時にはいくらかの外的支援が必要となることもあります。したがって、テクニカルエディタを雇うことができる資金を提供したスポンサーに感謝します。彼らのスポンサーシップは MASVS や MSTG の内容にいかなる形であれ影響を与えないことに注意します。スポンサーシップパッケージは [OWASP Project Wiki](https://www.owasp.org/index.php/OWASP_Mobile_Security_Testing_Guide#tab=Sponsorship_Packages "OWASP Mobile Security Testing Guide Sponsorship Packages") に記載されています。

### 名誉後援者

[![NowSecure](images/NowSecure_logo.png)](https://www.nowsecure.com/ "NowSecure")

次に、OWASPベイエリア支部の後援に感謝します。 最後に、Leanpubからこの本を購入し私たちを支援してくれた皆様に感謝します。
