# 關於本標準

![OWASP Logo](images/OWASP_logo.png)

歡迎參閱 Mobile Application Security Verification Standard (MASVS). MASVS 是一個社群的成果，目的在於建立一個安全需求的架構給人們去設計、開發和測試iOS跟Android的安全行動應用程式。

MASVS是結合社群的努力和業界意見反饋來訂定的標準。我們期望這份標準能夠隨著時間演進不斷更新，也十分歡迎來自社群的意見反饋。透過OWASP Mobile Project的Slack channel與我們連絡是聯絡我們的最佳方式，以下是我們的Slack channel連結: <https://owasp.slack.com/messages/project-mobile_omtg/details/>

可以從以下的網址創建帳號：[https://owasp.slack.com/join/shared_invite/zt-g398htpy-AZ40HOM1WUOZguJKbblqkw#/](https://owasp.slack.com/join/shared_invite/zt-g398htpy-AZ40HOM1WUOZguJKbblqkw#/).

## 版權和許可

[![Creative Commons License](images/CC-license.png)](https://creativecommons.org/licenses/by-sa/4.0/)

Copyright © 2021 The OWASP Foundation. 本文檔在 Creative Commons Attribution ShareAlike 3.0 協議許可下發布。 對於任何二次使用或發布，你必須向其他人說明清楚這項成果的版權。

<!-- \pagebreak -->

## 致謝

| 項目負責人 | 主要作者 | 貢獻者和校稿人員
| ------- | --- | ----------------- |
| Sven Schleier and Carlos Holguera | Bernhard Mueller, Sven Schleier, Jeroen Willemsen and Carlos Holguera | Alexander Antukh, Mesheryakov Aleksey, Elderov Ali, Bachevsky Artem, Jeroen Beckers, Jon-Anthoney de Boer, Damien Clochard, Ben Cheney, Will Chilcutt, Stephen Corbiaux, Manuel Delgado, Ratchenko Denis, Ryan Dewhurst, @empty_jack, Ben Gardiner, Anton Glezman, Josh Grossman, Sjoerd Langkemper, Vinícius Henrique Marangoni, Martin Marsicano, Roberto Martelloni, @PierrickV, Julia Potapenko, Andrew Orobator, Mehrad Rafii, Javier Ruiz, Abhinav Sejpal, Stefaan Seys, Yogesh Sharma, Prabhant Singh, Nikhil Soni, Anant Shrivastava, Francesco Stillavato, Abdessamad Temmar, Pauchard Thomas, Lukasz Wierzbicki |

<br/>

| 語言 | 翻譯和複查人員 |
| --------------- | ------------------------------------------------------------ |
| 繁体中文 | Peter Chi, and Lex Chien, Henry Hu, Leo Wang |
| 简体中文 | Bob Peng, Harold Zang, Jack S |
| 法文 | Romuald Szkudlarek, Abderrahmane Aftahi, Christian Dong (Review) |
| 德文 | Rocco Gränitz, Sven Schleier (Review) |
| 印地語 | Mukesh Sharma, Ritesh Kumar, Atul Kunwar, Parag Dave, Devendra Kumar Sinha, Vikrant Shah |
| 西班牙文 | Martin Marsicano, Carlos Holguera |
| 日文 | Koki Takeyama, Riotaro Okada (Review) |
| 韓文 | Youngjae Jeon, Jeongwon Cho, Jiyou Han, Jiyeon Sung |
| 俄文 | Gall Maxim, Eugen Martynov, Chelnokov Vladislav, Oprya Egor, Tereshin Dmitry |
| 波斯語 | Hamed Salimian, Ramin Atefinia, Dorna Azhirak, Bardiya Akbari, Mahsa Omidvar, Alireza Mazhari, Milad Khoshdel |
| 葡萄牙語 | Ana Filipa Mota, Fernando Nogueira, Filipa Gomes, Luis Fontes, Sónia Dias|
| 巴西葡萄牙語 | Mateus Polastro, Humberto Junior, Rodrigo Araujo, Maurício Ariza, Fernando Galves |

本文檔最初是 Jim Manico 撰寫的 OWASP Application Security Verification Standard 的一個分支。

## 贊助者

雖然 MASVS 和 MASTG 都是由社群自願創建和維護的，但有時仍需要一些外部的協助。因此，我們感謝我們的贊助者提供資金來聘請技術編輯。請注意，他們的贊助不會以任何方式影響 MASVS 或 MASTG 的內容。贊助方案可在[OWASP Project Wiki](https://owasp.org/www-project-mobile-app-security/#div-sponsorship "OWASP Mobile Application Security Testing Guide Sponsorship Packages")找到。

<img src="https://raw.githubusercontent.com/OWASP/owasp-mastg/master/Document/Images/Donators/donators.png"/>

最後，我們要感謝所有從[Leanpub](https://leanpub.com/mobile-security-testing-guide)購買這本書並以這種方式贊助我們的人。
