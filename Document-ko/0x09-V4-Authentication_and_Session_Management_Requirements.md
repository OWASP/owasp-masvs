# V4: 인증 및 세션 관리 요구사항

## 통제 목표

대부분의 경우 원격 서비스에 로그인하는 사용자는 전체 모바일 앱 아키텍처에서 필수적인 부분입니다. 대부분의 로직이 엔드포인트에서 발생하더라도 MASVS는 사용자 계정 및 세션을 관리하는 방법에 대한 몇 가지 기본 요구사항을 정의하고 있습니다.

## 보안 검증 요구사항

| # | MSTG-ID | 설명 | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **4.1** | MSTG-AUTH-1 | 앱이 사용자에게 원격 서비스에 대한 액세스를 제공하는 경우 사용자 이름과 암호로의 인증 방식은 원격 엔드 포인트에서 수행되어야 한다. | x | x |
| **4.2** | MSTG-AUTH-2 | 상태 저장 세션 관리를 사용하는 경우 원격 엔드 포인트는 무작위로 생성된 세션 식별자를 사용하여 사용자의 자격 증명을 보내지 않고 클라이언트 요청을 인증하여야 한다. | x | x |
| **4.3** | MSTG-AUTH-3 | 상태 비 저장 토큰 기반 인증을 사용하는 경우 서버는 보안 알고리즘을 사용하여 서명된 토큰을 제공하여야 한다. | x | x |
| **4.4** | MSTG-AUTH-4 | 사용자가 로그아웃하면 원격 엔드 포인트는 기존의 세션을 종료하여야 한다. | x | x |
| **4.5** | MSTG-AUTH-5 | 비밀번호 정책이 존재하며 원격 엔드 포인트에서 검증되어야 한다. | x | x |
| **4.6** | MSTG-AUTH-6 | 원격 엔드 포인트는 과도한 인증 시도에 대한 보호 메커니즘을 구현하여야 한다. | x | x |
| **4.7** | MSTG-AUTH-7 | 사전 정의 된 비 활동 기간 및 액세스 토큰이 만료 된 후 원격 엔드 포인트에서 세션이 무효화되어야 한다. | x | x |
| **4.8** | MSTG-AUTH-8 | 생체 인식 인증이 사용되는 경우 이벤트 바인딩(예: 단순히 "true"또는 "false"를 반환하는 API 사용) 되어서는 안된다. 대신 키 체인 및 키 스토어 잠금 해제를 할 때만 사용하여야 한다. | | x |
| **4.9** | MSTG-AUTH-9 | 2단계 인증 요소는 원격 엔드 포인트에 존재하여야 하며, 2FA 요구 사항이 지속적으로 적용되어야 한다.  | | x |
| **4.10** | MSTG-AUTH-10 | 민감한 트랜잭션에는 단계별 인증을 적용하여야 한다. | | x |
| **4.11** | MSTG-AUTH-11 | 앱은 사용자에게 사용자 계정의 모든 민감한 활동을 알려야 한다. 사용자는 장치 목록을 보거나, 상태 정보(IP 주소, 위치 등)를 보고 특정 장치를 차단할 수 있어야 한다. | | x |
| **4.12** | MSTG-AUTH-12 | 인증 모델은 원격 엔드포인트에서 정의되고 시행되어야 한다. | x | x |

## 참고

OWASP 모바일 보안 테스트 안내서(MASTG)는 이 섹션에 나열된 요구사항을 확인하기 위한 자세한 지침을 제공합니다.

- General: Authentication and Session Management - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x04e-Testing-Authentication-and-Session-Management.md>
- Android: Testing Local Authentication - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x05f-Testing-Local-Authentication.md>
- iOS: Testing Local Authentication - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x06f-Testing-Local-Authentication.md>

자세한 내용은 다음을 참조하십시오:

- OWASP Mobile Top 10: M4 (Insecure Authentication) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m4-insecure-authentication>
- OWASP Mobile Top 10: M6 (Insecure Authorization) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m6-insecure-authorization>
- CWE 287 (Improper Authentication) - <https://cwe.mitre.org/data/definitions/287.html>
- CWE 307 (Improper Restriction of Excessive Authentication Attempts) - <https://cwe.mitre.org/data/definitions/307.html>
- CWE 308 (Use of Single-factor Authentication) - <https://cwe.mitre.org/data/definitions/308.html>
- CWE 521 (Weak Password Requirements) - <https://cwe.mitre.org/data/definitions/521.html>
- CWE 604 (Use of Client-Side Authentication) - <https://cwe.mitre.org/data/definitions/604.html>
- CWE 613 (Insufficient Session Expiration) - <https://cwe.mitre.org/data/definitions/613.html>
