# V1: 架構, 設計和威脅模型分析準則

## 控制目標

在一個完美的世界中，整個開發階段都會考慮到安全性。 然而實際上，安全性常常只是 SDLC 後期的考慮因素。 除了技術控制之外， MASVS 需要制定流程，以確保在規劃行動應用程式的結構時明確考慮到安全性的問題，並確認所有元件的功能性和安全性是清楚的。 由於大多數行動應用程式是作為遠程服務的用戶端，因此必須確保妥善的安全標準也運用在這些服務 - 但獨立測試行動應用程式是不夠的。

“V1”這個類別列出了與應用程式的架構和設計有關的要求。 因此，這是唯一沒有對應到 OWASP Mobile Application Security Testing Guide 裡的技術測資的類別。 為了涵蓋威脅模型分析，安全 SDLC，密鑰管理等主題，MASVS 的用戶應參考相對應的OWASP項目 和/或 其他標準，例如下面連結所提到的。

## 安全驗證準則

以下列出了 MASVS-L1 和 MASVS-L2 的要求。

| # | MSTG-ID | 描述 | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **1.1** | MSTG-ARCH-1 | 所有應用程式組成元件都已歸類並且已知是必需的。 | x | x |
| **1.2** | MSTG-ARCH-2 | 安全控制永遠不會僅僅在客戶端強制執行，而是在相對應的遠程端點上也必須強制執行。 | x | x |
| **1.3** | MSTG-ARCH-3 | 行動應用程式的高級架構和所有連接的遠程服務已經被定義，並且該架構已解決了安全性的問題。 | x | x |
| **1.4** | MSTG-ARCH-4 | 在行動應用程式環境中被認為敏感的資料已被明確歸類。 | x | x |
| **1.5** | MSTG-ARCH-5 | 所有應用程式的組成都根據它們提供的業務功能 和/或 安全功能進行定義。 |   | x |
| **1.6** | MSTG-ARCH-6 | 行動應用程式和相關遠程服務的威脅模型已經制定，以識別潛在的威脅和對策。 |   | x |
| **1.7** | MSTG-ARCH-7 | 所有安全控制都有一個集中的管理。 |   | x |
| **1.8** | MSTG-ARCH-8 | 如何管理加密金鑰（如果有）有明確方針，而且加密金鑰生命週期需強制實施。 理想情況下，遵循 NIST SP 800-57 等鑰匙管理標準。 |   | x |
| **1.9** | MSTG-ARCH-9 | 存在強制行動應用程式更新的機制。 |   | x |
| **1.10** | MSTG-ARCH-10 | 安全性在軟體開發生命週期的所有階段中仔細納入考量。 |   | x |
| **1.11** | MSTG-ARCH-11 | 需要一個有效的責任披露政策被執行。 |  | x |
| **1.12** | MSTG-ARCH-12 | 應用程式需遵守隱私法規及政策。 | x | x |

## 參考

更多資訊請參閱：

- OWASP Mobile Top 10: M10 (Extraneous Functionality) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m10-extraneous-functionality>
- OWASP Thread modelling - <https://owasp.org/www-community/Application_Threat_Modeling>
- OWASP Secure SDLC Cheat Sheet - <https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets_excluded/Secure_SDLC_Cheat_Sheet.md>
- Microsoft SDL - <https://www.microsoft.com/en-us/securityengineering/sdl/>
- NIST SP 800-57 - <https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final>
- security.txt - <https://securitytxt.org/>
