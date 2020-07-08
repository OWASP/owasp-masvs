# V2: 資料存儲和隱私要求

## 管理目標

保護機敏資料（如用戶憑據和個人訊息）是行動安全的重點。首先，如果操作系統機制諸如 IPC 使用不當，這將會讓敏感的資料被無意中暴露在同一設備或其他應用程式上。此外，資料可能會無意中從雲端被存取，備份，甚至從鍵盤緩存中洩漏。此外，與其他類型的設備相比，行動設備很容易丟失或被盜。因此，第三方可以更容易地竊取相關資訊。在這種情況下，可以實施額外的保護機制使獲取機敏資料更加困難。

注意：由於 MASVS 是以應用程式開發為中心的，因此它並不包括像 MDM 那樣的解決方案和策略。我們建議您在企業環境中使用相關策略來進一步增強資料的安全性。

### 機敏資料的定義

MASVS 規範中的涉及敏感資料用戶憑證和在特定情況中被視為機敏的任何其他資料，例如：

- 可能被犯罪集團濫用的個人識別資料（PII）：社會安全號碼，信用卡號碼，銀行帳號，醫療資訊;
- 可能因洩漏其極機敏資料而導致財務損傷，合約資料，保密協議，管理資料等;
- 任何必須被法律保護或出於同原因而受到保護的資料。

## 安全驗證要求

通過遵循簡單的規則與定義可以防止絕大多數資料洩露問題， 本章中列出的大多管理目標對於所有驗證級別都是必需的。

| # | MSTG-ID | 描述 | L1 | L2 |
| -- | -------- | ---------------------- | - | - |
| **2.1** | MSTG-STORAGE-1 | 系統的憑證儲存功能適用於儲存機敏資料，如個人識別訊息，用戶憑證，加密密鑰等。 | ✓ | ✓ |
| **2.2** | MSTG-STORAGE-2 | 機敏資料不儲存在應用程式的服務器或系統以外的憑證儲存功能。 | ✓ | ✓ |
| **2.3** | MSTG-STORAGE-3 | 機敏資料未寫入應用程式日誌。 | ✓ | ✓ |
| **2.4** | MSTG-STORAGE-4 | 除非對架構有必要，否則不與第三方共享機敏資料。  | ✓ | ✓ |
| **2.5** | MSTG-STORAGE-5 | 於明文輸入機敏資料部分禁用鍵盤緩存。 | ✓ | ✓ |
| **2.6** | MSTG-STORAGE-6 | 機敏資料不通過 IPC 機制公開。 | ✓ | ✓ |
| **2.7** | MSTG-STORAGE-7 | 密碼和定義參數等機敏資料不會通過用戶界面公開。 | ✓ | ✓ |
| **2.8** | MSTG-STORAGE-8 | 在行動作業系統生成任何備份的檔案中不可包含機敏資料。 |   | ✓ |
| **2.9** | MSTG-STORAGE-9 | 行動應用程式移至背景執行時需刪除機敏資料。 |  | ✓ |
| **2.10** | MSTG-STORAGE-10 | 應用程式不會在記憶體中保存超過必要時效的機敏資料，並且在使用後會明確清除記憶體內容。 |  | ✓ |
| **2.11** | MSTG-STORAGE-11 | 應用程式採用了最低訪問安全策略，會要求用戶設置密碼等。 |  | ✓ |
| **2.12** | MSTG-STORAGE-12 | 應用程式已主動告知如何處理用戶的個人識別訊息，並且主動告知用戶的使用應用程式時要遵循的要點。 |  | ✓ |
| **2.13** | MSTG-STORAGE-13 | 機敏資料不應被儲存在行動應用裝置本機儲存空間上。機敏資料應儲存在遠端端點，然後在需要時讀取並儲存於記憶體中。 |  | ✓ |
| **2.14** | MSTG-STORAGE-14 | 如果機敏資料需要被儲存於行動應用裝置本機儲存空間，該資料應經過本機認證程序後可被使用之硬體加密系統加密後儲存。 |  | ✓ |
| **2.15** | MSTG-STORAGE-15 | 行動應用程式的本機儲存空間應在多次認證失敗後，自動進行資料清除之工作。 |  | ✓ |

## 參考

OWASP 行動安全檢測指南列出相關要求，並且相關章節中有詳細說明。

- For Android - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05d-Testing-Data-Storage.md>
- For iOS - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06d-Testing-Data-Storage.md>

更多相關信息，另請參閱：

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
