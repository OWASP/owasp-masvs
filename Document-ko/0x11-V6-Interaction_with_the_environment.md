# V6: 플랫폼 상호 작용 요구사항

## 통제 목표

이 그룹의 통제는 앱이 플랫폼 API와 표준 구성요소를 안전한 방식으로 사용한다는 것을 보장합니다. 또한, 이 통제에는 애플리케이션 간의 통신(IPC)을 포함합니다.

## 보안 검증 요구사항

| # | MSTG-ID | 설명 | L1 | L2 |
| -- | -------- | ---------------------- | - | - |
| **6.1** | MSTG-PLATFORM-1 | 앱은 필요한 최소한의 권한만 요구하여야 한다. | ✓ | ✓ |
| **6.2** | MSTG-PLATFORM-2 | 외부 소스 및 사용자의 모든 입력에 대해 검증하고 필요한 경우 적절하게 처리하여야 한다. 여기에는 UI를 통해 수신된 데이터, 인텐트, 사용자 정의 URL 및 네트워크 소스와 같은 IPC 메커니즘이 포함된다. | ✓ | ✓ |
| **6.3** | MSTG-PLATFORM-3 | 앱은 메커니즘이 제대로 보호되지 않는 한 사용자 정의 URL 체계를 통해 민감한 기능을 내보내지 않아야 한다. | ✓ | ✓ |
| **6.4** | MSTG-PLATFORM-4 | 엡은 메커니즘이 제대로 보호되지 않는 한 IPC 메터니즘을 통해 민감한 기능을 내보내지 않아야 한다. | ✓ | ✓ |
| **6.5** | MSTG-PLATFORM-5 | 명시적으로 필요한 경우가 아니면 웹뷰에서 자바스크립트를 사용하지 않아야 한다. | ✓ | ✓ |
| **6.6** | MSTG-PLATFORM-6 | 웹뷰는 필요 최소한의 프로토콜 핸들러 세트만 허용하도록 구성되어야 한다. (이상적으로는 https만 지원) file, tel 및 app-id와 같은 잠재적으로 위험한 핸들러는 비활성화하여야 한다. | ✓ | ✓ |
| **6.7** | MSTG-PLATFORM-7 | 앱의 네이티브 메소드가 웹뷰에 노출되는 경우 웹뷰가 앱 패키지에 포함된 자바스크립트만 렌더링하는지 검증하여야 한다. | ✓ | ✓ |
| **6.8** | MSTG-PLATFORM-8 | 객체 역직렬화는 안전한 직렬화 API를 사용하여 구현하여야 한다. | ✓ | ✓ |
| **6.9** | MSTG-PLATFORM-9 | 애플리케이션은 화면 오버레이 공격으로부터 자신을 보호하여야 한다. (Android 만 해당) |  | ✓ |
| **6.10** | MSTG-PLATFORM-10 | WebView를 종효하기 전에 WebView의 캐시, 스토리지 및 로드된 리소스(JavaScript 등)를 지워야 한다. |  | ✓ |
| **6.11** | MSTG-PLATFORM-11 | 민감한 데이터가 입력될 때마다 앱에서 사용자 지정 타사 키보드 사용을 방지하는지 확인하여야 한다. (iOS 만 해당) | | ✓ |

## 참고

OWASP 모바일 보안 테스트 안내서(MSTG)는 이 섹션에 나열된 요구사항을 확인하기 위한 자세한 지침을 제공합니다.

- Android: 플랫폼 상호 작용 테스트 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05h-Testing-Platform-Interaction.md>
- iOS: 플랫폼 상호 작용 테스트 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06h-Testing-Platform-Interaction.md>

자세한 내용은 다음을 참조하십시오:

- OWASP Mobile Top 10: M1 (Improper Platform Usage) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m1-improper-platform-usage>
- OWASP Mobile Top 10: M7 (Poor Code Quality) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m7-client-code-quality>
- CWE 20 (Improper Input Validation) - <https://cwe.mitre.org/data/definitions/20.html>
- CWE 79 (Improper Neutralization of Input During Web Page Generation) - <https://cwe.mitre.org/data/definitions/79.html>
- CWE 200 (Information Leak / Disclosure) - <https://cwe.mitre.org/data/definitions/200.html>
- CWE 250 (Execution with Unnecessary Privileges) - <https://cwe.mitre.org/data/definitions/250.html>
- CWE 672 (Operation on a Resource after Expiration or Release) - <https://cwe.mitre.org/data/definitions/672.html>
- CWE 749 (Exposed Dangerous Method or Function) - <https://cwe.mitre.org/data/definitions/749.html>
- CWE 772 (Missing Release of Resource after Effective Lifetime) - <https://cwe.mitre.org/data/definitions/772.html>
- CWE 920 (Improper Restriction of Power Consumption) - <https://cwe.mitre.org/data/definitions/920.html>
- CWE 925 (Improper Verification of Intent by Broadcast Receiver) - <https://cwe.mitre.org/data/definitions/925.html>
- CWE 926 (Improper Export of Android Application Components) - <https://cwe.mitre.org/data/definitions/926.html>
- CWE 927 (Use of Implicit Intent for Sensitive Communication) - <https://cwe.mitre.org/data/definitions/927.html>
- CWE 939 (Improper Authorization in Handler for Custom URL Scheme) - <https://cwe.mitre.org/data/definitions/939.html>
