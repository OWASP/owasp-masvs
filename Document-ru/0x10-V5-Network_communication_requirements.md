# V5: Требования к сетевому взаимодействию

## Цель верификации

Целью требований, перечисленных в этом разделе, является обеспечение конфиденциальности и целостности информации, передаваемой между мобильным приложением и сервером. Как минимум в мобильном приложении должен быть настроен безопасный шифрованный канал передачи данных с использованием протокола TLS с соответствующими настройками. L2 содержит меры усиленной защиты, такие, как SSL pinning.

## Требования безопасности

| # | MSTG-ID | Описание | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **5.1** | MSTG-NETWORK-1 | Данные, передаваемые по сети, шифруются с использованием TLS. Безопасный канал используется для всех сервисов приложения. | x | x |
| **5.2** | MSTG-NETWORK-2 | Настройки TLS соответствуют современным лучшим практикам, или максимально приближены к ним, если операционная система не поддерживает рекомендуемые стандарты. | x | x |
| **5.3** | MSTG-NETWORK-3 | Приложение верифицирует X.509 сертификаты сервера во время установления защищённого канала. Принимаются только сертификаты, подписанные доверенным удостоверяющим центром (CA). | x | x |
| **5.4** | MSTG-NETWORK-4 | В приложении реализован SSL pinning и соединение с серверами, которые предлагают другой сертификат или ключ, даже если они подписаны доверенным центром сертификации (CA) не устанавливается. |   | x |
| **5.5** | MSTG-NETWORK-5 | Приложение не полагается на единственный небезопасный канал связи (e-mail или SMS) для таких критических операций, как регистрация и восстановление аккаунта. |  | x |
| **5.6** | MSTG-NETWORK-6 | Приложение использует только актуальные версии библиотек для подключения к сети и обеспечения безопасного соединения. |  | x |

## Ссылки

OWASP MSTG содержит подробные инструкции по верификации требований, перечисленных в этом разделе.

- Общее: Тестирование сетевого взаимодействия - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04f-Testing-Network-Communication.md>
- Android: Тестирование сетевого взаимодействия - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05g-Testing-Network-Communication.md>
- iOS: Тестирование сетевого взаимодействия - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06g-Testing-Network-Communication.md>

Для получения дополнительной информации смотрите также:

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
