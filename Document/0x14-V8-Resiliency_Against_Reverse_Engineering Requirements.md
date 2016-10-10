# V8: Resiliency Against Reverse Engineering Requirements

## Control objective

This chapter covers defense-in-depth measures that are recommended for apps that process, or give access to, sensitive data or functionality. Lack of any of these controls does not cause a vulnerability - instead, they are meant to increase the app's resiliency against reverse engineering, making it more difficult for adversaries to gain an understanding of the app's internals or extract data from the app.

## Requirements

| # | Verified | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| **8.1** | Verify that debugging symbols have been removed from native binaries. |   | ✓ | ✓ | ✓ |
| **8.2** | Verify that Java bytecode has been obscured through identifier renaming.  |   | ✓ | ✓ | ✓ |
| **8.3** | Verify that the application detects whether it is being executed on a rooted or jailbroken device. Depending on the business requirement, users should be warned, or the app should terminate if the device is rooted. |   | ✓ | ✓ | ✓ |
| **8.4** | Verify that the app has been installed from a legitimate source. |   | ✓ | ✓ | ✓ |
| **8.5** | Verify that the app has some form of debugger detection and terminates when a debugger is detected, or prevents attaching a debugger using any method. All available means of debugging must be covered (e.g. JDWP and native). |   | ✓ | ✓ | ✓ |
| **8.6** | Verify that the app implements two or more functionally different methods of root detection and responds to the presence of a rooted device.  |   |  | ✓ | ✓ |
| **8.7** | Verify that the app either prevents, or detects and responds to, the presence of debuggers using at least three functionally different methods that don't rely on library calls or well-known high-level APIs. |   |   | ✓ | ✓ |
| **8.8** | Verify that the app detects and responds to tampering with its own files. |   |   | ✓ | ✓ |
| **8.9** | Verify that the app detects the presence of common reverse engineering tools, such as hooking frameworks and debugging servers. |   |   | ✓ | ✓ |
| **8.10** | Verify that the app detects whether it is run inside an emulator using any method, and responds when an emulator is detected.  |   |   | ✓ | ✓ |
| **8.11** | Verify that that the app implements multiple different responses to tampering, debugging and emulation, including stealthy responses that don't simply terminate the app. |   |   | ✓ | ✓ |
| **8.12** | Verify that all executable files and libraries belonging to the app are either encrypted on the file level and/or code and data segments inside the executables are encrypted or packed. Trivial static analysis should not reveal important code or data. |   |   | ✓ | ✓ |
| **8.13**| Verify that the application implements a 'device binding' functionality when a mobile device is treated as being trusted. Verify that the device fingerprint is derived from multiple device properties.  |   |   | ✓ | ✓ |
| **8.14** | Verify that all executable files and libraries belonging to the app are either encrypted on the file level and/or code and data segments inside the executables are encrypted or packed. Trivial static analysis should not reveal important code or data. |   |   | ✓ | ✓ |
| **8.15** | Verify that obfuscating transformations and reactive defenses are interdependent and well-integrated throughout the app.  |   |   | ✓ | ✓ |
| **8.16** | Verify that the app uses at least two additional, functionally different checks to detect whether it is running in an emulator, and responds appropriately when an emulator is detected.|   |   |   | ✓ |
| **8.17** | Verify that sensitive computations are obfuscated using advanced methods, and that the obfuscating transformations significantly increase the algorithmic complexity and apparent randomness of the relevant code and/or data. |   |   |   | ✓ |

## References

For more information, see also:

- OWASP Mobile Top 10: M8 - Code Tampering, M9 - Reverse Engineering
