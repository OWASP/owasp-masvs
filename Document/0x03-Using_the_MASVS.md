# The Mobile Application Security Verification Standard

The MASVS can be used to establish a level of confidence in the security of mobile apps. The requirements were developed with the following objectives in mind:

* Use as a metric - To provide application developers and application owners with a framework which allows to measure the security, and thus the degree of trust that can be placed in their mobile applications.
* Use as guidance - To provide guidance in regards to security controls necessary to implement and test in order to satisfy application security requirements
* Use during procurement - Provide a baseline for mobile app security verification requirements.

## Mobile AppSec Model

The MASVS defines two strict *security verification levels (L1 and L2)*, as well a reverse engineering resiliency level (MASVS-R) that is "flexible", i.e. adaptable to an app-specific threat model. MASVS-L1 and MASVS-L2 contain generic security requirements and are recommended for all mobile apps (L1) and apps that handle highly sensitive data (L2). MASVS-R covers additional software protection controls that can be applied if preventing reverse engineering and/or tampering is a goal.

Fulfilling the requirements in MASVS-L1 results in a secure app that follows security best practices appropriately and doesn't suffer from common vulnerabilities. MASVS-L2 adds additional controls, resulting in an app that is resilient against more sophisticated attacks in a regular environment, assuming the security controls of the mobile operating system are assumed to be intact and the end user is not viewed as a potential adversary. Fulfilling all, or subsets of, the software protection requirements in MASVS-R helps defend against specific threats when the end user is malicious and/or the mobile OS is compromised.

**Note that software protections (MASVS-R) must never be used as a replacement for security controls. The controls listed in MASVR-R are intended to add threat-specific, additional protective controls to apps that also fulfill the MASVS requirements in MASVS L1 or L2.**

![Verification Levels](images/masvs-levels-new.jpg)

### Verification Levels in Detail

#### MASVS-L1: Standard Security

A mobile app that achieves MASVS-L1 adheres to mobile application security best practices. It fulfills basic requirements in terms of code quality, handling of sensitive data, and interaction with the mobile environment. A testing process must be in place to verify the security controls. This level is appropriate for all mobile applications.

#### MASVS-L2: Defense-in-Depth

MASVS-L2 introduces advanced security controls that go beyond the standard requirements. To fulfill L2, a threat model must exist, and security must be considered during the design phase. The effectiveness of the controls must be verified using white-box testing. This level is appropriate for applications that handle sensitive data, such as mobile banking.

#### MASVS-R: Resiliency Against Reverse Engineering and Tampering

The app has state-of-the-art security, and is also resilient against specific, clearly defined client-side binary-level attacks, such as tampering, modding, or reverse engineering to extract sensitive code or data. Such an app either leverages hardware security features or sufficiently strong and verifiable software protection techniques. MASVS-R is applicable to apps that handle highly sensitive data and may serve as a means of protecting intellectual property or tamper-proofing an app.

### Recommended Use

Apps are verified against MASVS L1 or L2 depending on business risk. L1 is applicable to all mobile apps, while L2 is generally recommended for apps that handle sensitive data and/or functionality. MASVS-R (or parts of it) can be applied *in addition* to proper security verification, to counter specific threats, such as repackaging or extraction of sensitive data.

In summary, The following verification modes are available:

- MASVS L1
- MASVS L1+R
- MASVS L2
- MASVS L2+R

The different combinations reflect different grades of security and resiliency. The goal is to allow for flexibility: For example, a mobile game might not warrant adding MASVS-L2 measures such as 2FA for usability reasons, but have a strong business need for tampering prevention.

Different threats have different motivations. Some industries have unique information and technology assets and domain specific regulatory compliance requirements. Below we provide industry-specific guidance regarding recommended MASVS levels.

| Industry | Threat Profile | MASVS-L2 Recommendation | MASVS-R Recommendation |
| --- | --- | --- | --- | --- |
| Finance and Insurance | Although this segment will experience attempts from opportunistic attackers, it is often viewed as a high value target by motivated attackers and attacks are often financially motivated. Commonly, attackers are looking for sensitive data or account credentials that can be used to commit fraud or to benefit directly by leveraging money movement functionality built into applications. Techniques often include stolen credentials, application-level attacks, and social engineering. Some major compliance considerations include Payment Card Industry Data Security Standard (PCI DSS), Gramm Leech Bliley Act and Sarbanes-Oxley Act (SOX). | Apps that enable access to highly sensitive information like credit card numbers, personal information, or that can move limited amounts of money in limited ways. Examples include: (i) transfer money between accounts at the same institution or(ii) a slower form of money movement (e.g. ACH) with transaction limits or(iii) wire transfers with hard transfer limits within a period of time. | Apps that enable access to large amounts of sensitive information or that allow either rapid transfer of large sums of money (e.g. wire transfers) and/or transfer of large sums of money in the form of individual transactions or as a batch of smaller transfers. Here, additional protections that prevent extraction of user credentials and anti-tampering controls can be viable.  |
| Healthcare | Most attackers are looking for sensitive data like personally identifiable information (PII) and payment data that can be used for financial gain. Often the data can be used for identity theft, fraudulent payments, or a variety of fraud schemes. For the US healthcare sector, the Health Insurance Portability and Accountability Act (HIPAA) Privacy, Security, Breach Notification Rules and Patient Safety Rule. | Apps that enable access to sensitive medical information (Protected Health Information), Personally Identifiable Information, or payment data. | Apps used to control medical equipment, devices, or records that may endanger human life. Payment and Point of Sale systems (POS) that contain large amounts of transaction data that could be used to commit fraud.
| Gaming | Cheating is an important issue in online games, as a large amount of cheaters leads to a disgruntled the player base and can ultimately cause a game to fail. Popular games usually result in a modding scene that releases patched versions of games that enable features such as infinite in-game currency, threatening the business model on which the game is built. | Online games that use a client-server infrastructure where cheating is a potential issue. Games that process personally identifiable information or sensitive data, such as credit card information.| Games with an essential need to prevent modding and cheating, such as competitive online games.
| Manufacturing, professional, transportation, technology, utilities, infrastructure, and defense | BYOD exposes sensitive corporate data in ways that are difficult to control. Lost or compromised mobile devices may grant adversaries access to intellectual property or application functionality that could influence or disrupt sensitive systems. Data obtained from devices may be used for identity theft, fraudulent payments, or a variety of fraud schemes. To mitigate this threat, it is often desirable to employ containerization solutions that improve in an untrusted environment. | Apps that enable access to internal information or information about employees that may be leveraged in social engineering. Apps that enable access to intellectual property or trade secrets.| Apps that enable access to highly sensitive intellectual property, trade secrets, or government secrets (e.g. in the United States this may be anything classified at Secret or above) that is critical to the survival or success of the organization. Applications controlling sensitive functionality (e.g. transit, manufacturing equipment, control systems) where tampering could threaten safety of life.
