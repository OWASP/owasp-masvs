# V8: Defense-in-depth requirements

## Control objective

The primary objective of error handling and logging is to provide a useful reaction by the user, administrators, and incident response teams. The objective is not to create massive amounts of logs, but high quality logs, with more signal than discarded noise.

High quality logs will often contain sensitive data, and must be protected as per local data privacy laws or directives. This should include:

- Not collecting or logging sensitive information if not specifically required.
- Ensuring all logged information is handled securely and protected as per its data classification.
- Ensuring that logs are not forever, but have an absolute lifetime that is as short as possible.

If logs contain private or sensitive data, the definition of which varies from country to country, the logs become some of the most sensitive information held by the application and thus very attractive to attackers in their own right.

## Requirements

| # | Description | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| **8.1** | Verify that the application does not output error messages or stack traces containing sensitive data that could assist an attacker, including session id, software/framework versions and personal information | ✓ | ✓ | ✓ | ✓ |
| **8.2** | Verify that error handling logic in security controls denies access by default. |   | ✓ | ✓ | ✓ |
| **8.3** | Verify security logging controls provide the ability to log success and particularly failure events that are identified as security-relevant. |   | ✓ | ✓ | ✓ |
| **8.4** | Verify that each log event includes necessary information that would allow for a detailed investigation of the timeline when an event happens. |   | ✓ | ✓ | ✓ |

## References

For more information, please see:

- OWASP Testing Guide 4.0 content: Testing for Error Handling [https://www.owasp.org/index.php/Testing\_for\_Error\_Handling](https://www.owasp.org/index.php/Testing_for_Error_Handling)

