# V8: 彈性準則

## 控制目標

本節涵蓋對於存取機敏資料的功能的行動應用程序建議的縱身防禦措施。
缺少任何這些控件不會導致漏洞 - 相反的，它們增加逆向工程及特定的用戶端攻擊對行動應用程式的彈性

基於對未經授權篡改應用程式和/或代碼逆向工程所導致的風險的評估，應根據需要應用本節中的控件。
我們建議諮詢OWASP文件"逆向工程技術風險和未經授權的代碼修改逆向工程和代碼修改預防"(參考下面)列出的業務風險以及相關的技術威脅。

對下面的列表中的任何控件是有效的，應用程式必須滿足至少所有的MASVS-L1(換句話說，實體安全控件一定是到位)，以及V8內所有低編號的要求，
例如，下面的混淆控制列表"妨礙理解"一定是跟"應用程式隔離"結合，"妨礙動態分析和竄改"，和"設備綁定"

注意: 軟體保護絕不是使用在一個安全控制元件替換，MASVR-R中列出的控件旨在增加特定威脅，對滿足MASVS安全要求的應用程式，提供額外的保護控制

以下注意事項採用:

1. 威脅模型必須明確概述用戶端抵擋的威脅。 此外，必須具體說明該方案旨在提供的保護等級。 例如，一個明確的目標可以強制使搜尋特定惡意軟體的作者對應用程式投入大量的手動逆向工程作業來實作。

2. 威脅模型必須是敏感的。 例如，如果攻擊者可以簡單地將整個白箱code lift，那麼將加密金鑰隱藏在白箱中就沒有意義。

3. 保護的有效性應始終由具有測試所使用的特定類型防篡改和混淆經驗的專家進行驗證（另請參閱 Mobile Security Testing Guide 中的“逆向工程”和“評估軟體保護”章節）。

### 阻礙動態分析和篡改

| # | MSTG-ID | 描述 | R |
| -- | -------- | ---------------------- | - |
| **8.1** | MSTG-RESILIENCE-1 | 應用程式通過提醒用戶或終止應用程式來檢測並回應超級用戶權限或越獄設備的存在。 | ✓ |
| **8.2** | MSTG-RESILIENCE-2 | 應用程式防止和回應偵錯 和/或 檢測的偵錯器附加上去。 必須涵蓋所有可用的偵錯協議。 | ✓ |
| **8.3** | MSTG-RESILIENCE-3 | 應用程式檢測和回應自己的沙箱中可執行的檔案和重要資料遭竄改。 | ✓ |
| **8.4** | MSTG-RESILIENCE-4 | 應用程式檢測和回應設備上廣泛使用的逆向工程工具和架構的存在。 | ✓ |
| **8.5** | MSTG-RESILIENCE-5 | 應用程式檢測並回應在模擬器中運行。  | ✓ |
| **8.6** | MSTG-RESILIENCE-6 | 應用程式檢測並回應篡改其自己的記憶體空間中的程式碼和資料。 | ✓ |
| **8.7** | MSTG-RESILIENCE-7 | 應用程式在各個防禦類別（8.1到8.6）中實施多種機制。 請注意，彈性隨著所用機制的數量，原創性的多樣性而變化。 | ✓ |
| **8.8** | MSTG-RESILIENCE-8 | 檢測機制觸發不同類型的回應，包括延遲和暗中回應。 | ✓ |
| **8.9** | MSTG-RESILIENCE-9 | 混淆應用於程序化防禦，這反過來通過動態分析阻止去除混淆。  | ✓ |

### 裝置綁定

| # | MSTG-ID | 描述 | R |
| -- | -------- | ---------------------- | - |
| **8.10** | MSTG-RESILIENCE-10 | 應用程式使用從裝置特有的多個特性衍生的設備指紋實作“裝置綁定”功能。 | ✓ |

### 防止洩漏

| # | MSTG-ID | 描述 | R |
| -- | -------- | ---------------------- | - |
| **8.11** | MSTG-RESILIENCE-11 | 屬於應用程式的所有可執行的檔案和函式庫都在文件級別上加密 和/或 可執行的檔案內的重要程式碼和資料片段被加密或打包。 瑣碎的靜態分析不會顯示重要的程式碼或資據。 | ✓ |
| **8.12** | MSTG-RESILIENCE-12 | 考慮到當前發布的研究，如果混淆的目標是保護機密的計算，則使用混淆方案，該方案既適用於特定任務又良好的適用於手動和自動去混淆辦法。必須通過手動測試來驗證混淆方案的有效性。請注意，比起混淆，盡可能使用基於硬體的隔離功能。 | ✓ |

### 防止竊聽

| # | MSTG-ID | 描述 | R |
| -- | -------- | ---------------------- | - |
| **8.13** | MSTG-RESILIENCE-13 | 因應縱深防禦，除了需要與通訊對象有強度足夠的加密通訊架構，應用層也需要有足夠的加密機制去預防任何中間人竊聽的可能性產生。 | ✓ |

## 參考

OWASP Mobile Security Testing Guide 提供了有關驗證本章節中列出的準則的詳細使用說明。

- Android - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05j-Testing-Resiliency-Against-Reverse-Engineering.md>
- iOS - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06j-Testing-Resiliency-Against-Reverse-Engineering.md>

<div style="page-break-after: always; visibility: hidden">
\pagebreak
</div>

更多資訊請參閱：

- OWASP Mobile Top 10: M8 (Code Tampering) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m8-code-tampering>
- OWASP Mobile Top 10: M9 (Reverse Engineering) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m9-reverse-engineering>
- WASP Reverse Engineering Threats - <https://wiki.owasp.org/index.php/Technical_Risks_of_Reverse_Engineering_and_Unauthorized_Code_Modification>
- OWASP Reverse Engineering and Code Modification Prevention - <https://wiki.owasp.org/index.php/OWASP_Reverse_Engineering_and_Code_Modification_Prevention_Project>
