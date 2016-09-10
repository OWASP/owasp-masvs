# V7: Secure coding requirements

## Control objective

todo

## Requirements

| # | Description | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| **7.1** | Verify that no confidential data is stored in the application code. Examples of this kind of data are credentials, keys, etc. Reverse engineering techniques allow extraction of this data. | ✓ | ✓ | ✓ | ✓ |
| **7.2** | Verify that no confidential data is cached on the client device. Examples of this kind of data are credentials, keys, etc. Examples of caching vectors are keyboard key-presses, network requests, cookies, etc. Reverse engineering techniques allow extraction of this cached data. |   | ✓ | ✓ | ✓ |
| **7.3** | Verify that all data send, stored or received by the application, is validated. In the case the secure channel or the backend server is compromised, the application still has a way to protect against malicious or crafted data injections. |   | ✓ | ✓ | ✓ |
| **7.4** | Verify that all debugging, todo's and comments are removed from the source code before building the production application that will be pusblished or distributed. These informations could help an attacker during reverse engineering attempts, to better understand the application's internal logic. |   | ✓ | ✓ | ✓ |
| **7.5** | Verify that all error messages returned by the server and the application are generic in nature, and do not in any way disclose what was the underlying cause of the error. This kind of informations could help an attacker during his attacks, to better understand what makes the application crash. |   | ✓ | ✓ | ✓ |







## References

TODO

