# V4：身份验证 和 会话管理

## 控制目标

绝大多数的移动应用程序架构中, 用户登录到远程服务只是其中一个组成部分, 尽管大多数应用逻辑发生在客户终端。MASVS 定义了 `关于如何管理用户帐户和会话的基本需求`。

## 安全验证要求

| # | MSTG-ID | 描述 | L1 | L2 |
| --- | --- | --- | --- | --- |
| **4.1** | MSTG‑AUTH‑1 | 如果该应用提供给用户访问远程服务, 即某些形式的认证, 例如用户名/密码认证, 都应在远程终端施行. | ✓| ✓ |
| **4.2** | MSTG‑AUTH‑2 | 如果状态会话管理被使用，则远程端点使用随机生成的会话标识符来认证客户端请求，而不会发送用户的凭证. | ✓| ✓|
| **4.3** | MSTG‑AUTH‑3 | 如果无状态的基于令牌认证机制被使用，该服务器所提供的令牌应用安全算法签名。 | ✓| ✓ |
| **4.4** | MSTG‑AUTH‑4 | 当用户注销时，远程端点应终止已经存在的会话。 | ✓| ✓ |
| **4.5** | MSTG‑AUTH‑5 | 一套密码策略存在并且被强制执行在远程端点上.  | ✓| ✓ |
| **4.6** | MSTG‑AUTH‑6 | 该远程终端执行一种机制来对抗提交凭据的次数过多。 | ✓| ✓ |
| **4.7** | MSTG‑AUTH‑7 | 在预设不活动时间和访问令牌到期之后，在远程端点的会话将无效。 | ✓| ✓ |
| **4.8** | MSTG‑AUTH‑8 | 生物特征认证（如果有的话）不是事件绑定的（即，使用仅返回“true”或“false”的API）. 相反，它基于解锁钥匙串/密钥库。  | | ✓|
| **4.9** | MSTG‑AUTH‑9 | 第二个因素认证存在于远程端点, 并且始终如一的按需执行. | | ✓ |
| **4.10** | MSTG‑AUTH‑10 | 敏感交易需要逐步进行身份验证. | | ✓ |
| **4.11** | MSTG‑AUTH‑11 | 该应用通知该用户他/她的账户所有的敏感行为. 用可以查看设备列表, 查看场景信息 (IP 地址, 位置, 等等.) 以及屏蔽特定设备. | | ✓ |
| **4.12** | MSTG‑AUTH‑12 | 授权模型在远程端点应该被定义, 和被强制执行. | ✓| ✓ |

<div style="page-break-after: always;">
</div>

## 参考文献

OWASP移动安全性测试指南提供了验证上面列出的要求的详细说明。

- 常规：身份验证和会话管理 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04e-Testing-Authentication-and-Session-Management.md>
- Android：测试本地身份验证 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05f-Testing-Local-Authentication.md>
- iOS：测试本地身份验证 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06f-Testing-Local-Authentication.md>

有关更多信息，另请参见：

- OWASP 移动安全前 10: M4 (身份验证的不安全性) - <https://www.owasp.org/index.php/Mobile_Top_10_2016-M4-Insecure_Authentication>
- OWASP 移动安全前 10: M6 (授权的不安全性) - <https://www.owasp.org/index.php/Mobile_Top_10_2016-M6-Insecure_Authorization>
- CWE 287 (不正确的身份验证) - <https://cwe.mitre.org/data/definitions/287.html>
