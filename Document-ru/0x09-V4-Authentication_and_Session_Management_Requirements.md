# V4: Требования к аутентификации и управлению сессиями

## Цель верификации

В большинстве случаев авторизация в удаленных сервисах являются неотъемлемой частью общей архитектуры мобильного приложения. Несмотря на то, что большая часть логики происходит на бекэнде, MASVS определяет некоторые основные требования, касающиеся управления учетными записями пользователей и сессиями.

## Требования безопасности

| # | MSTG-ID | Описание | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **4.1** | MSTG-AUTH-1 | Если приложение предоставляет пользователям доступ к удалённым сервисам, на бэкенде должна быть реализована аутентификация, например, по логину и паролю. | ✓ | ✓ |
| **4.2** | MSTG-AUTH-2 | Если используются сессии, бекэнд случайно генерирует идентификаторы сессии для аутентификации клиентских запросов без отправки данных учётной записи.  | ✓ | ✓ |
| **4.3** | MSTG-AUTH-3 | Если используется аутентификация на основе токена, сервер предоставляет токен, подписанный с использованием безопасного криптоалгоритма. | ✓ | ✓ |
| **4.4** | MSTG-AUTH-4 | Бэкенд удаляет существующую сессию, когда пользователь выходит из системы. | ✓ | ✓ |
| **4.5** | MSTG-AUTH-5 | На сервере реализована парольная политика. | ✓ | ✓ |
| **4.6** | MSTG-AUTH-6 | На сервере реализован механизм защиты от перебора авторизационных данных. | ✓ | ✓ |
| **4.7** | MSTG-AUTH-7 | Биометрическая аутентификация не является event-bound (т.е. использует только API, которое возвращает «true» или «false»). Вместо этого она основана на разблокировке keychain/keystore. |   | ✓ |
| **4.8** | MSTG-AUTH-8 | Сессии становятся невалидными на бэкенде после определенного периода бездействия, срок действия токена истекает. | ✓ | ✓ |
| **4.9** | MSTG-AUTH-9 | Реализована и поддерживается двухфакторная аутентификация.  |   | ✓ |
| **4.10** | MSTG-AUTH-10 | Для выполнения чувствительных транзакций требуется дополнительная или повторная аутентификацию.  |   | ✓ |
| **4.11** | MSTG-AUTH-11 | Приложение информирует пользователя о всех важных действиях с их учетной записью. Пользователи могут просматривать список устройств, просматривать контекстную информацию (IP-адрес, местоположение и т.д.), и блокировать конкретные устройства. |  | ✓ |
| **4.12** | MSTG-AUTH-12 | Модели авторизации должны быть определены и проверенны на сервере. | ✓ | ✓ |

## Ссылки

OWASP MSTG содержит подробные инструкции по верификации требований, перечисленных в этом разделе.

- Общее: Аутентификация и управление сессиями - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04e-Testing-Authentication-and-Session-Management.md>
- Android: Тестирование локальной аутентификации - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05f-Testing-Local-Authentication.md>
- iOS: Тестирование локальной аутентификации - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06f-Testing-Local-Authentication.md>

Для получения дополнительной информации смотрите также:

- OWASP Mobile Top 10: M4 (Insecure Authentication) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m4-insecure-authentication>
- OWASP Mobile Top 10: M6 (Insecure Authorization) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m6-insecure-authorization>
- CWE 287 (Improper Authentication) - <https://cwe.mitre.org/data/definitions/287.html>
- CWE 307 (Improper Restriction of Excessive Authentication Attempts) - <https://cwe.mitre.org/data/definitions/307.html>
- CWE 308 (Use of Single-factor Authentication) - <https://cwe.mitre.org/data/definitions/308.html>
- CWE 521 (Weak Password Requirements) - <https://cwe.mitre.org/data/definitions/521.html>
- CWE 604 (Use of Client-Side Authentication) - <https://cwe.mitre.org/data/definitions/604.html>
- CWE 613 (Insufficient Session Expiration) - <https://cwe.mitre.org/data/definitions/613.html>
