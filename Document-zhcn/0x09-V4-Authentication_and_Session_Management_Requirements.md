# V4：身份验证 和 会话管理

## 控制目标

在绝大多数的移动应用程序架构中，用户登录到远程服务只是其中的一个组成部分。尽管大多数应用逻辑发生在客户终端，MASVS 定义了关于如何管理用户帐户和会话的基本要求。

## 安全验证要求

| # | MSTG-ID | 描述 | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **4.1** | MSTG-AUTH-1 | 如果该应用提供给用户访问远程服务，某些形式的认证，例如用户名/密码认证，都应在远程终端施行。 | ✓ | ✓ |
| **4.2** | MSTG-AUTH-2 | 如果状态会话管理被使用，则远程端点使用随机生成的会话标识符来认证客户端请求，而不会发送用户的凭证。 | ✓ | ✓ |
| **4.3** | MSTG-AUTH-3 | 如果无状态的基于令牌认证机制被使用，该服务器所提供的令牌应用安全算法签名。 | ✓ | ✓ |
| **4.4** | MSTG-AUTH-4 | 当用户注销时，远程端点应终止已经存在的会话。 | ✓ | ✓ |
| **4.5** | MSTG-AUTH-5 | 一套密码策略存在并且被强制执行在远程端点上。  | ✓ | ✓ |
| **4.6** | MSTG-AUTH-6 | 该远程终端执行一种机制来对抗提交凭据的次数过多。 | ✓ | ✓ |
| **4.7** | MSTG-AUTH-7 | 在预设不活动时间和访问令牌到期之后，在远程端点的会话将无效。 | ✓ | ✓ |
| **4.8** | MSTG-AUTH-8 | 生物特征认证（如果有的话）不是事件绑定的（即，使用仅返回“true”或“false”的API）. 相反，它基于解锁钥匙串/密钥库。  | | ✓ |
| **4.9** | MSTG-AUTH-9 | 第二个因素认证存在于远程端点, 并且始终如一的按需执行。 | | ✓ |
| **4.10** | MSTG-AUTH-10 | 敏感交易需要逐步进行身份验证。 | | ✓ |
| **4.11** | MSTG-AUTH-11 | 该应用通过用户账号通知其所有敏感行为。用户可以查看设备列表, 查看场景信息 (IP 地址，位置，等等。) 以及屏蔽特定设备。 | | ✓ |
| **4.12** | MSTG-AUTH-12 | 授权模型应该在远程端点被定义和被强制执行。 | ✓ | ✓ |

## 参考文献

OWASP移动安全性测试指南提供了验证上面列出的要求的详细说明。

- 常规：身份验证和会话管理 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04e-Testing-Authentication-and-Session-Management.md>
- Android：测试本地身份验证 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05f-Testing-Local-Authentication.md>
- iOS：测试本地身份验证 - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06f-Testing-Local-Authentication.md>

有关更多信息，另请参见：

- OWASP Mobile Top 10: M4 (Insecure Authentication) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m4-insecure-authentication>
- OWASP Mobile Top 10: M6 (Insecure Authorization) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m6-insecure-authorization>
- CWE 287 (Improper Authentication) - <https://cwe.mitre.org/data/definitions/287.html>
- CWE 307 (Improper Restriction of Excessive Authentication Attempts) - <https://cwe.mitre.org/data/definitions/307.html>
- CWE 308 (Use of Single-factor Authentication) - <https://cwe.mitre.org/data/definitions/308.html>
- CWE 521 (Weak Password Requirements) - <https://cwe.mitre.org/data/definitions/521.html>
- CWE 604 (Use of Client-Side Authentication) - <https://cwe.mitre.org/data/definitions/604.html>
- CWE 613 (Insufficient Session Expiration) - <https://cwe.mitre.org/data/definitions/613.html>
