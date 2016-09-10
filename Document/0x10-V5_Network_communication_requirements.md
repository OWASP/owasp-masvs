# V5: Network communication requirements

## Control objective

{overview)

Ensure that a verified application satisfies the following high level requirements:

(list)

## Requirements

-- TODO --

| # | Description | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| **5.1** | Verify that sensitive data is encrypted on the network using secure communication protocols. This guarantees integrity of the data as well as authenticity. For the HTTP protocol, this means that only HTTPS should be used| ✓ | ✓ | ✓ | ✓ |
| **5.2** | Verify the authenticity of the rest/web backend before any acton or data is send to it.| ✓ | ✓ | ✓ | ✓ |
| **5.2** | Verify that the rest/Web server authenticates the application before any data is send back to it. Parameters collected during the device binding process should be used to identify the devie itself. In the best case, this process is part of mutual authentication. | ✓ | ✓ | ✓ | ✓ |


(todo)


## References

For more information, please see:

- OWASP Testing Guide 4.0: Input Validation Testing
 [https://www.owasp.org/index.php/Testing\_for\_Input\_Validation](https://www.owasp.org/index.php/Testing_for_Input_Validation)
- OWASP Cheat Sheet: Input Validation       [https://www.owasp.org/index.php/Input\_Validation\_Cheat\_Sheet](https://www.owasp.org/index.php/Input_Validation_Cheat_Sheet)
- OWASP Testing Guide 4.0: Testing for HTTP Parameter Pollution [https://www.owasp.org/index.php/Testing\_for\_HTTP\_Parameter\_pollution\_%28OTG-INPVAL-004%29](https://www.owasp.org/index.php/Testing_for_HTTP_Parameter_pollution_%28OTG-INPVAL-004%29)
- OWASP LDAP Injection Cheat Sheet [https://www.owasp.org/index.php/LDAP\_Injection\_Prevention\_Cheat\_Sheet](https://www.owasp.org/index.php/LDAP_Injection_Prevention_Cheat_Sheet)
