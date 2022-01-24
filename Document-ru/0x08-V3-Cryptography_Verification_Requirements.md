# V3: Требования к криптографии

## Цель верификации

Криптография является неотъемлемым компонентом защиты данных, хранящихся на мобильном устройстве. Но кроме того, это область, в которой все может пойти не так, особенно когда стандартные правила не соблюдаются. Цель верификационных требований в этой главе состоит в том, чтобы убедиться, что проверяемое приложение использует криптографию в соответствии с лучшими практиками индустрии, такими, как:

- Использование проверенных криптографических библиотек;
- Правильный выбор и настройка криптографических алгоритмов;
- Подходящий генератор случайных чисел там, где это необходимо.

## Требования безопасности

| # | MSTG-ID | Описание | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **3.1** | MSTG-CRYPTO-1 | Приложение не использует симметричное шифрование с захардкоженными ключами в качестве единственного метода шифрования.| x | x |
| **3.2** | MSTG-CRYPTO-2 | Приложение использует проверенные реализации криптографических алгоритмов. | x | x |
| **3.3** | MSTG-CRYPTO-3 | Приложение использует подходящие криптографические алгоритмы для каждого конкретного случая, с параметрами, которые соответствуют лучшим практикам индустрии. | x | x |
| **3.4** | MSTG-CRYPTO-4 | Приложение не использует устаревшие и слабые криптографические протоколы и алгоритмы. | x | x |
| **3.5** | MSTG-CRYPTO-5 | Приложение не использует один и тот же ключ несколько раз. | x | x |
| **3.6** | MSTG-CRYPTO-6 | Все случайные значения генерируются с использованием безопасного генератора случайных чисел. | x | x |

## Ссылки

OWASP MSTG содержит подробные инструкции по верификации требований, перечисленных в этом разделе.

- Android: Тестирование криптографии - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05e-Testing-Cryptography.md>
- iOS: Тестирование криптографии - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06e-Testing-Cryptography.md>

Для получения дополнительной информации смотрите также:

- OWASP Mobile Top 10: M5 (Insufficient Cryptography) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m5-insufficient-cryptography>
- CWE 310 (Cryptographic Issues) - <https://cwe.mitre.org/data/definitions/310.html>
- CWE 321 (Use of Hard-coded Cryptographic Key) - <https://cwe.mitre.org/data/definitions/321.html>
- CWE 326 (Inadequate Encryption Strength) - <https://cwe.mitre.org/data/definitions/326.html>
- CWE 327 (Use of a Broken or Risky Cryptographic Algorithm) - <https://cwe.mitre.org/data/definitions/327.html>
- CWE 329 (Not Using a Random IV with CBC Mode) - <https://cwe.mitre.org/data/definitions/329.html>
- CWE 330 (Use of Insufficiently Random Values) - <https://cwe.mitre.org/data/definitions/330.html>
- CWE 337 (Predictable Seed in PRNG) - <https://cwe.mitre.org/data/definitions/337.html>
- CWE 338 (Use of Cryptographically Weak Pseudo Random Number Generator (PRNG)) - <https://cwe.mitre.org/data/definitions/338.html>
