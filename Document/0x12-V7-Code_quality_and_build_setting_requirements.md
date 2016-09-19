# V7: Code quality and build setting requirements

## Control objective

The goal of this control is to ensure that basic security coding practices are followed in developing the app, and that "free" security features offered by the compiler are activated.

## Requirements

| # | Description | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| **7.1** | Verify that the application catches and handles possible exceptions.| ✓ | ✓ | ✓ | ✓ |
| **7.2** | Verify that all debugging code is removed from the release build, and that the app does log detailed error messages. | ✓ | ✓ | ✓ | ✓ |
| **7.3** | Verify that error handling logic in security controls denies access by default. | ✓ | ✓ | ✓ | ✓ |
| **7.4** | Verify that untrusted external input is not concatenated into database queries or dynamically executed code. | ✓ | ✓ | ✓ | ✓ |
| **7.5** | If the app contains unmanaged code, verify that memory is allocated, freed and used securely.  | ✓ | ✓ | ✓ | ✓ | 
| **7.6** | Verify that the app is marked as a release build. | ✓ | ✓ | ✓ | ✓ |
| **7.7** | Verify that security features offered by the compiler, such as stack protection, PIE support and automatic reference counting, are activated. | ✓ | ✓ | ✓ | ✓ |
| **7.8** | Verify that Static Application Security Testing (SAST) is part of the development lifecycle.  |  | ✓ | ✓ | ✓ |
| **7.9** | Verify that Dynamic Application Security Testing (DAST) is part of the development lifecylce.  |  | ✓ | ✓ | ✓ |

## References

TODO

