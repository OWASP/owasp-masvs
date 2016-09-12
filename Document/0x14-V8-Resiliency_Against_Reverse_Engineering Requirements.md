# V8: Resiliency Against Reverse Engineering Requirements

## Control objective

... (todo) ...

## Requirements

| # | Verified | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| **9.1** | Verify that debugging symbols have been removed from native binaries. |   | ✓ | ✓ | ✓ |
| **9.2** | On Android, verify that the release bytecode has been minified with ProGuard.  |   | ✓ | ✓ | ✓ |
| **9.3** | Verify that the application detects whether it is being executed on a rooted (Android) or jailbroken (iOS) device. Depending on business requirement, users should be warned, or the app should terminate if the device is rooted. |   | ✓ | ✓ | ✓ |
| **9.4** | Verify that the app implements two or more methods of root detection and responds to the presence of a rooted device.  |   |  | ✓ | ✓ |
| **9.3** | Verify that the app has some form of debugger detection and terminates when a debugger is detected, or that the app prevents attaching a debugger using any method. On Android, both JDWP and native debugging must be covered. |   | ✓ | ✓ | ✓ |
| **9.4** | Verify that the app detects and responds to the presence of debuggers using at least two different methods that don't rely on library calls or well-known high-level APIs. |   |   | ✓ | ✓ |
| **9.5** | Verify that the app detects and responds to file tampering. |   |   | ✓ | ✓ |
| **9.6** | Verify that the app detects whether it is run inside an emulator using any method, and terminates when an emulator is detected.  |   |   | ✓ | ✓ |
| **9.7** | Verify that the app uses at least three separate, functionally different checks to detect whether it is running in an emulator, and responds appropriately when an emulator is detected. |   |   |   | ✓ |
| **9.8** | Verify that the app detects the presence of common reverse engineering tools, such as hooking frameworks and debugging servers. |   |   | ✓ | ✓ |
| **9.9** | Verify that all executable files and libraries belonging to the app are either encrypted on the file level and/or code and data segments inside the executables are encrypted or packed. Trivial static analysis should not reveal important code or data. |   |   | ✓ | ✓ |
| **9.10**| Verify that the application implements a 'device binding' functionality when a mobile device is treated as being trusted. Verify that the device fingerprint is derived from multiple different parameters.  |   |   | ✓ | ✓ |
| **9.9** | Verify that all executable files and libraries belonging to the app are either encrypted on the file level and/or code and data segments inside the executables are encrypted or packed. Trivial static analysis should not reveal important code or data. |   |   | ✓ | ✓ |

## References

... (todo) ...
