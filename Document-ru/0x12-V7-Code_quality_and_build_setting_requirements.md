# V7: Требования к качеству кода и настройкам сборки

## Цель контроля

Следование требованиям данного раздела обеспечивает использование базовых практик безопасного написания кода при разработке приложения, а также стандартных средств безопасности, встроенных в компилятор.

## Требования безопасности

| # | MSTG-ID | Описание | L1 | L2 |
| -- | -------- | ---------------------- | - | - |
| **7.1** | MSTG-CODE-1 | Приложение подписано валидным сертификатом. | ✓ | ✓ |
| **7.2** | MSTG-CODE-2 | Приложение было собрано в release режиме с настройками, подходящими для релизной сборки (например, без атрибута debuggable). | ✓ | ✓ |
| **7.3** | MSTG-CODE-3 | Отладочные символы удалены из нативных бинарных файлов. | ✓ | ✓ |
| **7.4** | MSTG-CODE-4 | Kод отладки и вспомогательный дла разработки код (например, тестовый код, бэкдоры, скрытые настройки) были удалены. Приложение не логирует подробные ошибки и отладочные сообщения. | ✓ | ✓ |
| **7.5** | MSTG-CODE-5 | Все сторонние компоненты, используемые мобильным приложением (библиотеки и фреймворки), идентифицированы и проверены на наличие известных уязвимостей. | ✓ | ✓ |
| **7.6** | MSTG-CODE-6 | Приложение обрабатывает возможные исключения.| ✓ | ✓ |
| **7.7** | MSTG-CODE-7 | В логике обработки связанных с безопасностью ошибок по умолчанию запрещается доступ. | ✓ | ✓ |
| **7.8** | MSTG-CODE-8 | В неконтролируемом коде память выделяется, освобождается и используется безопасно.  | ✓ | ✓ |
| **7.9** | MSTG-CODE-9 | Активированы все стандартные функции безопасности, предусмотренные инструментами разработчика (такие как минификация байт-кода, защита стека, поддержка PIE и ARC). | ✓ | ✓ |

## Ссылки

OWASP MSTG содержит подробные инструкции по проверке требований, перечисленных в этом разделе.

- Android: Тестирование качества кода и настроек сборки - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05i-Testing-Code-Quality-and-Build-Settings.md>
- iOS: Тестирование качества кода и настроек сборки - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06i-Testing-Code-Quality-and-Build-Settings.md>

Для получения дополнительной информации смотрите также:

- OWASP Mobile Top 10: M7 (Poor Code Quality) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m7-client-code-quality>
- CWE 20 (Improper Input Validation) - <https://cwe.mitre.org/data/definitions/20.html>
- CWE 89 (Improper Neutralization of Special Elements used in an SQL Command) - <https://cwe.mitre.org/data/definitions/89.html>
- CWE 95 (Improper Neutralization of Directives in Dynamically Evaluated Code ('Eval Injection')) - <https://cwe.mitre.org/data/definitions/95.html>
- CWE 119 (Improper Restriction of Operations within the Bounds of a Memory Buffer) - <https://cwe.mitre.org/data/definitions/119.html>
- CWE 215 (Information Exposure through Debug Information) - <https://cwe.mitre.org/data/definitions/215.html>
- CWE 388 (7PK - Errors) - <https://cwe.mitre.org/data/definitions/388.html>
- CWE 489 (Leftover Debug Code) - <https://cwe.mitre.org/data/definitions/489.html>
- CWE 502 (Deserialization of Untrusted Data) - <https://cwe.mitre.org/data/definitions/502.html>
- CWE 511 (Logic/Time Bomb) - <https://cwe.mitre.org/data/definitions/511.html>
- CWE 656 (Reliance on Security through Obscurity) - <https://cwe.mitre.org/data/definitions/656.html>
- CWE 676 (Use of Potentially Dangerous Function)  - <https://cwe.mitre.org/data/definitions/676.html>
- CWE 937 (OWASP Top Ten 2013 Category A9 - Using Components with Known Vulnerabilities) - <https://cwe.mitre.org/data/definitions/937.html>
