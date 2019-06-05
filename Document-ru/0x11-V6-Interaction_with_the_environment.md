# V6: Требования к взаимодействию с операционной системой

## Цель верификации

Следование требованиям этого раздела обеспечивают безопасное использование API операционной системы. Дополнительно содержатся требования к межпроцессному взаимодействию (IPC).

## Требования безопасности

| # | MSTG-ID | Описание |L2 |
| --- | --- | --- | --- | --- |
| **6.1** | MSTG‑PLATFORM‑1 | Приложение запрашивает минимально необходимый набор разрешений. | ✓ | ✓ |
| **6.2** | MSTG‑PLATFORM‑2 | Все данные, поступающие из внешних источников и от пользователя, валидируются и санитизируются. Сюда входят данные, полученные через пользовательский интерфейс, механизмы IPC (такие как intent-ы, кастомные URL-схемы) и из сети.| ✓ | ✓ |
| **6.3** | MSTG‑PLATFORM‑3 | Приложение не экспортирует чувствительные данные через кастомные URL-схемы, если эти механизмы не защищены должным образом. | ✓ | ✓ |
| **6.4** | MSTG‑PLATFORM‑4 | Приложение не экспортирует чувствительные данные через IPC механизмы без должной защиты. | ✓ | ✓ |
| **6.5** | MSTG‑PLATFORM‑5 | JavaScript отключен в компонентах WebView, если в нём нет необходимости. | ✓ | ✓ |
| **6.6** | MSTG‑PLATFORM‑6 | WebViews сконфигурирован с поддержкой минимального набора протоколов (в идеале только https). Поддержка потенциально опасных URL-схем (таких как: file, tel и app-id) отключена. | ✓ | ✓ |
| **6.7** | MSTG‑PLATFORM‑7 | Если нативные методы приложения используются WebView, верифицировать, что исполняются только Javascript объекты данного приложения. | ✓ | ✓ |
| **6.8** | MSTG‑PLATFORM‑8 | Десериализация объектов, если она есть, реализована с использованием безопасного API. | ✓ | ✓ |

<div style="page-break-after: always;"></div>

## Ссылки

OWASP MSTG содержит подробные инструкции по верификации требований, перечисленных в этом разделе.

- Android - [https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05h-Testing-Platform-Interaction.md](https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05h-Testing-Platform-Interaction.md)
- iOS - [https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06h-Testing-Platform-Interaction.md](https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06h-Testing-Platform-Interaction.md)

Для получения дополнительной информации смотрите также:

- OWASP Mobile Top 10: M1 - Improper Platform Usage: <https://www.owasp.org/index.php/Mobile_Top_10_2016-M1-Improper_Platform_Usage>
- CWE: <https://cwe.mitre.org/data/definitions/20.html>
- CWE: <https://cwe.mitre.org/data/definitions/749.html>
