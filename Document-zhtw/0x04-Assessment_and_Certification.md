# 評估與認證

## OWASP對MASVS認證和信任標誌的立場

OWASP是一個中立無廠商偏好的非營利組織。OWASP本身並不會認證/授權任何廠商、認證機構或者軟體。

任何這樣的保證聲明、信任標誌或認證，都不會是OWASP官方正式審查、註冊或認證的！因此，任何組織都必須十分謹慎地看待，且不應輕易相信任何宣稱其擁有MASVS認證或信任標誌的第三方機構。

這段聲明並不是阻止任何組織去提供相關的認證服務，但任何組織不該宣稱擁有OWASP官方的認證。

## 認證行動應用程式的指導綱領

The recommended way of verifying compliance of a mobile app with the MASVS is by performing an "open book" review, meaning that the testers are granted access to key resources such as architects and developers of the app, project documentation, source code, and authenticated access to endpoints, including access to at least one user account for each role.

It is important to note that the MASVS only covers security of the (client-side) mobile app and the network communication between the app and its remote endpoint(s), as well as a few basic and generic requirements related to user authentication and session management. It does not contain specific requirements for the remote services (e.g. web services) associated with the app, safe for a limited set of generic requirements pertaining to authentication and session management. However, MASVS V1 specifies that remote services must be covered by the overall threat model, and be verified against appropriate standards, such as the OWASP ASVS.

A certifying organization must include in any report the scope of the verification (particularly if a key component is out of scope), a summary of verification findings, including passed and failed tests, with clear indications of how to resolve the failed tests. Keeping detailed work papers, screenshots or movies, scripts to reliably and repeatedly exploit an issue, and electronic records of testing, such as intercepting proxy logs and associated notes such as a cleanup list, is considered standard industry practice. It is not sufficient to simply run a tool and report on the failures; this does not provide sufficient evidence that all issues at a certifying level have been tested and tested thoroughly. In case of dispute, there should be sufficient supportive evidence to demonstrate that every verified requirement has indeed been tested.

### 如何使用OWASP Mobile Security Testing Guide (MSTG)

OWASP MSTG是測試行動應用程式安全的指導手冊。它描述了驗證被列在MASVS中相關準則的技術流程。MSTG提供了一個測試方案的列表，每一個測試方案都可以連結到一個MASVS的準則。雖然MASVS的準則都是概念性的和通用性的，MSTG提供了對不同行動作業系統的相對應深層次的建議以及測試流程。

### 自動化資訊安全測試工具的使用

在可能的情況下，為了增加效率，程式碼掃描工具和黑箱測試工具的使用是被鼓勵的。然而，要完成MASVS的驗證是不可以只單獨依賴自動化工具的，因為每個行動應用程式都是不同的，而且了解應用程式的整體架構、商業邏輯和應用特定技術和框架帶來的缺點是驗證應用程式安全的必要條件。

## 其他使用方式

### As Detailed Security Architecture Guidance

One of the more common uses for the Mobile Application Security Verification Standard is as a resource for security architects. The two major security architecture frameworks, SABSA or TOGAF, are missing a great deal of information that is necessary to complete mobile application security architecture reviews. MASVS can be used to fill in those gaps by allowing security architects to choose better controls for issues common to mobile apps.

### As a Replacement for Off-the-shelf Secure Coding Checklists

Many organizations can benefit from adopting the MASVS, by choosing one of the two levels, or by forking MASVS and changing what is required for each application's risk level in a domain-specific way. We encourage this type of forking as long as traceability is maintained, so that if an app has passed requirement 4.1, this means the same thing for forked copies as the standard evolves.

### As a Basis for Security Testing Methodologies

A good mobile app security testing methodology should cover all requirements listed in the MASVS. The OWASP Mobile Security Testing Guide (MSTG) describes black-box and white-box test cases for each verification requirement.

### As a Guide for Automated Unit and Integration Tests

The MASVS is designed to be highly testable, with the sole exception of architectural requirements. Automated unit, integration and acceptance testing based on the MASVS requirements can be integrated in the continuous development lifecycle. This not only increases developer security awareness, but also improves the overall quality of the resulting apps, and reduces the amount of findings during security testing in the pre-release phase.

### For Secure Development Training

MASVS can also be used to define characteristics of secure mobile apps. Many "secure coding" courses are simply ethical hacking courses with a light smear of coding tips. This does not help developers. Instead, secure development courses can use the MASVS, with a strong focus on the proactive controls documented in the MASVS, rather than e.g. the Top 10 code security issues.
