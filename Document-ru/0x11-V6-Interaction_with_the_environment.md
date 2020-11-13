# V6: Требования к взаимодействию с операционной системой

## Цель верификации

Следование требованиям этого раздела обеспечивают безопасное использование API операционной системы. Дополнительно содержатся требования к межпроцессному взаимодействию (IPC).

## Требования безопасности

| # | MSTG-ID | Описание | L1 | L2 |
| -- | -------- | ---------------------- | - | - |
| **6.1** | MSTG-PLATFORM-1 | Приложение запрашивает минимально необходимый набор разрешений. | ✓ | ✓ |
| **6.2** | MSTG-PLATFORM-2 | Все данные, поступающие из внешних источников и от пользователя, валидируются и санитизируются. Сюда входят данные, полученные через пользовательский интерфейс, механизмы IPC (такие как intent-ы, кастомные URL-схемы) и из сети.| ✓ | ✓ |
| **6.3** | MSTG-PLATFORM-3 | Приложение не экспортирует чувствительные данные через кастомные URL-схемы, если эти механизмы не защищены должным образом. | ✓ | ✓ |
| **6.4** | MSTG-PLATFORM-4 | Приложение не экспортирует чувствительные данные через IPC механизмы без должной защиты. | ✓ | ✓ |
| **6.5** | MSTG-PLATFORM-5 | JavaScript отключен в компонентах WebView, если в нём нет необходимости. | ✓ | ✓ |
| **6.6** | MSTG-PLATFORM-6 | WebViews сконфигурирован с поддержкой минимального набора протоколов (в идеале только https). Поддержка потенциально опасных URL-схем (таких как: file, tel и app-id) отключена. | ✓ | ✓ |
| **6.7** | MSTG-PLATFORM-7 | Если нативные методы приложения используются WebView, верифицировать, что исполняются только Javascript объекты данного приложения. | ✓ | ✓ |
| **6.8** | MSTG-PLATFORM-8 | Десериализация объектов, если она есть, реализована с использованием безопасного API. | ✓ | ✓ |
| **6.9** | MSTG-PLATFORM-9 | Приложение защищает себя от атак наложения экрана. (Только для Андроид) |  | ✓ |
| **6.10** | MSTG-PLATFORM-10 | Кэш веб-представление, хранилище и загруженные ресурсы (JavaScript и т. д.) должены быть очищены до того, как веб-представление будет уничтожено. |  | ✓ |
| **6.11** | MSTG-PLATFORM-11 | Убедитесь, что приложение предотвращает использование пользовательских клавиатур сторонних производителей при вводе конфиденциальных данных. (Только для iOS) | | ✓ |

## Ссылки

OWASP MSTG содержит подробные инструкции по верификации требований, перечисленных в этом разделе.

- Android: Тестирование взаимодействия с платформой - [https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05h-Testing-Platform-Interaction.md](https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05h-Testing-Platform-Interaction.md)
- iOS: Тестирование взаимодействия с платформой - [https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06h-Testing-Platform-Interaction.md](https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06h-Testing-Platform-Interaction.md)

Для получения дополнительной информации смотрите также:

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
