# V2: 데이터 저장 및 개인 정보 요구사항

## 통제 목표

사용자 자격 증명 및 개인 정보와 같은 민감한 데이터를 보호하는 것이 모바일 보안의 핵심 초점입니다. 먼저, IPC와 같은 운영체제 메커니즘을 부적절하게 사용하게 되면 민감한 데이터가 의도하지 않게 동일한 장치에서 실행되는 다른 앱에 노출될 수 있습니다. 또한 데이터가 실수로 클라우드 저장소, 백업 또는 키보드 캐시로 유출될 수 있습니다. 또한 모바일 기기는 다른 유형의 기기에 비해 더 쉽게 분실하거나 도난당할 수 있으므로 공격자가 물리적으로 접근하기에 더 용이한 시나리오가 될 수 있습니다. 이 경우 민감한 데이터의 취득을 더 어렵게하기 위해 추가적인 보호대책이 필요합니다.

주의 : MASVS는 앱 중심이므로 MDM 솔루션에 의해 시행되는 것과 같은 장치 수준 정책은 다루지 않습니다. 우리는 기업적 측면에에서 데이터 보안을 보다 강화하기 위해 이러한 정책을 사용하는 것을 권장합니다.

### 민감한 데이터의 정의

MASVS의 민감한 데이터는 사용자 자격 증명과 특정 상황에서 민감한 것으로 간주되는 기타 모든 데이터를 포함합니다.

- 신분 도용에 악용될 수 있는 개인 식별 정보(PII): 사회보장번호(주민등록번호), 신용카드 번호, 은행 계좌번호, 건강 정보
- 유출될 경우 명예 실추 및 금전적 손실로 이어질 민감한 데이터: 계약 정보, 비공개 계약에 포함된 정보, 관리 정보
- 법률 또는 컴플라이언스 이유로 보호되어야 하는 모든 데이터.

## 보안 검증 요구사항

대부분의 데이터 공개의 문제는 아래의 간단한 규칙을 따르면 예방할 수 있습니다. 이 장에 나열된 대부분의 통제는 모든 검증 수준에서 필수 사항입니다.

| # | MSTG-ID | 설명 | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **2.1** | MSTG-STORAGE-1 | 개인 식별 정보(PII), 사용자 자격 증명 암호화 키 같은 중요한 데이터를 저장할 경우 시스템 자격 증명 저장소를 적절하게 사용하여야 한다. | x | x |
| **2.2** | MSTG-STORAGE-2 | 민감한 데이터는 앱 컨테이너 또는 시스템 자격 증명 저장 시설 외부에 저장하지 않아야 한다. | x | x |
| **2.3** | MSTG-STORAGE-3 | 민감한 데이터는 응용 프로그램 로그에 기록하지 않아야 한다. | x | x |
| **2.4** | MSTG-STORAGE-4 | 민감한 데이터는 아키텍처에서 필요한 부분이 아닌 한 제3자와 공유하지 않아야 한다. | x | x |
| **2.5** | MSTG-STORAGE-5 | 민감한 데이터를 처리하는 텍스트 입력에서 키보드 캐시가 비활성화 되어야 한다. | x | x |
| **2.6** | MSTG-STORAGE-6 | 민감한 데이터는 IPC 메커니즘을 통해 노출되지 않아야 한다. | x | x |
| **2.7** | MSTG-STORAGE-7 | 비밀번호 또는 핀과 같은 민감한 데이터는 사용자 인터페이스를 통해 노출되지 않아야 한다. | x | x |
| **2.8** | MSTG-STORAGE-8 | 민감한 데이터는 모바일 운영체제에서 생성된 백업에 포함되지 않아야 한다. |   | x |
| **2.9** | MSTG-STORAGE-9 | 민감한 데이터는 앱이 백그라운드로 이동할 때 뷰에서 제거되어야 한다. |  | x |
| **2.10** | MSTG-STORAGE-10 | 민감한 데이터는 앱이 필요한 것보다 더 긴 시간 동안 메모리에 유지되지 않아야 하며, 사용 후에는 메모리에서 명시적으로 삭제하여야 한다. |  | x |
| **2.11** | MSTG-STORAGE-11 | 앱은 사용자에게 장치 암호를 설정하도록 요구하는 것과 같은 최소한의 장치 액세스 보안 정책을 설정하도록 하여야 한다. |  | x |
| **2.12** | MSTG-STORAGE-12 | 앱은 처리되는 개인 식별 정보가 처리되는 방식과 사용자가 앱 사용시 준수해야하는 보안 모범 사례에 대해 통지하여야 한다. | x | x |
| **2.13** | MSTG-STORAGE-13 | 민감한 데이터는 모바일 장치 로컬에 저장해서는 안된다. 대신 필요한 경우 원격 엔드포인트에서 데이터를 검색하고 메모리에만 보관하여야 한다. |  | x |
| **2.14** | MSTG-STORAGE-14 | 민감한 데이터를 여전히 로컬에 저장해야하는 경우라면, 인증이 필요한 하드웨어 지원 저장소에서 파생된 키를 사용하여 암호화하여야 한다. |  | x |
| **2.15** | MSTG-STORAGE-15 | 과도한 인증 시도 실패 후에는 앱의 로컬 저장소를 지워야 한다. |  | x |

