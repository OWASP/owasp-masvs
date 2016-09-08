#
# Mobile Application Security Verification Standard

[date]

# Acknowledgements

## About the Standard

The Mobile Application Security Verification Standard is a list of security requirements for mobile apps that can be used by architects, developers, testers, security professionals, and consumers to define what a secure mobile application is.

## Copyright and License

Copyright © 2016 The OWASP Foundation. This document is released under the Creative Commons Attribution ShareAlike 3.0 license. For any reuse or distribution, you must make clear to others the license terms of this work.

| Project Leads | Lead Authors | Contributors and Reviewers |
| --- | --- | --- |
| Bernhard Mueller, Sven Schleier | T.b.d. | T.b.d. |

# Preface

Welcome to the Mobile Application Security Verification Standard (MASVS) version 1.0. The MASVS is a community-effort to establish a framework of security requirements and controls that focus on normalising the functional and non-functional security controls required when designing, developing and testing mobile applications on iOS and Android.

MASVS v1.0 is a culmination of community effort and industry feedback.

-- TODO - Further introduction --

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

Figure 3 - OWASP Mobile Application Security Verification Standard 1.0 Resliency Grades

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


# Assessing software has achieved a verification level

## OWASP's stance on MASVS Certifications and Trust Marks

OWASP, as a vendor-neutral not-for-profit organisation, does not certify any vendors, verifiers or software.

All such assurance assertions, trust marks, or certifications are not officially vetted, registered, or certified by OWASP, so an organization relying upon such a view needs to be cautious of the trust placed in any third party or trust mark claiming ASVS certification.

This should not inhibit organizations from offering such assurance services, as long as they do not claim official OWASP certification.

## Guidance for certifying organizations

The Application Security Verification Standard can be used as an open book verification of the application, including open and unfettered access to key resources such as architects and developers, project documentation, source code, authenticated access to test systems (including access to at least one account in each role), particularly for L2 and L3 verifications.

Historically, penetration testing and secure code reviews have included issues "by exception" – that is only failed issues appear in the final report. A certifying organization must include in any report the scope of the verification (particularly if a key component is out of scope, such as SSO authentication), a summary of verification findings, including passed and failed tests, with clear indications of how to resolve the failed tests.

Keeping detailed work papers, screenshots or movies, scripts to reliably and repeatedly exploit an issue, and electronic records of testing, such as intercepting proxy logs and associated notes such as a cleanup list, is considered standard industry practice and can be really useful as proofs of the findings for the most doubts developers. It is not sufficient to simply run a tool and report on the failures; this does not (at all) provide sufficient evidence that all issues at a certifying level have been tested and tested thoroughly. In case of dispute, there should be sufficient assurance evidence to demonstrate each and every verified requirement has indeed been tested.

## The role of automated penetration testing tools

Automated penetration tools are encouraged to provide as much as possible coverage and to exercise as many parameters as possible with many different forms of malicious inputs as possible.

It is not possible to fully complete ASVS verification using automated penetration testing tools alone. Whilst a large majority of requirements in L1 can be performed using automated tests, the overall majority of requirements are not amenable to automated penetration testing.

Please note that the lines between automated and manual testing have blurred as the application security industry matures. Automated tools are often manually tuned by experts and manual testers often leverage a wide variety of automated tools.

## The role of penetration testing

It is possible to perform a manual penetration test and verify all L1 issues without requiring access to source code, but this is not a leading practice. L2 requires at least some access to developers, documentation, code, and authenticated access to the system. Complete penetration testing coverage at Level 3 is not possible, as most of the additional issues involve review of system configuration, malicious code review, threat modelling, and other non-penetration testing artefacts.

## As detailed security architecture guidance

One of the more common uses for the Application Security Verification Standard is as a resource for security architects. The two major security architecture frameworks, SABSA or TOGAF, are missing a great deal of information that is necessary to complete application security architecture review. ASVS can be used to fill in those gaps by allowing security architects to choose better controls for common problems, such as data protection patterns and input validation strategies.

## As a replacement for off the shelf secure coding checklists

Many organizations can benefit from adopting the ASVS, by choosing one of the three levels, or by forking ASVS and changing what is required for each application risk level in a domain specific way. We encourage this type of forking as long as traceability is maintained, so that if an app has passed requirement 4.1, this means the same thing for forked copies as the standard as it evolves.

## As a guide for automated unit and integration tests

The ASVS is designed to highly testable, with the sole exception of architectural and malicious code requirements. By building unit and integration tests that test for specific and relevant fuzz and abuse cases, the application becomes nearly self-verifying with each and every build. For example, additional tests can be crafted for the test suite for a login controller, testing the username parameter for common usernames, account enumeration, brute forcing, LDAP and SQL injection, and XSS. Similarly, a test on the password parameter should include common passwords, password length, null byte injection, removing the parameter, XSS, account enumeration, and more.

