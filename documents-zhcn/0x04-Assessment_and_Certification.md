# 评估与认证

## OWASP对MASVS认证和信任标志的立场

OWASP是一个中立的，对无厂商偏好的非盈利性组织。OWASP不会对任何厂商和软件进行认证。

任何这样的保证声明，信任标志或认证，都不是经过OWASP官方审查，注册或认证的。因此，对于任何声称经过OWASP认证的第三方机构，各方必须谨慎地考虑其真实性。   (to all reviewer: 这句话不好翻译。欢迎大家建议)

这段声明并不是为了阻止任何组织提供认证服务，但任何组织都不应宣称拥有OWASP的官方认证。

## 认证移动应用程序的指南

移动应用安全认证标准（MASVS）推荐测试人员通过“Open Book”的方式对移动应用进行验证。也就是说，测试人员需要取得所有关于被测试应用的关键信息，比如，程序设计和开发人员的信息，项目文档，源码，用户服务登录权限，以及至少一个每个类别用户的测试用户名和密码。   (to all reviewer: 这句话不好翻译。欢迎大家建议)

需要注意的是，MASVS只涉及(客户端)移动应用程序的安全性、应用程序与其远程端点之间的网络通信，以及与用户身份验证和会话管理相关的一些基本和通用需求。它不包含与应用程序相关联的远程服务(如web服务)的特定要求，对于一组有限的与身份验证和会话管理相关的通用要求是安全的。但是，MASVS V1指定远程服务必须由整个威胁模型覆盖，并根据适当的标准(如OWASP ASVS)进行验证。 [TBD]

认证组织必须在任何报告中包括验证的范围(特别是在关键组件超出范围的情况下)，验证结果的摘要，包括通过和失败的测试，以及如何解决失败的测试的明确指示。保存详细的工作底稿、屏幕截图或电影、脚本以可靠地、反复地利用问题，以及测试的电子记录(如截取代理日志和相关注释，如清理列表)，被认为是标准的行业实践。仅仅运行一个工具并报告故障是不够的;这并不能提供充分的证据证明在认证级别上的所有问题都经过了彻底的测试。在出现争议的情况下，应该有足够的支持性证据来证明每一个经过验证的需求都确实经过了测试。 [TBD]

### 使用OWASP移动安全测试指南（MSTG）

OWASP MSTG是用于测试移动应用程序安全性的手册。它描述了验证MASVS中列出的相关安全准则的技术过程。MSTG提供了一个测试案例的列表，每个测试案例都映射到MASVS中的一个安全准则。相比MASVS对于安全准则的通用性和一般性的描述，MSTG提供了基于不同移动操作系统的详细建议以及测试流程。

### 自动化安全测试工具的作用

使用自动化扫描工具对移动应用程序进行静态与动态的扫描是可以提升安全性测试的效率。但是，仅仅通过使用自动化工具来完成对MASVS的验证是不切实际的。因为，每个移动应用程序都是不同的，而且了解应用程序的总体架构、业务逻辑和以及相关技术框架带来的缺点，是验证移动应用程序安全性的必要条件。

## 其他用途

### 作为详细的安全架构指南

MASVS可以被用作安全架构师的参考资料。SABSA与TOGAF，作为目前两个主流的的安全架构框架，缺少了很多关于移动安全架构评估的必要信息，而MASVS填补了这方面的空白。安全架构师可以使用MASVS作为参考来实现移动应用程序的安全设计。

### 作为安全编程检查清单

MASVS定义了两个安全检查级别用来对应不同的安全需求。按照自身需求，相关单位可以自行定义对其适用的安全检查清单。相关单位还可以对 MASVS 的 GitHub Repo 进行Fork操作来制定符合其自身需求的安全标准。但是注意由于MASVS可能进行更新，需要维护Fork版本的可追溯性。 也就是说，假如一个移动应用程序通过了安全测试准则4.1，随着MASVS的更新，此应用程序也通过的更新版本的安全测试准则4.1。    (to reviewer: 这句话不好翻译。欢迎大家建议)

### 作为移动安全测试的基准

一套完整的移动安全测试方法应该包括所有MASVS列出的安全准则。OWASP移动安全测试指南(MSTG)对每个安全准则的验证需求都给出了黑盒与白盒测试的相关案例。

### 作为自动化单元和集成测试的指南

大多数MASVS的安全准则（除了应用架构之外），都是可测的。MASVS所定义的安全准则都可作为自动化单元测试、集成测试和验收测试集成到持续的开发生命周期中。这不仅提高了开发人员的安全意识，还提高了最终应用程序的整体质量，并在发布早期的安全测试中减少了安全漏洞的数量。

### 作为安全开发培训的参考资料

MASVS还可以用来定义安全移动应用程序的特性。市面上很多“安全编程”的课程不过是传授一些黑客技巧顺带加一点安全编程的小提示。这样的课程因其覆盖面的局限性因此对开发人员没有很大的帮助。移动开发安全课程可以参考MASVS进行制定，在覆盖十大代码安全问题的同时，重点关注与强调MASVS中提及的主动安全防护控制。