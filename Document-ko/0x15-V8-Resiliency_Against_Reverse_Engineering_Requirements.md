# V8: 복원력 요구사항

## 통제 목표

이 섹션에서는 민감한 데이터 또는 기능을 처리하거나 액세스하는 앱에 권장되는 심층 방어 조치에 대해 설명합니다. 이러한 통제를 적용하지 않더라도 취약점이 발생하지는 않습니다. 대신 리버스 엔지니어링 및 특정 클라이언트측 공격에 대한 앱의 복원력을 향상 시키기 위한 것입니다.

이 섹션의 통제는 앱의 무단 변조 또는 코드 리버스 엔지니어링으로 인한 위험 평가를 기반으로 필요에 따라 적용하여야 합니다. 비즈니스 위험 및 관련 기술 위협에 대해서는 OWASP 문서 "Technical Risks of Reverse Engineering and Unauthorized Code Modification Reverse Engineering and Code Modification Prevention"(아래 자료 참조)를 참조하십시오.

아래 목록의 모든 통제가 효과적이기 위해서는 앱이 최소한 MASVS-L1을 충족해야 합니다.(즉, 견고한 보안 통제가 있어야 함). 뿐만 아니라 V8의 모든 하위 사항들이 요구됩니다. 예를 들어, "이해 방해"에 나열된 난독화 통제는 "동적 분석 및 변조 방지" 및 "장치 바인딩"과 결합되어야 합니다.

**메모 : 해당 소프트웨어 보호 기능을 보안 통제 대신 사용해서는 안됩니다. MASVR-R에 나열된 통제는 MASVS 보안 요구사항을 충족하는 앱에 위협별 보호 통제를 추가하기 위한 것입니다.**

다음과 같은 고려 사항이 적용됩니다:

1. 위협 모델은 방어하는 클라이언트측 위협을 명확하게 정의해야 합니다. 또한 체계가 제공하는 보호 등급을 지정해야 합니다. 예를 들어, 악성코드 작성자가 앱을 분석하는데 수동 리버스 엔지니어링에 상당한 노력을 투자하도록 만드는 것이 목표일 수 있습니다.

2. 위협 모델은 민감해야 합니다. 예를 들어, 공격자가 화이트박스 전체를 단순히 코드 리프팅 할 수 있다면 화이트박스 구현에서 암호화 키를 숨기는 것이 중요합니다.

3. 보호의 효과는 사용된 특정 유형의 변조 방지 및 난독화를 테스트한 경험이 있는 전문가가 항상 검증해야 합니다.(모바일 보안 테스트 가이드(MASTG)의 "리버스 엔지니어링" 및 "소프트웨어 보호 평가" 부분을 참조하십시오.)

### 동적 분석 및 변조 방지

| # | MSTG-ID | 설명 | R |
| -- | ----------- | ---------------------- | - |
| **8.1** | MSTG-RESILIENCE-1 | 앱은 사용자에게 경고하거나 앱을 종료하여 루팅 또는 탈옥 된 기기의 존재를 감지하여야 한다. | x |
| **8.2** | MSTG-RESILIENCE-2 | 앱은 디버깅을 방지하거나 디버거 연결을 감지하여야 한다. 사용 가능한 모든 디버깅 프로토콜이 포함되어야 한다. | x |
| **8.3** | MSTG-RESILIENCE-3 | 앱은 자체 샌드박스에서 실행 파일 및 중요한 데이터의 변조를 감지하여야 한다. | x |
| **8.4** | MSTG-RESILIENCE-4 | 앱은 장치에 널리 사용되는 리버스 엔지니어링 도구 및 프레임워크의 존재를 감지하여야 한다. | x |
| **8.5** | MSTG-RESILIENCE-5 | 앱은 에뮬레이터에서 실행되고 있는지 여부를 감지하고 대응하여야 한다. | x |
| **8.6** | MSTG-RESILIENCE-6 | 앱은 자체 메모리 공간에서 코드와 데이터 변조를 감지하여야 한다. | x |
| **8.7** | MSTG-RESILIENCE-7 | 앱은 각 방어 유형(8.1~8.6)에서 여러 메커니즘을 구현하여야 한다. 복원력은 사용된 메커니즘의 독창성의 양 및 다양성과 비례합니다. | x |
| **8.8** | MSTG-RESILIENCE-8 | 감지 메커니즘은 지연 응답과 스텔스 응답을 포함하여 다양한 종류 응답을 트리거하여야 한다. | x |
| **8.9** | MSTG-RESILIENCE-9 | 프로그램 난독화가 적용되고, 동적 분석을 통한 역 난독처리를 방해하여야 한다.  | x |

### 장치 바인딩

| # | MSTG-ID | 설명 | R |
| -- | ----------- | ---------------------- | - |
| **8.10** | MSTG-RESILIENCE-10 | 앱은 장치 고유의 여러 속성에서 파생되는 장치 지문을 사용하여 '장치 바인딩' 기능을 구현하여야 한다. | x |

### 이해 방해(Impede Comprehension)

| # | MSTG-ID | 설명 | R |
| -- | ----------- | ---------------------- | - |
| **8.11** | MSTG-RESILIENCE-11 | 앱에 속하는 모든 실행 파일 및 라이브러리는 파일 수준에서 암호화되거나 실행 파일 내의 중요한 코드 및 데이터 세그먼트가 암호화되거나 압축되어야 한다. 간단한 정적 분석은 중요한 코드나 데이터가 노출되지 않아야 한다. | x |
| **8.12** | MSTG-RESILIENCE-12 | 난독화의 목표가 민감한 계산을 보호하는 것이라면, 현재 공개된 연구를 고려하여 특정 작업에 적합하고 수동 및 자동화된 역 난독화 방법에 대해 강력한 난독화 체계가 사용되어야 한다. 난독화의 효과는 수동 테스트를 통해 검할 필요가 있다. 하드웨어 기반 격리 기능이 난독화 처리보다 우선시 된다. | x |

### 도청 방해(Impede Eavesdropping)

| # | MSTG-ID | 설명 | R |
| -- | ----------- | ---------------------- | - |
| **8.13** | MSTG-RESILIENCE-13 | 심층 방어로서, 통신 당사자를 확실하게 강화하는 것 외에도, 애플리케이션 레벨 페이로드 암호화를 적용하여 도청을 더욱 방해할 수 있다. | x |

## 참고

OWASP 모바일 보안 테스트 안내서(MASTG)는 이 섹션에 나열된 요구사항을 확인하기 위한 자세한 지침을 제공합니다.

- Android: 리버스 엔지니어링에 대한 복원력 테스트 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05j-Testing-Resiliency-Against-Reverse-Engineering.md>
- iOS: 리버스 엔지니어링에 대한 복원력 테스트 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06j-Testing-Resiliency-Against-Reverse-Engineering.md>

자세한 내용은 다음을 참조하십시오:

- OWASP Mobile Top 10: M8 (Code Tampering) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m8-code-tampering>
- OWASP Mobile Top 10: M9 (Reverse Engineering) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m9-reverse-engineering>
- OWASP Reverse Engineering Threats - <https://wiki.owasp.org/index.php/Technical_Risks_of_Reverse_Engineering_and_Unauthorized_Code_Modification>
- OWASP Reverse Engineering and Code Modification Prevention - <https://wiki.owasp.org/index.php/OWASP_Reverse_Engineering_and_Code_Modification_Prevention_Project>
