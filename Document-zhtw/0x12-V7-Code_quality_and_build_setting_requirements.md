# V7: 程式碼品質與建立設定要求

## 控管目的

此控管目的是確保實作編碼時將遵照應用程式開發基本安全性，且基本(免費)安全性功能是藉由啟用編譯器所提供。

## 安全性驗證要求

| # | MSTG-ID | 說明 | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **7.1** | MSTG-CODE-1 | 應用程式經由有效的憑證所提供所簽章，其私鑰是受到適當保護的 | x | x |
| **7.2** | MSTG-CODE-2 | 應用程式已在發佈模式建置，其設定適用於發佈版本(不可除錯的)| x | x |
| **7.3** | MSTG-CODE-3 | 除錯標記已從原生二元碼中移除 | x | x |
| **7.4** | MSTG-CODE-4 | 除錯程式碼已移除（如測試代碼，後門，隱藏設定等），應用程式將不紀錄詳細錯誤或偵錯訊息| x | x |
| **7.5** | MSTG-CODE-5 | 所有行動應用程式使用的第三方套件，如函式庫及框架，皆經識別及已知漏洞查驗 | x | x |
| **7.6** | MSTG-CODE-6 | 應用程式進行例外處理| x | x |
| **7.7** | MSTG-CODE-7 | 預設無法存取安全性控管的錯誤處理邏輯 | x | x |
| **7.8** | MSTG-CODE-8 | 在非託管程式碼，記憶體將被安全的被分配、釋出及使用  | x | x |
| **7.9** | MSTG-CODE-9 | 由Toolchain所提供的免費安全性功能將啟用，如簡化位元組碼(byte-code)、堆疊(Stack)保護、PIE支援、自動參考計數(Reference Counting)| x | x |

## 參考資料

OWASP 行動應用安全性測試指南針對此章節所列出的認證要，提供詳細的說明

- Android - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x05i-Testing-Code-Quality-and-Build-Settings.md>
- iOS - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x06i-Testing-Code-Quality-and-Build-Settings.md>

更多資訊，請參考：

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
