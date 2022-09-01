# V5: 네트워크 통신 요구사항

## 통제 목표

이 장에서 다루는 통제의 목적은 모바일 앱과 원격 서비스 엔드 포인트 간에 교환되는 정보의 기밀성과 무결성을 보장하기 위한 것입니다. 최소한 모바일 앱은 적절한 설정을 적용한 TLS 프로토콜을 사용하여 네트워크 통신을 위한 암호화된 보안 채널을 제공해야 합니다. 레벨 2에는 SSL 피닝과 같은 심층 방어 조치가 추가되어 있습니다.

## 보안 검증 요구사항

| # | MSTG-ID | 설명 | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **5.1** | MSTG-NETWORK-1 | 데이터는 TLS를 사용하여 네트워크에서 암호화되어야 한다. 보안 채널은 앱 전체에 일관되게 사용하여야 한다. | x | x |
| **5.2** | MSTG-NETWORK-2 | TLS 설정은 현재 모범 사례와 일치하여야 하며, 모바일 운영 체제가 권장 표준을 지원하지 않는 경우 가능한 한 가장 가까운 모범 사례와 일치하여야 한다. | x | x |
| **5.3** | MSTG-NETWORK-3 | 보안 채널이 설정되면 앱은 원격 앤드 포인트의 X.509 인증서를 검증하여야 한다. 신뢰할 수 있는 CA가 서명한 인증서만 허용하여야 한다. | x | x |
| **5.4** | MSTG-NETWORK-4 | 앱은 자체 인증서 저장소를 사용하거나 앤드 포인트 인증서 또는 공개 키를 피닝하여야 한다. 그 후 신뢰할 수 있는 CA가 서명한 경우에도 다른 인증서 또는 키를 제공하는 앤드 포인트와의 연결을 거부할 수 있어야 한다. |   | x |
| **5.5** | MSTG-NETWORK-5 | 앱은 등록 및 계정 복구와 같은 중요한 작업을 처리할 때 안전하지 않은 단일 통신 채널(이메일 또는 SMS)에 의존하지 않아야 한다. |  | x |
| **5.6** | MSTG-NETWORK-6 | 앱은 최신 연결 라이브러리 및 보안 라이브러리에만 의존하여야 한다. |  | x |

## 참고

OWASP 모바일 보안 테스트 안내서(MASTG)는 이 섹션에 나열된 요구사항을 확인하기 위한 자세한 지침을 제공합니다.

- General: 네트워크 통신 테스트 - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x04f-Testing-Network-Communication.md>
- Android: 네트워크 통신 테스트 - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x05g-Testing-Network-Communication.md>
- iOS: 네트워크 통신 테스트 - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x06g-Testing-Network-Communication.md>

자세한 내용은 다음을 참조하십시오:

- OWASP Mobile Top 10: M3 (Insecure Communication) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m3-insecure-communication>
- CWE 295 (Improper Certificate Validation) - <https://cwe.mitre.org/data/definitions/295.html>
- CWE 296 (Improper Following of a Certificate's Chain of Trust) - <https://cwe.mitre.org/data/definitions/296.html>
- CWE 297 (Improper Validation of Certificate with Host Mismatch) - <https://cwe.mitre.org/data/definitions/297.html>
- CWE 298 (Improper Validation of Certificate Expiration) - <https://cwe.mitre.org/data/definitions/298.html>
- CWE 308 (Use of Single-factor Authentication) - <https://cwe.mitre.org/data/definitions/308.html>
- CWE 319 (Cleartext Transmission of Sensitive Information) - <https://cwe.mitre.org/data/definitions/319.html>
- CWE 326 (Inadequate Encryption Strength) - <https://cwe.mitre.org/data/definitions/326.html>
- CWE 327 (Use of a Broken or Risky Cryptographic Algorithm) - <https://cwe.mitre.org/data/definitions/327.html>
- CWE 780 (Use of RSA Algorithm without OAEP) - <https://cwe.mitre.org/data/definitions/780.html>
- CWE 940 (Improper Verification of Source of a Communication Channel) - <https://cwe.mitre.org/data/definitions/940.html>
- CWE 941 (Incorrectly Specified Destination in a Communication Channel) - <https://cwe.mitre.org/data/definitions/941.html>
