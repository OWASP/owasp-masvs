# V4：身份验证和会话管理要求

## 控制目标

在大多数情况下，用户登录到远程服务是整个移动应用程序体系结构的组成部分。 即使大多数逻辑发生在端点上，MASVS仍定义了一些有关如何管理用户帐户和会话的基本要求。

## 安全验证要求

| # | MSTG-ID |描述L1 | L2 |
| --- | --- | --- | --- | --- |
| **4.1** | MSTG‑AUTH‑1 |如果该应用程序为用户提供了访问远程服务的权限，则会在远程端点执行某种形式的身份验证，例如用户名/密码身份验证。 | ✓| ✓|
| **4.2** | MSTG‑AUTH‑2 |如果使用有状态会话管理，则远程端点将使用随机生成的会话标识符来认证客户端请求，而不发送用户的凭据。 | ✓| ✓|
| **4.3** | MSTG‑AUTH‑3 |如果使用基于无状态令牌的身份验证，则服务器将提供使用安全算法签名的令牌。 | ✓| ✓|
| **4.4** | MSTG‑AUTH‑4 |当用户注销时，远程端点将终止现有会话。 | ✓| ✓|
| **4.5** | MSTG‑AUTH‑5 |密码策略存在并在远程端点上强制执行。 | ✓| ✓|
| **4.6** | MSTG‑AUTH‑6 |远程终结点实现了一种机制来防止凭据提交次数过多。 | ✓| ✓|
| **4.7** | MSTG‑AUTH‑7 |在预定义的不活动时间段和访问令牌到期后，会话将在远程端点上无效。 | ✓| ✓|
| **4.8** | MSTG‑AUTH‑8 |生物识别身份验证（如果有的话）不是事件绑定的（即，使用仅返回"true"或" false"的API）。相反，它基于解锁钥匙串/密钥库。 | | ✓|
| **4.9** | MSTG‑AUTH‑9 |身份验证的第二个因素存在于远程端点，并且2FA要求始终得到执行。 | | ✓|
| **4.10** | MSTG‑AUTH‑10 |敏感交易需要逐步认证。 | | ✓|
| **4.11** | MSTG‑AUTH‑11 |该应用程序通过其帐户通知用户所有敏感活动。用户能够查看设备列表，查看上下文信息（IP地址，位置等），并阻止特定设备。 | | ✓|
| **4.12** | MSTG‑AUTH‑12 |授权模型应在远程端点上定义和实施。 | ✓| ✓|

<div style="page-break-after: always;">
</div>

## 参考文献

OWASP移动安全性测试指南提供了验证上面列出的要求的详细说明。

- 常规：身份验证和会话管理 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04e-Testing-Authentication-and-Session-Management.md>
- Android：测试本地身份验证 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05f-Testing-Local-Authentication.md>
- iOS：测试本地身份验证 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06f-Testing-Local-Authentication.md>

有关更多信息，另请参见：

- OWASP Mobile Top 10: M4 (不安全身份验证) - <https://www.owasp.org/index.php/Mobile_Top_10_2016-M4-Insecure_Authentication>
- OWASP Mobile Top 10: M6 (不安全授权) - <https://www.owasp.org/index.php/Mobile_Top_10_2016-M6-Insecure_Authorization>
- CWE 287 (身份验证不正确) - <https://cwe.mitre.org/data/definitions/287.html>
