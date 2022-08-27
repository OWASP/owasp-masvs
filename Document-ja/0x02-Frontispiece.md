# 本標準について

![OWASP Logo](images/OWASP_logo.png)

Mobile Application Security Verification Standard (MASVS) へようこそ。MASVS は iOS および Android 上のセキュアなモバイルアプリケーションを設計、開発、テストするときに必要となるセキュリティ要件のフレームワークを確立するためのコミュニティの取組みです。

MASVS はコミュニティにおける取組みと業界からのフィードバックの成果です。私たちは本標準が時間の経過とともに進化することを期待しており、コミュニティからのフィードバックを歓迎します。私たちと連絡を取る最善の方法は OWASP Mobile Project Slack チャンネルを利用することです。

<https://owasp.slack.com/messages/project-mobile_omtg/details/>

アカウントは以下の URL で作成できます。

[https://owasp.slack.com/join/shared_invite/zt-g398htpy-AZ40HOM1WUOZguJKbblqkw#/](https://owasp.slack.com/join/shared_invite/zt-g398htpy-AZ40HOM1WUOZguJKbblqkw#/)

## 著作権とライセンス

[![Creative Commons License](images/CC-license.png)](https://creativecommons.org/licenses/by-sa/4.0/)

Copyright © 2021 The OWASP Foundation. 本著作物は [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/) に基づいてライセンスされています。再使用または配布する場合は、他者に対し本著作物のライセンス条項を明らかにする必要があります。

<!-- \pagebreak -->

## 謝辞

| プロジェクトリーダー | 主執筆者 | 共同執筆者およびレビュー担当者 |
| ------- | --- | ----------------- |
| Sven Schleier and Carlos Holguera | Bernhard Mueller, Sven Schleier, Jeroen Willemsen and Carlos Holguera | Alexander Antukh, Mesheryakov Aleksey, Elderov Ali, Bachevsky Artem, Jeroen Beckers, Jon-Anthoney de Boer, Damien Clochard, Ben Cheney, Will Chilcutt, Stephen Corbiaux, Manuel Delgado, Ratchenko Denis, Ryan Dewhurst, @empty_jack, Ben Gardiner, Anton Glezman, Josh Grossman, Sjoerd Langkemper, Vinícius Henrique Marangoni, Martin Marsicano, Roberto Martelloni, @PierrickV, Julia Potapenko, Andrew Orobator, Mehrad Rafii, Javier Ruiz, Abhinav Sejpal, Stefaan Seys, Yogesh Sharma, Prabhant Singh, Nikhil Soni, Anant Shrivastava, Francesco Stillavato, Abdessamad Temmar, Pauchard Thomas, Lukasz Wierzbicki |

<br/>

| 言語 | 翻訳者およびレビュー担当者 |
| --------------- | ------------------------------------------------------------ |
| ブラジルポルトガル語 | Mateus Polastro, Humberto Junior, Rodrigo |
| 繁体字中国語 | Peter Chi, and Lex Chien, Henry Hu, Leo Wang |
| 簡体字中国語 | Bob Peng, Harold Zang, Jack S |
| フランス語 | Romuald Szkudlarek, Abderrahmane Aftahi, Christian Dong (Review) |
| ドイツ語 | Rocco Gränitz, Sven Schleier (Review) |
| 日本語 | Koki Takeyama, Riotaro Okada (Review) |
| 韓国語 | Youngjae Jeon, Jeongwon Cho, Jiyou Han, Jiyeon Sung |
| ヒンディー語 | Mukesh Sharma, Ritesh Kumar, Atul Kunwar, Parag Dave, Devendra Kumar Sinha, Vikrant Shah |
| ペルシア語 | Hamed Salimian, Ramin Atefinia, Dorna Azhirak, Bardiya Akbari, Mahsa Omidvar, Alireza Mazhari, Milad Khoshdel |
| ポルトガル語 | Ana Filipa Mota, Fernando Nogueira, Filipa Gomes, Luis Fontes, Sónia Dias|
| ロシア語 | Gall Maxim, Eugen Martynov, Chelnokov Vladislav (Review), Oprya Egor (Review), Tereshin Dmitry (Review) |
| スペイン語 | Martin Marsicano, Carlos Holguera |

本ドキュメントは Jim Manico により執筆された OWASP Web アプリケーションセキュリティ検証標準のフォークとして始まりました。

## スポンサー

MASVS と MASTG のいずれもコミュニティにより無償奉仕で作成および維持されていますが、時にはいくらかの外的支援が必要となることもあります。したがって、テクニカルエディタを雇うことができる資金を提供したスポンサーに感謝します。彼らのスポンサーシップは MASVS や MASTG の内容にいかなる形であれ影響を与えないことに注意します。スポンサーシップパッケージは [OWASP Project Wiki](https://owasp.org/www-project-mobile-app-security/#div-sponsorship "OWASP Mobile Application Security Testing Guide Sponsorship Packages") に記載されています。

![OWASP MASTG](../Document/images/Donators/donators.png) \

最後に、[Leanpub](https://leanpub.com/mobile-security-testing-guide)からこの本を購入し私たちを支援してくれた皆様に感謝します。
