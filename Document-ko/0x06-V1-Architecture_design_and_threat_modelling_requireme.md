# V1: 아키텍처, 디자인 및 위협 모델링 요구사항

## 통제 목표

이상적인 세계에서는 모든 개발 단계에서 보안이 고려될 것입니다. 그러나 실제로 보안은 SDLC의 마지막 단계에서만 고려되는 경우가 많습니다. 기술적인 통제 외에도, MASVS는 모바일 앱의 아키텍처를 계획할 때 보안이 명시적으로 해결되었는지 확인하고, 모든 구성 요소의 기능 및 보안 역할이 명확하다는 것을 보장하는 프로세스를 갖추는 것을 요구합니다. 대부분의 모바일 앱은 원격 서비스 클라이언트로 동작하기 때문에 해당 서비스에도 적절한 보안 기준을 적용해야 합니다. - 모바일 앱을 단독으로 테스트하는 것만으로는 충분하지 않습니다.

"V1" 카테고리에는 앱의 아키텍처와 디자인에 관련된 요구사항이 나열되어 있습니다. 따라서, OWASP 모바일 테스트 가이드의 기술 테스트 사례에 매핑되지 않는 카테고리는 이 카테고리가 유일합니다. 위협 모델링, 보안 SDLC, 키 관리와 같은 주제를 다루기 위해 MASVS 사용자는 각 OWASP 프로젝트 또는 아래에 링크된 것과 같은 다른 표준을 참조해야 합니다.

## 보안 검증 요구사항

MASVS-L1 및 MASVS-L2의 요구사항은 다음과 같습니다.

| # | MSTG-ID | 설명 | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **1.1** | MSTG-ARCH-1 | 모든 앱 구성 요소가 필요한 것으로 식별되어야 한다. | x | x |
| **1.2** | MSTG-ARCH-2 | 보안 통제는 클라이언트측에서만 적용되는 것이 아니라 각각의 원격 엔드 포인트에서도 적용되어야 한다. | x | x |
| **1.3** | MSTG-ARCH-3 | 모바일 앱과 연결되는 모든 원격 서비스에 수준 높은 아키텍처가 정의되어야 하고 해당 아키텍처에서 보안이 지원되어야 한다. | x | x |
| **1.4** | MSTG-ARCH-4 | 모바일 앱의 컨텍스트에서 민감한 것으로 간주되는 데이터가 명확하게 식별되어야 한다. | x | x |
| **1.5** | MSTG-ARCH-5 | 모든 앱 구성 요소는 비즈니스 기능과 보안 기능이 적용되어야 한다. |  | x |
| **1.6** | MSTG-ARCH-6 | 모바일 앱과 연관된 원격 서비스의 위협 모델을 만들어 잠재적인 위협에 대한 대책을 적용하여야 한다. |  | x |
| **1.7** | MSTG-ARCH-7 | 모든 보안 통제는 중앙 집중식으로 구현되어야 한다. |  | x |
| **1.8** | MSTG-ARCH-8 | 암호화 키(있는 경우)를 관리하는 방법에 대한 명시적인 정책이 있으며 암호화 키의 수명주기가 적용되어야 한다. (NIST SP 800-57 등과 같은 키 관리 표준을 준수하는 것이 좋음) |  | x |
| **1.9** | MSTG-ARCH-9 | 모바일 앱의 업데이트를 강제화하는 메커니즘이 존재하여야 하다. |  | x |
| **1.10** | MSTG-ARCH-10 | 소프트웨어 개발 수명주기의 모든 부분에서 보안을 적용하여야 한다. |  | x |
| **1.11** | MSTG-ARCH-11 | 책임 있는 공개 정책이 시행되고 있으며 효과적으로 적용되어야 한다. |  | x |
| **1.12** | MSTG-ARCH-12 | 앱은 개인정보 보호법 및 규정을 준수해야 한다. | x | x |

## 참고

자세한 내용은 다음을 참조하십시오:

- OWASP Mobile Top 10: M10 (Extraneous Functionality) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m10-extraneous-functionality>
- OWASP Threat modelling - <https://owasp.org/www-community/Application_Threat_Modeling>
- OWASP Secure SDLC Cheat Sheet - <https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets_excluded/Secure_SDLC_Cheat_Sheet.md>
- Microsoft SDL - <https://www.microsoft.com/en-us/sdl/>
- NIST SP 800-57 - <https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final>
- security.txt - <https://securitytxt.org/>
