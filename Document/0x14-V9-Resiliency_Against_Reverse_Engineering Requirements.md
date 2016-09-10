# V9: Resiliency Against Reverse Engineering Requirements

## Control objective

There are three key elements to sound data protection: Confidentiality, Integrity and Availability (CIA). This standard assumes that data protection is enforced on a trusted system, such as a server, which has been hardened and has sufficient protections.

Applications have to assume that all user devices are compromised in some way. Where an application transmits or stores sensitive information on insecure devices, such as shared computers, phones and tablets, the application is responsible for ensuring data stored on these devices is encrypted and cannot be easily illicitly obtained, altered or disclosed.

Ensure that a verified application satisfies the following high level data protection requirements:

- **Confidentiality** : Data should be protected from unauthorised observation or disclosure both in transit and when stored.
- **Integrity** : Data should be protected being maliciously created, altered or deleted by unauthorized attackers.
- **Availability** : Data should be available to authorized users as required



These requirements describe protections mechanisms against known reverse engineering attacks and techniques.

## Requirements

| # | Description | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| **9.1** | Verify that all forms containing sensitive information have disabled client side caching, including autocomplete features. | ✓ | ✓ | ✓ | ✓ |
| **9.2** | Verify that the list of sensitive data processed by the application is identified, and that there is an explicit policy for how access to this data must be controlled, encrypted and enforced under relevant data protection directives. |   |   | ✓ | ✓ |
| **9.3** | Verify that all sensitive data is sent to the server in the HTTP message body or headers (i.e., URL parameters are never used to send sensitive data). | ✓ | ✓ | ✓ | ✓ |
| **9.4** | Verify that the application sets appropriate anti-caching headers as per the risk of the application, such as the following: Expires: Tue, 03 Jul 2001 06:00:00 GMTLast-Modified: {now} GMTCache-Control: no-store, no-cache, must-revalidate, max-age=0Cache-Control: post-check=0, pre-check=0Pragma: no-cache | ✓ | ✓ | ✓ | ✓ |
| **9.5** | Verify that on the server, all cached or temporary copies of sensitive data stored are protected from unauthorized access or purged/invalidated after the authorized user accesses the sensitive data. |   | ✓ | ✓ | ✓ |
| **9.6** | Verify that there is a method to remove each type of sensitive data from the application at the end of the required retention policy. |   |   | ✓ | ✓ |
| **9.7** | Verify the application minimizes the number of parameters in a request, such as hidden fields, Ajax variables, cookies and header values. |   | ✓ | ✓ | ✓ |
| **9.8** | Verify the application has the ability to detect and alert on abnormal numbers of requests for data harvesting for an example screen scraping. |   |   | ✓ | ✓ |
| **9.9** | Verify that data stored in client side storage - such as HTML5 local storage, session storage, IndexedDB, regular cookies or Flash cookies - does not contain sensitive or PII). | ✓ | ✓ | ✓ | ✓ |
| **9.10** | Verify accessing sensitive data is logged, if the data is collected under relevant data protection directives or where logging of accesses is required. |   | ✓ | ✓ | ✓ |
| **9.11** | Verify that sensitive data is rapidly sanitized from memory as soon as it is no longer needed and handled in accordance to functions and techniques supported by the framework/library/operating system. Once malware gains root privileges, or a malicious actor gains physical access to the device, the memory could be dumped and analysed. |   |   | ✓ | ✓ |
| **9.12** | Verify that a form of source code obfuscation is implemented, to increase the cost of reverse engineering attacks on protocols or application components |   |   | ✓ | ✓ |
| **9.13** | Verify that anti-debugging and anti-emulator functionalities are implemented, to increase the cost of reverse engineering attacks on the application as well as protecting runtime data streams |   |   |   | ✓ |
| **9.13** | Verify that the application doesn't implement easy logic testing, especially for enabling or disabling security specific functionalities. By simply writing to these variables in memory, the application's logic could be tampered with. Furthermore, the possibility of reading these variables could help an attacker understanding the application's logic while reverse engineering it |   |   |   | ✓ |


## References

For more information, please see:

- User Privacy Protection Cheat Sheet: [https://www.owasp.org/index.php/User\_Privacy\_Protection\_Cheat\_Sheet](https://www.owasp.org/index.php/User_Privacy_Protection_Cheat_Sheet)
