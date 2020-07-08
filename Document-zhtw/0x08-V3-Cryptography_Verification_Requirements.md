# V3: 加密要求

## 管理目標

加密是保護行動設備上儲存的資料的重要因素。 特別是如果不遵守標準規則開發，事情可能出現嚴重錯誤。 本章中的管理目的是檢測經過驗證的應用程序是否根據行業最佳實踐使用加密，例如：

- 使用經過驗證的加密方式;
- 正確選擇和設置加密明文;
- 在需要亂數的地方皆有使用亂數產生器.

## 安全檢測要求

| # | MSTG-ID | 描述 | L1 | L2 |
| -- | -------- | ---------------------- | - | - |
| **3.1** | MSTG-CRYPTO-1 | 應用程式不可使用 hardcoded 作為加密方法。| ✓ | ✓ |
| **3.2** | MSTG-CRYPTO-2 | 應用程式中使用驗證過的加密演算法。 | ✓ | ✓ |
| **3.3** | MSTG-CRYPTO-3 | 使用適用於該案例中所應使用的加密演算法，並基於業界最佳實踐的方式設定其參數。 | ✓ | ✓ |
| **3.4** | MSTG-CRYPTO-4 | 應用程式不應使用基於安全目的而被廣泛棄用的加密協議和算法。 | ✓ | ✓ |
| **3.5** | MSTG-CRYPTO-5 | 加密金鑰不重複使用。 | ✓ | ✓ |
| **3.6** | MSTG-CRYPTO-6 | 所有亂數是經由安全的亂數產生器產生。 | ✓ | ✓ |

## 參考

OWASP 行動安全檢測指南列出相關要求，並且相關章節中有詳細說明。

- Android - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05e-Testing-Cryptography.md>
- iOS - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06e-Testing-Cryptography.md>

更多相關信息，另請參閱：

- OWASP Mobile Top 10: M5 (Insufficient Cryptography) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m5-insufficient-cryptography>
- CWE 310 (Cryptographic Issues) - <https://cwe.mitre.org/data/definitions/310.html>
- CWE 321 (Use of Hard-coded Cryptographic Key) - <https://cwe.mitre.org/data/definitions/321.html>
- CWE 326 (Inadequate Encryption Strength) - <https://cwe.mitre.org/data/definitions/326.html>
- CWE 327 (Use of a Broken or Risky Cryptographic Algorithm) - <https://cwe.mitre.org/data/definitions/327.html>
- CWE 329 (Not Using a Random IV with CBC Mode) - <https://cwe.mitre.org/data/definitions/329.html>
- CWE 330 (Use of Insufficiently Random Values) - <https://cwe.mitre.org/data/definitions/330.html>
- CWE 337 (Predictable Seed in PRNG) - <https://cwe.mitre.org/data/definitions/337.html>
- CWE 338 (Use of Cryptographically Weak Pseudo Random Number Generator (PRNG)) - <https://cwe.mitre.org/data/definitions/338.html>
