# V3: 암호화 요구사항

## 통제 목표

암호화는 모바일 장치에 저장된 데이터를 보호하는데 필수적인 요소입니다. 또한 표준 규칙을 따르지 않을 때 상황이 끔찍하게 잘못될 수 있는 영역이기도 합니다. 이 장의 통제 목적은 검증된 애플리케이션이 다음과 같은 업계 모범 사례에 따라 암호화를 사용하는지 확인하는 것입니다.

- 검증된 암호화 라이브러리 사용
- 암호화 기본 요소의 올바른 선택 및 구성
- 무작위 값이 필요한 경우 적절한 난수 발생기 사용

## 보안 검증 요구사항

| # | MSTG-ID | 설명 | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **3.1** | MSTG-CRYPTO-1 | 앱은 암호화의 유일한 방법으로 하드 코드 된 키를 사용하는 암호화에 의존하지 않아야 한다. | x | x |
| **3.2** | MSTG-CRYPTO-2 | 앱은 검증된 암호화 알고리즘으로 구현하여야 한다. | x | x |
| **3.3** | MSTG-CRYPTO-3 | 앱은 업계 모범 사례를 준수하는 매개 변수로 구성된 특정 유스케이스에 적합한 암호화 알고리즘을 사용하여야 한다. | x | x |
| **3.4** | MSTG-CRYPTO-4 | 앱은 보안적인 목적으로 더 이상 사용되지 않고 사라질 암호화 프로토콜과 알고리즘을 사용하지 않아야 한다. | x | x |
| **3.5** | MSTG-CRYPTO-5 | 앱은 여러 목적으로 동일한 암호화 키를 재사용하지 않아야 한다. | x | x |
| **3.6** | MSTG-CRYPTO-6 | 모든 난수 값은 충분히 안전한 난수 생성기를 사용하여 생성하여야 한다. | x | x |

## 참고

OWASP 모바일 보안 테스트 안내서(MSTG)는 이 섹션에 나열된 요구사항을 확인하기 위한 자세한 지침을 제공합니다.

- Android: 암호화 테스트 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05e-Testing-Cryptography.md>
- iOS: 암호화 테스트 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06e-Testing-Cryptography.md>

자세한 내용은 다음을 참조하십시오:

- OWASP Mobile Top 10: M5 (Insufficient Cryptography) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m5-insufficient-cryptography>
- CWE 310 (Cryptographic Issues) - <https://cwe.mitre.org/data/definitions/310.html>
- CWE 321 (Use of Hard-coded Cryptographic Key) - <https://cwe.mitre.org/data/definitions/321.html>
- CWE 326 (Inadequate Encryption Strength) - <https://cwe.mitre.org/data/definitions/326.html>
- CWE 327 (Use of a Broken or Risky Cryptographic Algorithm) - <https://cwe.mitre.org/data/definitions/327.html>
- CWE 329 (Not Using a Random IV with CBC Mode) - <https://cwe.mitre.org/data/definitions/329.html>
- CWE 330 (Use of Insufficiently Random Values) - <https://cwe.mitre.org/data/definitions/330.html>
- CWE 337 (Predictable Seed in PRNG) - <https://cwe.mitre.org/data/definitions/337.html>
- CWE 338 (Use of Cryptographically Weak Pseudo Random Number Generator (PRNG)) - <https://cwe.mitre.org/data/definitions/338.html>
