# Using the Mobile Application Security Verification Standard

MASVS has two main goals:
·      to help organizations develop and maintain secure mobile applications
·      to allow security service, security tools vendors, and consumers to align their requirements and offerings

Figure 1 - Uses of MASVS for organizations and tool/service providers

## Mobile Application Security Verification Levels

The Mobile Application Security Verification Standard defines three security verification levels, with each level increasing in depth. 

- MASVS Level 1 -- Basic Security
- MASVS Level 2 -- Standard Security
- MASVS Level 3 -- Defense-in-Depth

Each MASVS level contains a list of security requirements. Each of these requirements can also be mapped to security-specific features and capabilities that must be built into software by developers. The MASVS level reflects the overall security of the app, and an app that fullfills the level 3 requirements is considered to have state-of-the-art security.

Figure 2 - OWASP Mobile Application Security Verification Standard 1.0 Levels

Depending on the threat model and sensitivity of the data processed by the app, developers may opt to implement additional software protection mechanisms. To verify these optional defenses, MASVS offers a separate set of requirements and defines four resiliency grades as follows. 

- Resiliency Grade 1 -- Light Protection
- Resiliency Grade 2 -- Medium Protection
- Resiliency Grade 3 -- Strong Protection
- Resiliency Grade 4 -- Very Strong Protection

Figure 3 - OWASP Mobile Application Security Verification Standard 1.0 Resiliency Grades

## How to use this standard

One of the best ways to use the Mobile Application Security Verification Standard is to use it as blueprint create a Secure Coding Checklist specific to your application, platform or organization. Tailoring the MASVS to your use cases will increase the focus on the security requirements that are most important to your projects and environments.

### Level 1: Opportunistic

-- TODO: Describe the levels

### Level 2: Standard

### Level 3: Advanced



## Applying MASVS in Practice

Different threats have different motivations. Some industries have unique information and technology assets and domain specific regulatory compliance requirements.

Below we provide industry-specific guidance regarding recommended MASVS levels. Although some unique criteria and some differences in threats exist for each industry, a common theme throughout all industry segments is that opportunistic attackers will look for any easily exploitable vulnerable applications, which is why MASVS Level 1 is recommended for all applications regardless of industry. This is a suggested starting point to manage the easiest to find risks. Organizations are strongly encouraged to look more deeply at their unique risk characteristics based on the nature of their business. At the other end of the spectrum is MASVS Level 3, which is reserved for those cases that might endanger human safety or when a full application breach could severely impact the organization.

| Industry | Threat Profile | L1 Recommendation | L2 Recommendation | L3 Recommendation |
| --- | --- | --- | --- | --- |
| Finance and Insurance | Although this segment will experience attempts from opportunistic attackers, it is often viewed as a high value target by motivated attackers and attacks are often financially motivated. Commonly, attackers are looking for sensitive data or account credentials that can be used to commit fraud or to benefit directly by leveraging money movement functionality built into applications. Techniques often include stolen credentials, application-level attacks, and social engineering. Some major compliance considerations include Payment Card Industry Data Security Standard (PCI DSS),Gramm Leech Bliley Act and
Sarbanes-Oxley Act (SOX). | All network accessible applications. | Applications that contain sensitive information like credit card numbers, personal information, that can move limited amounts of money in limited ways. Examples include:  (i) transfer money between accounts at the same institution or(ii) a slower form of money movement (e.g. ACH) with transaction limits or(iii) wire transfers with hard transfer limits within a period of time. | Applications that contain large amounts of sensitive information or that allow either rapid transfer of large sums of money (e.g. wire transfers) and/or transfer of large sums of money in the form of individual transactions or as a batch of smaller transfers. |
| Manufacturing, professional, transportation, technology, utilities, infrastructure, and defense | These industries may not appear to have very much in common, but the threat actors who are likely to attack organizations in this segment are more likely to perform focused attacks with more time, skill, and resources. Often the sensitive information or systems are not easy to locate and require leveraging insiders and social engineering techniques. Attacks may involve insiders, outsiders, or be collusion between the two. Their goals may include gaining access to intellectual property for strategic or technological advantage. We also do not want to overlook attackers looking to abuse application functionality influence the behaviour of or disrupt sensitive systems.
Most attackers are looking for sensitive data that can be used to directly or indirectly profit from to include personally identifiable information and payment data. Often the data can be used for identity theft, fraudulent payments, or a variety of fraud schemes. | All network accessible applications. | Applications containing internal information or information about employees that may be leveraged in social engineering. Applications containing nonessential, but important intellectual property or trade secrets. | Applications containing valuable intellectual property, trade secrets, or government secrets (e.g. in the United States this may be anything classified at Secret or above) that is critical to the survival or success of the organization. Applications controlling sensitive functionality (e.g. transit, manufacturing equipment, control systems) or that have the possibility of threatening safety of lif |
| Healthcare | Most attackers are looking for sensitive data that can be used to directly or indirectly profit from to include personally identifiable information and payment data. Often the data can be used for identity theft, fraudulent payments, or a variety of fraud schemes.
For the US healthcare sector, the Health Insurance Portability and
Accountability Act (HIPAA) Privacy, Security, Breach Notification
Rules and Patient Safety Rule ( [http://www.hhs.gov/ocr/privacy/](http://www.hhs.gov/ocr/privacy/)= [.](http://www.hhs.gov/ocr/privacy/) | All network accessible applications | Applications with small or moderate amounts of sensitive medical information (Protected Health Information), Personally Identifiable Information, or payment data. | Applications used to control medical equipment, devices, or records that may endanger human life. Payment and Point of Sale systems (POS) that contain large amounts of transaction data that could be used to commit fraud. This includes any administrative interfaces for these applications |
| Retail, food, hospitality | Many of the attackers in this segment utilize opportunistic "smash and grab" tactics. However, there is also a regular threat of specific attacks on applications known to contain payment information, perform financial transactions, or store personally identifiable information. Although less likely than the threats mentioned above, there is also the possibility of more advanced threats attacking this industry segment to steal intellectual property, gain competitive intelligence, or gain an advantage with the target organization or a business partner in negotiations. | All network accessible applications. | Suitable for business applications, product catalogue information, internal corporate information, and applications with limited user information (e.g. contact information). Applications with small or moderate amounts of payment data or checkout functionality. | Payment and Point of Sale systems (POS) that contain large amounts of transaction data that could be used to commit fraud. This includes any administrative interfaces for these applications. Applications with a large volume of sensitive information like full credit card numbers, mother's maiden name, social security numbers etc. |