## As secure development training

ASVS can also be used to define characteristics of secure software. Many "secure coding" courses are simply ethical hacking courses with a light smear of coding tips. This does not help developers. Instead, secure development courses can use the ASVS with a strong focus on the proactive controls found in the ASVS, rather than the Top 10 negative things not to do.


# Detailed Verification Requirements

V1.        Architecture, design and threat modelling

V2.        Data storage and privacy

V3.        Cryptography

V4.        Authentication and session management

V5.        Network communication

V6.        Interaction with the environment

V7.        Secure coding

V8.        Defense-in-depth

V9.        Resiliency against reverse engineering


# V1: Architecture, design and threat modelling requirements

## Control objective

Ensure that a verified application satisfies the following high level requirements:

- At level 1, components of the application are identified and have a reason for being in the app
- At level 2, the architecture has been defined and the code adheres to the architecture
- At level 3, the architecture and design is in place, in use, and effective

Note: This section has been re-introduced in version 3.0, but is essentially the same architectural controls as version 1.0 of the ASVS.

## Requirements

| # | Description | 1 | 2 | 3 | Since |
| --- | --- | --- | --- | --- | --- |
| **1.1** | Verify that all application components are identified and are known to be needed. | ✓ | ✓ | ✓ | 1.0 |
| **1.2** | Verify that all components, such as libraries, modules, and external systems, that are not part of the application but that the application relies on to operate are identified. |   | ✓ | ✓ | 1.0 |
| **1.3** | Verify that a high-level architecture for the application has been defined. |   | ✓ | ✓ | 1.0 |
| **1.4** | Verify that all application components are defined in terms of the business functions and/or security functions they provide. |   |   | ✓ | 1.0 |
| **1.5** | Verify that all components that are not part of the application but that the application relies on to operate are defined in terms of the functions, and/or security functions, they provide. |   |   | ✓ | 1.0 |
| **1.6** | Verify that a threat model for the target application has been produced and covers off risks associated with Spoofing, Tampering, Repudiation, Information Disclosure, and Elevation of privilege (STRIDE). |   |   | ✓ | 1.0 |
| **1.7** | Verify all security controls (including libraries that call external security services) have a centralized implementation. |   | ✓ | ✓ | 3.0 |
| **1.8** | Verify that components are segregated from each other via a defined security control, such as network segmentation, firewall rules, or cloud based security groups. |   | ✓ | ✓ | 3.0 |
| **1.9** | Verify the application has a clear separation between the data layer, controller layer and the display layer, such that security decisions can be enforced on trusted systems. |   | ✓ | ✓ | 3.0 |
| **1.10** | Verify that there is no sensitive business logic, secret keys or other proprietary information in client side code. |   | ✓ | ✓ | 3.0 |

## References

For more information, please see:

[TODO]

# V2: Data Storage and Privacy requirements

## Control objective

Authentication is the act of establishing, or confirming, something (or someone) as authentic, that is, that claims made by or about the thing are true. Ensure that a verified application satisfies the following high level requirements:

- Verifies the digital identity of the sender of a communication.
- Ensures that only those authorised are able to authenticate and credentials are transported in a secure manner.

## Requirements

-- TODO --

| # | Description | 1 | 2 | 3 | Since |
| --- | --- | --- | --- | --- | --- |
| **2.1** | Verify all pages and resources by default require authentication except those specifically intended to be public (Principle of complete mediation). | ✓ | ✓ | ✓ | 1.0 |
| **2.2** | Verify that all password fields do not echo the user's password when it is entered. | ✓ | ✓ | ✓ | 1.0 |
| **2.4** | Verify all authentication controls are enforced on the server side. | ✓ | ✓ | ✓ | 1.0 |

## References

For more information, please see:

-- TODO --


# V3: Cryptography Verificiation Requirements

## Control objective

One of the core components of any web-based application is the mechanism by which it controls and maintains the state for a user interacting with it. This is referred to this as Session Management and is defined as the set of all controls governing state-full interaction between a user and the web-based application.

Ensure that a verified application satisfies the following high level session management requirements:

- Sessions are unique to each individual and cannot be guessed or shared
- Sessions are invalidated when no longer required and timed out during periods of inactivity.

## Requirements

