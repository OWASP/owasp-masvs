# V1: Architecture, design and threat modelling requirements

## Control objective

Ensure that a verified application satisfies the following high level requirements:

- At level 1, components of the application are identified and have a reason for being in the app
- At level 2, the architecture has been defined and the code adheres to the architecture
- At level 3, the architecture and design is in place, in use, and effective

Note: This section has been re-introduced in version 3.0, but is essentially the same architectural controls as version 1.0 of the ASVS.

## Requirements

| # | Description | 1 | 2 | 3 | Since |
| --- | --- | --- | --- | --- | --- |
| **1.1** | Verify that all application components are identified and are known to be needed. | ✓ | ✓ | ✓ | 1.0 |
| **1.2** | Verify that all components, such as libraries, modules, and external systems, that are not part of the application but that the application relies on to operate are identified. |   | ✓ | ✓ | 1.0 |
| **1.3** | Verify that a high-level architecture for the application has been defined. |   | ✓ | ✓ | 1.0 |
| **1.4** | Verify that all application components are defined in terms of the business functions and/or security functions they provide. |   |   | ✓ | 1.0 |
| **1.5** | Verify that all components that are not part of the application but that the application relies on to operate are defined in terms of the functions, and/or security functions, they provide. |   |   | ✓ | 1.0 |
| **1.6** | Verify that a threat model for the target application has been produced and covers off risks associated with Spoofing, Tampering, Repudiation, Information Disclosure, and Elevation of privilege (STRIDE). |   |   | ✓ | 1.0 |
| **1.7** | Verify all security controls (including libraries that call external security services) have a centralized implementation. |   | ✓ | ✓ | 3.0 |
| **1.8** | Verify that components are segregated from each other via a defined security control, such as network segmentation, firewall rules, or cloud based security groups. |   | ✓ | ✓ | 3.0 |
| **1.9** | Verify the application has a clear separation between the data layer, controller layer and the display layer, such that security decisions can be enforced on trusted systems. |   | ✓ | ✓ | 3.0 |
| **1.10** | Verify that there is no sensitive business logic, secret keys or other proprietary information in client side code. |   | ✓ | ✓ | 3.0 |

## References

For more information, please see:

[TODO]
