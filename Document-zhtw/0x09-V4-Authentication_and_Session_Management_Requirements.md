# V4: 身份驗證和對談管理準則

## 控制目標

在多數情況下，登錄遠端服務的用戶是整個行動應用程式架構整體的ㄧ部分。 即使大多數邏輯發生在端點，MASVS定義了有關如何管理用戶帳戶和對談的一些基本要求。

## 安全驗證準則

| # | MSTG-ID | 描述 | L1 | L2 |
| --- | --- | --- | --- | --- |
| **4.1** | MSTG‑AUTH‑1 | 如果應用程式向用戶提供對遠端服務的訪問權限，則用戶名/密碼驗證等一些形式的身份驗證會在遠端端點執行。 | ✓ | ✓ |
| **4.2** | MSTG‑AUTH‑2 | 如果使用有狀態的對談管理，則遠端端點使用隨機生成的交談識別碼來驗證客戶端請求，而不發送用戶憑證。  | ✓ | ✓ |
| **4.3** | MSTG‑AUTH‑3 | 如果使用無狀態token-based驗證方式，則服務器會提供使用安全算法簽名的token。 | ✓ | ✓ |
| **4.4** | MSTG‑AUTH‑4 | 當用戶登出時，遠端端點會終止現有對談。 | ✓ | ✓ |
| **4.5** | MSTG‑AUTH‑5 | 存在密碼方針，並在遠端端點強制實行。 | ✓ | ✓ |
| **4.6** | MSTG‑AUTH‑6 | 遠端端點實施了一個可以防止多次提交憑證的機制。 | ✓ | ✓ |
| **4.7** | MSTG‑AUTH‑7 | 在事先定義的不活動時段和用來訪問的token過期後，對談在遠端端點將無效。 | ✓ | ✓ |
| **4.8** | MSTG‑AUTH‑8 | 生物辨識認證（如果有的話）不受事件限制（即是像簡單地返回“真”或“假”的API）。 相反，它是基於解鎖鑰匙串/密鑰庫。 |   | ✓ |
| **4.9** | MSTG‑AUTH‑9 | 遠端端點存在第二個驗證要素，並且始終強制執行2FA準則。  |   | ✓ |
| **4.10** | MSTG‑AUTH‑10 | 敏感的交易需要進一步認證。  |   | ✓ |
| **4.11** | MSTG‑AUTH‑11 | 應用程式通過其帳戶通知用戶所有登錄活動。 用戶可以查看用於訪問帳戶的裝置列表，以及阻檔特定裝置。 |  | ✓ |

<div style="page-break-after: always;"></div>

## 參考

OWASP Mobile Security Testing Guide 提供了有關驗證本章節中列出的準則的詳細使用說明。

- In general - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04e-Testing-Authentication-and-Session-Management.md>
- For Android - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05f-Testing-Local-Authentication.md>
- For iOS - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06f-Testing-Local-Authentication.md>

更多資訊請參閱：

- OWASP Mobile Top 10: M4 - Insecure Authentication: <https://www.owasp.org/index.php/Mobile_Top_10_2016-M4-Insecure_Authentication>
- OWASP Mobile Top 10: M6 - Insecure Authorization: <https://www.owasp.org/index.php/Mobile_Top_10_2016-M6-Insecure_Authorization>
- CWE:  <https://cwe.mitre.org/data/definitions/287.html>
