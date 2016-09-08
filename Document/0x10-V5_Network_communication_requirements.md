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
