# V7: Code quality and build setting requirements

## Control objective

todo

## Requirements

| # | Description | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| **7.1** | Verify that the application catches and handles possible exceptions.| ✓ | ✓ | ✓ | ✓ |
| **7.2** | Verify that all debugging code is removed from the release build, and that the app does log detailed error messages. | ✓ | ✓ | ✓ | ✓ |
| **7.3** | Verify that error handling logic in security controls denies access by default. | ✓ | ✓ | ✓ | ✓ |
| **7.4** | Do not concatenate untrusted external input into database queries or dynamically executed code. | ✓ | ✓ | ✓ | ✓ |
| **7.5** | If the app contains unmanaged code, verify that memory is allocated, freed and used securely.  | ✓ | ✓ | ✓ | ✓ | 
| **7.6** | Verify that the app is marked as a release build. | ✓ | ✓ | ✓ | ✓ |
| **7.7** | Verify that security features offered by the compiler, such as stack protection, PIE support and automatic reference counting, are activated. | ✓ | ✓ | ✓ | ✓ |

## References

TODO

