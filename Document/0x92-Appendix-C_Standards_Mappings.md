# Appendix C: Standards Mappings

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
