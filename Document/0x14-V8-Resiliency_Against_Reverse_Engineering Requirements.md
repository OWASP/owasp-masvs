# V8: Resiliency Against Reverse Engineering Requirements

## Control objective

This chapter covers defense-in-depth measures that are recommended for apps that process, or give access to, sensitive data or functionality. Lack of any of these controls does not cause a vulnerability - instead, they are meant to increase the app's resiliency against reverse engineering, making it more difficult for adversaries to gain an understanding of the app's internals or extract data from the app.

## Requirements

| # | Verified | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| **8.1** | Verify that debugging symbols have been removed from native binaries. |   | ✓ | ✓ | ✓ |
| **8.2** | Verify that Java bytecode has been obscured through identifier renaming.  |   | ✓ | ✓ | ✓ |
| **8.3** | Verify that the application detects whether it is being executed on a rooted or jailbroken device. Depending on the business requirement, users should be warned, or the app should terminate if the device is rooted. |   | ✓ | ✓ | ✓ |
| **8.4** | Verify that the app checks its installation source, and only runs if installed from a trusted source. |   | ✓ | ✓ | ✓ |
| **8.5** | Verify that the app has some form of debugger detection and terminates when a debugger is detected, or prevents attaching a debugger using any method. All available means of debugging must be covered (e.g. JDWP and native). |   | ✓ | ✓ | ✓ |
| **8.6** | Verify that the app implements two or more functionally different methods of root detection and responds to the presence of a rooted device either by alerting the user or terminating the app. |   |  | ✓ | ✓ |
| **8.7** | Verify that the app implements multiple debugging defenses that result in *strong* resiliency against debugging. All available means of debugging must be covered (e.g. JDWP and native).\* |   |  | ✓ | ✓ |
| **8.8** | Verify that the app detects and responds to tampering with executable files and critical data. |   |   | ✓ | ✓ |
| **8.9** | Verify that the app detects the presence of widely used reverse engineering tools, such as code injection tools, hooking frameworks and debugging servers. |   |   | ✓ | ✓ |
| **8.10** | Verify that the app detects whether it is run inside an emulator using any method, and responds by terminating or malfunctioning when an emulator is detected.  |   |   | ✓ | ✓ |
| **8.11** | Verify that that the app implements multiple different responses to tampering, debugging and emulation, including stealthy responses that don't simply terminate the app. |   |   | ✓ | ✓ |
| **8.12** | Verify that all executable files and libraries belonging to the app are either encrypted on the file level and/or important code and data segments inside the executables are encrypted or packed. Trivial static analysis should not reveal important code or data. |   |   | ✓ | ✓ |
| **8.13**| Verify that the application implements a 'device binding' functionality when a mobile device is treated as being trusted. Verify that the device fingerprint is derived from multiple device properties.  |   |   | ✓ | ✓ |
| **8.14** | Verify that obfuscating transformations and functional defenses are interdependent and well-integrated throughout the app (e.g. defensive functions are obfuscated). |   |   | ✓ | ✓ |
| **8.15** | Verify that the app uses multiple means of emulator detection, and verify that the anti-emulation defenses implement result in *strong* resiliency against emulation.\* |   |   |   | ✓ |
| **8.16** | Verify that sensitive computations take place in a trusted environment that is isolated from the mobile operating system. Hardware-based SE or TEE should be used whenever available. |   |   |   | ✓ |
| **8.17** | If hardware-based isolation is unavailable, verify that *strong* obfuscation has been applied to isolate sensitive data and computations, and verify the robustness of the obfuscation.* |   |   |   | ✓ |

\* Considered sufficiently *strong* as per the current industry standard. Please refer to the Mobile Security Testing Guide (MSTG) for details.

## References

For more information, see also:

- OWASP Mobile Top 10: M8 - Code Tampering, M9 - Reverse Engineering
