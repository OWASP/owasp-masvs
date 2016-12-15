# V7: Code quality and build setting requirements

## Control objective

The goal of this control is to ensure that basic security coding practices are followed in developing the app, and that "free" security features offered by the compiler are activated.

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
| **7.8** | Verify that static and dynamic application security testing are performed as part of the development lifecycle, and that the configuration of the SAST and DAST tools is tailored to the app. |   | ✓ | ✓ | ✓ |
| **7.9** | Verify that App must be code signed and provisioned with valid certificate. |   | ✓ | ✓ | ✓ |

## References

For more information, see also:

- OWASP Mobile Top 10:  M7 - Client Code Quality
- CWE: https://cwe.mitre.org/data/definitions/119.html
- CWE: https://cwe.mitre.org/data/definitions/89.html
- CWE: https://cwe.mitre.org/data/definitions/388.html
- CWE: https://cwe.mitre.org/data/definitions/489.html
