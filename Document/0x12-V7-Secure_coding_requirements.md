# V7: Secure coding requirements

## Control objective

todo

## Requirements

| # | Description | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| **7.1** | Verify that no confidential data is stored in the application code. Examples of this kind of data are credentials, keys, etc. Reverse engineering techniques allow extraction of this data. | ✓ | ✓ | ✓ | ✓ |
| **7.2** | Verify that no confidential data is cached on the client device. Examples of this kind of data are credentials, keys, etc. Examples of caching vectors are keyboard key-presses, network requests, cookies, etc. Reverse engineering techniques allow extraction of this cached data. |   | ✓ | ✓ | ✓ |
| **7.3** | Verify that all data send, stored or received by the application, is validated. In the case the secure channel or the backend server is compromised, the application still has a way to protect against malicious or crafted data injections. |   | ✓ | ✓ | ✓ |





## References

TODO