## 참고

OWASP 모바일 보안 테스트 안내서(MSTG)는 이 섹션에 나열된 요구사항을 확인하기 위한 자세한 지침을 제공합니다.

- Android: 데이터 저장소 테스트 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05d-Testing-Data-Storage.md>
- iOS: 데이터 저장소 테스트 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06d-Testing-Data-Storage.md>

자세한 내용은 다음을 참조하십시오:

- OWASP Mobile Top 10: M1 (Improper Platform Usage) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m1-improper-platform-usage>
- OWASP Mobile Top 10: M2 (Insecure Data Storage) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m2-insecure-data-storage>
- CWE 117 (Improper Output Neutralization for Logs) - <https://cwe.mitre.org/data/definitions/117.html>
- CWE 200 (Information Exposure) - <https://cwe.mitre.org/data/definitions/200.html>
- CWE 276 (Incorrect Default Permissions) - <https://cwe.mitre.org/data/definitions/276.html>
- CWE 311 (Missing Encryption of Sensitive Data) - <https://cwe.mitre.org/data/definitions/311.html>
- CWE 312 (Cleartext Storage of Sensitive Information) - <https://cwe.mitre.org/data/definitions/312.html>
- CWE 316 (Cleartext Storage of Sensitive Information in Memory) - <https://cwe.mitre.org/data/definitions/316.html>
- CWE 359 (Exposure of Private Information ('Privacy Violation')) - <https://cwe.mitre.org/data/definitions/359.html>
- CWE 522 (Insufficiently Protected Credentials) - <https://cwe.mitre.org/data/definitions/522.html>
- CWE 524 (Information Exposure Through Caching) - <https://cwe.mitre.org/data/definitions/524.html>
- CWE 530 (Exposure of Backup File to an Unauthorized Control Sphere) - <https://cwe.mitre.org/data/definitions/530.html>
- CWE 532 (Information Exposure Through Log Files) - <https://cwe.mitre.org/data/definitions/532.html>
- CWE 534 (Information Exposure Through Debug Log Files) - <https://cwe.mitre.org/data/definitions/534.html>
- CWE 634 (Weaknesses that Affect System Processes) - <https://cwe.mitre.org/data/definitions/634.html>
- CWE 798 (Use of Hard-coded Credentials) - <https://cwe.mitre.org/data/definitions/798.html>
- CWE 921 (Storage of Sensitive Data in a Mechanism without Access Control) - <https://cwe.mitre.org/data/definitions/921.html>
- CWE 922 (Insecure Storage of Sensitive Information) - <https://cwe.mitre.org/data/definitions/922.html>
