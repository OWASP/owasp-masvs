# V7: Code Quality and Build Setting Requirements

## Control Objective

The goal of this control is to ensure that basic security coding practices are followed in developing the app, and that "free" security features offered by the compiler are activated.

## Security Verification Requirements

| # | Description | L1 | L2 |
| --- | --- | --- | --- |
| **7.1** | The app is signed and provisioned with valid certificate. | ✓ | ✓ |
| **7.2** | The app has been built in release mode, with settings appropriate for a release build (e.g. non-debuggable). | ✓ | ✓ |
| **7.3** | Debugging symbols have been removed from native binaries. | ✓ | ✓ |
| **7.4** | Debugging code has been removed, and the app does not log verbose errors or debugging messages. | ✓ | ✓ |
| **7.5** | The app catches and handles possible exceptions.| ✓ | ✓ |
| **7.6** | Error handling logic in security controls denies access by default. | ✓ | ✓ |
| **7.7** | In unmanaged code, memory is allocated, freed and used securely.  | ✓ | ✓ |
| **7.8** | Security features offered by the compiler, such as stack protection, PIE support and automatic reference counting, are activated. | ✓ | ✓ |
| **7.9** | Java bytecode has been minified.  | ✓ | ✓ |

## References

The OWASP Mobile Security Testing Guide provides detailed instructions for verifying the requirements listed in this section, as well as best practices by mobile operating system:

(...TODO... link this to v1.0 instead of master once tagged).

- Android - https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05i-Testing-Code-Quality-and-Build-Settings.md
- iOS - https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06i-Testing-Code-Quality-and-Build-Settings.md

For more information, see also:

- OWASP Mobile Top 10:  M7 - Client Code Quality
- CWE: https://cwe.mitre.org/data/definitions/119.html
- CWE: https://cwe.mitre.org/data/definitions/89.html
- CWE: https://cwe.mitre.org/data/definitions/388.html
- CWE: https://cwe.mitre.org/data/definitions/489.html