| # | **Description** | **1** | **2** | **3** | **Since** |
| --- | --- | --- | --- | --- | --- |
| **3.1** | Verify that there is no custom session manager, or that the custom session manager is resistant against all common session management attacks. | ✓ | ✓ | ✓ | 1.0 |
| **3.2** | Verify that sessions are invalidated when the user logs out. | ✓ | ✓ | ✓ | 1.0 |
| **3.3** | Verify that sessions timeout after a specified period of inactivity. | ✓ | ✓ | ✓ | 1.0 |
| **3.4** | Verify that sessions timeout after an administratively-configurable maximum time period regardless of activity (an absolute timeout). |   |   | ✓ | 1.0 |
| **3.5** | Verify that all pages that require authentication have easy and visible access to logout functionality. | ✓ | ✓ | ✓ | 1.0 |

## References

For more information, please see:

- OWASP Testing Guide 4.0: Session Management Testing [https://www.owasp.org/index.php/Testing\_for\_Session\_Management](https://www.owasp.org/index.php/Testing_for_Session_Management)
- OWASP Session Management Cheat Sheet: [https://www.owasp.org/index.php/Session\_Management\_Cheat\_Sheet](https://www.owasp.org/index.php/Session_Management_Cheat_Sheet)

# V4: Authentication and Session Management Requirements

## Control objective

Authorization is the concept of allowing access to resources only to those permitted to use them. Ensure that a verified application satisfies the following high level requirements:

- Persons accessing resources holds valid credentials to do so.
- Users are associated with a well-defined set of roles and privileges.
- Role and permission metadata is protected from replay or tampering.

## Requirements

| **#** | **Description** | **1** | **2** | **3** | **Since** |
| --- | --- | --- | --- | --- | --- |
| **4.1** | Verify that the principle of least privilege exists - users should only be able to access functions, data files, URLs, controllers, services, and other resources, for which they possess specific authorization. This implies protection against spoofing and elevation of privilege. | ✓ | ✓ | ✓ | 1.0 |
| **4.4** | Verify that access to sensitive records is protected, such that only authorized objects or data is accessible to each user (for example, protect against users tampering with a parameter to see or alter another user's account). | ✓ | ✓ | ✓ | 1.0 |
| **4.5** | Verify that directory browsing is disabled unless deliberately desired. Additionally, applications should not allow discovery or disclosure of file or directory metadata, such as Thumbs.db, .DS\_Store, .git or .svn folders. | ✓ | ✓ | ✓ | 1.0 |
| **4.8** | Verify that access controls fail securely. | ✓ | ✓ | ✓ | 1.0 |
| **4.9** | Verify that the same access control rules implied by the presentation layer are enforced on the server side. | ✓ | ✓ | ✓ | 1.0 |
| **4.10** | Verify that all user and data attributes and policy information used by access controls cannot be manipulated by end users unless specifically authorized. |   | ✓ | ✓ | 1.0 |
| **4.11** | Verify that there is a centralized mechanism (including libraries that call external authorization services) for protecting access to each type of protected resource. |   |   | ✓ | 1.0 |
| **4.12** | Verify that all access control decisions can be logged and all failed decisions are logged. |   | ✓ | ✓ | 2.0 |
| **4.13** | Verify that the application or framework uses strong random anti-CSRF tokens or has another transaction protection mechanism. | ✓ | ✓ | ✓ | 2.0 |
| **4.14** | Verify the system can protect against aggregate or continuous access of secured functions, resources, or data. For example, consider the use of a resource governor to limit the number of edits per hour or to prevent the entire database from being scraped by an individual user. |   | ✓ | ✓ | 2.0 |
| **4.15** | Verify the application has additional authorization (such as step up or adaptive authentication) for lower value systems, and / or segregation of duties for high value applications to enforce anti-fraud controls as per the risk of application and past fraud. |   | ✓ | ✓ | 3.0 |
| **4.16** | Verify that the application correctly enforces context-sensitive authorisation so as to not allow unauthorised manipulation by means of parameter tampering. | ✓ | ✓ | ✓ | 3.0 |

## References

For more information, please see:

- OWASP Testing Guide 4.0: Authorization [https://www.owasp.org/index.php/Testing\_for\_Authorization](https://www.owasp.org/index.php/Testing_for_Authorization)
- OWASP Cheat Sheet: Access Control [https://www.owasp.org/index.php/Access\_Control\_Cheat\_Sheet](https://www.owasp.org/index.php/Access_Control_Cheat_Sheet)



# V5: Network communication requirements

## Control objective

The most common web application security weakness is the failure to properly validate input coming from the client or from the environment before using it. This weakness leads to almost all of the major vulnerabilities in web applications, such as cross site scripting, SQL injection, interpreter injection, locale/Unicode attacks, file system attacks, and buffer overflows.

Ensure that a verified application satisfies the following high level requirements:

- All input is validated to be correct and fit for the intended purpose.
- Data from an external entity or client should never be trusted and should be handled accordingly.

## Requirements

-- TODO --

| # | Description | 1 | 2 | 3 | Since |
| --- | --- | --- | --- | --- | --- |
| **5.1** | Verify that the runtime environment is not susceptible to buffer overflows, or that security controls prevent buffer overflows. | ✓ | ✓ | ✓ | 1.0 |
| **5.3** | Verify that server side input validation failures result in request rejection and are logged. | ✓ | ✓ | ✓ | 1.0 |
| **5.5** | Verify that input validation routines are enforced on the server side. | ✓ | ✓ | ✓ | 1.0 |
| **5.6** | Verify that a single input validation control is used by the application for each type of data that is accepted. |   |   | ✓ | 1.0 |
| **5.10** | Verify that all SQL queries, HQL, OSQL, NOSQL and stored procedures, calling of stored procedures are protected by the use of prepared statements or query parameterization, and thus not susceptible to SQL injection | ✓ | ✓ | ✓ | 2.0 |


## References

For more information, please see:

- OWASP Testing Guide 4.0: Input Validation Testing
 [https://www.owasp.org/index.php/Testing\_for\_Input\_Validation](https://www.owasp.org/index.php/Testing_for_Input_Validation)
- OWASP Cheat Sheet: Input Validation       [https://www.owasp.org/index.php/Input\_Validation\_Cheat\_Sheet](https://www.owasp.org/index.php/Input_Validation_Cheat_Sheet)
- OWASP Testing Guide 4.0: Testing for HTTP Parameter Pollution [https://www.owasp.org/index.php/Testing\_for\_HTTP\_Parameter\_pollution\_%28OTG-INPVAL-004%29](https://www.owasp.org/index.php/Testing_for_HTTP_Parameter_pollution_%28OTG-INPVAL-004%29)
- OWASP LDAP Injection Cheat Sheet [https://www.owasp.org/index.php/LDAP\_Injection\_Prevention\_Cheat\_Sheet](https://www.owasp.org/index.php/LDAP_Injection_Prevention_Cheat_Sheet)

# V6: Interaction with the environment

**This section was incorporated into V5 in Application Security Verification Standard 2.0. ASVS requirement 5.16 addresses contextual output encoding to help prevent Cross Site Scripting.**

# V7: Secure coding requirements

## Control objective

Ensure that a verified application satisfies the following high level requirements:

- That all cryptographic modules fail in a secure manner and that errors are handled correctly.
- That a suitable random number generator is used when randomness is required.
- That access to keys is managed in a secure way.

## Requirements

| **#** | **Description** | **1** | **2** | **3** | **Since** |
| --- | --- | --- | --- | --- | --- |
| **7.2** | Verify that all cryptographic modules fail securely, and errors are handled in a way that does not enable oracle padding. | ✓ | ✓ | ✓ | 1.0 |
| **7.6** | Verify that all random numbers, random file names, random GUIDs, and random strings are generated using the cryptographic module's approved random number generator when these random values are intended to be not guessable by an attacker. |   | ✓ | ✓ | 1.0 |
| **7.7** | Verify that cryptographic algorithms used by the application have been validated against FIPS 140-2 or an equivalent standard. | ✓ | ✓ | ✓ | 1.0 |
| **7.8** | Verify that cryptographic modules operate in their approved mode according to their published security policies. |   |   | ✓ | 1.0 |
| **7.9** | Verify that there is an explicit policy for how cryptographic keys are managed (e.g., generated, distributed, revoked, and expired). Verify that this key lifecycle is properly enforced. |   | ✓ | ✓ | 1.0 |
| **7.11** | Verify that all consumers of cryptographic services do not have direct access to key material. Isolate cryptographic processes, including master secrets and consider the use of a hardware key vault (HSM). |   |   | ✓ | 3.0 |
| **7.12** | _Personally Identifiable Information_ should be stored encrypted at rest and ensure that communication goes via protected channels. |   | ✓ | ✓ | 3.0 |
| **7.13** | Verify that where possible, keys and secrets are zeroed when destroyed. |   | ✓ | ✓ | 3.0 |
| **7.14** | Verify that all keys and passwords are replaceable, and are generated or replaced at installation time. |   | ✓ | ✓ | 3.0 |
| **7.15** | Verify that random numbers are created with proper entropy even when the application is under heavy load, or that the application degrades gracefully in such circumstances. |   |   | ✓ | 3.0 |

## References

For more information, please see:

- OWASP Testing Guide 4.0: Testing for weak Cryptography [https://www.owasp.org/index.php/Testing\_for\_weak\_Cryptography](https://www.owasp.org/index.php/Testing_for_weak_Cryptography)
- OWASP Cheat Sheet: Cryptographic Storage [https://www.owasp.org/index.php/Cryptographic\_Storage\_Cheat\_Sheet](https://www.owasp.org/index.php/Cryptographic_Storage_Cheat_Sheet)



# V8: Defense-in-depth requirements

## Control objective

The primary objective of error handling and logging is to provide a useful reaction by the user, administrators, and incident response teams. The objective is not to create massive amounts of logs, but high quality logs, with more signal than discarded noise.

High quality logs will often contain sensitive data, and must be protected as per local data privacy laws or directives. This should include:

- Not collecting or logging sensitive information if not specifically required.
- Ensuring all logged information is handled securely and protected as per its data classification.
- Ensuring that logs are not forever, but have an absolute lifetime that is as short as possible.

If logs contain private or sensitive data, the definition of which varies from country to country, the logs become some of the most sensitive information held by the application and thus very attractive to attackers in their own right.

## Requirements

| # | Description | 1 | 2 | 3 | Since |
| --- | --- | --- | --- | --- | --- |
| **8.1** | Verify that the application does not output error messages or stack traces containing sensitive data that could assist an attacker, including session id, software/framework versions and personal information | ✓ | ✓ | ✓ | 1.0 |
| **8.2** | Verify that error handling logic in security controls denies access by default. |   | ✓ | ✓ | 1.0 |
| **8.3** | Verify security logging controls provide the ability to log success and particularly failure events that are identified as security-relevant. |   | ✓ | ✓ | 1.0 |
| **8.4** | Verify that each log event includes necessary information that would allow for a detailed investigation of the timeline when an event happens. |   | ✓ | ✓ | 1.0 |

## References

For more information, please see:

- OWASP Testing Guide 4.0 content: Testing for Error Handling [https://www.owasp.org/index.php/Testing\_for\_Error\_Handling](https://www.owasp.org/index.php/Testing_for_Error_Handling)


# V9: Resiliency Against Reverse Engineering Requirements

## Control objective

There are three key elements to sound data protection: Confidentiality, Integrity and Availability (CIA). This standard assumes that data protection is enforced on a trusted system, such as a server, which has been hardened and has sufficient protections.

Applications have to assume that all user devices are compromised in some way. Where an application transmits or stores sensitive information on insecure devices, such as shared computers, phones and tablets, the application is responsible for ensuring data stored on these devices is encrypted and cannot be easily illicitly obtained, altered or disclosed.

Ensure that a verified application satisfies the following high level data protection requirements:

- **Confidentiality** : Data should be protected from unauthorised observation or disclosure both in transit and when stored.
- **Integrity** : Data should be protected being maliciously created, altered or deleted by unauthorized attackers.
- **Availability** : Data should be available to authorized users as required

## Requirements

| # | Description | 1 | 2 | 3 | Since |
| --- | --- | --- | --- | --- | --- |
| **9.1** | Verify that all forms containing sensitive information have disabled client side caching, including autocomplete features. | ✓ | ✓ | ✓ | 1.0 |
| **9.2** | Verify that the list of sensitive data processed by the application is identified, and that there is an explicit policy for how access to this data must be controlled, encrypted and enforced under relevant data protection directives. |   |   | ✓ | 1.0 |
| **9.3** | Verify that all sensitive data is sent to the server in the HTTP message body or headers (i.e., URL parameters are never used to send sensitive data). | ✓ | ✓ | ✓ | 1.0 |
| **9.4** | Verify that the application sets appropriate anti-caching headers as per the risk of the application, such as the following: Expires: Tue, 03 Jul 2001 06:00:00 GMTLast-Modified: {now} GMTCache-Control: no-store, no-cache, must-revalidate, max-age=0Cache-Control: post-check=0, pre-check=0Pragma: no-cache | ✓ | ✓ | ✓ | 1.0 |
| **9.5** | Verify that on the server, all cached or temporary copies of sensitive data stored are protected from unauthorized access or purged/invalidated after the authorized user accesses the sensitive data. |   | ✓ | ✓ | 1.0 |
| **9.6** | Verify that there is a method to remove each type of sensitive data from the application at the end of the required retention policy. |   |   | ✓ | 1.0 |
| **9.7** | Verify the application minimizes the number of parameters in a request, such as hidden fields, Ajax variables, cookies and header values. |   | ✓ | ✓ | 2.0 |
| **9.8** | Verify the application has the ability to detect and alert on abnormal numbers of requests for data harvesting for an example screen scraping. |   |   | ✓ | 2.0 |
| **9.9** | Verify that data stored in client side storage - such as HTML5 local storage, session storage, IndexedDB, regular cookies or Flash cookies - does not contain sensitive or PII). | ✓ | ✓ | ✓ | 3.0 |
| **9.10** | Verify accessing sensitive data is logged, if the data is collected under relevant data protection directives or where logging of accesses is required. |   | ✓ | ✓ | 3.0 |
| **9.11** | Verify that sensitive data is rapidly sanitized from memory as soon as it is no longer needed and handled in accordance to functions and techniques supported by the framework/library/operating system. |   | ✓ | ✓ | 3.0 |

## References

For more information, please see:

- User Privacy Protection Cheat Sheet: [https://www.owasp.org/index.php/User\_Privacy\_Protection\_Cheat\_Sheet](https://www.owasp.org/index.php/User_Privacy_Protection_Cheat_Sheet)

# V10: Communications security verification requirements

## Control objective

Ensure that a verified application satisfies the following high level requirements:

- That TLS is used where sensitive data is transmitted
- That strong algorithms and ciphers are used at all times.

## Requirements

| **#** | **Description** | **1** | **2** | **3** | **Since** |
| --- | --- | --- | --- | --- | --- |
| **10.1** | Verify that a path can be built from a trusted CA to each Transport Layer Security (TLS) server certificate, and that each server certificate is valid. | ✓ | ✓ | ✓ | 1.0 |
| **10.3** | Verify that TLS is used for all connections (including both external and backend connections) that are authenticated or that involve sensitive data or functions, and does not fall back to insecure or unencrypted protocols. Ensure the strongest alternative is the preferred algorithm. | ✓ | ✓ | ✓ | 3.0 |
| **10.4** | Verify that backend TLS connection failures are logged. |   |   | ✓ | 1.0 |
| **10.5** | Verify that certificate paths are built and verified for all client certificates using configured trust anchors and revocation information. |   |   | ✓ | 1.0 |
| **10.6** | Verify that all connections to external systems that involve sensitive information or functions are authenticated. |   | ✓ | ✓ | 1.0 |
| **10.8** | Verify that there is a single standard TLS implementation that is used by the application that is configured to operate in an approved mode of operation. |   |   | ✓ | 1.0 |
| **10.10** | Verify that TLS certificate public key pinning is implemented with production and backup public keys. For more information, please see the references below. |   |   | ✓ | 3.0 |
| **10.11** | Verify that HTTP Strict Transport Security headers are included on all requests and for all subdomains, such as Strict-Transport-Security: max-age=15724800; includeSubdomains | ✓ | ✓ | ✓ | 3.0 |
| **10.12** | Verify that production website URL has been submitted to preloaded list of Strict Transport Security domains maintained by web browser vendors. Please see the references below. |   |   | ✓ | 3.0 |
| **10.13** | Ensure forward secrecy ciphers are in use to mitigate passive attackers recording traffic. | ✓ | ✓ | ✓ | 3.0 |
| **10.14** | Verify that proper certification revocation, such as Online Certificate Status Protocol (OCSP) Stapling, is enabled and configured. | ✓ | ✓ | ✓ | 3.0 |
| **10.15** | Verify that only strong algorithms, ciphers, and protocols are used, through all the certificate hierarchy, including root and intermediary certificates of your selected certifying authority. | ✓ | ✓ | ✓ | 3.0 |
| **10.16** | Verify that the TLS settings are in line with current leading practice, particularly as common configurations, ciphers, and algorithms become insecure. | ✓ | ✓ | ✓ | 3.0 |

## References

For more information, please see:

- **OWASP – TLS Cheat Sheet.** [https://www.owasp.org/index.php/Transport\_Layer\_Protection\_Cheat\_Sheet](https://www.owasp.org/index.php/Transport_Layer_Protection_Cheat_Sheet)
- **Notes on "Approved modes of TLS"**. In the past, the ASVS referred to the US standard FIPS 140-2, but as a global standard, applying US standards this can be difficult, contradictory, or confusing to apply. A better method of achieving compliance with 10.8 would be to review guides such as ( [https://wiki.mozilla.org/Security/Server\_Side\_TLS)](https://wiki.mozilla.org/Security/Server_Side_TLS)), generate known good configurations ( [https://mozilla.github.io/server-side-tls/ssl-config-generator/](https://mozilla.github.io/server-side-tls/ssl-config-generator/)), and use known TLS evaluation tools, such as sslyze, various vulnerability scanners or trusted TLS online assessment services to obtain a desired level of security. In general, we see non-compliance for this section being the use of outdated or insecure ciphers and algorithms, the lack of perfect forward secrecy, outdated or insecure SSL protocols, weak preferred ciphers, and so on.
- **Certificate pinning**. For more information please review [https://tools.ietf.org/html/rfc7469](https://tools.ietf.org/html/rfc7469). The rationale behind certificate pinning for production and backup keys is business continuity - see [https://noncombatant.org/2015/05/01/about-http-public-key-pinning/](https://noncombatant.org/2015/05/01/about-http-public-key-pinning/)
- **Pre-loading HTTP Strict Transport Security**
 [https://www.chromium.org/hsts](https://www.chromium.org/hsts)



# Appendix A: Glossary

- **Access Control** – A means of restricting access to files, referenced functions, URLs, and data based on the identity of users and/or groups to which they belong.
- **Address Space Layout Randomization (ASLR)** – A technique to help protect against buffer overflow attacks.
- **Application Security** – Application-level security focuses on the analysis of components that comprise the application layer of the Open Systems Interconnection Reference Model (OSI Model), rather than focusing on for example the underlying operating system or connected networks.
- **Application Security Verification** – The technical assessment of an application against the OWASP ASVS.
- **Application Security Verification Report** – A report that documents the overall results and supporting analysis produced by the verifier for a particular application.
- **Authentication** – The verification of the claimed identity of an application user.
- **Automated Verification** – The use of automated tools (either dynamic analysis tools, static analysis tools, or both) that use vulnerability signatures to find problems.
- **Back Doors** – A type of malicious code that allows unauthorized access to an application.
- **Blacklist** – A list of data or operations that are not permitted, for example a list of characters that are not allowed as input.
- **Cascading Style Sheets** (CSS) - A style sheet language used for describing the presentation semantics of document written in a markup language, such as HTML.
- **Certificate Authority** (CA) – An entity that issues digital certificates.
- **Communication Security** – The protection of application data when it is transmitted between application components, between clients and servers, and between external systems and the application.
- **Component** – a self-contained unit of code, with associated disk and network interfaces that communicates with other components.
- **Cross-Site Scripting** (XSS) – A security vulnerability typically found in web applications allowing the injection of client-side scripts into content.
- **Cryptographic module** – Hardware, software, and/or firmware that implements cryptographic algorithms and/or generates cryptographic keys.
- **Denial of Service (DoS) Attacks** – The flooding of an application with more requests than it can handle.
- **Design Verification** – The technical assessment of the security architecture of an application.
- **Dynamic Verification** – The use of automated tools that use vulnerability signatures to find problems during the execution of an application.
- **Easter Eggs** – A type of malicious code that does not run until a specific user input event occurs.
- **External Systems** – A server-side application or service that is not part of the application.
- **FIPS 140-2** – A standard that can be used as the basis for the verification of the design and implementation of cryptographic modules
- **Globally Unique Identifier** (GUID) – a unique reference number used as an identifier in software.
- **HyperText Markup Language (HTML)** - The main markup language for the creation of web pages and other information displayed in a web browser.
- **Hyper Text Transfer Protocol** (HTTP) – An application protocol for distributed, collaborative, hypermedia information systems. It is the foundation of data communication for the World Wide Web.
- **Input Validation** – The canonicalization and validation of untrusted user input.
- **Lightweight Directory Access Protocol (LDAP)** – An application protocol for accessing and maintaining distributed directory information services over a network.
- **Malicious Code** – Code introduced into an application during its development unbeknownst to the application owner, which circumvents the application's intended security policy. Not the same as malware such as a virus or worm!
- **Malware** – Executable code that is introduced into an application during runtime without the knowledge of the application user or administrator.
- **Open Web Application Security Project** (OWASP) – The Open Web Application Security Project (OWASP) is a worldwide free and open community focused on improving the security of application software. Our mission is to make application security "visible," so that people and organizations can make informed decisions about application security risks. See: http://www.owasp.org/
- **Output encoding** – The canonicalization and validation of application output to Web browsers and to external systems.
- **Personally Identifiable Information** (PII) - is information that can be used on its own or with other information to identify, contact, or locate a single person, or to identify an individual in context.
- **Positive**** validation** – See whitelist.
- **Security Architecture** – An abstraction of an application's design that identifies and describes where and how security controls are used, and also identifies and describes the location and sensitivity of both user and application data.
- **Security Configuration** – The runtime configuration of an application that affects how security controls are used.
- **Security Control** – A function or component that performs a security check (e.g. an access control check) or when called results in a security effect (e.g. generating an audit record).
- **SQL Injection (SQLi)** – A code injection technique used to attack data driven applications, in which malicious SQL statements are inserted into an entry point.
- **Static Verification** – The use of automated tools that use vulnerability signatures to find problems in application source code.
- **Target of Verification (TOV)** – If you are performing application security verification according to the OWASP ASVS requirements, the verification will be of a particular application. This application is called the "Target of Verification" or simply the TOV.
- **Threat Modeling** - A technique consisting of developing increasingly refined security architectures to identify threat agents, security zones, security controls, and important technical and business assets.
- **Transport Layer Security** – Cryptographic protocols that provide communication security over the Internet
- **URI/URL/URL fragments** – A Uniform Resource Identifier is a string of characters used to identify a name or a web resource. A Uniform Resource Locator is often used as a reference to a resource.
- **User acceptance testing (UAT)**– Traditionally a test environment that behaves like the production environment where all software testing is performed before going live.
- **Verifier** - The person or team that is reviewing an application against the OWASP ASVS requirements.
- **Whitelist** – A list of permitted data or operations, for example a list of characters that are allowed to perform input validation.
- **XML** – A markup language that defines a set of rules for encoding documents.

# Appendix B: References

The following OWASP projects are most likely to be useful to users/adopters of this standard:

- OWASP Testing Guide
 [https://www.owasp.org/index.php/OWASP\_Testing\_Project](https://www.owasp.org/index.php/OWASP_Testing_Project)
- OWASP Code Review Guide
 [http://www.owasp.org/index.php/Category:OWASP\_Code\_Review\_Project](http://www.owasp.org/index.php/Category:OWASP_Code_Review_Project)
- OWASP Cheat Sheets
 [https://www.owasp.org/index.php/OWASP\_Cheat\_Sheet\_Series](https://www.owasp.org/index.php/OWASP_Cheat_Sheet_Series)
- OWASP Proactive Controls
 [https://www.owasp.org/index.php/OWASP\_Proactive\_Controls](https://www.owasp.org/index.php/OWASP_Proactive_Controls)
- OWASP Top 10
 [https://www.owasp.org/index.php/Top\_10\_2013-Top\_10](https://www.owasp.org/index.php/Top_10_2013-Top_10)
- OWASP Mobile Top 10
 [https://www.owasp.org/index.php/Projects/OWASP\_Mobile\_Security\_Project\_-\_Top\_Ten\_Mobile\_Risks](https://www.owasp.org/index.php/Projects/OWASP_Mobile_Security_Project_-_Top_Ten_Mobile_Risks)

Similarly, the following web sites are most likely to be useful to users/adopters of this standard:

- MITRE Common Weakness Enumeration - [http://cwe.mitre.org/](http://cwe.mitre.org/)
- PCI Security Standards Council - [https://www.pcisecuritystandards.org](https://www.pcisecuritystandards.org)
- PCI Data Security Standard (DSS) v3.0 Requirements and Security Assessment Procedures [https://www.pcisecuritystandards.org/documents/PCI\_DSS\_v3.pdf](https://www.pcisecuritystandards.org/documents/PCI_DSS_v3.pdf)

# Appendix D: Standards Mappings

PCI DSS 6.5 is derived from the OWASP Top 10 2004/2007, with some recent process extensions. The ASVS is a strict superset of the OWASP Top 10 2013 (154 items to 10 items), so all of the issues covered by OWASP Top 10 and PCI DSS 6.5.x are handled by more fine grained ASVS control requirements. For example, "Broken authentication and session management" maps exactly to sections V2 Authentication and V3 Session Management.

Full mapping is achieved by verification level 3, although verification level 2 will address most PCI DSS 6.5 requirements except 6.5.3 and 6.5.4. Process issues, such as PCI DSS 6.5.6, are not covered by the ASVS.

| PCI-DSS 3.0 | ASVS 3.0 | Description |
| --- | --- | --- |
| 6.5.1 Injection flaws, particularly SQL injection. Also consider OS Command Injection, LDAP and XPath injection flaws as well as other injection flaws | 5.11, 5.12, 5.13, 8.14, 16.2 | Exact mapping. |
| 6.5.2 Buffer overflows | 5.1 | Exact mapping |
| 6.5.3 Insecure cryptographic storage | v7 - all | Comprehensive mapping from Level 1 up |
| 6.5.4 Insecure communications | v10 - all | Comprehensive mapping from Level 1 up |
| 6.5.5 Improper error handling | 3.6, 7.2, 8.1, 8.2 | Exact mapping |
| 6.5.7 Cross-site scripting (XSS) | 5.16, 5.20, 5.21, 5.24, 5.25, 5.26, 5.27, 11.4,11.15 | ASVS breaks down XSS into several requirements highlighting the complexity of XSS defense especially for legacy applications |
| 6.5.8 Improper Access Control (such as insecure direct object references, failure to restrict URL access, directory traversal and failure to restrict user access to functions). | v4 - all | Comprehensive mapping from Level 1 up |
| 6.5.9 Cross-site request forgery (CSRF). | 4.13 | Exact mapping. ASVS considers CSRF defense to be an aspect of access control. |
| 6.5.10 Broken authentication and session management. | v2 and v3 - all | Comprehensive mapping from Level 1 up |
