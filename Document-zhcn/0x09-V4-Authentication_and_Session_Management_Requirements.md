# V4：身份验证 和 会话管理要求

## 控制目标

在大多数情况下，用户登录到远程服务是整个移动应用程序架构的一个组成部分。尽管大多数逻辑发生在终端，MASVS定义了一些关于如何管理用户帐户和会话的基本需求。

## 安全验证要求

| # | MSTG-ID | 描述 | L1 | L2 |
| --- | --- | --- | --- | --- |
| **4.1** | MSTG‑AUTH‑1 |如果应用程序为用户提供对远程服务的访问，则在远程端点执行某种形式的身份验证，如用户名/密码身份验证。| ✓| ✓ |
| **4.2** | MSTG‑AUTH‑2 |如果使用有状态会话管理，则远程端点使用随机生成的会话标识符对客户机请求进行身份验证，而不发送用户的凭据。 | ✓| ✓|
| **4.3** | MSTG‑AUTH‑3 |如果使用基于无状态令牌的身份验证，则服务器应该提供使用安全算法签名的令牌。 | ✓| ✓ |
| **4.4** | MSTG‑AUTH‑4 |当用户注销时，远程端点终止现有会话。 | ✓| ✓ |
| **4.5** | MSTG‑AUTH‑5 |存在密码策略，并在远程端点强制执行。 | ✓| ✓ |
| **4.6** | MSTG‑AUTH‑6 |远远程端点实现一种机制来防止过多次数地提交凭据。| ✓| ✓ |
| **4.7** | MSTG‑AUTH‑7 |在在预定义的不活动期间和访问令牌过期后，远程端点会话将失效。 | ✓| ✓ |
| **4.8** | MSTG‑AUTH‑8 |生物识别身份验证（如果有的话）是不受事件绑定的（即，使用仅返回"true"或"false"的API）.相反，它基于解锁钥匙串/密钥库. | | ✓|
| **4.9** | MSTG‑AUTH‑9 |第二个身份验证因素存在于远程端点，并且始终强制执行2FA要求。 | | ✓ |
| **4.10** | MSTG‑AUTH‑10 |敏感交易必须逐步认证. | | ✓ |
| **4.11** | MSTG‑AUTH‑11 |该应用会通知用户所有相关的敏感活动。用户可以查看设备列表，查看上下文信息(IP地址、位置等)，并阻止特定的设备。 | | ✓ |
| **4.12** | MSTG‑AUTH‑12 |授权模型应在远程端点上定义和实施. | ✓| ✓ |

<div style="page-break-after: always;">
</div>

## 参考文献

OWASP移动安全性测试指南提供了验证上面列出的要求的详细说明。

- 常规：身份验证和会话管理 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04e-Testing-Authentication-and-Session-Management.md>
- Android：测试本地身份验证 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05f-Testing-Local-Authentication.md>
- iOS：测试本地身份验证 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06f-Testing-Local-Authentication.md>

有关更多信息，另请参见：

- OWASP 移动安全前 10: M4 (不安全身份验证) - <https://www.owasp.org/index.php/Mobile_Top_10_2016-M4-Insecure_Authentication>
- OWASP 移动安全前 10: M6 (不安全授权) - <https://www.owasp.org/index.php/Mobile_Top_10_2016-M6-Insecure_Authorization>
- CWE 287 (身份验证不正确) - <https://cwe.mitre.org/data/definitions/287.html>
