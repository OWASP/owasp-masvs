# 본 표준에 대하여

<img src="images/OWASP_logo.png" title="OWASP LOGO" />

모바일 애플리케이션 보안 검증 표준(MASVS) 1.2에 오신것을 환영합니다. MASVS는 iOS 및 Android에서 안전한 모바일 앱을 설계, 개발, 테스트하는데 필요한 보안 요구사항의 프레임워크를 확립하기 위한 커뮤니티 활동입니다.

MASVS는 커뮤니티 활동과 업계 피드백의 성과입니다. 우리는 이 표준이 시간이 지남에 따라 발전하는 것을 기대하고 있으며, 커뮤니티의 피드백을 환영합니다.

우리와 연락하는 가장 좋은 방법은 OWASP Mobile Project Slack 채널을 이용하는 것입니다: <https://owasp.slack.com/messages/project-mobile_omtg/details/>

계정은 다음의 URL에서 만들 수 있습니다: [https://owasp.slack.com/join/shared_invite/zt-g398htpy-AZ40HOM1WUOZguJKbblqkw#/](https://owasp.slack.com/join/shared_invite/zt-g398htpy-AZ40HOM1WUOZguJKbblqkw#/)

## 저작권 및 라이센스

[<img src="images/CC-license.png" title="License" width="200px" height="45px" />](https://creativecommons.org/licenses/by-sa/4.0/)

Copyright © 2020 The OWASP Foundation. 본 저작물은 [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/)를 따릅니다. 재사용 또는 배포를 위해 본 저작물의 라이센스 조건을 다른 사람에게 명확하게 제시해야합니다.

<!-- \pagebreak -->

## 감사의 말

| 프로젝트 리더 | 책임 저자 | 공동저자 및 검토자
| ------- | --- | ----------------- |
| Sven Schleier, Jeroen Willemsen and Carlos Holguera | Bernhard Mueller | Alexander Antukh, Mesheryakov Aleksey, Bachevsky Artem, Jeroen Beckers, Vladislav Chelnokov, Ben Cheney, Peter Chi, Lex Chien, Stephen Corbiaux, Manuel Delgado, Ratchenko Denis, Ryan Dewhurst, Tereshin Dmitry, Christian Dong, Oprya Egor, Ben Gardiner, Rocco Gränitz, Henry Hu, Sjoerd Langkemper, Vinícius Henrique Marangoni, Martin Marsicano, Roberto Martelloni, Gall Maxim, Eugen Martynov, Riotaro Okada, Abhinav Sejpal, Stefaan Seys, Yogesh Sharma, Prabhant Singh, Sven Schleier, Nikhil Soni, Anant Shrivastava, Francesco Stillavato, Romuald Szkudlarek, Abderrahmane Aftahi, Abdessamad Temmar, Koki Takeyama, Chelnokov Vladislav, Leo Wang |

<br/>

| 언어 | 번역자 및 검토자 |
| --- | ------------------------------ |
| 중국어 전통 | Peter Chi, and Lex Chien, Henry Hu, Leo Wang |
| 중국어 간체 | Bob Peng, Harold Zang, Jack S |
| 프랑스어 | Romuald Szkudlarek, Abderrahmane Aftahi, Christian Dong (Review) |
| 독일어 | Rocco Gränitz, Sven Schleier (Review) |
| 스페인어 | Martin Marsicano, Carlos Holguera |
| 일본어 | Koki Takeyama, Riotaro Okada (Review) |
| 러시어아 | Gall Maxim, Eugen Martynov, Chelnokov Vladislav (Review), Oprya Egor (Review), Tereshin Dmitry (Review) |
| 힌디 어 | Mukesh Sharma, Ritesh Kumar, Atul Kunwar, Parag Dave, Devendra Kumar Sinha, Vikrant Shah |
| 한국어 | Youngjae Jeon, Jeongwon Cho, Jiyou Han, Jiyeon Sung |

본 문서는 Jim Manico가 작성한 OWASP 애플리케이션 보안 검증 표준의 포크로 시작되었습니다.

## 스폰서

MASVS와 MSTG는 모두 커뮤니티에서 자발적으로 생성되고 유지되지만, 때때로 약간의 외부 도움이 필요합니다. 따라서 기술 편집자를 고용할 수 있도록 자금을 기부해 주신 스폰서들에게 감사드립니다. 그들의 후원은 어떤식으로든 MASVS 또는 MSTG의 내용에 영향을 미치지 않는다는 점을 알려드립니다. 스폰서 패키지는 [OWASP Project Wiki](https://owasp.org/www-project-mobile-security-testing-guide/#div-sponsorship "OWASP Mobile Security Testing Guide Sponsorship Packages")에 설명되어 있습니다..

### 명예 후원자

[<img src="images/NowSecure_logo.png" title="NowSecure" width="200px" height="58px" />](https://www.nowsecure.com/ "NowSecure")

### 자선 후원자

[<img src="images/Randorisec_logo.png" title="Randorisec" width="200px" height="58px" />](https://www.randorisec.fr/ "RandoriSec")

다음으로 우리는 OWASP Bay Area Chapter의 후원에 감사의 말씀을 전합니다. 마지막으로 Leanpub에서 이 책을 구입하여 후원해 주신 모든 분들께 감사드립니다.
