# V8: Defense-in-depth requirements

## Control objective

The primary objective of error handling and logging is to provide a useful reaction by the user, administrators, and incident response teams. The objective is not to create massive amounts of logs, but high quality logs, with more signal than discarded noise.

High quality logs will often contain sensitive data, and must be protected as per local data privacy laws or directives. This should include:

- Not collecting or logging sensitive information if not specifically required.
- Ensuring all logged information is handled securely and protected as per its data classification.
- Ensuring that logs are not forever, but have an absolute lifetime that is as short as possible.

If logs contain private or sensitive data, the definition of which varies from country to country, the logs become some of the most sensitive information held by the application and thus very attractive to attackers in their own right.

## Requirements


| # | Logging | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| **8.1** | Verify that the application does not output error messages or stack traces containing sensitive data that could assist an attacker, including session id, software/framework versions and personal information | ✓ | ✓ | ✓ | ✓ |
| **8.2** | Verify that error handling logic in security controls denies access by default. |   | ✓ | ✓ | ✓ |
| **8.3** | Verify security logging controls provide the ability to log success and particularly failure events that are identified as security-relevant. Any anomalies and disruptions in the normal application flow should be detected and reported back to the application server along with a state report of the device (rooted/jailbroken, user identifier, device fingerprint, etc.) . The server then decides the appropriate actions in accordance with the business requirements|   |   | ✓ | ✓ |
| **8.4** | Verify that each log event includes necessary information that would allow for a detailed investigation of the timeline when an event happens. |   | ✓ | ✓ | ✓ |


| # | Rooting | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| **8.8** | Verify that the application is capable of detecting it is being executed on a rooted (Android) or jailbroken (iOS) device. Depending on business requirements and the nature of the data contained in the application, the decision could be made to eiter warn the user or to deny the application from normal usage. |   |   | ✓ | ✓ |
| **8.9** | Verify that the application is capable of detecting when cloacking tools are used to hide the rooted (Android) or jailbroken (iOS) status of a  device. If this is a business critical requirement, use a thrid party trust provider to 'measure' the status. |   |   | ✓ | ✓ |


| # | Device Binding | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| **8.10** | Verify that the application implements a 'device binding' functionality when a mobile device is treated as being trusted. A fingerprint should be derived from different parameters in order to detect if an application has e.g. been copied from one device to another. During device binding, this fingerprint is send to the backend server in order to associate the device to an account. |   |   | ✓ | ✓ |
| **8.10** | Verify that the device's fingerprint matches the stored value on the backend server, every time the application is launched. This is necessary to detect if an application has e.g. been copied from one device to another. |   |   | ✓ | ✓ |
| **8.11** | Verify that a device fingerprint is not stored in the device. It should be computed at runtime and based on multiple device properties. A stored fingerprint value could allow for easy spoofing, as the fingerprint is actualy only one parameter.|   |   | ✓ | ✓ |
| **8.11** | Verify that the attributes and properties used to compute the device fingerprint make it unique. Ensure enough parameters are used to prevent easy spoofing of these values. On the other hand, if a device is updated or the configuration changes, the fingerprint could change. The application should be able to handle these changes and take appropriate actions. |   |   | ✓ | ✓ |


| # | Data Leakage | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| **8.5** | Verify that the application implements a timeout functionality. The purpose of this timeout is to protect the application against unwanted actions or against data leakage. This could be the case when an application is used by another user (e.g. stolen or leaved unattended). When a timout occurs, all the data has to be removed from memory and the application should be closed or at least the views should be refreshed or replaced. Session timout delays depend on business requirements and the nature of the data contained in it. (e.g. finanical, medical, etc.) |   |   | ✓ | ✓ |
| **8.6** | Verify that the application implements a lockout functionality. The purpose of this lockout is to protect the application when it is send to the background (other application opened) or when the device itself is locked. When the device is locked, all the data has to be removed from memory and the application's session should be closed. The need for a lockout functionality depends on business requirements and the nature of the data contained in the application. (e.g. finanical, medical, etc.) |   |   | ✓ | ✓ |
| **8.7** | Verify that an application which requires to be unlocked, implements a protection against bruteforce attacks. If the locking mechanism depends on server side API calls, then this can easily be implemented on server/API level. A remote session should either way be setup via server side interaction, and should never be done on the client side. If the application is "offline" in nature, a counter mechanism should be implemented to protect against brute-force attacks. |   |   | ✓ | ✓ |
| **8.12** | Verify that all sensitive data shown in the application views are properly protected. Passwords for example should always be replaced with stars (*) in order to prevent data leakage. Whenever a lockout, timeout, application backgrounding occures, the sensitive data should always be removed from the views|   |   | ✓ | ✓ |

## References

For more information, please see:

- OWASP Testing Guide 4.0 content: Testing for Error Handling [https://www.owasp.org/index.php/Testing\_for\_Error\_Handling](https://www.owasp.org/index.php/Testing_for_Error_Handling)

